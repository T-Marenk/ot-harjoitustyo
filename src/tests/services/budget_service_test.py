import unittest
from time import strftime, localtime
from datetime import datetime
from dateutil.relativedelta import relativedelta
from services.budget_service import BudgetService, UsernameTakenError, NotaNumberError, WrongUsernameError, WrongPasswordError, DescriptionTooLongError, PasswordsDontMatchError, NoPasswordError, NoUsernameError, NoDescriptionError
from entities.expence import Expence
from entities.user import User


class FakeBudgetRepository:
    def __init__(self, expences=None):
        self.expences = expences or []

    def add_expence(
            self,
            expence
    ):
        expence.expence = str(expence.expence)
        self.expences.append(expence)

        return self.expences

    def find_all(
        self
    ):
        return self.expences

    def find_by_username(self, username):
        return_expences = []

        for expence in self.expences:
            if expence.username == username:
                return_expences.append(expence)

        return return_expences

    def delete_expence(self, expence_id):
        for expence in self.expences:
            if expence.expence_id == expence_id:
                self.expences.remove(expence)

    def delete_all(self):
        self.expences = []


class FakeUserRepository:
    def __init__(self, users=None, budgets=None):
        self.users = users or []
        self.budgets = budgets or []

    def create_user(self, username, password):
        user = User(username, password)
        self.users.append(user)

    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def find_all(self):
        return self.users

    def set_budget(self, username, budget, month):
        self.budgets.append((username, budget, month))

    def update_budget(self, username, budget, month):
        for b in self.budgets:
            if b[0] == username and b[2] == month:
                self.budgets.remove(b)
                self.budgets.append((username, budget, month))
                break

    def find_budget(self, username, month):
        for b in self.budgets:
            if b[0] == username and b[2] == month:
                return [b[1]]


class TestBudgetService(unittest.TestCase):
    def setUp(self):
        self.budget_service = BudgetService(
            FakeBudgetRepository(),
            FakeUserRepository()
        )

        time = localtime()
        next_time = datetime.today() + relativedelta(months=1)
        self.month = strftime("%m-%Y", time)
        self.next_month = datetime.strftime(next_time, "%m-%Y")

    def test_create_user(self):
        self.budget_service.create_user('Tyyppi', '1234', '1234')

        user = self.budget_service.find_user('Tyyppi')

        self.assertEqual(user.username, 'Tyyppi')
        self.assertEqual(user.password, '1234')

    def test_create_user_no_same_user_added_twice(self):
        self.budget_service.create_user('Tyyppi', '1234', '1234')
        self.assertRaises(
            UsernameTakenError, self.budget_service.create_user, 'Tyyppi', '1234', '1234')

    def test_create_user_no_username_or_password_given(self):
        self.assertRaises(
            NoUsernameError, self.budget_service.create_user, '', '1234', '1234')
        self.assertRaises(
            NoPasswordError, self.budget_service.create_user, 'Tyyppi', '', '')

    def test_create_user_passwords_not_the_same(self):
        self.assertRaises(PasswordsDontMatchError,
                          self.budget_service.create_user, 'Tyyppi', '123', '1234')

    def test_login_correct_user(self):
        self.budget_service.create_user('Tyyppi', '1234', '1234')
        self.budget_service.login('Tyyppi', '1234')

        user = self.budget_service.get_user()

        self.assertEqual(user.username, 'Tyyppi')

    def test_login_incorrect_credentials(self):
        self.budget_service.create_user('Tyyppi', '1234', '1234')
        self.assertRaises(WrongUsernameError,
                          self.budget_service.login, 'T', '1234')
        self.assertRaises(WrongPasswordError,
                          self.budget_service.login, 'Tyyppi', '123')

    def test_logout(self):
        self.budget_service.create_user('Tyyppi', '1234', '1234')
        self.budget_service.login('Tyyppi', '1234')
        self.budget_service.logout()

        user = self.budget_service.get_user()

        self.assertEqual(user, None)

    def test_find_all_finds_all(self):
        self.budget_service.add_expence(
            'Soda', 2, 'Tyyppi', "25-04-2022", True)
        self.budget_service.add_expence(
            'Bread', 3.12, 'Henkilö', "21-02-2010", True)
        expences = self.budget_service.find_all()

        self.assertEqual(len(expences), 2)

    def test_add_expence_correct(self):
        self.budget_service.add_expence(
            'Soda', 2, 'Tyyppi', "25-04-2022", True)
        expences = self.budget_service.find_all()

        self.assertEqual(expences[0].description, 'Soda')
        self.assertEqual(expences[0].amount, -2)
        self.assertEqual(expences[0].expence, "True")
        self.assertEqual(expences[0].date, "25-04-2022")

    def test_add_transaction_amount_not_a_positive_number(self):
        self.assertRaises(NotaNumberError, self.budget_service.add_expence,
                          'Cola', 'A', 'Tyyppi', '12-05-2022', True)
        self.assertRaises(NotaNumberError, self.budget_service.add_expence,
                          'Cola', '-2', 'Tyyppi', '12-05-2022', True)

    def test_add_transaction_invalid_description_given(self):
        self.assertRaises(NoDescriptionError, self.budget_service.add_expence,
                          '', '2', 'Tyyppi', '12-05-2022', True)
        self.assertRaises(DescriptionTooLongError, self.budget_service.add_expence,
                          'This transaction description is over 40 characters long', '2', 'Tyyppi', '12-05-2022', True)

    def test_find_transactions_by_username(self):
        self.budget_service.add_expence(
            'Soda', 2, 'Tyyppi', "25-04-2022", True)
        self.budget_service.add_expence(
            'Bread', 3.12, 'Henkilö', "21-02-2010", True)
        self.budget_service.add_expence(
            'Money', 112, 'Tyyppi', "23-04-2022", False)

        budget = self.budget_service.find_all()

        self.assertEqual(len(budget), 3)

        budget = self.budget_service.find_by_username('Tyyppi')

        self.assertEqual(len(budget), 2)
        self.assertEqual(budget[0].username, 'Tyyppi')
        self.assertEqual(budget[1].username, 'Tyyppi')

    def test_find_this_month_budget(self):
        self.budget_service.add_expence(
            'Soda', 2, 'Tyyppi', '12-'+str(self.month), True)
        self.budget_service.add_expence(
            'Bread', 2.21, 'Tyyppi', '12-'+str(self.next_month), True)
        self.budget_service.add_expence(
            'Money', 12.12, 'Tyyppi', '12-'+str(self.month), False)

        budget = self.budget_service.find_by_username('Tyyppi')

        self.assertEqual(len(budget), 3)

        budget = self.budget_service.this_month_budget('Tyyppi')

        self.assertEqual(len(budget), 2)
        self.assertEqual(budget[0].date[3:10], self.month)
        self.assertEqual(budget[1].date[3:10], self.month)

    def test_find_only_expences(self):
        self.budget_service.add_expence(
            'Soda', 2, 'Tyyppi', "25-04-2022", "True")
        self.budget_service.add_expence(
            'Bread', 3.12, 'Tyyppi', "21-02-2010", "True")
        self.budget_service.add_expence(
            'Money', 112, 'Tyyppi', "23-04-2022", "False")

        budget = self.budget_service.find_by_username('Tyyppi')

        self.assertEqual(len(budget), 3)

        budget = self.budget_service.find_expences('Tyyppi')

        self.assertEqual(len(budget), 2)
        self.assertEqual(budget[0].expence, "True")
        self.assertEqual(budget[1].expence, "True")

    def test_find_only_month_expences(self):
        self.budget_service.add_expence(
            'Soda', 2, 'Tyyppi', '12-'+str(self.month), "True")
        self.budget_service.add_expence(
            'Bread', 2.21, 'Tyyppi', '12-'+str(self.next_month), "True")
        self.budget_service.add_expence(
            'Money', 12.12, 'Tyyppi', '12-'+str(self.month), "False")

        budget = self.budget_service.find_by_username('Tyyppi')

        self.assertEqual(len(budget), 3)

        budget = self.budget_service.find_expences('Tyyppi', True)

        self.assertEqual(len(budget), 1)
        self.assertEqual(budget[0].expence, "True")

    def test_find_only_incomes(self):
        self.budget_service.add_expence(
            'Soda', 2, 'Tyyppi', "25-04-2022", "False")
        self.budget_service.add_expence(
            'Bread', 3.12, 'Tyyppi', "21-02-2010", "True")
        self.budget_service.add_expence(
            'Money', 112, 'Tyyppi', "23-04-2022", "False")

        budget = self.budget_service.find_by_username('Tyyppi')

        self.assertEqual(len(budget), 3)

        budget = self.budget_service.find_income('Tyyppi')

        self.assertEqual(len(budget), 2)
        self.assertEqual(budget[0].expence, "False")
        self.assertEqual(budget[1].expence, "False")

    def test_find_only_month_incomes(self):
        self.budget_service.add_expence(
            'Soda', 2, 'Tyyppi', '12-'+str(self.month), "True")
        self.budget_service.add_expence(
            'Bread', 2.21, 'Tyyppi', '12-'+str(self.next_month), "True")
        self.budget_service.add_expence(
            'Money', 12.12, 'Tyyppi', '12-'+str(self.month), "False")

        budget = self.budget_service.find_by_username('Tyyppi')

        self.assertEqual(len(budget), 3)

        budget = self.budget_service.find_income('Tyyppi', True)

        self.assertEqual(len(budget), 1)
        self.assertEqual(budget[0].expence, "False")

    def test_find_user_month_budget_no_budget_set(self):
        self.budget_service.add_expence(
            'Soda', 2, 'Tyyppi', '12-'+str(self.month), True)
        self.budget_service.add_expence(
            'Bread', 2.21, 'Tyyppi', '12-'+str(self.month), True)
        self.budget_service.add_expence(
            'Money', 12.12, 'Tyyppi', '12-'+str(self.month), False)

        self.budget_service.create_user('Tyyppi', '1234', '1234')
        self.budget_service.login('Tyyppi', '1234')

        budget, left_budget = self.budget_service.find_budget()

        self.assertEqual(budget, 0)
        self.assertEqual(f"{left_budget:.2f}", "7.91")

    def test_set_budget_for_month(self):
        self.budget_service.create_user('Tyyppi', '1234', '1234')
        self.budget_service.login('Tyyppi', '1234')

        self.budget_service.set_month_budget('600')

        budget, left = self.budget_service.find_budget()

        self.assertEqual(budget, 600)
        self.assertEqual(left, 600)

    def test_set_budget_for_month_invalid_budget(self):
        self.budget_service.create_user('Tyyppi', '1234', '1234')
        self.budget_service.login('Tyyppi', '1234')

        self.assertRaises(
            NotaNumberError, self.budget_service.set_month_budget, 'A')
        self.assertRaises(
            NotaNumberError, self.budget_service.set_month_budget, '-600')

    def test_update_users_month_budget(self):
        self.budget_service.create_user('Tyyppi', '1234', '1234')
        self.budget_service.login('Tyyppi', '1234')
        self.budget_service.add_expence(
            'Something', 100, 'Tyyppi', '12-'+str(self.month), True)
        self.budget_service.set_month_budget('600')

        self.budget_service.set_month_budget('700')

        budget, left = self.budget_service.find_budget()

        self.assertEqual(budget, 700)
        self.assertEqual(left, 600)

    def test_delete_expence(self):
        self.budget_service.add_expence(
            'Soda', 2, 'Tyyppi', "25-04-2022", "False")
        self.budget_service.add_expence(
            'Bread', 3.12, 'Tyyppi', "21-02-2010", "True")
        self.budget_service.add_expence(
            'Money', 112, 'Tyyppi', "23-04-2022", "False")

        budget = self.budget_service.find_by_username('Tyyppi')

        self.assertEqual(len(budget), 3)

        self.budget_service.delete_expence(budget[0].expence_id)

        budget = self.budget_service.find_by_username('Tyyppi')

        self.assertEqual(len(budget), 2)
        self.assertEqual(budget[1].description, 'Money')
        self.assertEqual(budget[0].description, 'Bread')

    def test_delete_all(self):
        self.budget_service.add_expence(
            'Soda', 2, 'Tyyppi', "25-04-2022", True)
        self.budget_service.add_expence(
            'Money', 3.12, 'Henkilö', "21-02-2010", False)

        self.budget_service.delete_all()

        expences = self.budget_service.find_all()

        self.assertEqual(expences, [])
