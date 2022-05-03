# Käyttöohje

Lataa projektin viimeisin version [releasin] _Assests_ osion alta valitsemalla _Source code_.

## Ohjelman käynnistäminen

Ennen ensimmäistä suoritus kertaa asenna tarvittavat riippuvuudet:

```bash
poetry install
```

Jonka jälkeen suorita sovellukselle alkutoimenpiteet:

```bash
poetry run invoke build
```

Tämän jälkeen voit käynnistää sovelluksen:

```bash
poetry run invoke start
```

## Kirjautuminen

Sovelluksen käynnistys käynnistää kirjautumisnäkymän:

![kirjautuminen](https://user-images.githubusercontent.com/95504014/166429090-49518dbb-e32b-4c66-946d-e5c434570c3a.png)

Sisään kirjautuminen on mahdollista olemassa olevalle käyttäjälle kirjoittamalla käyttäjän käyttäjätunnus ylempään kenttään, salasana alempaan kenttään,jonka jälkeen painamalla "Kirjaudu sisään"-nappia pääsee kirjautumaan sisälle

## Uuden käyttäjän luominen

Uuden käyttäjän luomisnäkymään pääsee kirjautumisnäkymästä painamalla "Uusi käyttäjä" -painiketta

Tämä avaa seuraavan näkymän:

![new_user](https://user-images.githubusercontent.com/95504014/166429512-3f7235e9-eac8-4c05-b445-c092212e2d68.png)

Kirjoittamalla syöttökenttiin uuden käyttäjän tiedot ja painamalla "Luo käyttäjä" -nappia saa luotua uuden käyttäjän

Jos käyttäjän luominen onnistuu, palaa sovellus kirjautusnäkymään

## Budjetin tarkastelu sekä menojen ja tulojen poisto

Onnistunut sisään kirjautuminen tuo esille päänäkymän.

Tässä näkymässä näkee lisätyt menot ja tulot. Painamalla "Näytä kaikki tapahtumat" näet kaikki menot ja tulot ja painamalla "Näytä tämän kuun tapahtumat" näet vain meneillään olevan kuukauden tapahtumat

Tapahtuman poistaminen onnistuu painamalla "Poista" halutun tapahtuman vieressä

![päänäkymä](https://user-images.githubusercontent.com/95504014/166429955-8e1542a0-ce33-45bb-b84b-4d44a253187d.png)

Mikäli poisto onnistuu, sitä ei ole enään näkyvillä näkymässä

Painamalla näkymässä olevaa "Kirjaudu ulos" painiketta pääsee kirjautumaan ulos. Tämä näyttää taas kirjautumisnäkymän, josta pääsee kirjautumaan sisään toisella käyttäjällä

## Menojen ja tulojen lisääminen

Päänäkymästä pääsee lisäämään uuden menon tai tulon painamalla "Lisää meno" tai "Lisää tulo" nappia

Molemmat näkymät toimivat samalla tavalla. Täyttämällä vaaditut tiedot syöttökenttiin ja valitsemalla kalenterista päivämäärän, jonka jälkeen painamalla joko "Lisää meno" tai "Lisää tulo" nappia saa tapahtuman lisättyä sovellukseen

![Lisaa_meno](https://user-images.githubusercontent.com/95504014/166430544-2c6a7545-cb25-4a9b-8a27-112601e26562.png)

![lisaa_tulo](https://user-images.githubusercontent.com/95504014/166430616-a86d2169-51fc-45bf-93eb-407e0e3f46f1.png)

Mikäli lisääminen onnistuu, näyttää sovellus päänäkymän, jossa juuri lisätty tapahtuma on myös näkyvillä
