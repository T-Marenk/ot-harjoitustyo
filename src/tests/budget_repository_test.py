import unittest
from repositories.budget_repository import budget_repository
from entities.expence import Expence

class TestBudgetRepository(unittest.TestCase):
    def setUp(self):
        budget_repository.delete_all()

    def test_add_expence_correctly(self):
        expence = Expence(True, -2, 'Cola')
        budget_repository.add_expence(expence)

        expences = budget_repository.find_all()

        self.assertEqual(expences[0].expence, 'True')
        self.assertEqual(expences[0].amount, '-2')
        self.assertEqual(expences[0].description, 'Cola')

