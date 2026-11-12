"""Exercise transfers and rollback on isolated desktops, never the user's files."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import struct
import tempfile
import unittest
from unittest.mock import patch
import zipfile
import deploy

SIZES = (3940,3968,3968,3968,3664,3968,3968,3968,3968,3968,3968,3968,3968,3836)

class DeliveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.desktop = self.root/'Desktop';self.desktop.mkdir()
        self.cache = self.root/'cache'
        self.rom = bytearray(1024)
        struct.pack_into('<28H', self.rom, 64, *[v for pair in zip(deploy.OFFSETS,SIZES) for v in pair])
        self.package = self.root/'release.zip'
        self.make_package()
        self.guard = patch.object(deploy, 'running_emulator', return_value=False)
        self.guard.start()

    def tearDown(self):
        self.guard.stop();self.tmp.cleanup()

    def make_package(self, bad=False):
        sha = hashlib.sha256(self.rom).hexdigest() if not bad else '0'*64
        with zipfile.ZipFile(self.package,'w') as z:
            for name,data in {'pokeemerald.gba':bytes(self.rom),'Play.cmd':b'play',
                'load-companion-history.lua':b'helper','emulator/mgba-celio.exe':b'emulator',
                'verification.json':json.dumps({'source_commit':'fixture', 'compiled_game':{'sha256':sha}}).encode()}.items():
                z.writestr(name,data)

    def build(self, name, stamp, hours, required_history=False):
        folder=self.desktop/('EmeraldCompanions-'+name);folder.mkdir()
        (folder/'BUILD-INFO.json').write_text('{}')
        (folder/'EmeraldCompanions.gba').write_bytes(self.rom)
        data=bytearray(b'\xff'*131072)
        for i,size in enumerate(SIZES):
            sec=bytearray(4096)
            if i==0:
                struct.pack_into('<H',sec,14,hours)
                if required_history:
                    struct.pack_into('<II',sec,3884,0x31484345,1)
                    sec[3892:3908]=b'I'*16;sec[3908:3940]=b'D'*32
            struct.pack_into('<HHII',sec,4084,i,deploy.checksum(sec[:size]),deploy.SIGNATURE,7)
            data[i*4096:(i+1)*4096]=sec
        save=folder/'EmeraldCompanions.sav';save.write_bytes(data+b'R'*16)
        os.utime(save,(stamp,stamp))
        history=folder/'companion-history';history.mkdir();(history/(name+'.history')).write_bytes(name.encode())
        return folder,save

    def args(self, **changes):
        values=dict(package=str(self.package),download_url=None,package_sha256=None,
                    desktop=str(self.desktop),cache=str(self.cache),save=None,furthest=False,
                    skip_save=False,apply=True)
        values.update(changes);return argparse.Namespace(**values)

    def test_latest_pair_renamed_intact_and_all_old_builds_archived(self):
        old,_=self.build('older',1000,20)
        latest,save=self.build('latest',2000,6)
        original=save.read_bytes()
        result=deploy.deliver(self.args())
        current=self.desktop/deploy.CURRENT
        self.assertEqual((current/'pokeemerald.sav').read_bytes(), original)
        self.assertEqual((current/'companion-history/latest.history').read_bytes(),b'latest')
        self.assertFalse((current/'companion-history/older.history').exists())
        self.assertEqual(Path(result['archived_save']).read_bytes(), original)
        self.assertFalse(old.exists());self.assertFalse(latest.exists())
        self.assertEqual(len(result['archived_to']),2)

    def test_invalid_package_preserves_existing_desktop(self):
        folder,save=self.build('original',1000,6);original=save.read_bytes()
        self.make_package(bad=True)
        with self.assertRaisesRegex(ValueError,'hash'):
            deploy.deliver(self.args())
        self.assertEqual(save.read_bytes(),original);self.assertTrue(folder.is_dir())

    def test_missing_required_history_blocks_replacement(self):
        folder,save=self.build('original',1000,6,required_history=True)
        with self.assertRaisesRegex(ValueError,'snapshot'):
            deploy.deliver(self.args())
        self.assertTrue(folder.is_dir());self.assertTrue(save.is_file())

    def test_skip_save_omits_both_save_and_history(self):
        self.build('original',1000,6)
        deploy.deliver(self.args(skip_save=True))
        current=self.desktop/deploy.CURRENT
        self.assertFalse((current/'pokeemerald.sav').exists())
        self.assertFalse(list((current/'companion-history').glob('*.history')))

    def test_failed_activation_restores_archived_folder(self):
        folder,save=self.build('original',1000,6);original=save.read_bytes()
        native_rename=Path.rename
        def fail_activation(path,target):
            if path.name.startswith('staged-'):
                raise OSError('simulated failed activation')
            return native_rename(path,target)
        with patch.object(Path,'rename',fail_activation):
            with self.assertRaisesRegex(OSError,'simulated'):
                deploy.deliver(self.args())
        self.assertTrue(folder.is_dir());self.assertEqual(save.read_bytes(),original)
        self.assertFalse((self.desktop/deploy.CURRENT).exists())

    def test_same_build_does_not_archive_again(self):
        self.build('original',1000,6)
        deploy.deliver(self.args())
        count=len(list((self.desktop/deploy.ARCHIVE).iterdir()))
        result=deploy.deliver(self.args())
        self.assertEqual(result['status'],'already_current')
        self.assertEqual(len(list((self.desktop/deploy.ARCHIVE).iterdir())),count)

    def test_path_escape_is_rejected(self):
        with self.assertRaises(ValueError):
            deploy.beneath(self.desktop/'..'/'escape',self.desktop)

    def test_download_requires_and_verifies_archive_checksum(self):
        sha=deploy.digest(self.package)
        result=deploy.deliver(self.args(package=None,download_url=self.package.as_uri(),package_sha256=sha))
        self.assertEqual(result['status'],'installed')
        self.assertEqual(deploy.digest(Path(result['package'])),sha)

    def test_corrupt_latest_save_never_overwrites_valid_progress(self):
        _,valid=self.build('valid',1000,6)
        original=valid.read_bytes()
        _,corrupt=self.build('corrupt',2000,20)
        corrupt.write_bytes(b'bad')
        result=deploy.deliver(self.args())
        self.assertEqual((self.desktop/deploy.CURRENT/'pokeemerald.sav').read_bytes(),original)
        self.assertEqual(len(result['rejected_saves']),1)

if __name__=='__main__':
    unittest.main()
