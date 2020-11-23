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
from GUI_Application_History_Page import Application_History_Page
import Project_412

class Adoption_Certificate_Page(tk.Frame):
    def __init__(self, master=None, **kwargs):

        self.userInfo = kwargs['UserInfo']
        self.dogInfo = kwargs['dogSelection']

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

        master.geometry("600x450+1089+727")
        master.minsize(120, 1)
        master.maxsize(2564, 1421)
        master.resizable(1, 1)
        master.title("Adoption Certificate Page")
        master.configure(background="#2291ff")
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")

        self.nameLabel = ttk.Label(master)
        self.nameLabel.place(relx=0.05, rely=0.333, height=29, width=300)
        self.nameLabel.configure(background="#2291ff")
        self.nameLabel.configure(foreground="#ffffff")
        self.nameLabel.configure(font="-family SimSun -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.nameLabel.configure(relief="flat")
        self.nameLabel.configure(anchor='w')
        self.nameLabel.configure(justify='left')
        self.nameLabel.configure(text='''Adopter Name:''')

        self.nameLabel_1 = ttk.Label(master)
        self.nameLabel_1.place(relx=0.05, rely=0.4, height=29, width=300)
        self.nameLabel_1.configure(background="#2291ff")
        self.nameLabel_1.configure(foreground="#ffffff")
        self.nameLabel_1.configure(font="-family SimSun -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.nameLabel_1.configure(relief="flat")
        self.nameLabel_1.configure(anchor='w')
        self.nameLabel_1.configure(justify='left')
        self.nameLabel_1.configure(text='''Adoption Administrator:''')

        self.nameLabel_2 = ttk.Label(master)
        self.nameLabel_2.place(relx=0.05, rely=0.467, height=32, width=236)
        self.nameLabel_2.configure(background="#2291ff")
        self.nameLabel_2.configure(foreground="#ffffff")
        self.nameLabel_2.configure(font="-family SimSun -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.nameLabel_2.configure(relief="flat")
        self.nameLabel_2.configure(anchor='w')
        self.nameLabel_2.configure(justify='left')
        self.nameLabel_2.configure(text='''Adopted Dog ID:''')

        self.nameLabel_3 = ttk.Label(master)
        self.nameLabel_3.place(relx=0.05, rely=0.644, height=29, width=236)
        self.nameLabel_3.configure(background="#2291ff")
        self.nameLabel_3.configure(foreground="#ffffff")
        self.nameLabel_3.configure(font="-family SimSun -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.nameLabel_3.configure(relief="flat")
        self.nameLabel_3.configure(anchor='w')
        self.nameLabel_3.configure(justify='left')
        self.nameLabel_3.configure(text='''Shelter Name:''')

        self.nameLabel_4 = ttk.Label(master)
        self.nameLabel_4.place(relx=0.05, rely=0.711, height=29, width=236)
        self.nameLabel_4.configure(background="#2291ff")
        self.nameLabel_4.configure(foreground="#ffffff")
        self.nameLabel_4.configure(font="-family SimSun -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.nameLabel_4.configure(relief="flat")
        self.nameLabel_4.configure(anchor='w')
        self.nameLabel_4.configure(justify='left')
        self.nameLabel_4.configure(text='''Shelter Address:''')

        self.nameLabel_1 = ttk.Label(master)
        self.nameLabel_1.place(relx=0.05, rely=0.778, height=29, width=236)
        self.nameLabel_1.configure(background="#2291ff")
        self.nameLabel_1.configure(foreground="#ffffff")
        self.nameLabel_1.configure(font="-family SimSun -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.nameLabel_1.configure(relief="flat")
        self.nameLabel_1.configure(anchor='w')
        self.nameLabel_1.configure(justify='left')
        self.nameLabel_1.configure(text='''Shelter Phone Number:''')

        self.adopterNameLabel = ttk.Label(master)
        self.adopterNameLabel.place(relx=0.483, rely=0.333, height=29, width=296)

        self.adopterNameLabel.configure(background="#2291ff")
        self.adopterNameLabel.configure(foreground="#ffffff")
        self.adopterNameLabel.configure(font="-family SimSun -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.adopterNameLabel.configure(relief="flat")
        self.adopterNameLabel.configure(anchor='w')
        self.adopterNameLabel.configure(justify='left')
        self.adopterNameLabel.configure(text=self.userInfo['USERINFO']['name'])

        self.adoptionAdminLabel = ttk.Label(master)
        self.adoptionAdminLabel.place(relx=0.483, rely=0.4, height=29, width=296)

        self.adoptionAdminLabel.configure(background="#2291ff")
        self.adoptionAdminLabel.configure(foreground="#ffffff")
        self.adoptionAdminLabel.configure(font="-family SimSun -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.adoptionAdminLabel.configure(relief="flat")
        self.adoptionAdminLabel.configure(anchor='w')
        self.adoptionAdminLabel.configure(justify='left')
        self.adoptionAdminLabel.configure(text='''[Info Here]''')

        self.dogIDLabel = ttk.Label(master)
        self.dogIDLabel.place(relx=0.483, rely=0.467, height=29, width=296)
        self.dogIDLabel.configure(background="#2291ff")
        self.dogIDLabel.configure(foreground="#ffffff")
        self.dogIDLabel.configure(font="-family SimSun -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.dogIDLabel.configure(relief="flat")
        self.dogIDLabel.configure(anchor='w')
        self.dogIDLabel.configure(justify='left')
        self.dogIDLabel.configure(text=self.dogInfo[8])     #load dogID

        self.shelterNameLabel = ttk.Label(master)
        self.shelterNameLabel.place(relx=0.483, rely=0.644, height=29, width=296)

        self.shelterNameLabel.configure(background="#2291ff")
        self.shelterNameLabel.configure(foreground="#ffffff")
        self.shelterNameLabel.configure(font="-family SimSun -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.shelterNameLabel.configure(relief="flat")
        self.shelterNameLabel.configure(anchor='w')
        self.shelterNameLabel.configure(justify='left')
        self.shelterNameLabel.configure(text='''[Info Here]''')

        self.shelterAddressLabel = ttk.Label(master)
        self.shelterAddressLabel.place(relx=0.483, rely=0.711, height=29
                , width=296)
        self.shelterAddressLabel.configure(background="#2291ff")
        self.shelterAddressLabel.configure(foreground="#ffffff")
        self.shelterAddressLabel.configure(font="-family SimSun -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.shelterAddressLabel.configure(relief="flat")
        self.shelterAddressLabel.configure(anchor='w')
        self.shelterAddressLabel.configure(justify='left')
        self.shelterAddressLabel.configure(text='''[Info Here]''')

        self.adopterNameLabel_9 = ttk.Label(master)
        self.adopterNameLabel_9.place(relx=0.483, rely=0.778, height=29
                , width=296)
        self.adopterNameLabel_9.configure(background="#2291ff")
        self.adopterNameLabel_9.configure(foreground="#ffffff")
        self.adopterNameLabel_9.configure(font="-family SimSun -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.adopterNameLabel_9.configure(relief="flat")
        self.adopterNameLabel_9.configure(anchor='w')
        self.adopterNameLabel_9.configure(justify='left')
        self.adopterNameLabel_9.configure(text='''[Info Here]''')

        self.newAdoptButton = tk.Button(master)
        self.newAdoptButton.place(relx=0.25, rely=0.93, anchor = 'center', height=34, width=240)
        self.newAdoptButton.configure(activebackground="#ff8a15")
        self.newAdoptButton.configure(activeforeground="#000000")
        self.newAdoptButton.configure(background="#f47a00")
        self.newAdoptButton.configure(disabledforeground="#a3a3a3")
        self.newAdoptButton.configure(font="-family {Trebuchet MS} -size 14 -weight normal -slant roman -underline 0 -overstrike 0")
        self.newAdoptButton.configure(foreground="#ffffff")
        self.newAdoptButton.configure(highlightbackground="#d9d9d9")
        self.newAdoptButton.configure(highlightcolor="black")
        self.newAdoptButton.configure(pady="0")
        self.newAdoptButton.configure(text='''New Adoption''')
        self.newAdoptButton.configure(command=self.changePage)

        self.manageButton = tk.Button(master)
        self.manageButton.place(relx=0.75, rely=0.93, anchor = 'center', height=34, width=240)
        self.manageButton.configure(activebackground="#ff8a15")
        self.manageButton.configure(activeforeground="#000000")
        self.manageButton.configure(background="#f47a00")
        self.manageButton.configure(disabledforeground="#a3a3a3")
        self.manageButton.configure(font="-family {Trebuchet MS} -size 14 -weight normal -slant roman -underline 0 -overstrike 0")
        self.manageButton.configure(foreground="#ffffff")
        self.manageButton.configure(highlightbackground="#d9d9d9")
        self.manageButton.configure(highlightcolor="black")
        self.manageButton.configure(pady="0")
        self.manageButton.configure(text='''Manage Adoption History''')
        self.manageButton.configure(command=self.changePage2)

        self.Label1 = tk.Label(master)
        self.Label1.place(relx=0.5, rely=0.067, anchor = 'center', height=41, width=700)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#2291ff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 24 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Adoption Certificate''')

        self.infoApLabel = tk.Label(master)
        self.infoApLabel.place(relx=0.5, rely=0.178, anchor = 'center', height=22, width=700)
        self.infoApLabel.configure(activebackground="#f9f9f9")
        self.infoApLabel.configure(activeforeground="black")
        self.infoApLabel.configure(background="#2291ff")
        self.infoApLabel.configure(disabledforeground="#a3a3a3")
        self.infoApLabel.configure(foreground="#ffffff")
        self.infoApLabel.configure(highlightbackground="#d9d9d9")
        self.infoApLabel.configure(highlightcolor="black")
        self.infoApLabel.configure(text='''Please visit the shelter to finalize your adoption and bring home your new friend!''')

        self.TSeparator1 = ttk.Separator(master)
        self.TSeparator1.place(relx=0.1, rely=0.267, relwidth=0.783)

    def changePage(self):
        self.master.change(GUI_Application_Page.Application_Page)   
    def changePage2(self):
        self.master.change(Application_History_Page)      