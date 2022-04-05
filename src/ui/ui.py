from services.budget import budget 

ORDERS = { 
        "x": "lopeta x",
        "1": "Lisää meno 1",
        "2": "Lisää tulo 2"
}

class BudgetApp:
    def __init__(self):

        self._service = budget

    def start(self):
        self._print_guide()
        
        while True:
            order = input("Komento: ")
            if order == 'x':
                break
            elif order == '1':
                self._add_expence()
            elif order == '2':
                self._add_income()

    def _print_guide(self):
        
        print("Komennot")

        for i in ORDERS:
            print(ORDERS[i])

    def _add_expence(self):
        des = input("Anna kuvaus menosta: ")
        amount = int(input("Määrä euroina: "))

        print(self._service.add_expence(des, amount,))

    def _add_income(self):
        des = input("Anna kuvaus menosta: ")
        amount = input("Määrä euroina: ")

        print(self._service.add_income(des, amount))

    
