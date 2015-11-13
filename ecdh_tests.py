#!/usr/bin/env python3

import unittest

from ecdh import *

# -----------------
# NIST test vectors
# -----------------

# KAS_ECC_CDH_PrimitiveTest.txt:
#  CAVS 14.1
#  ECC CDH Primitive (SP800-56A Section 5.7.1.2) Test Information for "testecccdh"

# [P-256]
# (QCAVSx, QCAVSy) ==> pub_key_B
# dIUT ==> prv_key_A
# ZIUT ==> Z


class ECDHTests(unittest.TestCase):
    def test_nist_vector_zero(self):
        QCAVSx = 0x700c48f77f56584c5cc632ca65640db91b6bacce3a4df6b42ce7cc838833d287
        QCAVSy = 0xdb71e509e3fd9b060ddb20ba5c51dcc5948d46fbf640dfe0441782cab85fa4ac
        dIUT = 0x7d7dc5f71eb29ddaf80d6214632eeae03d9058af1fb6d22ed80badb62bc1a534
        ZIUT = 0x46fc62106420ff012e54a434fbdd2d25ccc5852060561e68040dd7778997bd7b
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_one(self):
        QCAVSx = 0x809f04289c64348c01515eb03d5ce7ac1a8cb9498f5caa50197e58d43a86a7ae
        QCAVSy = 0xb29d84e811197f25eba8f5194092cb6ff440e26d4421011372461f579271cda3
        dIUT = 0x38f65d6dce47676044d58ce5139582d568f64bb16098d179dbab07741dd5caf5
        ZIUT = 0x057d636096cb80b67a8c038c890e887d1adfa4195e9b3ce241c8a778c59cda67
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_two(self):
        QCAVSx = 0xa2339c12d4a03c33546de533268b4ad667debf458b464d77443636440ee7fec3
        QCAVSy = 0xef48a3ab26e20220bcda2c1851076839dae88eae962869a497bf73cb66faf536
        dIUT = 0x1accfaf1b97712b85a6f54b148985a1bdc4c9bec0bd258cad4b3d603f49f32c8
        ZIUT = 0x2d457b78b4614132477618a5b077965ec90730a8c81a1c75d6d4ec68005d67ec
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_three(self):
        QCAVSx = 0xdf3989b9fa55495719b3cf46dccd28b5153f7808191dd518eff0c3cff2b705ed
        QCAVSy = 0x422294ff46003429d739a33206c8752552c8ba54a270defc06e221e0feaf6ac4
        dIUT = 0x207c43a79bfee03db6f4b944f53d2fb76cc49ef1c9c4d34d51b6c65c4db6932d
        ZIUT = 0x96441259534b80f6aee3d287a6bb17b5094dd4277d9e294f8fe73e48bf2a0024
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_four(self):
        QCAVSx = 0x41192d2813e79561e6a1d6f53c8bc1a433a199c835e141b05a74a97b0faeb922
        QCAVSy = 0x1af98cc45e98a7e041b01cf35f462b7562281351c8ebf3ffa02e33a0722a1328
        dIUT = 0x59137e38152350b195c9718d39673d519838055ad908dd4757152fd8255c09bf
        ZIUT = 0x19d44c8d63e8e8dd12c22a87b8cd4ece27acdde04dbf47f7f27537a6999a8e62
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_five(self):
        QCAVSx = 0x33e82092a0f1fb38f5649d5867fba28b503172b7035574bf8e5b7100a3052792
        QCAVSy = 0xf2cf6b601e0a05945e335550bf648d782f46186c772c0f20d3cd0d6b8ca14b2f
        dIUT = 0xf5f8e0174610a661277979b58ce5c90fee6c9b3bb346a90a7196255e40b132ef
        ZIUT = 0x664e45d5bba4ac931cd65d52017e4be9b19a515f669bea4703542a2c525cd3d3
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_six(self):
        QCAVSx = 0x6a9e0c3f916e4e315c91147be571686d90464e8bf981d34a90b6353bca6eeba7
        QCAVSy = 0x40f9bead39c2f2bcc2602f75b8a73ec7bdffcbcead159d0174c6c4d3c5357f05
        dIUT = 0x3b589af7db03459c23068b64f63f28d3c3c6bc25b5bf76ac05f35482888b5190
        ZIUT = 0xca342daa50dc09d61be7c196c85e60a80c5cb04931746820be548cdde055679d
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_seven(self):
        QCAVSx = 0xa9c0acade55c2a73ead1a86fb0a9713223c82475791cd0e210b046412ce224bb
        QCAVSy = 0xf6de0afa20e93e078467c053d241903edad734c6b403ba758c2b5ff04c9d4229
        dIUT = 0xd8bf929a20ea7436b2461b541a11c80e61d826c0a4c9d322b31dd54e7f58b9c8
        ZIUT = 0x35aa9b52536a461bfde4e85fc756be928c7de97923f0416c7a3ac8f88b3d4489
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_eight(self):
        QCAVSx = 0x94e94f16a98255fff2b9ac0c9598aac35487b3232d3231bd93b7db7df36f9eb9
        QCAVSy = 0xd8049a43579cfa90b8093a94416cbefbf93386f15b3f6e190b6e3455fedfe69a
        dIUT = 0x0f9883ba0ef32ee75ded0d8bda39a5146a29f1f2507b3bd458dbea0b2bb05b4d
        ZIUT = 0x605c16178a9bc875dcbff54d63fe00df699c03e8a888e9e94dfbab90b25f39b4
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_nine(self):
        QCAVSx = 0xe099bf2a4d557460b5544430bbf6da11004d127cb5d67f64ab07c94fcdf5274f
        QCAVSy = 0xd9c50dbe70d714edb5e221f4e020610eeb6270517e688ca64fb0e98c7ef8c1c5
        dIUT = 0x2beedb04b05c6988f6a67500bb813faf2cae0d580c9253b6339e4a3337bb6c08
        ZIUT = 0xf96e40a1b72840854bb62bc13c40cc2795e373d4e715980b261476835a092e0b
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_ten(self):
        QCAVSx = 0xf75a5fe56bda34f3c1396296626ef012dc07e4825838778a645c8248cff01658
        QCAVSy = 0x33bbdf1b1772d8059df568b061f3f1122f28a8d819167c97be448e3dc3fb0c3c
        dIUT = 0x77c15dcf44610e41696bab758943eff1409333e4d5a11bbe72c8f6c395e9f848
        ZIUT = 0x8388fa79c4babdca02a8e8a34f9e43554976e420a4ad273c81b26e4228e9d3a3
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_eleven(self):
        QCAVSx = 0x2db4540d50230756158abf61d9835712b6486c74312183ccefcaef2797b7674d
        QCAVSy = 0x62f57f314e3f3495dc4e099012f5e0ba71770f9660a1eada54104cdfde77243e
        dIUT = 0x42a83b985011d12303db1a800f2610f74aa71cdf19c67d54ce6c9ed951e9093e
        ZIUT = 0x72877cea33ccc4715038d4bcbdfe0e43f42a9e2c0c3b017fc2370f4b9acbda4a
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_twelve(self):
        QCAVSx = 0xcd94fc9497e8990750309e9a8534fd114b0a6e54da89c4796101897041d14ecb
        QCAVSy = 0xc3def4b5fe04faee0a11932229fff563637bfdee0e79c6deeaf449f85401c5c4
        dIUT = 0xceed35507b5c93ead5989119b9ba342cfe38e6e638ba6eea343a55475de2800b
        ZIUT = 0xe4e7408d85ff0e0e9c838003f28cdbd5247cdce31f32f62494b70e5f1bc36307
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_thirteen(self):
        QCAVSx = 0x15b9e467af4d290c417402e040426fe4cf236bae72baa392ed89780dfccdb471
        QCAVSy = 0xcdf4e9170fb904302b8fd93a820ba8cc7ed4efd3a6f2d6b05b80b2ff2aee4e77
        dIUT = 0x43e0e9d95af4dc36483cdd1968d2b7eeb8611fcce77f3a4e7d059ae43e509604
        ZIUT = 0xed56bcf695b734142c24ecb1fc1bb64d08f175eb243a31f37b3d9bb4407f3b96
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_fourteen(self):
        QCAVSx = 0x49c503ba6c4fa605182e186b5e81113f075bc11dcfd51c932fb21e951eee2fa1
        QCAVSy = 0x8af706ff0922d87b3f0c5e4e31d8b259aeb260a9269643ed520a13bb25da5924
        dIUT = 0xb2f3600df3368ef8a0bb85ab22f41fc0e5f4fdd54be8167a5c3cd4b08db04903
        ZIUT = 0xbc5c7055089fc9d6c89f83c1ea1ada879d9934b2ea28fcf4e4a7e984b28ad2cf
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_fifteen(self):
        QCAVSx = 0x19b38de39fdd2f70f7091631a4f75d1993740ba9429162c2a45312401636b29c
        QCAVSy = 0x09aed7232b28e060941741b6828bcdfa2bc49cc844f3773611504f82a390a5ae
        dIUT = 0x4002534307f8b62a9bf67ff641ddc60fef593b17c3341239e95bdb3e579bfdc8
        ZIUT = 0x9a4e8e657f6b0e097f47954a63c75d74fcba71a30d83651e3e5a91aa7ccd8343
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_sixteen(self):
        QCAVSx = 0x2c91c61f33adfe9311c942fdbff6ba47020feff416b7bb63cec13faf9b099954
        QCAVSy = 0x6cab31b06419e5221fca014fb84ec870622a1b12bab5ae43682aa7ea73ea08d0
        dIUT = 0x4dfa12defc60319021b681b3ff84a10a511958c850939ed45635934ba4979147
        ZIUT = 0x3ca1fc7ad858fb1a6aba232542f3e2a749ffc7203a2374a3f3d3267f1fc97b78
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_seventeen(self):
        QCAVSx = 0xa28a2edf58025668f724aaf83a50956b7ac1cfbbff79b08c3bf87dfd2828d767
        QCAVSy = 0xdfa7bfffd4c766b86abeaf5c99b6e50cb9ccc9d9d00b7ffc7804b0491b67bc03
        dIUT = 0x1331f6d874a4ed3bc4a2c6e9c74331d3039796314beee3b7152fcdba5556304e
        ZIUT = 0x1aaabe7ee6e4a6fa732291202433a237df1b49bc53866bfbe00db96a0f58224f
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_eighteen(self):
        QCAVSx = 0xa2ef857a081f9d6eb206a81c4cf78a802bdf598ae380c8886ecd85fdc1ed7644
        QCAVSy = 0x563c4c20419f07bc17d0539fade1855e34839515b892c0f5d26561f97fa04d1a
        dIUT = 0xdd5e9f70ae740073ca0204df60763fb6036c45709bf4a7bb4e671412fad65da3
        ZIUT = 0x430e6a4fba4449d700d2733e557f66a3bf3d50517c1271b1ddae1161b7ac798c
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_nineteen(self):
        QCAVSx = 0xccd8a2d86bc92f2e01bce4d6922cf7fe1626aed044685e95e2eebd464505f01f
        QCAVSy = 0xe9ddd583a9635a667777d5b8a8f31b0f79eba12c75023410b54b8567dddc0f38
        dIUT = 0x5ae026cfc060d55600717e55b8a12e116d1d0df34af831979057607c2d9c2f76
        ZIUT = 0x1ce9e6740529499f98d1f1d71329147a33df1d05e4765b539b11cf615d6974d3
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_twenty(self):
        QCAVSx = 0xc188ffc8947f7301fb7b53e36746097c2134bf9cc981ba74b4e9c4361f595e4e
        QCAVSy = 0xbf7d2f2056e72421ef393f0c0f2b0e00130e3cac4abbcc00286168e85ec55051
        dIUT = 0xb601ac425d5dbf9e1735c5e2d5bdb79ca98b3d5be4a2cfd6f2273f150e064d9d
        ZIUT = 0x4690e3743c07d643f1bc183636ab2a9cb936a60a802113c49bb1b3f2d0661660
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_twenty_one(self):
        QCAVSx = 0x317e1020ff53fccef18bf47bb7f2dd7707fb7b7a7578e04f35b3beed222a0eb6
        QCAVSy = 0x09420ce5a19d77c6fe1ee587e6a49fbaf8f280e8df033d75403302e5a27db2ae
        dIUT = 0xfefb1dda1845312b5fce6b81b2be205af2f3a274f5a212f66c0d9fc33d7ae535
        ZIUT = 0x30c2261bd0004e61feda2c16aa5e21ffa8d7e7f7dbf6ec379a43b48e4b36aeb0
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_twenty_two(self):
        QCAVSx = 0x45fb02b2ceb9d7c79d9c2fa93e9c7967c2fa4df5789f9640b24264b1e524fcb1
        QCAVSy = 0x5c6e8ecf1f7d3023893b7b1ca1e4d178972ee2a230757ddc564ffe37f5c5a321
        dIUT = 0x334ae0c4693d23935a7e8e043ebbde21e168a7cba3fa507c9be41d7681e049ce
        ZIUT = 0x2adae4a138a239dcd93c243a3803c3e4cf96e37fe14e6a9b717be9599959b11c
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_twenty_three(self):
        QCAVSx = 0xa19ef7bff98ada781842fbfc51a47aff39b5935a1c7d9625c8d323d511c92de6
        QCAVSy = 0xe9c184df75c955e02e02e400ffe45f78f339e1afe6d056fb3245f4700ce606ef
        dIUT = 0x2c4bde40214fcc3bfc47d4cf434b629acbe9157f8fd0282540331de7942cf09d
        ZIUT = 0x2e277ec30f5ea07d6ce513149b9479b96e07f4b6913b1b5c11305c1444a1bc0b
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())

    def test_nist_vector_twenty_four(self):
        QCAVSx = 0x356c5a444c049a52fee0adeb7e5d82ae5aa83030bfff31bbf8ce2096cf161c4b
        QCAVSy = 0x57d128de8b2a57a094d1a001e572173f96e8866ae352bf29cddaf92fc85b2f92
        dIUT = 0x85a268f9d7772f990c36b42b0a331adc92b5941de0b862d5d89a347cbf8faab0
        ZIUT = 0x1e51373bd2c6044c129c436e742a55be2a668a85ae08441b6756445df5493857
        a = "{0:0>{width}x}".format(dIUT, width=bitLen(genP256.ecc.n) // 4)
        B = ECPoint(QCAVSx, QCAVSy, secp256r1)
        Z = ecdh(a, B)
        Zi_str = "{0:0>{width}X}".format(ZIUT, width=bitLen(genP256.ecc.n) // 4)
        self.assertEqual(Z, Zi_str.upper())


if __name__ == '__main__':
    unittest.main()
