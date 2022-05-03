# Arkkitehtuuri

## Rakenne

Pakkauskaavio sovelluksen toiminnasta

![Screenshot from 2022-04-12 18-20-38](https://user-images.githubusercontent.com/95504014/162996756-450cd265-69e4-4da5-ba73-b0fd9e66e222.png)

## Sovelluslogiikka

Sovelluksessa luokat [Expence](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/src/entities/expence.py) ja [User](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/src/entities/user.py) muodostavat pohjan sovelluksessä käytettäville käyttäjille sekä menoilla/tuloille. Näitä voidaan kuvata seuraavasti:

```mermaid
 classDiagram
  Expence "*" --> "1" User
    class User{
      username
      password
    }
    class Expence{
      expence
      amount
      description
      expence_id
      username
      date
    }
```

Sovelluksen suurimmasta osasta toiminnallisuudesta vastaa luokka [BudgetService](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/src/services/budget_service.py), joka tarjoaa sovellukselle muun muassa seuraavat metodit:

- `add_expence(description, amount, username, date, expence)`
- `create_user(username, password)`
- `this_month_budget(username)`
- `delete_expence(expence_id)`

Yhteydestä tietokantaan sekä tiedostoihin hoitavat [BudgerRepository](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/src/repositories/budget_repository.py) ja [UserRepository](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/src/repositories/user_repository.py) luokkien oliot ja metodit

Luokkien välistä suhdetta kuvaava luokkakaavio:
![luokka_kaavio](https://user-images.githubusercontent.com/95504014/166419945-30719fde-28fb-4bdc-9b78-2a1e9dc665de.png)

## Pysyvä tallennus

Sovelluksella on kaksi tapaa tallentaa tietoa pysyvästi. `BudgetRepository` huolehtii menojen ja tulojen tallentamisesta, jotka tallennetaan 
CSV tiedostoon ja `UserRepository` tallentaa käyttäjät ja niihin liittyvät tiedot, jotka puolestaa tallennetaan SQLite-tietokantaan. 

### Tiedostot
Menot ja tulot sekä käyttäjät tallennetaan erillisiin tiedostoihin. Tiedostojen nimet määritellään juurihakemistosta löytyvässä [.env](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/.env)-tiedostossa.

`BudgetRepository`-luokka tallentaa CSV-tiedostoon seuraavalla tyylillä:
```
5dd09b8b-8f5b-450d-bb8d-f37cd9f0b83a;False;654.32;Palkka;Tyyppi;02-05-2022
68788a8d-63d1-4c2e-940a-4eeb26fd2cac;True;-12.34;Ruokaostokset;Henkilö;30-04-2022
```
Tallenustapa on siis menon/tulon id, totuusarvo joka kertoo, onko kyseessä meno vai tulo, määrä, kuvaus, käyttäjätunnut ja päivämäärä. Osat erotetaan toisistaan puolipisteellä (;).

`UserRepository`-luokka tallentaa käyttäjät SQLite-tietokannan tauluun `users`. Tietokanta alustetaan tiedostossa [initialize_database.py](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/src/initialize_database.py) sovellusta rakentaessa.

## Päätoiminnallisuudet

Sovelluksen toiminnallisuuksia kuvattuna sekvenssikaavioilla

### Sisään kirjautuminen

Käyttäjä antaa käyttäjänimen ja salasanan syötekenttiin, jonka jälkeen hän painaa "Kirjaudu sisään" -nappia, josta seuraa seuraavat tapahtumat:

![login_sekvenssi_kaavio](https://user-images.githubusercontent.com/95504014/166416534-ad98f790-c874-46b5-8915-7b0c62711023.png)

### Uuden käyttäjän luominen

Kun käyttäjä on syöttänyt haluamansa käyttäjänimen ja salasanan käyttöliittymässä teksikenttiin, painamalla nappia "Luo käyttäjä" tapahtuu seuraavat toimenpiteet

![new-user_sekvenssi_kaavio](https://user-images.githubusercontent.com/95504014/166416692-537e5d64-fbfe-45c6-9f7f-be443c30439f.png)

### Uusi meno sekä tulo

Käyttäjä antaa sovelluksessa tiedon menon tai tulon nimestä, menon/tulon määrän sekä valitsee päivämäärän, jolloin se on lisätty. Tämän jälkeen painamalla nappia "Lisää tulo" tai "Lisää meno", riippuen kumpaa lisätään, tapahtuu seuraavat tapahtumat:

Menon lisäys:
![add_expence_sekvenssi_kaavio](https://user-images.githubusercontent.com/95504014/166416878-40037b3d-c638-4f07-9a49-c00afa8fe8b4.png)

Tulon lisäsys:
![add_income_sekvenssi_kaavio](https://user-images.githubusercontent.com/95504014/166416884-c7d05f98-d092-4c1a-a410-68f4f7205da5.png)
