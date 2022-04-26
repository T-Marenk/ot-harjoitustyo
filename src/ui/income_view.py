from tkinter import ttk, constants
from services.budget_service import budget_service


class AddIncomeView:
    def __init__(
            self,
            root,
            handle_button
    ):
        self._root = root
        self._frame = None
        self._handle_button = handle_button
        self._income_amount = None
        self._income_name = None
        self._user = budget_service.get_user()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="Tulon nimi:")
        self._income_name = ttk.Entry(master=self._frame)

        label_amount = ttk.Label(master=self._frame, text="Määrä euroina:")
        self._income_amount = ttk.Entry(master=self._frame)

        add_income = ttk.Button(
            master=self._frame, text="Lisää tulo", command=self._add_income)
        cancel = ttk.Button(master=self._frame,
                            text="Peruuta", command=self._cancel)

        label.grid(row=0, column=0, padx=5, pady=5)
        self._income_name.grid(row=0, column=1, sticky=(
            constants.W, constants.E), padx=5, pady=5)
        label_amount.grid(row=1, column=0, padx=5, pady=5)
        self._income_amount.grid(row=1, column=1, sticky=(
            constants.W, constants.E), padx=5, pady=5)
        add_income.grid(row=2, column=0, sticky=(
            constants.W, constants.E), padx=5, pady=5)
        cancel.grid(row=2, column=1, sticky=(constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=500)

    def _add_income(self):
        amount = float(self._income_amount.get())
        name = self._income_name.get()
        budget_service.add_income(name, amount, self._user.username, False)

        self._income_name = None
        self._income_amount = None

        self._handle_button('main_view')

    def _cancel(self):
        self._handle_button('main_view')
