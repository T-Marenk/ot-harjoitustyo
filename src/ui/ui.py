from tkinter import ttk
from ui.main_view import MainView
from ui.expence_view import AddExpenceView
from ui.income_view import AddIncomeView
from ui.login import LoginView
from ui.new_user import RegisterView
from ui.set_budget import SetBudgetView
from ui.graph_spending_view import GraphView


class UI:
    """Graafisesta käyttöliittymästä vastaava luokka
    """

    def __init__(
            self,
            root
    ):
        self._root = root
        self._current_view = None

    def start(self):
        self._login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_view_switch(
            self,
            view_switch
    ):
        if view_switch == 'add_expence':
            self._add_expence_page()
        elif view_switch == 'main_view':
            self._show_main_page()
        elif view_switch == 'add_income':
            self._add_income_page()
        elif view_switch == 'register':
            self._register_view()
        elif view_switch == 'login':
            self._login_view()
        elif view_switch == 'set_budget':
            self._set_budget_view()
        elif view_switch == 'show_graph':
            self._show_graph_view()

    def _show_main_page(self):
        self._hide_current_view()

        self._current_view = MainView(
            self._root,
            self._handle_view_switch
        )
        self._current_view.pack()

    def _add_expence_page(self):
        self._hide_current_view()

        self._current_view = AddExpenceView(
            self._root,
            self._handle_view_switch
        )

        self._current_view.pack()

    def _add_income_page(self):
        self._hide_current_view()

        self._current_view = AddIncomeView(
            self._root,
            self._handle_view_switch
        )

        self._current_view.pack()

    def _login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._handle_view_switch
        )

        self._current_view.pack()

    def _register_view(
            self
    ):
        self._hide_current_view()

        self._current_view = RegisterView(
            self._root,
            self._login_view
        )

        self._current_view.pack()

    def _set_budget_view(
            self
    ):
        self._hide_current_view()

        self._current_view = SetBudgetView(
            self._root,
            self._handle_view_switch
        )

        self._current_view.pack()

    def _show_graph_view(
            self
    ):
        self._hide_current_view()

        self._current_view = GraphView(
            self._root,
            self._handle_view_switch
        )

        self._current_view.pack()
