# Changelog

## Viikko 3

- Sovellukseen pystyy lisäämään menon tai tulon
- Lisätty BudgetRepository luokka, joka kirjoittaa expences.csv tiedostoon menot ja tulot
- Lisätty BudgetService, joka vastaa sovelluslogiikasta
- Lisätty Expence luokka, joka kuvastaa yhtä menoa tai tuloa
- Testattu, että BudgetRepository luokka lisää menot ja tulot oikealla tavalla tiedostoon

## Viikko 4

- Graafinen käyttöliittymä lisätty
- Pohja käyttäjille
  - Lisätty User luokka, joka kuvaa yhtä käyttäjää
  - Lisätty UserRepository, joka vastaa yhteydestä tietokantaan
- Käyttöliittymässä pystyy näkemään lisätyt menot ja tulot
- Sqlite tietokanta, johon tallennetaan käyttäjien tieto
- Testien määrää lisätty, aloitettu BudgetService luokan testaaminen
