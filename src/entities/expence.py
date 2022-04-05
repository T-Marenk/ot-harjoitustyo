import uuid

class Expence:
    """Luokka, jonka avulla kuvastetaan yksittäistä menoa tai tuloa
    """

    def __init__(
            self,
            expence,
            amount,
            description,
            expence_id=None
    ):
        """Luokan konstrukti, joka luo menon tai tulon
        
        Args:
            expence: totuusarvo, joka kertoo, onko kyseessä tulo vai meno
            amount: menon tai tulon määrä
            expence_id: Menon tai tulon id:tä kuvaava osa. Luodaan automaattisesti uuid:llä
            description: Kuvaus tulosta tai menosta
        """

        self.expence = expence
        self.amount = amount
        self.description = description
        self.expence_id = expence_id or str(uuid.uuid4())