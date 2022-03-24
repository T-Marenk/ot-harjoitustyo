import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikea_aluksi(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_onnistuu(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.1")

    def test_saldo_vahenee_oikealla_tavalla(self):
        self.maksukortti.lataa_rahaa(100)
        self.maksukortti.ota_rahaa(50)
        self.assertEqual(str(self.maksukortti), "saldo: 0.6")

    def test_saldo_ei_mene_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_otto_palauttaa_true(self):
        arvo = self.maksukortti.ota_rahaa(10)
        self.assertEqual(arvo, True)

    def test_rahan_otto_palauttaa_false(self):
        arvo = self.maksukortti.ota_rahaa(20)
        self.assertEqual(arvo, False)
