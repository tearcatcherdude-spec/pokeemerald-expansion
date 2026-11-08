// Specific remembered Kanto object observations.
extern const u8 Text_Food[];
static const u8 sPipKantoObject_0[] = _("PIP: A meal somebody left\nunattended. I am demonstrating\lgreat character.$");
extern const u8 Text_VideoGame[];
static const u8 sPipKantoObject_1[] = _("PIP: We are outside, looking at a\ngame inside. A productive\lafternoon.$");
extern const u8 Text_Computer[];
static const u8 sPipKantoObject_2[] = _("PIP: It has a very serious\nscreen. My notes would ruin the\latmosphere.$");
extern const u8 Text_ImpressiveMachine[];
static const u8 sPipKantoObject_3[] = _("PIP: A machine with this many\nbuttons should make toast at\lleast.$");
extern const u8 Text_Blueprints[];
static const u8 sPipKantoObject_4[] = _("PIP: I understand the arrows. The\nrest appears to be expensive.$");
extern const u8 Text_Burglary[];
static const u8 sPipKantoObject_5[] = _("PIP: We should leave their things\nalone. Someone has done enough\lhere.$");
extern const u8 Text_DishesPlatesNeatlyLinedUp[];
static const u8 sPipKantoObject_6[] = _("PIP: All the plates match. This\nhousehold has its life together.$");
extern const u8 Text_Kitchen[];
static const u8 sPipKantoObject_7[] = _("PIP: A kitchen. At last, a\nresearch facility I understand.$");
extern const u8 Text_Dresser[];
static const u8 sPipKantoObject_8[] = _("PIP: A drawer full of somebody\nelse's socks is still somebody\lelse's drawer.$");
extern const u8 Text_Snacks[];
static const u8 sPipKantoObject_9[] = _("PIP: Emergency snacks. I admire a\nhousehold with an emergency plan.$");
extern const u8 Text_Painting[];
static const u8 sPipKantoObject_10[] = _("PIP: I like it. Please do not ask\nme to explain the composition.$");
extern const u8 Text_Telephone[];
static const u8 sPipKantoObject_11[] = _("PIP: If it rings, you answer. I\nam not prepared to sound\lresponsible.$");
extern const u8 Text_PowerPlantMachine[];
static const u8 sPipKantoObject_12[] = _("PIP: If it starts humming, I will\npolitely hum from farther away.$");
extern const u8 Text_AdvertisingPoster[];
static const u8 sPipKantoObject_13[] = _("PIP: The poster says exciting. My\nwallet heard expensive.$");
extern const u8 Text_TastyFood[];
static const u8 sPipKantoObject_14[] = _("PIP: That smells wonderful. I am\ntrying to make this a subtle\lobservation.$");
extern const u8 Text_Cup[];
static const u8 sPipKantoObject_15[] = _("PIP: Somebody put that down for a\nreason. Let us respect the\lbeverage.$");
extern const u8 Text_BlinkingLights[];
static const u8 sPipKantoObject_16[] = _("PIP: The lights are doing their\nbest. I hope somebody understands\lthem.$");
extern const u8 Text_NeatlyLinedUpTools[];
static const u8 sPipKantoObject_17[] = _("PIP: Every tool has a place. My\nbag is going to feel judged.$");
extern const u8 Text_Bookshelf[];
static const u8 sPipKantoObject_18[] = _("PIP: A whole shelf of books. I\nhope the ladder has a happy\lending.$");
extern const u8 Text_PokeMartShelf[];
static const u8 sPipKantoObject_19[] = _("PIP: All these supplies, neatly\narranged. My bag could learn\lsomething.$");
struct PipObjectReaction { const u8 *original; const u8 *comment; };
static const struct PipObjectReaction sPipKantoObjects[] = {
    {Text_Food, sPipKantoObject_0},
    {Text_VideoGame, sPipKantoObject_1},
    {Text_Computer, sPipKantoObject_2},
    {Text_ImpressiveMachine, sPipKantoObject_3},
    {Text_Blueprints, sPipKantoObject_4},
    {Text_Burglary, sPipKantoObject_5},
    {Text_DishesPlatesNeatlyLinedUp, sPipKantoObject_6},
    {Text_Kitchen, sPipKantoObject_7},
    {Text_Dresser, sPipKantoObject_8},
    {Text_Snacks, sPipKantoObject_9},
    {Text_Painting, sPipKantoObject_10},
    {Text_Telephone, sPipKantoObject_11},
    {Text_PowerPlantMachine, sPipKantoObject_12},
    {Text_AdvertisingPoster, sPipKantoObject_13},
    {Text_TastyFood, sPipKantoObject_14},
    {Text_Cup, sPipKantoObject_15},
    {Text_BlinkingLights, sPipKantoObject_16},
    {Text_NeatlyLinedUpTools, sPipKantoObject_17},
    {Text_Bookshelf, sPipKantoObject_18},
    {Text_PokeMartShelf, sPipKantoObject_19},
};
