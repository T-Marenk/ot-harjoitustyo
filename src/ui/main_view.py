from tkinter import ttk, constants

class MainView:
    def __init__(self, root, handle_button):
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
        label = ttk.Label(master=self._frame, text="Mitä haluat tehdä")

        add_expence_button = ttk.Button(master=self._frame, text="Lisää meno", command=lambda: self._handle_button('add_expence'))

        add_income_button = ttk.Button(master=self._frame, text="Lisää tulo", command=lambda: self._hande_button('add_income'))

        label.grid(columnspan=2, sticky=constants.W)
        add_expence_button.grid(columnspan=2, sticky=(constants.W, constants.E), padx=3, pady=3)
        add_income_button.grid(columnspan=2, sticky=(constants.W, constants.E), padx=4, pady=4)

        self._frame.grid_columnconfigure(1, weight=1, minsize=500)
