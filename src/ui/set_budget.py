from tkinter import ttk, constants, StringVar
from services.budget_service import budget_service, NotaNumberError


class SetBudgetView:
    def __init__(
            self,
            root,
            switch
    ):
        self._root = root
        self._switch = switch
        self._frame = None
        self._error = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_error(self, error):
        self._error.set(error)
        self._error_label.grid(
            row=4, column=0, sticky=constants.EW, padx=5, pady=5)

    def _remove_error(self):
        self._error_label.grid_remove()

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
        budget = self._insert_budget.get()

        try:
            budget_service.set_month_budget(budget)
            self._switch('main_view')
        except NotaNumberError:
            self._initialize_error('Budjetin tulee olla positiivinen luku')

    def _cancel(self):
        self._switch('main_view')

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error = StringVar(master=self._frame)

        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error, foreground="red")

        self._initialize_label()

        self._initialize_insert()

        self._initialize_button()

        self._initialize_cancel()

        self._frame.grid_columnconfigure(0, weight=1)

        self._remove_error()
