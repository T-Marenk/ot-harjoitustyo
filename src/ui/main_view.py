from tkinter import ttk, constants
from services.budget_service import budget_service


class ListBudget:
    """Päänäkymään tapahtumat alustava luokka
    """

    def __init__(
            self,
            root,
            budget,
            user,
            delete_expence,
            number
    ):
        self._root = root
        self._budget = budget
        self._frame = None
        self._delete_expence = delete_expence
        self._user = user
        self._scrollbar = None
        self._expence_start = number

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
    ):
        total_frame = ttk.Frame(master=self._frame)

        budget, left_budget = budget_service.find_budget()

        start_budget = ttk.Label(
            master=total_frame,
            text=f'Alkuperäinen budjetti: {budget:.2f} €'
        )

        budget_now = ttk.Label(
            master=total_frame,
            text=f'Tämänhetkinen budjetti: {left_budget:.2f} €'
        )

        start_budget.grid(row=0, column=0, padx=5, pady=5)
        budget_now.grid(row=0, column=1, padx=5, pady=5)

        total_frame.pack(fill=constants.X)

    def _initialize_label(self):
        label_frame = ttk.Frame(master=self._frame)

        date_label = ttk.Label(master=label_frame, text="Päivämäärä")
        name_label = ttk.Label(master=label_frame, text="Nimi")
        amount_label = ttk.Label(master=label_frame, text="Määrä")

        date_label.grid(row=1, column=0, sticky=constants.EW, padx=5, pady=5)
        name_label.grid(row=1, column=1, sticky=constants.EW, padx=5, pady=5)
        amount_label.grid(row=1, column=2, sticky=constants.EW, padx=5, pady=5)

        label_frame.grid_columnconfigure(0, minsize=100)
        label_frame.grid_columnconfigure(1, minsize=250)

        label_frame.pack(fill=constants.X)

    def _initialize_expence(
            self,
            expence
    ):
        expence_frame = ttk.Frame(master=self._frame)
        date = ttk.Label(master=expence_frame, text=f'{expence.date}')
        label = ttk.Label(master=expence_frame, text=f'{expence.description}')
        amount = ttk.Label(master=expence_frame, text=f'{expence.amount} €')
        delete_button = ttk.Button(
            master=expence_frame,
            text='Poista',
            command=lambda: self._delete_expence(expence.expence_id)
        )

        date.grid(row=0, column=0, sticky=constants.EW, padx=5, pady=5)
        label.grid(row=0, column=1, sticky=constants.EW, padx=5, pady=5)
        amount.grid(row=0, column=2, sticky=constants.EW, padx=5, pady=5)
        delete_button.grid(
            row=0, column=3, sticky=constants.EW, padx=5, pady=5)

        expence_frame.grid_columnconfigure(0, minsize=100)
        expence_frame.grid_columnconfigure(1, minsize=250)
        expence_frame.grid_columnconfigure(2, minsize=100)

        expence_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        total = 0

        self._initialize_total()

        self._initialize_label()

        for expence in self._budget[self._expence_start:self._expence_start+5]:
            self._initialize_expence(expence)


class MainView:
    """Sovelluksen päänäkymää luonnehtiva luokka
    """

    def __init__(
            self,
            root,
            handle_button
    ):

        self._root = root
        self._frame = None
        self._list_budget_frame = None
        self._list_budget_view = None
        self._month = False
        self._expence_number = 0
        self._length = 0
        self._budget = None
        self._handle_button = handle_button
        self._user = budget_service.get_user()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _delete_expence(
            self,
            expence_id
    ):
        budget_service.delete_expence(expence_id)
        self._budget = None
        self._initialize_budget()

    def _increase_expences(
            self,
    ):
        if self._length > self._expence_number + 10:
            self._expence_number + 5
        elif self._length > 5:
            self._expence_number = self._length - 5
        else:
            self._expence_number = 0
        self._initialize_budget()

    def _all_budget(self):
        self._month = False
        self._budget = budget_service.find_by_username(self._user.username)
        self._initialize_budget()

    def _this_month_budget(self):
        self._month = True
        self._budget = budget_service.this_month_budget(self._user.username)
        self._initialize_budget()

    def _decrease(self):
        if self._expence_number - 5 > 0:
            self._expence_number -= 5
        else:
            self._expence_number = 0
        self._initialize_budget()

    def _logout(self):
        budget_service.logout()
        self._handle_button('login')

    def _show_expences(self):
        self._budget = budget_service.find_expences(
            self._user.username, self._month)
        self._initialize_budget()

    def _show_income(self):
        self._budget = budget_service.find_income(
            self._user.username, self._month)
        self._initialize_budget()

    def _initialize_budget(
            self
    ):
        if self._list_budget_view:
            self._list_budget_view.destroy()
        if not self._budget:
            self._budget = budget_service.find_by_username(self._user.username)

        if len(self._budget) != self._length:
            self._length = len(self._budget)
            self._expence_number = 0

        self._list_budget_view = ListBudget(
            self._list_budget_frame,
            self._budget,
            self._user,
            self._delete_expence,
            self._expence_number
        )

        self._list_budget_view.pack()

        self._list_budget_frame.grid(
            row=8,
            column=0,
            columnspan=2,
            sticky=constants.EW,
            padx=5,
            pady=5
        )

    def _initialize_welcome_label(self):
        label = ttk.Label(
            master=self._frame, text=f"Hei { self._user.username }! Mitä haluat tehdä?"
        )

        label.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky=constants.EW,
            padx=5,
            pady=5
        )

    def _initialize_expence_button(self):
        add_expence_button = ttk.Button(
            master=self._frame,
            text="Lisää meno",
            command=lambda: self._handle_button('add_expence'))

        add_expence_button.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW,
            padx=5,
            pady=5
        )

    def _initialize_income_button(self):
        add_income_button = ttk.Button(
            master=self._frame, text="Lisää tulo", command=lambda: self._handle_button('add_income'))

        add_income_button.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky=constants.EW,
            padx=5,
            pady=5
        )

    def _initialize_set_budget_button(self):
        set_budget_button = ttk.Button(
            master=self._frame,
            text="Aseta budjetti kuukaudelle",
            command=lambda: self._handle_button('set_budget')
        )

        set_budget_button.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky=constants.EW,
            padx=5,
            pady=5
        )

    def _initialize_show_graph(self):
        show_graph_button = ttk.Button(
            master=self._frame,
            text="Näytä kuukauden menot diagrammina",
            command=lambda: self._handle_button('show_graph'))

        show_graph_button.grid(row=4, columnspan=2,
                               sticky=constants.EW, padx=5, pady=5)

    def _initialize_logout_button(self):
        logout_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command=lambda: self._logout()
        )

        logout_button.grid(
            row=5,
            columnspan=3,
            sticky=constants.EW,
            padx=5,
            pady=5
        )

    def _initialize_all_button(self):
        show_all_button = ttk.Button(
            master=self._frame,
            text="Näytä kaikki tapahtumat",
            command=lambda: self._all_budget()
        )

        show_all_button.grid(
            row=6, column=0, sticky=constants.EW, padx=5, pady=5)

    def _initialize_month_button(self):
        this_month_button = ttk.Button(
            master=self._frame,
            text="Näytä tämän kuun tapahtumat",
            command=lambda: self._this_month_budget()
        )

        this_month_button.grid(
            row=6, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize_show_expences(self):
        expences_button = ttk.Button(
            master=self._frame,
            text="Näytä menot",
            command=lambda: self._show_expences()
        )

        expences_button.grid(
            row=7, column=0, sticky=constants.EW, padx=5, pady=5)

    def _initialize_show_income(self):
        incomes_button = ttk.Button(
            master=self._frame,
            text="Näytä tulot",
            command=lambda: self._show_income()
        )

        incomes_button.grid(
            row=7, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize_next_6_button(self):
        next_button = ttk.Button(
            master=self._frame,
            text="Seuraavat 5 tapahtumaa",
            command=self._increase_expences
        )

        next_button.grid(row=9, column=0, sticky=constants.EW, padx=5, pady=5)

    def _initialize_last_6_button(self):
        last_button = ttk.Button(
            master=self._frame,
            text="Viimeiset 5 tapahtumaa",
            command=self._decrease
        )

        last_button.grid(row=9, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._list_budget_frame = ttk.Frame(master=self._frame)

        self._initialize_welcome_label()

        self._initialize_expence_button()

        self._initialize_income_button()

        self._initialize_set_budget_button()

        self._initialize_show_graph()

        self._initialize_logout_button()

        self._initialize_all_button()

        self._initialize_month_button()

        self._initialize_show_expences()

        self._initialize_show_income()

        self._initialize_next_6_button()

        self._initialize_last_6_button()

        self._initialize_budget()

        self._frame.grid_columnconfigure(0, weight=1)
