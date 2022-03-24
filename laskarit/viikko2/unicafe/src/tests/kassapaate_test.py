import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_rahamaara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luotu_kassapaate_edullisten__maara_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_luotu_kassapaate_maukkaiden_maara_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_kateinen_lisaa_kassassa_olevaa_rahamaaraa_oikean_maaran_ja_oikea_vaihtoraha(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihto, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_maukkaasti_kateinen_lisaa_kassaan_oikean_maaran_ja_oikea_vaihtoraha(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(vaihto, 50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_edullinen_kateisella_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaasti_kateisella_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullisesti_kateisella_liian_pieni_maksu_toimii_oikein(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihto, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaasti_kateisella_liian_pieni_maksu_toimii_oikein(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(350)
        self.assertEqual(vaihto, 350)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisesti_kortilla_veloitetaan_oikea_maara_ja_palautetaan_true(self):
        kortti = Maksukortti(240)
        arvo = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti), "saldo: 0.0")
        self.assertEqual(arvo, True)

    def test_maukkaasti_kortilla_veloitetaan_oikea_maara_ja_palautetaan_true(self):
        kortti = Maksukortti(440)
        arvo = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti), "saldo: 0.4")
        self.assertEqual(arvo, True)

    def test_edullisesti_kortilla_kasvattaa_lounaiden_maaraa(self):
        kortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaasti_kortilla_kasvattaa_lounaiden_maaraa(self):
        kortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullisesti_kortilla_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(50)
        arvo = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(arvo, False)
        self.assertEqual(str(kortti), "saldo: 0.5")
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaasti_kortilla_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(150)
        arvo = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(arvo, False)
        self.assertEqual(str(kortti), "saldo: 1.5")
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortilla_syodessa_kassa_ei_muutu(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_ladattava_raha_nakyy_kortilla(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 240)
        self.assertEqual(str(kortti), "saldo: 2.4")

    def test_kortille_ladattava_raha_on_kassassa(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 550)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100550)

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, -20)
        self.assertEqual(str(kortti), "saldo: 0.0")
