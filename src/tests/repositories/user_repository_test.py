import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()

    def test_create_user_correctly(self):
        user_repository.create_user('Tyyppi', '1234')
        user = user_repository.find_all()

        self.assertEqual(user[0].username, 'Tyyppi')
        self.assertEqual(user[0].password, '1234')

    def test_find_correct_user(self):
        user_repository.create_user('Tyyppi', '1234')
        user_repository.create_user('Henkilö', '5678')

        user = user_repository.find_user('Henkilö')

        self.assertEqual(user.username, 'Henkilö')
        self.assertEqual(user.password, '5678')

    def test_set_budget_to_user(self):
        user_repository.create_user('Tyyppi', '1234')
        user_repository.set_budget('Tyyppi', '650', '05')

        budget = user_repository.find_budget('Tyyppi', '05')

        self.assertEqual(budget[0], 650)

    def test_update_user_budget(self):
        user_repository.create_user('Tyyppi', '1234')
        user_repository.set_budget('Tyyppi', '650', '05')

        budget = user_repository.find_budget('Tyyppi', '05')

        self.assertEqual(budget[0], 650)

        user_repository.update_budget('Tyyppi', '450', '05')

        budget = user_repository.find_budget('Tyyppi', '05')

        self.assertEqual(budget[0], 450)

    def test_get_correct_user_budget(self):
        user_repository.create_user('Tyyppi', '1234')
        user_repository.create_user('Henkilö', '5678')

        user_repository.set_budget('Tyyppi', '650', '05')
        user_repository.set_budget('Henkilö', '300', '05')

        budget = user_repository.find_budget('Henkilö', '05')

        self.assertEqual(budget[0], 300)

    def test_get_correct_month_budget(self):
        user_repository.create_user('Tyyppi', '1234')

        user_repository.set_budget('Tyyppi', '650', '05')
        user_repository.set_budget('Tyyppi', '300', '06')

        budget = user_repository.find_budget('Tyyppi', '06')

        self.assertEqual(budget[0], 300)
