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

from GUI_Dogs_Available_Page import Dogs_Available_Page
import Project_412

class Application_Page(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master)

        self.comboboxSex = tk.StringVar()
        self.comboboxBreed = tk.StringVar()
        self.comboboxMaint = tk.StringVar()
        self.comboboxIntake = tk.StringVar()
        self.comboboxAge = tk.StringVar()
        self.comboboxTemp = tk.StringVar()

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

        master.geometry("600x452+1143+768")
        master.minsize(120, 1)
        master.maxsize(2564, 1421)
        master.resizable(1, 1)
        master.title("Application Page")
        master.configure(background="#2291ff")
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")

        self.applicationLabel = tk.Label(master)
        self.applicationLabel.place(relx=0.5, rely=0.088, anchor = 'center', height=31, width=338)
        self.applicationLabel.configure(activebackground="#f9f9f9")
        self.applicationLabel.configure(activeforeground="black")
        self.applicationLabel.configure(background="#2291ff")
        self.applicationLabel.configure(disabledforeground="#a3a3a3")
        self.applicationLabel.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 24 -weight normal -slant roman -underline 0 -overstrike 0")
        self.applicationLabel.configure(foreground="#ffffff")
        self.applicationLabel.configure(highlightbackground="#d9d9d9")
        self.applicationLabel.configure(highlightcolor="black")
        self.applicationLabel.configure(text='''Pet Application''')

        self.infoApLabel = tk.Label(master)
        self.infoApLabel.place(relx=0.5, rely=0.199, anchor = 'center', height=22, width=700)
        self.infoApLabel.configure(activebackground="#f9f9f9")
        self.infoApLabel.configure(activeforeground="black")
        self.infoApLabel.configure(background="#2291ff")
        self.infoApLabel.configure(disabledforeground="#a3a3a3")
        self.infoApLabel.configure(foreground="#ffffff")
        self.infoApLabel.configure(highlightbackground="#d9d9d9")
        self.infoApLabel.configure(highlightcolor="black")
        self.infoApLabel.configure(text='''Please answer the following questions so we can match you with compatible dogs.''')

        self.TSeparator1 = ttk.Separator(master)
        self.TSeparator1.place(relx=0.1, rely=0.288, relwidth=0.783)

        self.menubar = tk.Menu(master,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        master.configure(menu = self.menubar)

        self.sexCBox = ttk.Combobox(master, state='readonly')
        self.sexCBox.place(relx=0.533, rely=0.354, relheight=0.046
                , relwidth=0.288)
        self.sexCBox.configure(textvariable=self.comboboxSex)
        self.sexCBox.configure(takefocus="")
        self.sexCBox['values'] = ('[any]','male', 'female') 

        self.nameLabel = ttk.Label(master)
        self.nameLabel.place(relx=0.1, rely=0.354, height=29, width=166)
        self.nameLabel.configure(background="#2291ff")
        self.nameLabel.configure(foreground="#ffffff")
        self.nameLabel.configure(font="-family SimSun -size 13 -weight normal -slant roman -underline 0 -overstrike 0")
        self.nameLabel.configure(relief="flat")
        self.nameLabel.configure(anchor='w')
        self.nameLabel.configure(justify='left')
        self.nameLabel.configure(text='''Sex Preference:''')

        self.nameLabel_5 = ttk.Label(master)
        self.nameLabel_5.place(relx=0.1, rely=0.442, height=29, width=166)
        self.nameLabel_5.configure(background="#2291ff")
        self.nameLabel_5.configure(foreground="#ffffff")
        self.nameLabel_5.configure(font="-family SimSun -size 13 -weight normal -slant roman -underline 0 -overstrike 0")
        self.nameLabel_5.configure(relief="flat")
        self.nameLabel_5.configure(anchor='w')
        self.nameLabel_5.configure(justify='left')
        self.nameLabel_5.configure(text='''Breed Preference:''')

        self.breedCBox = ttk.Combobox(master, state='readonly')
        self.breedCBox.place(relx=0.533, rely=0.442, relheight=0.046
                , relwidth=0.288)
        self.breedCBox.configure(textvariable=self.comboboxBreed)
        self.breedCBox.configure(takefocus="")
        self.breedCBox['values'] = ('[any]','affenpinscher','Afghan hound','Airedale terrier','Akita','Alaskan Malamute','American Staffordshire terrier','American water spaniel','Australian cattle dog','Australian shepherd','Australian terrier','basenji','basset hound','beagle','bearded collie','Bedlington terrier','Bernese mountain dog','bichon frise','black and tan coonhound','bloodhound','border collie','border terrier','borzoi','Boston terrier','bouvier des Flandres','boxer','briard','Brittany','Brussels griffon','bull terrier','bulldog','bullmastiff','cairn terrier','Canaan dog','Chesapeake Bay retriever','Chihuahua','Chinese crested','Chinese shar-pei','chow chow','Clumber spaniel','cocker spaniel','collie','curly-coated retriever','dachshund','Dalmatian','Doberman pinscher','English cocker spaniel','English setter','English springer spaniel','English toy spaniel','Eskimo dog','Finnish spitz','flat-coated retriever','fox terrier','foxhound','French bulldog','German shepherd','German shorthaired pointer','German wirehaired pointer','golden retriever','Gordon setter','Great Dane','greyhound','Irish setter','Irish water spaniel','Irish wolfhound','Jack Russell terrier','Japanese spaniel','keeshond','Kerry blue terrier','komondor','kuvasz','Labrador retriever','Lakeland terrier','Lhasa apso','Maltese','Manchester terrier','mastiff','Mexican hairless','Newfoundland','Norwegian elkhound','Norwich terrier','otterhound','papillon','Pekingese','pointer','Pomeranian','poodle','pug','puli','Rhodesian ridgeback','Rottweiler','Saint Bernard','saluki','Samoyed','schipperke','schnauzer','Scottish deerhound','Scottish terrier','Sealyham terrier','Shetland sheepdog','shih tzu','Siberian husky','silky terrier','Skye terrier','Staffordshire bull terrier','soft-coated wheaten terrier','Sussex spaniel','spitz','Tibetan terrier','vizsla','Weimaraner','Welsh terrier','West Highland white terrier','whippet','Yorkshire terrier') 

        self.nameLabel_6 = ttk.Label(master)
        self.nameLabel_6.place(relx=0.097, rely=0.531, height=29, width=216)
        self.nameLabel_6.configure(background="#2291ff")
        self.nameLabel_6.configure(foreground="#ffffff")
        self.nameLabel_6.configure(font="-family SimSun -size 13 -weight normal -slant roman -underline 0 -overstrike 0")
        self.nameLabel_6.configure(relief="flat")
        self.nameLabel_6.configure(anchor='w')
        self.nameLabel_6.configure(justify='left')
        self.nameLabel_6.configure(text='''Intake Type Preference:''')

        self.intakeCBox = ttk.Combobox(master, state='readonly')
        self.intakeCBox.place(relx=0.533, rely=0.531, relheight=0.046
                , relwidth=0.288)
        self.intakeCBox.configure(textvariable=self.comboboxIntake)
        self.intakeCBox.configure(takefocus="")
        self.intakeCBox['values'] = ('[any]', 'surrendered', 'stray') 

        self.nameLabel_7 = ttk.Label(master)
        self.nameLabel_7.place(relx=0.097, rely=0.619, height=29, width=230)
        self.nameLabel_7.configure(background="#2291ff")
        self.nameLabel_7.configure(foreground="#ffffff")
        self.nameLabel_7.configure(font="-family SimSun -size 13 -weight normal -slant roman -underline 0 -overstrike 0")
        self.nameLabel_7.configure(relief="flat")
        self.nameLabel_7.configure(anchor='w')
        self.nameLabel_7.configure(justify='left')
        self.nameLabel_7.configure(text='''Temperament Preference:''')

        self.temperamentCBox = ttk.Combobox(master, state='readonly')
        self.temperamentCBox.place(relx=0.533, rely=0.619, relheight=0.046
                , relwidth=0.288)
        self.temperamentCBox.configure(textvariable=self.comboboxTemp)
        self.temperamentCBox.configure(takefocus="")
        self.temperamentCBox['values'] = ('[any]', 'assertive', 'neutral', 'passive') 

        self.nameLabel_8 = ttk.Label(master)
        self.nameLabel_8.place(relx=0.097, rely=0.708, height=29, width=246)
        self.nameLabel_8.configure(background="#2291ff")
        self.nameLabel_8.configure(foreground="#ffffff")
        self.nameLabel_8.configure(font="-family SimSun -size 13 -weight normal -slant roman -underline 0 -overstrike 0")
        self.nameLabel_8.configure(relief="flat")
        self.nameLabel_8.configure(anchor='w')
        self.nameLabel_8.configure(justify='left')
        self.nameLabel_8.configure(text='''Maintenence Level:''')

        self.maintenenceCBox = ttk.Combobox(master, state='readonly')
        self.maintenenceCBox.place(relx=0.533, rely=0.708, relheight=0.046
                , relwidth=0.288)
        self.maintenenceCBox.configure(textvariable=self.comboboxMaint)
        self.maintenenceCBox.configure(takefocus="")
        self.maintenenceCBox['values'] = ('[any]','low', 'medium', 'high')

        self.nameLabel_9 = ttk.Label(master)
        self.nameLabel_9.place(relx=0.097, rely=0.796, height=29, width=230)
        self.nameLabel_9.configure(background="#2291ff")
        self.nameLabel_9.configure(foreground="#ffffff")
        self.nameLabel_9.configure(font="-family SimSun -size 13 -weight normal -slant roman -underline 0 -overstrike 0")
        self.nameLabel_9.configure(relief="flat")
        self.nameLabel_9.configure(anchor='w')
        self.nameLabel_9.configure(justify='left')
        self.nameLabel_9.configure(text='''Maximum Age:''')

        self.ageCBox = ttk.Combobox(master, state='readonly')
        self.ageCBox.place(relx=0.533, rely=0.796, relheight=0.046
                , relwidth=0.288)
        self.ageCBox.configure(textvariable=self.comboboxAge)
        self.ageCBox.configure(takefocus="")
        self.ageCBox['values'] = ('[any]', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13')

        self.searchButton = tk.Button(master)
        self.searchButton.place(relx=0.5, rely=0.93, anchor = 'center', height=34, width=201)
        self.searchButton.configure(activebackground="#ff8a15")
        self.searchButton.configure(activeforeground="#000000")
        self.searchButton.configure(background="#f47a00")
        self.searchButton.configure(disabledforeground="#a3a3a3")
        self.searchButton.configure(font="-family {Trebuchet MS} -size 14 -weight normal -slant roman -underline 0 -overstrike 0")
        self.searchButton.configure(foreground="#ffffff")
        self.searchButton.configure(highlightbackground="#d9d9d9")
        self.searchButton.configure(highlightcolor="black")
        self.searchButton.configure(pady="0")
        self.searchButton.configure(text='''Search Dogs''')
        self.searchButton.configure(command=self.changePage)

        self.setDefaults()
        
    def setDefaults(self):
        #print("ran")
        self.maintenenceCBox.set('[any]')
        self.sexCBox.set('[any]')
        self.intakeCBox.set('[any]')
        self.temperamentCBox.set('[any]')
        self.breedCBox.set('[any]')
        self.ageCBox.set('[any]')

    def changePage(self):
        result = Project_412.getDogs(self.breedCBox.get(), self.intakeCBox.get(), self.sexCBox.get(),
                                    self.maintenenceCBox.get(), self.temperamentCBox.get(), self.ageCBox.get())
        #print(result)
        #print(self.breedCBox.get())
        self.master.change(Dogs_Available_Page, res = result)

    
