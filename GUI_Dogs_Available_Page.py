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

from GUI_Adoption_Certificate_Page import Adoption_Certificate_Page
import Project_412

class Dogs_Available_Page(tk.Frame):
    def __init__(self, master=None, **kwargs):

        tk.Frame.__init__(self, master)
        
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

        master.geometry("600x450+1022+761")
        master.minsize(120, 1)
        master.maxsize(2564, 1421)
        master.resizable(1, 1)
        master.title("New masterlevel")
        master.configure(background="#2291ff")
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")

        self.menubar = tk.Menu(master,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        master.configure(menu = self.menubar)

        self.Label1 = tk.Label(master)
        self.Label1.place(relx=0.5, rely=0.089, anchor = 'center', height=41, width=700)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#2291ff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 24 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Available Dogs''')

        self.infoApLabel = tk.Label(master)
        self.infoApLabel.place(relx=0.5, rely=0.222, anchor = 'center', height=22, width=700)
        self.infoApLabel.configure(activebackground="#f9f9f9")
        self.infoApLabel.configure(activeforeground="black")
        self.infoApLabel.configure(background="#2291ff")
        self.infoApLabel.configure(disabledforeground="#a3a3a3")
        self.infoApLabel.configure(foreground="#ffffff")
        self.infoApLabel.configure(highlightbackground="#d9d9d9")
        self.infoApLabel.configure(highlightcolor="black")
        self.infoApLabel.configure(text='''Please select the dog you would like to adopt.''')

        self.TSeparator1 = ttk.Separator(master)
        self.TSeparator1.place(relx=0.117, rely=0.311, relwidth=0.783)

        self.dogListBox = tk.Listbox(master)
        self.dogListBox.place(relx=0.067, rely=0.378, relheight=0.449
                , relwidth=0.89)
        self.dogListBox.configure(background="white")
        self.dogListBox.configure(disabledforeground="#a3a3a3")
        self.dogListBox.configure(font="TkFixedFont")
        self.dogListBox.configure(foreground="#000000")
        self.dogListBox.configure(highlightbackground="#d9d9d9")
        self.dogListBox.configure(highlightcolor="black")
        self.dogListBox.configure(selectbackground="blue")
        self.dogListBox.configure(selectforeground="white")

        self.adoptButton = tk.Button(master)
        self.adoptButton.place(relx=0.5, anchor = 'center', rely=0.93, height=34, width=201)
        self.adoptButton.configure(activebackground="#ff8a15")
        self.adoptButton.configure(activeforeground="#000000")
        self.adoptButton.configure(background="#f47a00")
        self.adoptButton.configure(disabledforeground="#a3a3a3")
        self.adoptButton.configure(font="-family {Trebuchet MS} -size 14 -weight normal -slant roman -underline 0 -overstrike 0")
        self.adoptButton.configure(foreground="#ffffff")
        self.adoptButton.configure(highlightbackground="#d9d9d9")
        self.adoptButton.configure(highlightcolor="black")
        self.adoptButton.configure(pady="0")
        self.adoptButton.configure(text='''Register Adoption''')
        self.adoptButton.configure(command=self.changePage)

    def changePage(self):
        self.master.change(Adoption_Certificate_Page, res='')