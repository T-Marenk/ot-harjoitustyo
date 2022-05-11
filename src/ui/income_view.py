from tkinter import ttk, constants, StringVar
from tkcalendar import DateEntry
from services.budget_service import budget_service, NotaNumberError, DescriptionTooLongError, NoDescriptionError


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
        self._cal = None
        self._user = budget_service.get_user()
        self._error = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _add_income(self):
        amount = self._income_amount.get()
        name = self._income_name.get()
        date = self._cal.get_date().strftime("%d-%m-%Y")
        try:
            budget_service.add_expence(
                name, amount, self._user.username, date, False)
            self._handle_button('main_view')
        except NotaNumberError:
            self._initialize_error('Määrän tulee olla positiivinen luku')
        except DescriptionTooLongError:
            self._initialize_error('Kuvaus saa olla enintään 40 merkkiä pitkä')
        except NoDescriptionError:
            self._initialize_error('Syötä kuvaus')

    def _cancel(self):
        self._handle_button('main_view')

    def _initialize_error(self, error):
        self._error.set(error)
        self._error_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def _remove_error(self):
        self._error_label.grid_remove()

    def _initialize_name(self):
        label = ttk.Label(master=self._frame, text="Tulon nimi:")
        self._income_name = ttk.Entry(master=self._frame)

        label.grid(row=0, column=0, padx=5, pady=5)
        self._income_name.grid(
            row=0, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize_amount(self):
        label_amount = ttk.Label(master=self._frame, text="Määrä euroina:")
        self._income_amount = ttk.Entry(master=self._frame)

        label_amount.grid(row=1, column=0, padx=5, pady=5)
        self._income_amount.grid(
            row=1, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize_calendar(self):
        when = ttk.Label(master=self._frame, text="Valitse tulon päivämäärä")
        self._cal = DateEntry(master=self._frame, selectmode='day')

        when.grid(row=2, column=0)
        self._cal.grid(row=2, column=1, sticky=constants.EW, padx=15)

    def _initialize_buttons(self):
        add_income = ttk.Button(
            master=self._frame, text="Lisää tulo", command=self._add_income)
        cancel = ttk.Button(master=self._frame,
                            text="Peruuta", command=self._cancel)

        add_income.grid(row=3, columnspan=2,
                        sticky=constants.EW, padx=5, pady=5)
        cancel.grid(row=4, columnspan=2, sticky=constants.EW, padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error = StringVar(master=self._frame)

        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error, foreground="red")

        self._initialize_name()

        self._initialize_amount()

        self._initialize_calendar()

        self._initialize_buttons()

        self._frame.grid_columnconfigure(1, weight=1, minsize=500)

        self._remove_error()
