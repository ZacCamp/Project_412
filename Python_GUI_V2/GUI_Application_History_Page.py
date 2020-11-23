import sys

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

import GUI_Application_Page

class Application_History_Page(tk.Frame):
    def __init__(self, master=None, **kwargs):

        tk.Frame.__init__(self, master, **kwargs)

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        master.geometry("600x450+1087+728")
        master.minsize(120, 1)
        master.maxsize(2564, 1421)
        master.resizable(1, 1)
        master.title("Application History Page")
        master.configure(background="#2291ff")
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")

        self.Application_History = tk.Label(master)
        self.Application_History.place(relx=0.5, rely=0.089, anchor = 'center', height=41
                , width=700)
        self.Application_History.configure(activebackground="#f9f9f9")
        self.Application_History.configure(activeforeground="black")
        self.Application_History.configure(background="#2291ff")
        self.Application_History.configure(disabledforeground="#a3a3a3")
        self.Application_History.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 24 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Application_History.configure(foreground="#ffffff")
        self.Application_History.configure(highlightbackground="#d9d9d9")
        self.Application_History.configure(highlightcolor="black")
        self.Application_History.configure(text='''Application History''')

        self.infoApLabel = tk.Label(master)
        self.infoApLabel.place(relx=0.5, rely=0.222, anchor = 'center', height=22, width=700)
        self.infoApLabel.configure(activebackground="#f9f9f9")
        self.infoApLabel.configure(activeforeground="black")
        self.infoApLabel.configure(background="#2291ff")
        self.infoApLabel.configure(disabledforeground="#a3a3a3")
        self.infoApLabel.configure(foreground="#ffffff")
        self.infoApLabel.configure(highlightbackground="#d9d9d9")
        self.infoApLabel.configure(highlightcolor="black")
        self.infoApLabel.configure(text='''Select records you would like to delete.''')

        self.TSeparator1 = ttk.Separator(master)
        self.TSeparator1.place(relx=0.117, rely=0.311, relwidth=0.783)

        self.applicationListBox = tk.Listbox(master)
        self.applicationListBox.place(relx=0.5, rely=0.6, anchor = 'center', relheight=0.449
                , relwidth=0.89)
        self.applicationListBox.configure(background="white")
        self.applicationListBox.configure(disabledforeground="#a3a3a3")
        self.applicationListBox.configure(font="TkFixedFont")
        self.applicationListBox.configure(foreground="#000000")
        self.applicationListBox.configure(highlightbackground="#d9d9d9")
        self.applicationListBox.configure(highlightcolor="black")
        self.applicationListBox.configure(selectbackground="blue")
        self.applicationListBox.configure(selectforeground="white")

        self.deleteButton = tk.Button(master)
        self.deleteButton.place(relx=0.25, rely=0.93, anchor = 'center', height=34, width=201)
        self.deleteButton.configure(activebackground="#ff8a15")
        self.deleteButton.configure(activeforeground="#000000")
        self.deleteButton.configure(background="#f47a00")
        self.deleteButton.configure(disabledforeground="#a3a3a3")
        self.deleteButton.configure(font="-family {Trebuchet MS} -size 14 -weight normal -slant roman -underline 0 -overstrike 0")
        self.deleteButton.configure(foreground="#ffffff")
        self.deleteButton.configure(highlightbackground="#d9d9d9")
        self.deleteButton.configure(highlightcolor="black")
        self.deleteButton.configure(pady="0")
        self.deleteButton.configure(text='''Delete''')

        self.exitButton = tk.Button(master)
        self.exitButton.place(relx=0.75, rely=0.93, height=34, anchor = 'center', width=201)
        self.exitButton.configure(activebackground="#ff8a15")
        self.exitButton.configure(activeforeground="#000000")
        self.exitButton.configure(background="#f47a00")
        self.exitButton.configure(disabledforeground="#a3a3a3")
        self.exitButton.configure(font="-family {Trebuchet MS} -size 14 -weight normal -slant roman -underline 0 -overstrike 0")
        self.exitButton.configure(foreground="#ffffff")
        self.exitButton.configure(highlightbackground="#d9d9d9")
        self.exitButton.configure(highlightcolor="black")
        self.exitButton.configure(pady="0")
        self.exitButton.configure(text='''Exit''')
        self.exitButton.configure(command=self.changePage)

    def changePage(self):
        self.master.change(GUI_Application_Page.Application_Page)        