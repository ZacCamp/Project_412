
import sys
import Project_412

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

from GUI_Application_Page import Application_Page

class Landing_Page(tk.Frame):
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

        master.geometry("689x452+1095+735")
        master.minsize(120, 1)
        master.maxsize(2564, 1421)
        master.resizable(1, 1)
        master.title("Landing Page")
        master.configure(background="#2291ff")
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")

        self.welcomeLabel = tk.Label(master)
        self.welcomeLabel.place(relx=.5, rely=0.111, anchor = 'center', height=41, width=400)
        self.welcomeLabel.configure(activebackground="#f9f9f9")
        self.welcomeLabel.configure(activeforeground="black")
        self.welcomeLabel.configure(background="#2291ff")
        self.welcomeLabel.configure(disabledforeground="#a3a3a3")
        self.welcomeLabel.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 24 -weight normal -slant roman -underline 0 -overstrike 0")
        self.welcomeLabel.configure(foreground="#ffffff")
        self.welcomeLabel.configure(highlightbackground="#d9d9d9")
        self.welcomeLabel.configure(highlightcolor="black")
        self.welcomeLabel.configure(text='''Welcome To Pet Finder!''')

        self.infoLabel = tk.Label(master)
        self.infoLabel.place(relx=0.5, rely=0.199, anchor = 'center', height=21, width=500)
        self.infoLabel.configure(activebackground="#f9f9f9")
        self.infoLabel.configure(activeforeground="black")
        self.infoLabel.configure(background="#2291ff")
        self.infoLabel.configure(disabledforeground="#a3a3a3")
        self.infoLabel.configure(foreground="#ffffff")
        self.infoLabel.configure(highlightbackground="#d9d9d9")
        self.infoLabel.configure(highlightcolor="black")
        self.infoLabel.configure(text='''Please provide us with some basic information before we continue.''')

        self.nameLabel = ttk.Label(master)
        self.nameLabel.place(relx=0.131, rely=0.42, height=30, width=70)
        self.nameLabel.configure(background="#2291ff")
        self.nameLabel.configure(foreground="#ffffff")
        self.nameLabel.configure(font="-family SimSun -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.nameLabel.configure(relief="flat")
        self.nameLabel.configure(anchor='w')
        self.nameLabel.configure(justify='left')
        self.nameLabel.configure(text='''Name:''')

        self.numberLabel = ttk.Label(master)
        self.numberLabel.place(relx=0.131, rely=0.553, height=30, width=170)
        self.numberLabel.configure(background="#2291ff")
        self.numberLabel.configure(foreground="#ffffff")
        self.numberLabel.configure(font="-family SimSun -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.numberLabel.configure(relief="flat")
        self.numberLabel.configure(anchor='w')
        self.numberLabel.configure(justify='left')
        self.numberLabel.configure(text='''Phone Number:''')

        self.zipLabel = ttk.Label(master)
        self.zipLabel.place(relx=0.131, rely=0.686, height=30, width=102)
        self.zipLabel.configure(background="#2291ff")
        self.zipLabel.configure(foreground="#ffffff")
        self.zipLabel.configure(font="-family SimSun -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.zipLabel.configure(relief="flat")
        self.zipLabel.configure(anchor='w')
        self.zipLabel.configure(justify='left')
        self.zipLabel.configure(text='''Zip Code:''')

        self.nameEntry = tk.Entry(master)
        self.nameEntry.place(relx=0.392, rely=0.42,height=20, relwidth=0.412)
        self.nameEntry.configure(background="white")
        self.nameEntry.configure(disabledforeground="#a3a3a3")
        self.nameEntry.configure(font="TkFixedFont")
        self.nameEntry.configure(foreground="#000000")
        self.nameEntry.configure(highlightbackground="#d9d9d9")
        self.nameEntry.configure(highlightcolor="black")
        self.nameEntry.configure(insertbackground="black")
        self.nameEntry.configure(selectbackground="blue")
        self.nameEntry.configure(selectforeground="white")

        self.phoneEntry = tk.Entry(master)
        self.phoneEntry.place(relx=0.392, rely=0.553,height=20, relwidth=0.412)
        self.phoneEntry.configure(background="white")
        self.phoneEntry.configure(disabledforeground="#a3a3a3")
        self.phoneEntry.configure(font="TkFixedFont")
        self.phoneEntry.configure(foreground="#000000")
        self.phoneEntry.configure(highlightbackground="#d9d9d9")
        self.phoneEntry.configure(highlightcolor="black")
        self.phoneEntry.configure(insertbackground="black")
        self.phoneEntry.configure(selectbackground="blue")
        self.phoneEntry.configure(selectforeground="white")

        self.zipEntry = tk.Entry(master)
        self.zipEntry.place(relx=0.392, rely=0.686,height=20, relwidth=0.412)
        self.zipEntry.configure(background="white")
        self.zipEntry.configure(disabledforeground="#a3a3a3")
        self.zipEntry.configure(font="TkFixedFont")
        self.zipEntry.configure(foreground="#000000")
        self.zipEntry.configure(highlightbackground="#d9d9d9")
        self.zipEntry.configure(highlightcolor="black")
        self.zipEntry.configure(insertbackground="black")
        self.zipEntry.configure(selectbackground="blue")
        self.zipEntry.configure(selectforeground="white")

        self.beginApplicationButton = tk.Button(master)
        self.beginApplicationButton.place(relx=0.5, rely=0.841, anchor = 'center', height=34
                , width=201)
        self.beginApplicationButton.configure(activebackground="#ff8a15")
        self.beginApplicationButton.configure(activeforeground="#000000")
        self.beginApplicationButton.configure(background="#f47a00")
        self.beginApplicationButton.configure(disabledforeground="#a3a3a3")
        self.beginApplicationButton.configure(font="-family {Trebuchet MS} -size 14 -weight normal -slant roman -underline 0 -overstrike 0")
        self.beginApplicationButton.configure(foreground="#ffffff")
        self.beginApplicationButton.configure(highlightbackground="#d9d9d9")
        self.beginApplicationButton.configure(highlightcolor="black")
        self.beginApplicationButton.configure(pady="0")
        self.beginApplicationButton.configure(text='''Begin Application''')
        self.beginApplicationButton.configure(command=self.changePage)

        self.TSeparator1 = ttk.Separator(master)
        self.TSeparator1.place(relx=0.145, rely=0.288, relwidth=0.682)

    def changePage(self):
        userInfo = {'name': self.nameEntry.get(), 'phone': self.phoneEntry.get(), 'zip':self.zipEntry.get()}
        self.master.change(Application_Page, USERINFO =userInfo)
        













    