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

## Viikko 5

- Sisään- ja uloskirjautuminen lisätty
- Käyttäjän luominen mahdollista
- Käyttäjä kohtaiset menot ja tulot
- Testien määrää lisätty

## Viikko 6

- Tapahtumille lisätty päivämäärä
  - Tapahtumaa lisätessä pystyy valitsemaan päivämäärän
- Mahdollista nähdä tapahtumat meneillään olevalta kuukaudelta tai kaikki tapahtumat
- Testejä lisätty
  - `UserRepository` luokan testaaminen aloitettu
  - Vanhojen testien korjaaminen toimimaan nykyisellä tilanteella
  - Päivämäärien toimivuus testeissä
- Käyttöliittymän parantaminen
  - Paremmin asetellut painikkeet ja parempi käyttökokemus 
