from ui.ui import UI
from tkinter import Tk


def main():
    window = Tk()
    window.title("Budget right")

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
