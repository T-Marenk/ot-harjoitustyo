from tkinter import ttk, constants
from services.budget_service import budget_service


class ListBudget:
    def __init__(
            self,
            root,
            budget
    ):
        self._root = root
        self._budget = budget
        self._frame = None

        self._initialize()

    def pack(
            self
    ):
        self._frame.pack(fill=constants.X)

    def destroy(
            self
    ):
        self._frame.destroy()

    def _initialize_total(
            self,
            total
    ):
        label_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=label_frame,
                          text=f'Tämän hetkinen budjetti: {total} €')
        label.grid(
            row=0,
            column=0
        )
        label_frame.pack(fill=constants.X)

    def _initialize_expence(
            self,
            expence
    ):
        expence_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=expence_frame, text=f'{expence.description}:')
        amount = ttk.Label(master=expence_frame, text=f'{expence.amount} €')

        label.grid(row=0, column=0, sticky=constants.W, padx=5, pady=5)
        amount.grid(row=0, column=1, sticky=constants.W, padx=1, pady=1)

        expence_frame.grid_columnconfigure(0, weight=1)
        expence_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        total = 0

        for expence in self._budget:
            total += float(expence.amount)

        self._initialize_total(
            total
        )

        for expence in self._budget:
            self._initialize_expence(expence)


class MainView:
    def __init__(self, root, handle_button):
        self._root = root
        self._frame = None
        self._list_budget_frame = None
        self._list_budget_view = None
        self._handle_button = handle_button

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_budget(
            self
    ):
        if self._list_budget_view:
            self._list_budget_view.destroy()

        budget = budget_service.find_all()

        self._list_budget_view = ListBudget(
            self._list_budget_frame,
            budget
        )

        self._list_budget_view.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._list_budget_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=self._frame, text="Mitä haluat tehdä?")

        add_expence_label = ttk.Label(master=self._frame, text="Uusi meno:")
        add_expence_button = ttk.Button(
            master=self._frame, text="Lisää meno", command=lambda: self._handle_button('add_expence'))

        add_income_label = ttk.Label(
            master=self._frame,
            text="Uusi tulo:"
        )
        add_income_button = ttk.Button(
            master=self._frame, text="Lisää tulo", command=lambda: self._handle_button('add_income'))

        self._initialize_budget()

        label.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        add_expence_label.grid(
            row=1,
            column=1,
            sticky=(constants.EW)
        )

        add_expence_button.grid(
            row=1,
            column=2,
            sticky=(constants.W, constants.E),
            padx=3,
            pady=3
        )

        add_income_label.grid(
            row=2,
            column=1,
            sticky=(constants.EW)
        )

        add_income_button.grid(
            row=2,
            column=2,
            sticky=(constants.W, constants.E),
            padx=3,
            pady=3
        )

        self._list_budget_frame.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(2, weight=1, minsize=400)