from tkinter import ttk, constants
from services.budget_service import budget_service


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
        self._is_user = False

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
        label = ttk.Label(master=self._frame, text="Luo uusi käyttäjä")
        username_label = ttk.Label(master=self._frame, text="Käyttäjänimi:")
        self._username = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Salasana:")
        self._password = ttk.Entry(master=self._frame)

        create = ttk.Button(master=self._frame,
                            text="Luo käyttäjä", command=self._create)
        back_button = ttk.Button(
            master=self._frame, text="Takaisin", command=lambda: self._switch())

        error = ttk.Label(master=self._frame, text="Käyttäjä on jo olemassa")

        username_label.grid(row=0, column=0)
        self._username.grid(row=0, column=1, sticky=constants.EW)
        password_label.grid(row=1, column=0)
        self._password.grid(row=1, column=1, sticky=constants.EW)
        create.grid(row=2, column=0, columnspan=2, sticky=constants.EW)
        back_button.grid(row=3, column=0, columnspan=2, sticky=constants.EW)
        if self._is_user:
            error.grid(row=4, columnspan=2)

    def _create(
            self
    ):
        username = self._username.get()
        password = self._password.get()

        success = budget_service.create_user(username, password)

        if success:
            self._switch()
        else:
            self.destroy()
            self._is_user = True
            self._initialize()
            self.pack()
