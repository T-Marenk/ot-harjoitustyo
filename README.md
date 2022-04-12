# Budjetointisovellus

Tämä projekti on Helsingin yliopiston kurssia *Ohjelmistotekniikka* varten.

Sovellusksen tarkoitus on auttaa käyttäjiä seuraamaan rahankäyttöään ja auttaa heitä budjetoimaan menojaan ja tulojaan

## Dokumentaatio

[vaatimuusmaarittely.md](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito.md](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjapito.md)

[changelog.md](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[arkkitehtuuri.md](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

## Nykyinen tilanne

Sovellusta pystyy käyttämään graafisessa käyttöliitymässä, jossa pystyy näkemään menot ja tulot sekä lisäämään niitä

Toiminnassa olevat ominaisuudet

- Menojen lisääminen sovellukseen
- Tulojen lisääminen sovellukseen
- Menot ja tulot tallennetaan tiedostoon, josta ne voi lukea seuraavalla suorituskerralla myös
- Menot ja tulot nähtävissä sovelluksessa

Aloitetut toiminnot, mutta hyvin keskeneräiset

- Käyttäjät

Puuttuvat toiminnot

- Menojen ja tulojen poisto

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
