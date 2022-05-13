import uuid


class Expence:
    """Luokka, jonka avulla kuvastetaan yksittäistä menoa tai tuloa
    """

    def __init__(
            self,
            expence,
            amount,
            description,
            username,
            date,
            expence_id=None
    ):
        """Luokan konstrukti, joka luo menon tai tulon

        Args:
            expence: totuusarvo, joka kertoo, onko kyseessä tulo vai meno
            amount: menon tai tulon määrä
            description: Kuvaus tulosta tai menosta
            username: Osa, joka kertoo mille käyttäjälle kyseinen meno kuuluu
            date: tapahtuman päivämäärä
            expence_id: Menon tai tulon id:tä kuvaava osa. Luodaan automaattisesti uuid:llä
        """

        self.expence = expence
        self.amount = amount
        self.description = description
        self.expence_id = expence_id or str(uuid.uuid4())
        self.username = username
        self.date = date
