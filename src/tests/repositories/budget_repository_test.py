import unittest
from repositories.budget_repository import budget_repository
from entities.expence import Expence
from datetime import datetime


class TestBudgetRepository(unittest.TestCase):
    def setUp(self):
        budget_repository.delete_all()
        self.expence1 = Expence(True, -2, 'Cola', 'Tyyppi', "30-04-2022")
        self.expence2 = Expence(True, -7, 'Food', 'Henkilö', "05-05-2022")
        self.income1 = Expence(False, 432, 'Pay', 'Tyyppi', "29-11-2019")

    def test_add_expence_correctly(self):
        budget_repository.add_expence(self.expence1)

        expences = budget_repository.find_all()

        self.assertEqual(expences[0].amount, '-2')

    def test_add_expence_marked_correctly(self):
        budget_repository.add_expence(self.expence1)

        expences = budget_repository.find_all()

        self.assertEqual(expences[0].expence, 'True')

    def test_add_expence_name_correct(self):
        budget_repository.add_expence(self.expence1)

        expences = budget_repository.find_all()

        self.assertEqual(expences[0].description, 'Cola')

    def test_add_expence_date_correct(self):
        budget_repository.add_expence(self.expence1)

        expences = budget_repository.find_all()

        self.assertEqual(expences[0].date, "30-04-2022")

    def test_add_income_amount_correctly(self):
        budget_repository.add_expence(self.income1)

        expences = budget_repository.find_all()

        self.assertEqual(expences[0].amount, '432')

    def test_add_income_marked_correctly(self):
        budget_repository.add_expence(self.income1)

        expences = budget_repository.find_all()

        self.assertEqual(expences[0].expence, 'False')

    def test_add_income_name_correct(self):
        budget_repository.add_expence(self.income1)

        expences = budget_repository.find_all()

        self.assertEqual(expences[0].description, 'Pay')

    def test_delete_transaction_correctly(self):
        budget_repository.add_expence(self.income1)
        budget_repository.add_expence(self.expence1)

        expences = budget_repository.find_all()

        self.assertEqual(len(expences), 2)

        budget_repository.delete_expence(expences[1].expence_id)

        expences = budget_repository.find_all()

        self.assertEqual(len(expences), 1)
        self.assertEqual(expences[0].description, 'Cola')

    def test_find_only_user_transactions(self):
        budget_repository.add_expence(self.expence1)
        budget_repository.add_expence(self.expence2)
        budget_repository.add_expence(self.income1)

        expences = budget_repository.find_all()

        self.assertEqual(len(expences), 3)

        expences = budget_repository.find_by_username('Tyyppi')

        self.assertEqual(len(expences), 2)
        self.assertEqual(expences[0].username, 'Tyyppi')
