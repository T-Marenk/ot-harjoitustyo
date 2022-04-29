from tkinter import ttk, constants
from tkcalendar import DateEntry
from services.budget_service import budget_service



class AddExpenceView:
    def __init__(
            self,
            root,
            handle_button
    ):
        self._root = root
        self._frame = None
        self._handle_button = handle_button
        self._expence_amount = None
        self._expence_name = None
        self._cal = None
        self._user = budget_service.get_user()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="Menon nimi:")
        self._expence_name = ttk.Entry(master=self._frame)

        label_amount = ttk.Label(master=self._frame, text="Määrä euroina:")
        self._expence_amount = ttk.Entry(master=self._frame)

        when = ttk.Label(master=self._frame, text="Valitse tulon päivämäärä")
        self._cal = DateEntry(master=self._frame, selectmode='day')

        add_expence = ttk.Button(
            master=self._frame, text="Lisää meno", command=self._add_expence)
        cancel = ttk.Button(master=self._frame,
                            text="Peruuta", command=self._cancel)

        label.grid(row=0, column=0, padx=5, pady=5)
        self._expence_name.grid(row=0, column=1, sticky=constants.EW, padx=5, pady=5)
        label_amount.grid(row=1, column=0, padx=5, pady=5)
        self._expence_amount.grid(row=1, column=1, sticky=constants.EW, padx=5, pady=5)
        when.grid(row=2, column=0)
        self._cal.grid(row=2, column=1, padx=15)
        add_expence.grid(row=3, columnspan=2, sticky=constants.EW, padx=5, pady=5)
        cancel.grid(row=4, columnspan=2, sticky=constants.EW, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=500)

    def _add_expence(self):
        amount = float(self._expence_amount.get())
        name = self._expence_name.get()
        date = self._cal.get_date().strftime("%d-%m-%Y")
        budget_service.add_expence(name, amount, self._user.username, date, True)

        self._handle_button('main_view')

    def _cancel(
            self
    ):
        self._handle_button('main_view')
