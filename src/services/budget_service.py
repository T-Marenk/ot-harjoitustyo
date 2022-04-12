from entities.expence import Expence

from repositories.budget_repository import budget_repository as default_budget_repository

from repositories.user_repository import user_repository

class BudgetService:
    def __init__(
            self,
            budget_repository=default_budget_repository
    ):
        """Luokan konstrukti
        """

        self._user = None
        self._user_repository = user_repository
        self._budget_repository = budget_repository

    def add_expence(
            self,
            description,
            amount,
            expence=True
    ):
        """Lisää menon budjettiin.

        Args:
            amount: Menon suuruus
            description: Kuvaus menosta tai tulosta
        Returns:
            budjetin nykyisen tilanteen
        """
        amount *= -1
        expence = Expence(expence, amount, description)

        self._budget_repository.add_expence(expence)

    def create_user(
            self,
            username,
            password
    ):
        pass

    def add_income(
            self,
            description,
            amount,
            expence=False
    ):
        """Lisää tulon budjettiin.

        Args:
            amount: Tulon suuruus
            description: Kuvaus tulosta
        Returns:
            budjetin nykyinen tilanne
        """

        expence = Expence(expence, amount, description)

        self._budget_repository.add_expence(expence)

    def find_all(
            self
    ):
        """Hakee kaikki menot ja tulot
        """

        expences = self._budget_repository.find_all()

        return expences

    def find_expence(
            self
    ):
        pass

    def find_income(
            self
    ):
        pass

    def delete_expence(
            self
    ):
        pass

    def delete_all(
            self
    ):
        self._budget_repository.delete_all()


budget_service = BudgetService()