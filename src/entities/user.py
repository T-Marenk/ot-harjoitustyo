class User:
    """Luokka, jonka avulla kuvastetaan yksittäistä käyttäjää
    """
    def __init__(
            self,
            username,
            password
    ):
        """Luoka konstrukti

        Args:
            username: käyttäjän käyttäjänimi
            password: käyttäjän salasana
        """

        self.username = username
        self.password = password
