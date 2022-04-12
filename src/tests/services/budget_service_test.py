import unittest
from services.budget_service import BudgetService
from entities.expence import Expence

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

class TestBudgetService(unittest.TestCase):
    def setUp(self):
        self.budget_service = BudgetService(
                FakeBudgetRepository()
        )
            
        self.expence_a = Expence('Soda', -2, True)
    
    def test_find_all_finds_all(self):
        expences = self.budget_service.find_all()

        self.assertEqual(len(expences), 0)

    def test_add_expence(self):
        self.budget_service.add_expence('Soda', 2, True)

        expences = self.budget_service.find_all()

        self.assertEqual(len(expences), 1)
        self.assertEqual(expences[0].description, 'Soda')
        self.assertEqual(expences[0].amount, -2)
        self.assertEqual(expences[0].expence, True)
