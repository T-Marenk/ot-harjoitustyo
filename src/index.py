from ui.ui import UI
from tkinter import Tk


def main():
    window = Tk()
    window.title("Budget right")

    window.geometry("640x480")

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
