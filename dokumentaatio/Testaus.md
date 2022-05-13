# Testausdokumentti

Ohjelman testaus on suoritettu automatisoiduin unittesteillä sekä manuaalisesti testatuin järjestelmätason testeinä

## Automatisoidut testit

### Sovelluslogiikka

Sovelluslogiikasta vastaava `BudgeService`-luokka testataan ![TestBudgetService](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/src/tests/services/budget_service_test.py)-luokalla. 
Testausta varten `BudgetService`-luokan alustus toimii niin, että sille injektoidaan riippuvuuksiksi repositorio-oliot, jotka pysyväistallennuksen sijasta
tallentavat tiedot vain muistiin. Testejä varten on luotu luokat `FakeBudgetRepository` ja `FakeUserRepository`, jotka hoitavat tallennuksen testeissä.

### Repositoriot

TODO

### Testauskattavuus

Käyttöliittymä pois lukien sovelluksen testauskattavuus on 98%

![](https://github.com/T-Marenk/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/coverage_report.png)

Testaus ei suorita _build.py_ tai _initialize_databse.py_ komentoriviltä. Testaus ei testaa tilannetta, jossa yritetään hakea kirjautumattoman
käyttäjän budjettia.

## Järjestelmätestaus

TODO

### Asentaminen ja konfigurointi

TODO
