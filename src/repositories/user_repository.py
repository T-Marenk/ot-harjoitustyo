from database_connection import get_database_connection
from entities.user import User


def get_user(row):
    return User(row['username'], row['password']) if row else None


class UserRepository:
    """Käyttäjä tietokannan yhteydestä vastaava luokka
    """

    def __init__(
            self,
            connection
    ):
        """Luokan konstruktori

        Args:
            connection: yhteys SQLite-tietokantaan
        """

        self._connection = connection

    def find_user(
            self,
            username
    ):
        """Hakee tietyn käyttäjän tietokannasta

        Args:
            username: halutun käyttäjän käyttäjänimi
        Returns:
            Halutun käyttäjän, jos se löytyi tietokannasta
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM USERS WHERE username = ?',
            (username,)
        )

        row = cursor.fetchone()

        return get_user(row)

    def create_user(
        self,
        username,
        password
    ):
        """Luo uuden käyttäjän tietokantaan

        Args:
            username: käyttäjänimi uudelle käyttäjälle
            password: salasana uudelle käyttäjälle
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'INSERT INTO users (username, password) VALUES (?, ?)',
            (username, password)
        )

        self._connection.commit()

    def find_budget(
            self,
            username,
            month
    ):
        """Hakee tietokannasta käyttäjän kuukauden budjetin

        Args:
            username: Halutun käyttäjän käyttäjänimi
            month: Halutun kuukauden budjetti
        Returns:
            Käyttäjän kuukauden budjetin
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT budget FROM budget WHERE username=? AND month=?', (
                username, month)
        )

        budget = cursor.fetchone()

        return budget

    def set_budget(
            self,
            username,
            budget,
            month
    ):
        """Asettaa käyttäjälle budjetin kuukaudelle

        Args:
            username: halutun käyttäjän käyttäjänimi
            budget: bujetti kuukaudelle
            month: kuukausi, jolle budjetti asetetaan
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'INSERT INTO budget (username, budget, month) VALUES (?, ?, ?)',
            (username, budget, month)
        )

        self._connection.commit()

    def update_budget(
            self,
            username,
            budget,
            month
    ):
        """Päivittää tietokannassa käyttäjän budjetin

        Args:
            username: halutun käyttäjän käyttäjänimi
            budget: budjetti kuukaudelle
            month: kuukausi, jolle budjetti asetetaan
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'UPDATE budget SET budget=? WHERE username=? AND month=?',
            (budget, username, month)
        )

        self._connection.commit()

    def find_all(self):
        """Hakee tietokannasta kaikki käyttäjät

        Returns:
            Kaikki tietokannasta löytyvät käyttäjät
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM users'
        )

        rows = cursor.fetchall()

        return [get_user(row) for row in rows]

    def delete_all(
        self,
    ):
        """Poistaa kaikki käyttäjät tietokannasta
        """

        cursor = self._connection.cursor()

        cursor.execute('delete from users')

        self._connection.commit()


user_repository = UserRepository(get_database_connection())
