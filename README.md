# Budjetointisovellus

Tämä projekti on Helsingin yliopiston kurssia *Ohjelmistotekniikka* varten.

Sovellusksen tarkoitus on auttaa käyttäjiä seuraamaan rahankäyttöään ja auttaa heitä budjetoimaan menojaan ja tulojaan

## Dokumentaatio

[vaatimuusmaarittely.md](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito.md](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjapito.md)

[changelog.md](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[arkkitehtuuri.md](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[kayttoohje.md](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

## Releases

[Release 1](https://github.com/T-Marenk/ot-harjoitustyo/releases/tag/viikko5)

## Nykyinen tilanne

Sovellusta pystyy käyttämään graafisessa käyttöliitymässä, jossa pystyy näkemään menot ja tulot sekä lisäämään niitä käyttäjä kohtaisesti. Käyttäjä on 

Toiminnassa olevat ominaisuudet

- Menojen lisääminen sovellukseen
- Tulojen lisääminen sovellukseen
- Menot ja tulot tallennetaan tiedostoon, josta ne voi lukea myös seuraavalla suorituskerralla
- Menot ja tulot nähtävissä sovelluksessa
- Yksittäisten menojen ja tulojen poistaminen
- Tapahtumilla on päivämäärät
  - Näe kaikki tapahtumat
  - Näe vain meneillään olevan kuukauden tapahtumat 

Puuttuvat toiminnot

- Näe vain menot tai tulot
- Kuukausittaisen budjetin asettaminen

## Asennus

1. Asenna riippuvuudet suorittamalla:

```bash
poetry install
```

2. Loput vaaditut aloitustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Sovelluksen saa käyntiin komennolla:

```bash
poetry run invoke start
```

### Testaaminen

Luodut testit on mahdollista ajaa komennolla

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuus on mahdollista luoda komennolla

```bash
poetry run invoke coverage-report
```

Raportti luodaan _htmlcov_-hakemistoon.
