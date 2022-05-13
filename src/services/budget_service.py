from time import localtime, strftime

from entities.expence import Expence

from repositories.budget_repository import budget_repository as default_budget_repository

from repositories.user_repository import user_repository as default_user_repository


class WrongUsernameError(Exception):
    pass


class WrongPasswordError(Exception):
    pass


class NotaNumberError(Exception):
    pass


class DescriptionTooLongError(Exception):
    pass


class PasswordsDontMatchError(Exception):
    pass


class UsernameTakenError(Exception):
    pass


class NoPasswordError(Exception):
    pass


class NoUsernameError(Exception):
    pass


class NoDescriptionError(Exception):
    pass


class BudgetService:
    """Sovelluslogiikasta vastaava luokka
    """

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
        """Hakee nykyisen käyttäjän

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

        Raises:
            NotaNumber: Tuottaa virheen, jos annettu määrä ei ole positiivinen numero
            DescriptionTooLong: Tuottaa virheen, jos tapahtuman kuvaus on yli 40 merkkiä pitkä
        """
        try:
            amount = float(amount)
        except ValueError as error:
            raise NotaNumberError() from error

        if amount < 0:
            raise NotaNumberError()

        if description == "":
            raise NoDescriptionError()

        if len(description) > 40:
            raise DescriptionTooLongError()

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

        Raises:
            WrongUsername: Käyttäjänimeä ei löytynyt tietokannasta
        Returns:
            totuusarvon, joka kertoo, onnistuiko sisään kirjautuminen
        """

        user = self._user_repository.find_user(username)

        if not user:
            raise WrongUsernameError()
        if user.password != password:
            raise WrongPasswordError()
        self._user = user

    def logout(
            self
    ):
        """Kirjaa käyttäjän ulos sovelluksesta
        """

        self._user = None

    def create_user(
            self,
            username,
            password,
            password2
    ):
        """Luo uuden käyttäjän sovellukseen

        Args:
            username: uuden käyttäjän käyttäjänimi
            password: uuden käyttäjän salasana
            password2: uuden käyttäjän salasana toiseen kertaan1

        Raises:
            UsernameTaken: Virhe, jos käyttäjänimi on jo olemassa
            PasswordsDontMatch: Virhe, jos salasanat eivät ole samat
        """

        user = self._user_repository.find_user(username)

        if user:
            raise UsernameTakenError()

        if username == "":
            raise NoUsernameError()

        if password != password2:
            raise PasswordsDontMatchError()

        if password == "":
            raise NoPasswordError()

        self._user_repository.create_user(username, password)

    def find_all(
            self
    ):
        """Hakee kaikki menot ja tulot
        """

        expences = self._budget_repository.find_all()

        return expences

    def find_by_username(
            self,
            username
    ):
        """Hakee tietyn käyttäjän menot ja tulot

        Args:
            username: halutun käyttäjän menot ja tulot
        Returns:
            Käyttäjän kaikki menot ja tulot
        """

        return self._budget_repository.find_by_username(username)

    def this_month_budget(
            self,
            username
    ):
        """Hakee meneillään olevan kuukauden menot ja tulot

        Args:
            username: Käyttäjä, jonka menot ja tulot halutaan
        Returns:
            Kuun menot ja tulot käyttäjälle
        """

        current_month = strftime("%m-%Y", localtime())

        all_expences = self._budget_repository.find_by_username(username)
        expences = []

        for expence in all_expences:
            if expence.date[3:10] == current_month:
                expences.append(expence)

        return expences

    def find_expences(self, username, month=False):
        """Hakee tietokannasta käyttäjän menot

        Args:
            username: Haluttu käyttäjä
            month: Kertoo, haetaanko tämän kuukauden vai kaikki menot
        Returns:
            Halutut menot
        """

        if month:
            current_month = strftime("%m-%Y", localtime())

        all_expences = self._budget_repository.find_by_username(username)
        expences = []

        for expence in all_expences:
            if month:
                if expence.expence == "True" and current_month == expence.date[3:10]:
                    expences.append(expence)
            else:
                if expence.expence == "True":
                    expences.append(expence)

        return expences

    def find_income(
            self,
            username,
            month=False
    ):
        """Hakee tietokannasta käyttäjän tulot

        Args:
            username: Haluttu käyttäjä
            month: Totuusarvo, joka kertoo, haetaanko vain nykyisen kuukauden tulot
        Returns:
            Halutut tulot
        """

        if month:
            current_month = strftime("%m-%Y", localtime())

        all_expences = self._budget_repository.find_by_username(username)
        expences = []

        for expence in all_expences:
            if month:
                if expence.expence == "False" and current_month == expence.date[3:10]:
                    expences.append(expence)
            else:
                if expence.expence == "False":
                    expences.append(expence)

        return expences

    def find_budget(
            self
    ):
        """Hakee budjetin nykyisen tilanteen

        Returns:
            alkuperäisen budjetin ja jäljellä olevan budjetin, jos on asetettu budjetti
            muuten palauttaa menojen ja tulojen summan
        """

        month = strftime("%m", localtime())

        username = self._user.username

        budget = self._user_repository.find_budget(username, month)

        if budget:
            budget = budget[0]
            left_budget = budget

            expences = self.find_expences(username, True)

            for expence in expences:
                left_budget += float(expence.amount)

            return budget, left_budget

        expences = self.this_month_budget(username)
        budget = 0

        for expence in expences:
            budget += float(expence.amount)

        return 0,  budget

    def set_month_budget(
            self,
            budget
    ):
        """Asettaa käyttäjälle kuukauden budjetin

        Args:
            budget: haluttu budjetti
        """

        try:
            budget = float(budget)
        except ValueError as error:
            raise NotaNumberError from error

        if budget < 0:
            raise NotaNumberError()

        month = strftime("%m", localtime())

        username = self._user.username

        e_budget = self._user_repository.find_budget(username, month)

        if e_budget:
            self._user_repository.update_budget(username, budget, month)
        else:
            self._user_repository.set_budget(username, budget, month)

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

    def find_user(
            self,
            username
    ):
        """Hakee tietokannasta tietyn käyttäjän

        Args:
            username: halutun käyttäjän käyttäjänimi
        Returns:
            Halutun käyttäjän
        """

        return self._user_repository.find_user(username)


budget_service = BudgetService()
