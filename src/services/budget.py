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
            amount
    ):
        """Lisää menon budjettiin.

        Args:
            amount: Menon suuruus
            description: Kuvaus menosta tai tulosta
        Returns:
            budjetin nykyisen tilanteen
        """
        
        expence = Expence(desciption, amount)




budget = BudgetService()

print(budget.add_expence(10))

