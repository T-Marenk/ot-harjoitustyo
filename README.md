# Budjetointisovellus

Tämä projekti on Helsingin yliopiston kurssia *Ohjelmistotekniikka* varten.

Sovellusksen tarkoitus on auttaa käyttäjiä seuraamaan rahankäyttöään ja auttaa heitä budjetoimaan menojaan ja tulojaan

## Dokumentaatio

[vaatimuusmaarittely.md](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito.md](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjapito.md)

[changelog.md](TODO)

## Nykyinen tilanne

Sovellus on vasta hyvin alkuvaiheissa. Väliaikaisesti käyttöliittymänä toimii yksinkertainen testiliittymä, jolla pystyy testaamaan nykyisiä toimintoja. Tämä vaihtuu myöhemmin graafiseksi käyttöliittymäksi

Toiminnassa olevat ominaisuudet

- Menojen lisääminen sovellukseen
- Tulojen lisääminen sovellukseen
- Menot ja tulot tallennetaan tiedostoon, josta ne voi lukea seuraavalla suorituskerralla myös

Puuttuvat toiminnot

- Käyttäjät
- Menojen ja tulojen tarkastelu
- Menojen ja tulojen poisto

## Asennus

1. Asenna riippuvuudet suorittamalla:

```bash
poetry install
```

2. Sovelluksen saa käyntiin komennolla:

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
