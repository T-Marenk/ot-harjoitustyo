from tkinter import ttk, constants, StringVar
from services.budget_service import budget_service, UsernameTakenError, PasswordsDontMatchError, NoUsernameError, NoPasswordError


class RegisterView:
    def __init__(
            self,
            root,
            login_view
    ):
        self._root = root
        self._switch = login_view
        self._frame = None
        self._username = None
        self._password = None
        self._password2 = None
        self._error = None
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

    def _create(
            self
    ):
        username = self._username.get()
        password = self._password.get()
        password2 = self._password2.get()

        try:
            budget_service.create_user(username, password, password2)
            self._switch()
        except UsernameTakenError:
            self._initialize_error('Käyttäjänimi on jo olemassa')
        except PasswordsDontMatchError:
            self._initialize_error('Salasanat eivät täsmää')
        except NoUsernameError:
            self._initialize_error('Syötä käyttäjänimi')
        except NoPasswordError:
            self._initialize_error('Syötä salasana')

    def _initialize_error(self, error):
        self._error.set(error)
        self._error_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def _remove_error(self):
        self._error_label.grid_remove()

    def _initialize_label(self):
        label = ttk.Label(master=self._frame,
                          text="Luo uusi käyttäjä", foreground="green")

        label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    def _initialize_username(self):
        username_label = ttk.Label(master=self._frame, text="Käyttäjänimi:")
        self._username = ttk.Entry(master=self._frame)

        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username.grid(row=1, column=1, columnspan=2,
                            sticky=constants.EW, padx=5, pady=5)

    def _initialize_password(self):
        password_label = ttk.Label(master=self._frame, text="Salasana:")
        self._password = ttk.Entry(master=self._frame)

        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password.grid(
            row=2, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize_second(self):
        password2_label = ttk.Label(
            master=self._frame, text="Salasana uudestaan:")
        self._password2 = ttk.Entry(master=self._frame)

        password2_label.grid(
            row=3, column=0, sticky=constants.EW, padx=5, pady=5)
        self._password2.grid(
            row=3, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize_buttons(self):
        create = ttk.Button(master=self._frame,
                            text="Luo käyttäjä", command=self._create)
        back_button = ttk.Button(
            master=self._frame, text="Takaisin", command=lambda: self._switch())

        create.grid(row=4, column=0, columnspan=2,
                    sticky=constants.EW, padx=5, pady=5)
        back_button.grid(row=5, column=0, columnspan=2,
                         sticky=constants.EW, padx=5, pady=5)

    def _initialize(
            self
    ):
        self._frame = ttk.Frame(master=self._root)

        self._error = StringVar(master=self._frame)

        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error, foreground="red")

        self._initialize_label()

        self._initialize_username()

        self._initialize_password()

        self._initialize_second()

        self._initialize_buttons()

        self._frame.grid_columnconfigure(1, weight=1)

        self._remove_error()
