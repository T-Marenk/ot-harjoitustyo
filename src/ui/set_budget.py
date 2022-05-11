from tkinter import ttk, constants
from services.budget_service import budget_service


class SetBudgetView:
    def __init__(
            self,
            root,
            switch
    ):
        self._root = root
        self._switch = switch
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_label(self):
        label = ttk.Label(
            master=self._frame,
            text="Aseta budjetti kuukaudelle"
        )

        label.grid(row=0, column=0, padx=5, pady=5)

    def _initialize_insert(self):
        self._insert_budget = ttk.Entry(
            master=self._frame)

        self._insert_budget.grid(
            row=1, column=0, sticky=constants.EW, padx=5, pady=5)

    def _initialize_button(self):
        button = ttk.Button(
            master=self._frame,
            text="Aseta budjetti",
            command=lambda: self._set_budget()
        )

        button.grid(row=2, column=0, columnspan=2,
                    sticky=constants.EW, padx=5, pady=5)

    def _initialize_cancel(self):
        cancel = ttk.Button(
            master=self._frame,
            text="Peruuta",
            command=lambda: self._cancel()
        )

        cancel.grid(row=3, column=0, columnspan=2,
                    sticky=constants.EW, padx=5, pady=5)

    def _set_budget(self):
        budget = float(self._insert_budget.get())

        budget_service.set_month_budget(budget)

        self._switch('main_view')

    def _cancel(self):
        self._switch('main_view')

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_label()

        self._initialize_insert()

        self._initialize_button()

        self._initialize_cancel()

        self._frame.grid_columnconfigure(0, weight=1)
