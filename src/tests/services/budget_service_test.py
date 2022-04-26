import unittest
from services.budget_service import BudgetService
from entities.expence import Expence
from entities.user import User


class FakeBudgetRepository:
    def __init__(self, expences=None):
        self.expences = expences or []

    def add_expence(
            self,
            expence
    ):
        self.expences.append(expence)

        return self.expences

    def find_all(
        self
    ):
        return self.expences
    
    def delete_all(self):
        self.expences = []

class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def create_user(self, username, password):
        user = User(username, password)
        self.users.append(user)
    
    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user

class TestBudgetService(unittest.TestCase):
    def setUp(self):
        self.budget_service = BudgetService(
            FakeBudgetRepository(),
            FakeUserRepository()
        )
         
        self.budget_service.create_user('Tyyppi', '1234') 
        self.budget_service.add_expence('Soda', 2, 'Tyyppi', True)

        self.budget_service.add_expence('Bread', 3.12, 'Henkilö', True)
    def test_find_all_finds_all(self): 
        expences = self.budget_service.find_all()

        self.assertEqual(len(expences), 2)

    def test_add_expence(self):
        expences = self.budget_service.find_all()

        self.assertEqual(expences[0].description, 'Soda')
        self.assertEqual(expences[0].amount, -2)
        self.assertEqual(expences[0].expence, True)

    def test_login(self):
        self.budget_service.login('Tyyppi', '1234')

        user = self.budget_service.get_user()
       
        self.assertEqual(user.username, 'Tyyppi')

    def test_logout(self):
        self.budget_service.login('Tyyppi', '1234')
        self.budget_service.logout()

        user = self.budget_service.get_user()

        self.assertEqual(user, None)

    def test_delete_all(self):
        self.budget_service.delete_all()
        expences = self.budget_service.find_all()

        self.assertEqual(expences, [])
