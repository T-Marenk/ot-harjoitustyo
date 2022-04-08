from entities.expence import Expence

from repositories.budget_repository import budget_repository


class BudgetService:
    def __init__(
            self
    ):
        """Luokan konstrukti
        """

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

        expences = self._budget_repository.add_expence(expence)

        total = 0
        for i in expences:
            total += int(i.amount)
        return total

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

        expences = self._budget_repository.add_expence(expence)

        total = 0
        for i in expences:
            total += int(i.amount)
        return total


budget = BudgetService()
