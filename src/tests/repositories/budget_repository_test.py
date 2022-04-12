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

        self.assertEqual(expences[0].amount, '-2')

    def test_add_expence_marked_correctly(self):
        expence = Expence(True, -2, 'Cola')
        budget_repository.add_expence(expence)

        expences = budget_repository.find_all()

        self.assertEqual(expences[0].expence, 'True')

    def test_add_expence_name_correct(self):
        expence = Expence(True, -2, 'Cola')
        budget_repository.add_expence(expence)

        expences = budget_repository.find_all()

        self.assertEqual(expences[0].description, 'Cola')

    def test_add_income_amount_correctly(self):
        income = Expence(False, 432, 'Pay')
        budget_repository.add_expence(income)

        expences = budget_repository.find_all()

        self.assertEqual(expences[0].amount, '432')

    def test_add_income_marked_correctly(self):
        income = Expence(False, 432, 'Pay')
        budget_repository.add_expence(income)

        expences = budget_repository.find_all()

        self.assertEqual(expences[0].expence, 'False')

    def test_add_income_name_correct(self):
        income = Expence(False, 432, 'Pay')
        budget_repository.add_expence(income)

        expences = budget_repository.find_all()

        self.assertEqual(expences[0].description, 'Pay')
