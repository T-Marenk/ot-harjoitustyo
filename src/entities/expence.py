import uuid

class Expence:
    """Luokka, jonka avulla kuvastetaan yksittäistä menoa tai tuloa
    """

    def __init__(
            self,
            expence,
            amount,
            expence_id=None
    ):
        """Luokan konstrukti, joka luo menon tai tulon
        
        Args:
            expence: kuvaus menosta tai tulosta
            amount: menon tai tulon määrä
            expence_id: Menon tai tulon id:tä kuvaava osa. Luodaan automaattisesti uuid:llä
        """

        self.expence = expence
        self.amount = amount
        self.expence_id = expence_id or str(uuid.uuid4())
