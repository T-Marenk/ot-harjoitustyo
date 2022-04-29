from entities.expence import Expence

from repositories.budget_repository import budget_repository as default_budget_repository

from repositories.user_repository import user_repository as default_user_repository


class BudgetService:
    def __init__(
            self,
            budget_repository=default_budget_repository,
            user_repository=default_user_repository
    ):
        """Luokan konstrukti
        """

        self._user = None
        self._user_repository = user_repository
        self._budget_repository = budget_repository

    def get_user(self):
        """Nykyisen käyttäjän haku

        Returns:
            nykyisen käyttäjän
        """

        return self._user

    def add_expence(
            self,
            description,
            amount,
            username,
            date,
            expence
    ):
        """Lisää menon budjettiin.

        Args:
            amount: Menon suuruus
            description: Kuvaus menosta tai tulosta
            username: Käyttäjä, jolle meno/tulo lisätään
            date: menon/tulon päivämäärä
            expence: totuusarvo, joka kertoo, onko kyseessä meno vai tulo
        """

        if expence:
            amount *= -1

        expence = Expence(expence, amount, description, username, date)

        self._budget_repository.add_expence(expence)

    def login(
            self,
            username,
            password
    ):
        """Kirjaa käyttäjän sisään sovellukseen

        Args:
            username: käyttäjän käyttäjänimi
            password: käyttäjän salasana
        Returns:
            totuusarvon, joka kertoo, onnistuiko sisään kirjautuminen
        """

        user = self._user_repository.find_user(username)
        if not user:
            return True
        if user.password == password:
            self._user = user
            return False
        return True

    def logout(
            self
    ):
        """Kirjaa käyttäjän ulos sovelluksesta
        """

        self._user = None

    def create_user(
            self,
            username,
            password
    ):
        """Luo uuden käyttäjän sovellukseen

        Args:
            username: uuden käyttäjän käyttäjänimi
            password: uuden käyttäjän salasana
        """
        user = self._user_repository.find_user(username)
        
        if user:
            return False

        self._user_repository.create_user(username, password)
        
        return True

    def find_all(
            self
    ):
        """Hakee kaikki menot ja tulot
        """

        expences = self._budget_repository.find_all()

        return expences

    def delete_expence(
            self,
            expence_id
    ):
        """Poistaa yhden menon/tulon

        Args:
            expence_id: Menon/tulon id
        """

        self._budget_repository.delete_expence(expence_id)

    def delete_all(
            self
    ):
        """Poistaa kaikki menot ja tulot
        """

        self._budget_repository.delete_all()

    def find_expence(
            self
    ):
        pass

    def find_income(
            self
    ):
        pass

budget_service = BudgetService()
