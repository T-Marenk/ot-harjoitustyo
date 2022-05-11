from tkinter import ttk, constants, StringVar
from services.budget_service import budget_service, WrongUsernameError, WrongPasswordError


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
        self._error_label = None

        self._initialize()

    def pack(
            self
    ):
        self._frame.pack(fill=constants.X)

    def destroy(
            self
    ):
        self._frame.destroy()

    def _login(
            self
    ):
        username = self._username.get()
        password = self._password.get()
        try:
            budget_service.login(username, password)
            self._switch('main_view')
        except WrongUsernameError:
            self._initialize_error('Väärä käyttäjänimi')
        except WrongPasswordError:
            self._initialize_error('Väärä salasana')

    def _initialize_error(self, error):
        self._error.set(error)

        self._error_label.grid(row=4, columnspan=2,
                               sticky=constants.EW, padx=5, pady=5)

    def _remove_error(self):
        self._error_label.grid_remove()

    def _initialize_username(self):
        username_label = ttk.Label(master=self._frame, text="Käyttäjänimi:")
        self._username = ttk.Entry(master=self._frame)

        username_label.grid(row=0, column=0, padx=5, pady=5)
        self._username.grid(
            row=0, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize_password(self):
        password_label = ttk.Label(master=self._frame, text="Salasana:")
        self._password = ttk.Entry(master=self._frame)

        password_label.grid(row=1, column=0, padx=5, pady=5)
        self._password.grid(
            row=1, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize_login(self):
        login_button = ttk.Button(
            master=self._frame, text="Kirjaudu sisään", command=self._login)

        login_button.grid(row=2, columnspan=2,
                          sticky=constants.EW, padx=5, pady=5)

    def _initialize_new_button(self):
        new_button = ttk.Button(
            master=self._frame, text="Uusi käyttäjä", command=lambda: self._switch('register'))

        new_button.grid(row=3, columnspan=2,
                        sticky=constants.EW, padx=5, pady=5)

    def _initialize(
            self
    ):
        self._frame = ttk.Frame(master=self._root)

        self._error = StringVar(master=self._frame)

        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error, foreground="red")

        self._initialize_username()

        self._initialize_password()

        self._initialize_login()

        self._initialize_new_button()

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

        self._remove_error()
