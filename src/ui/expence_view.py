from tkinter import ttk, constants

class AddExpenceView:
    def __init__(
            self,
            root,
            handle_button
    ):
        self._root = root
        self._frame = None
        self._handle_button = handle_button

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        
        label = ttk.Label(master=self._frame, text="Menon nimi:")
        expence_name = ttk.Entry(master=self._frame)

        label_amount = ttk.Label(master=self._frame, text="Määrä euroina:")
        expence_amount = ttk.Entry(master=self._frame)
    
        label.grid(row=0, column=0, padx=5, pady=5)
        expence_name.grid(row=0, column=1, sticky=(constants.W, constants.E), padx=5, pady=5)
        label_amount.grid(row=1, column=0, padx=5, pady=5)
        expence_amount.grid(row=1, column=1, padx=5, pady=5)
