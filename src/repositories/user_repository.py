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
        """

        self._connection = connection

    def find_user(
            self,
            username
    ):
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

        cursor = self._connection.cursor()

        cursor.execute(
            'INSERT INTO users (username, password) VALUES (?, ?)',
            (username, password)
        )

        self._connection.commit()

    def delete_all(
        self,
    ):

        cursor = self._connection.cursor()

        cursor.execute('delete from users')

        self._connection.commit()


user_repository = UserRepository(get_database_connection())
