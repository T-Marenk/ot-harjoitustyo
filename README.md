# Budjetointisovellus

Tämä projekti on Helsingin yliopiston kurssia *Ohjelmistotekniikka* varten.

Sovellusksen tarkoitus on auttaa käyttäjiä seuraamaan rahankäyttöään ja auttaa heitä budjetoimaan menojaan ja tulojaan

## Dokumentaatio

[Vaatimuusmäärittely](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjapito.md)

[Changelog](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

[Testausdokumentto](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/dokumentaatio/Testaus.md)

## Releases

[Release 1](https://github.com/T-Marenk/ot-harjoitustyo/releases/tag/viikko5)

[Release 2](https://github.com/T-Marenk/ot-harjoitustyo/releases/tag/viikko6)

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

## Muut toiminnot

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

### Pylint

Seuraavalla komennolla on mahdollista suorittaa [.pylintrc](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/.pylintrc) määritellyt tarkistukset:

```bsah
poetry run invoke lint
```
