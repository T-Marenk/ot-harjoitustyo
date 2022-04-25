from tkinter import ttk, constants
from services.budget_service import budget_service

class LoginView:
    """Kirjautumisnäkymää luonnehtiva luokka
    """

    def __init__(
            self,
            root,
            switch,
    ):
        self._root = root
        self._frame = None
        self._switch = switch
        self._username = None
        self._password = None
        self._login_fail = False

        self._initialize()
    
    def pack(
            self
    ):
        self._frame.pack(fill=constants.X)

    def destroy(
            self
    ):
        self._frame.destroy()

    def _initialize(
            self
    ):
        self._frame = ttk.Frame(master=self._root)
        username_label = ttk.Label(master=self._frame, text="Käyttäjänimi:")
        self._username = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Salasana:")
        self._password = ttk.Entry(master=self._frame)
        
        login_button = ttk.Button(master=self._frame, text="Kirjaudu sisään", comman=self._login)
        
        if self._login_fail:
            fail_label = ttk.Label(master=self._frame, text="Kirjautuminen epäonnistui")

        username_label.grid(row=0, column=0)
        self._username.grid(row=0, column=1, sticky=constants.EW)
        password_label.grid(row=1, column=0)
        self._password.grid(row=1, column=1, sticky=constants.EW)
        login_button.grid(row=2, column=0, sticky=constants.EW)
        if self._login_fail:
            fail_label.grid(row=3, column=0)

    def _login(
            self
    ):
        username = self._username.get()
        password = self._password.get()
        fail = budget_service.login(username, password)
        if fail:
            self._login_fail = True
            self.destroy()
            self._initialize()
            self.pack()
        else:
            self._switch()
