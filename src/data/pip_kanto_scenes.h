// Specific reactions to the authored paired Kanto scenes.
static const u8 sPipLivingKanto_0[] = _("PIP: Science has made an\nimportant distinction. Lunch is\lnot a mineral.$");
extern const u8 LivingKanto_Scene0_A[], LivingKanto_Scene0_B[];
static const u8 sPipLivingKanto_1[] = _("PIP: An umbrella that stops rain.\nThey could be onto something.$");
extern const u8 LivingKanto_Scene1_A[], LivingKanto_Scene1_B[];
static const u8 sPipLivingKanto_2[] = _("PIP: I learned the tune and where\nhe keeps the spare key.$");
extern const u8 LivingKanto_Scene2_A[], LivingKanto_Scene2_B[];
static const u8 sPipLivingKanto_3[] = _("PIP: We can help water them\nbefore we go.$");
extern const u8 LivingKanto_Scene3_A[], LivingKanto_Scene3_B[];
static const u8 sPipLivingKanto_4[] = _("PIP: The notebook has to work\nvery hard now.$");
extern const u8 LivingKanto_Scene4_A[], LivingKanto_Scene4_B[];
static const u8 sPipLivingKanto_5[] = _("PIP: I hope our entry says mostly\nharmless.$");
extern const u8 LivingKanto_Scene5_A[], LivingKanto_Scene5_B[];
static const u8 sPipLivingKanto_6[] = _("PIP: I predict that I will also\nwant lunch.$");
extern const u8 LivingKanto_Scene6_A[], LivingKanto_Scene6_B[];
static const u8 sPipLivingKanto_7[] = _("PIP: I will keep my geological\nopinions quiet.$");
extern const u8 LivingKanto_Scene7_A[], LivingKanto_Scene7_B[];
static const u8 sPipLivingKanto_8[] = _("PIP: Three pillows is an\nambitious hiking strategy.$");
extern const u8 LivingKanto_Scene8_A[], LivingKanto_Scene8_B[];
static const u8 sPipLivingKanto_9[] = _("PIP: Finally, a battle I am\nqualified to lose.$");
extern const u8 LivingKanto_Scene9_A[], LivingKanto_Scene9_B[];
static const u8 sPipLivingKanto_10[] = _("PIP: Somewhere a bicycle is\nanswering.$");
extern const u8 LivingKanto_Scene10_A[], LivingKanto_Scene10_B[];
static const u8 sPipLivingKanto_11[] = _("PIP: This club has a very\nreasonable attendance policy.$");
extern const u8 LivingKanto_Scene11_A[], LivingKanto_Scene11_B[];
struct PipSceneReaction { const u8 *script; const u8 *text; u16 resolvedFlag; };
static const struct PipSceneReaction sPipKantoScenes[] = {
    {LivingKanto_Scene0_A, sPipLivingKanto_0, 0xa8e0},
    {LivingKanto_Scene0_B, sPipLivingKanto_0, 0xa8e0},
    {LivingKanto_Scene1_A, sPipLivingKanto_1, 0xa8e1},
    {LivingKanto_Scene1_B, sPipLivingKanto_1, 0xa8e1},
    {LivingKanto_Scene2_A, sPipLivingKanto_2, 0xa8e2},
    {LivingKanto_Scene2_B, sPipLivingKanto_2, 0xa8e2},
    {LivingKanto_Scene3_A, sPipLivingKanto_3, 0xa8e3},
    {LivingKanto_Scene3_B, sPipLivingKanto_3, 0xa8e3},
    {LivingKanto_Scene4_A, sPipLivingKanto_4, 0xa8e4},
    {LivingKanto_Scene4_B, sPipLivingKanto_4, 0xa8e4},
    {LivingKanto_Scene5_A, sPipLivingKanto_5, 0xa8e5},
    {LivingKanto_Scene5_B, sPipLivingKanto_5, 0xa8e5},
    {LivingKanto_Scene6_A, sPipLivingKanto_6, 0xa8e6},
    {LivingKanto_Scene6_B, sPipLivingKanto_6, 0xa8e6},
    {LivingKanto_Scene7_A, sPipLivingKanto_7, 0xa8e7},
    {LivingKanto_Scene7_B, sPipLivingKanto_7, 0xa8e7},
    {LivingKanto_Scene8_A, sPipLivingKanto_8, 0xa8e8},
    {LivingKanto_Scene8_B, sPipLivingKanto_8, 0xa8e8},
    {LivingKanto_Scene9_A, sPipLivingKanto_9, 0xa8e9},
    {LivingKanto_Scene9_B, sPipLivingKanto_9, 0xa8e9},
    {LivingKanto_Scene10_A, sPipLivingKanto_10, 0xa8ea},
    {LivingKanto_Scene10_B, sPipLivingKanto_10, 0xa8ea},
    {LivingKanto_Scene11_A, sPipLivingKanto_11, 0xa8eb},
    {LivingKanto_Scene11_B, sPipLivingKanto_11, 0xa8eb},
};
