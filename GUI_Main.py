try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from GUI_Landing_Page import Landing_Page



class Mainframe(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        Landing_Page(self)
        

    def change(self, frame, **kwargs):
        list = self.place_slaves()
        for l in list:
            l.destroy()
        self.frame = frame(self)


if __name__ == "__main__":
    app = Mainframe()
    app.mainloop()