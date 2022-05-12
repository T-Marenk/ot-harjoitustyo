from tkinter import ttk, constants
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from time import localtime, strftime
from datetime import datetime
from services.budget_service import budget_service


class GraphView:
    def __init__(
            self,
            root,
            handle_button
    ):
        self._root = root
        self._frame = None
        self._switch = handle_button
        self._dates = []
        self._amounts = None
        self._df = None
        self._user = budget_service.get_user()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_dates(self):
        month = strftime("%m", localtime())

        if month == "02":
            x = 29
        elif month in ["01", "03", "05", "07", "08", "10", "12"]:
            x = 32
        else:
            x = 31

        for i in range(1, x):
            date = i
            self._dates.append(date)

    def _initialize_amounts(self):
        self._amounts = [0]*len(self._dates)

        budget = budget_service.this_month_budget(self._user.username)

        for transaction in budget:
            i = int(transaction.date[0:2]) - 1
            self._amounts[i] += float(transaction.amount)

    def _initialize_dataframe(self):
        data = {'Day': self._dates,
                'Total': self._amounts}

        self._df = DataFrame(data, columns=['Day', 'Total'])

    def _initialize_graph(self):
        figure = plt.Figure(figsize=(6, 5), dpi=100)
        ax = figure.add_subplot(111)
        bar = FigureCanvasTkAgg(figure, self._frame)
        bar.get_tk_widget().grid(row=0, column=0, sticky=constants.EW)
        df = self._df[['Day', 'Total']].groupby('Day').sum()
        df.plot(kind='bar', legend=True, ax=ax)
        ax.set_title('Tämän kuukauden tapahtumat päivittäin')
        ax.hlines(y=0, xmin=0, xmax=32, color="black")

    def _initialize_return(self):
        return_button = ttk.Button(
            master=self._frame,
            text="Palaa päänäkymään",
            command=lambda: self._switch('main_view'))

        return_button.grid(
            row=1, column=0, sticky=constants.EW, padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(self._root)

        self._initialize_dates()

        self._initialize_amounts()

        self._initialize_dataframe()

        self._initialize_graph()

        self._initialize_return()

        self._frame.grid_columnconfigure(0, weight=1)
