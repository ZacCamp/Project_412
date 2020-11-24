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

        self.userInfo = kwargs['UserInfo']  #store the user information
        self.availableDogs = kwargs['Query']  #grab the results from SQL statement
        
        
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

        self.breedLabel = tk.Label(master)
        self.breedLabel.place(relx=0.117, rely=0.351, anchor = 'center', height=31, width=70)
        self.breedLabel.configure(activebackground="#f9f9f9")
        self.breedLabel.configure(activeforeground="black")
        self.breedLabel.configure(background="#2291ff")
        self.breedLabel.configure(disabledforeground="#a3a3a3")
        self.breedLabel.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 7 -weight normal -slant roman -underline 0 -overstrike 0")
        self.breedLabel.configure(foreground="#ffffff")
        self.breedLabel.configure(highlightbackground="#d9d9d9")
        self.breedLabel.configure(highlightcolor="black")
        self.breedLabel.configure(text='''Breed''')

        self.intakeLabel = tk.Label(master)
        self.intakeLabel.place(relx=0.267, rely=0.351, anchor = 'center', height=31, width=95)
        self.intakeLabel.configure(activebackground="#f9f9f9")
        self.intakeLabel.configure(activeforeground="black")
        self.intakeLabel.configure(background="#2291ff")
        self.intakeLabel.configure(disabledforeground="#a3a3a3")
        self.intakeLabel.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 7 -weight normal -slant roman -underline 0 -overstrike 0")
        self.intakeLabel.configure(foreground="#ffffff")
        self.intakeLabel.configure(highlightbackground="#d9d9d9")
        self.intakeLabel.configure(highlightcolor="black")
        self.intakeLabel.configure(text='''Intake type''')

        self.sexLabel = tk.Label(master)
        self.sexLabel.place(relx=0.417, rely=0.351, anchor = 'center', height=31, width=95)
        self.sexLabel.configure(activebackground="#f9f9f9")
        self.sexLabel.configure(activeforeground="black")
        self.sexLabel.configure(background="#2291ff")
        self.sexLabel.configure(disabledforeground="#a3a3a3")
        self.sexLabel.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 7 -weight normal -slant roman -underline 0 -overstrike 0")
        self.sexLabel.configure(foreground="#ffffff")
        self.sexLabel.configure(highlightbackground="#d9d9d9")
        self.sexLabel.configure(highlightcolor="black")
        self.sexLabel.configure(text='''Sex''')

        self.maintenanceLabel = tk.Label(master)
        self.maintenanceLabel.place(relx=0.567, rely=0.351, anchor = 'center', height=31, width=95)
        self.maintenanceLabel.configure(activebackground="#f9f9f9")
        self.maintenanceLabel.configure(activeforeground="black")
        self.maintenanceLabel.configure(background="#2291ff")
        self.maintenanceLabel.configure(disabledforeground="#a3a3a3")
        self.maintenanceLabel.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 7 -weight normal -slant roman -underline 0 -overstrike 0")
        self.maintenanceLabel.configure(foreground="#ffffff")
        self.maintenanceLabel.configure(highlightbackground="#d9d9d9")
        self.maintenanceLabel.configure(highlightcolor="black")
        self.maintenanceLabel.configure(text='''Maintenance''')

        self.temperamenLabel = tk.Label(master)
        self.temperamenLabel.place(relx=0.717, rely=0.351, anchor = 'center', height=31, width=95)
        self.temperamenLabel.configure(activebackground="#f9f9f9")
        self.temperamenLabel.configure(activeforeground="black")
        self.temperamenLabel.configure(background="#2291ff")
        self.temperamenLabel.configure(disabledforeground="#a3a3a3")
        self.temperamenLabel.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 7 -weight normal -slant roman -underline 0 -overstrike 0")
        self.temperamenLabel.configure(foreground="#ffffff")
        self.temperamenLabel.configure(highlightbackground="#d9d9d9")
        self.temperamenLabel.configure(highlightcolor="black")
        self.temperamenLabel.configure(text='''Temperament''')
        
        self.ageLabel = tk.Label(master)
        self.ageLabel.place(relx=0.867, rely=0.351, anchor = 'center', height=31, width=95)
        self.ageLabel.configure(activebackground="#f9f9f9")
        self.ageLabel.configure(activeforeground="black")
        self.ageLabel.configure(background="#2291ff")
        self.ageLabel.configure(disabledforeground="#a3a3a3")
        self.ageLabel.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 7 -weight normal -slant roman -underline 0 -overstrike 0")
        self.ageLabel.configure(foreground="#ffffff")
        self.ageLabel.configure(highlightbackground="#d9d9d9")
        self.ageLabel.configure(highlightcolor="black")
        self.ageLabel.configure(text='''Age''')

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

        for item in self.availableDogs:  #Load the query results into the listbox
            self.dogListBox.insert(tk.END,item)
        

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
        petSelected = (self.dogListBox.get(self.dogListBox.curselection()))         #get the selected dog from listbox
        ShelterInfo = Project_412.getShelters(petSelected[7])                       #get shelter info
        ShelterAdmin = Project_412.getShelterEmployee(petSelected[7])               #get admin info
        Project_412.insertAdoption(self.userInfo['USERINFO']['personID'],ShelterAdmin[1],petSelected[8] )   #create the new entry in the adoptions table
        self.master.change(Adoption_Certificate_Page, UserInfo= self.userInfo, dogSelection = petSelected, shelterInfo = ShelterInfo , shelterAdmin = ShelterAdmin)