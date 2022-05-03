import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()

    def test_create_user(self):
        user_repository.create_user('Tyyppi', '1234')
        user = user_repository.find_all()

        self.assertEqual(user[0].username, 'Tyyppi')
        self.assertEqual(user[0].password, '1234')

    def test_find_user(self):
        user_repository.create_user('Tyyppi', '1234')
        user_repository.create_user('Henkilö', '5678')

        user = user_repository.find_user('Henkilö')

        self.assertEqual(user.username, 'Henkilö')
        self.assertEqual(user.password, '5678')
