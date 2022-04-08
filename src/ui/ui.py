from tkinter import Tk, ttk
from ui.main_view import MainView
from ui.expence_view import AddExpenceView

class UI:
    """Graafisesta käyttöliittymästä hoitava luokka
    """

    def __init__(
            self,
            root
    ):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_main_page()
    
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
