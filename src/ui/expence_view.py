from tkinter import ttk, constants
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

        add_expence = ttk.Button(
            master=self._frame, text="Lisää meno", command=self._add_expence)
        cancel = ttk.Button(master=self._frame,
                            text="Peruuta", command=self._cancel)

        label.grid(row=0, column=0, padx=5, pady=5)
        self._expence_name.grid(row=0, column=1, sticky=(
            constants.W, constants.E), padx=5, pady=5)
        label_amount.grid(row=1, column=0, padx=5, pady=5)
        self._expence_amount.grid(row=1, column=1, sticky=(
            constants.W, constants.E), padx=5, pady=5)
        add_expence.grid(row=2, column=0, sticky=(
            constants.W, constants.E), padx=5, pady=5)
        cancel.grid(row=2, column=1, sticky=(constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=500)

    def _add_expence(self):
        amount = float(self._expence_amount.get())
        name = self._expence_name.get()
        budget_service.add_expence(name, amount, True)

        self._expence_name = None
        self._expence_amount = None

        self._handle_button('main_view')

    def _cancel(
            self
    ):
        self._handle_button('main_view')
