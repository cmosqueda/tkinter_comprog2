from tkinter import *
from tkinter import ttk
# from PIL import ImageTk, Image

class Application:
    def __init__(self, main):
        # Tk.__init__(self, main)
        self.main = main
        self.main.geometry('520x340')
        # self.main.resizable(False, False)
        self.main.title('TUkinter')
        self.main.iconbitmap("tu_icon_blue.ico")
        

        self.initialize_ui()    #diri mahitabo tanan

        self.allTopics()    #tawgon niya tanan frames sa topics


    def initialize_ui(self):

        ############### MENU BAR ###############
        self.menuBar = Menu(self.main)

        #commands in Topics cascade
        self.actionMenu = Menu(self.menuBar, tearoff=0)
        self.actionMenu.add_command(label='Go to topics', command=lambda: self.showFrame(self.topicsFrame))
        self.actionMenu.add_command(label='Youtube tutorials', command=0)
        self.actionMenu.add_command(label='Website resources', command=0)
        self.actionMenu.add_command(label='IDE recommendations', command=0)
        self.actionMenu.add_separator()
        self.actionMenu.add_command(label='Go back', command=lambda: self.showFrame(self.welcomeFrame))

        #add Actions cascade in menuBar
        self.menuBar.add_cascade(label='Actions', menu=self.actionMenu)


        #configure menuBar
        self.main.config(menu=self.menuBar)


        ############### WELCOME FRAME ###############
        self.welcomeFrame = Frame(self.main)
        self.welcomeFrame.grid(row=0, column=0, columnspan=7, rowspan=10)
        #welcomeFrame will show up as default

        #insert logo here


        self.welcomeTitle = Label(self.welcomeFrame,
                                    text='Welcome to TUkinter!',
                                    font=('Helvetica, 15'))
        self.welcomeTitle.grid(row=0, column=1, columnspan=6, pady=50, sticky='nsew')
        

        self.welcomeText = Label(self.welcomeFrame,
                                    text="TUkinter is a simple tutorial application for tkinter that is designed using pythons tkinter library. The contents of this tutorial application will likely focus on covering the basics of using tkinter for GUI development. This project will come handy especially to beginners who are learning tkinter for the first time, as well as instructors teaching python's tkinter.", 
                                    wraplength=480,
                                    font=('Helvetica', '9'))
        self.welcomeText.grid(row=1, column=1, columnspan=6, padx=20, pady=10, sticky='n')


        ############### TOPICS FRAME ###############
        self.topicsFrame = Frame(self.main)
        # self.topicsFrame.grid(row=0, column=0, columnspan=7, rowspan=10)
        #topicsFrame will only show when called by Topics command from actionMenu

        self.topicsTitle = Label(self.topicsFrame,
                                    text='Choose any topic you want to learn:',
                                    font=('Helvetica', '14'))
        self.topicsTitle.grid(row=0, column=0, columnspan=7, pady=5)

        #create listbox to store all topics
        self.topics_listBox = Listbox(self.topicsFrame,
                                        selectmode=BROWSE,
                                        relief=FLAT,
                                        font=('Helvetica', '12'))
        self.topics_listBox.grid(row=1, column=0, columnspan=4, ipadx=140, ipady=18, padx=25, pady=5)

        #create topic values
        self.topics = ['Getting started with Tkinter',
                        'Geometry Managers',
                        'Geometry Managers: Pack Layout',
                        'Geometry Managers: Grid Layout',
                        'Geometry Managers: Place Layout',
                        'Widgets',
                        'Label widget',
                        'Button widget',
                        'Entry widget',
                        'Frame widget',
                        'Canvas widget',
                        'Menu widget',
                        'Listbox widget',
                        'Scrollbar widget',
                        'Notebook widget',
                        'File I/O',
                        'A simple employee data managemet system',
                        'A simple calculator application']

        #iterate every topic
        for topic in range(len(self.topics)):
            self.topics_listBox.insert(END, self.topics[topic])

        # print(self.topics[0])   #getting started with tkinter


        #create view button
        self.viewTopicBtn = Button(self.topicsFrame,
                                    text='View topic',
                                    font=('Helvetica', '10'),
                                    command=self.showTopic)
        self.viewTopicBtn.bind('<Enter>', self.btn_on_enter)
        self.viewTopicBtn.bind('<Leave>', self.btn_on_leave)
        self.viewTopicBtn.grid(row=2, column=3, padx=80, pady=5, ipadx=10, sticky='nsew')



        # pass

    ############### function to display and forget frames ###############
    def showFrame(self, frame):
        #destroy all other frames first
        for child in self.main.winfo_children():
            if child != frame:
                child.grid_forget()

        #display selected frame depending on what's clicked in the menu
        if frame == self.topicsFrame:
            self.topicsFrame.grid(row=0, column=0, columnspan=7, rowspan=10)
        elif frame == self.welcomeFrame:
            self.welcomeFrame.grid(row=0, column=0, columnspan=7, rowspan=10)
        else:
            print('No frame is selected')


    #function to display selected topic
    def showTopic(self):
        #forget sa tanan active nga frames
        for child in self.main.winfo_children():
            child.grid_forget()

        # #use curselection method to retrieve indices of selected items

        self.topicVal = []
        topic_title = self.topics_listBox.curselection()
        for i in topic_title:
            select = self.topics_listBox.get(i)
            self.topicVal.append(select)

        for val in self.topicVal:
            # print(f'Topic {val}')
            #ay sge icheck nlang niya ang string oi

            if val == 'Getting started with Tkinter':
                self.topic0Frame.grid(row=0, column=0)      #GETTING STARTED WITH TKINTER
                print('Getting started with Tkinter')
            elif val == 'Geometry Managers':
                self.topic1Frame.grid(row=0, column=0)    #GEOMETRY MANAGERS
                print('Geometry Managers')
            elif val == 'Geometry Managers: Pack Layout':
                self.topic2Frame.grid(row=0, column=0)      #GEOMERTY MANAGER: PACK LAYOUT
                print('Geometry Managers: Pack Layout')
            elif val == 'Geometry Managers: Grid Layout':
                self.topic3Frame.grid(row=0, column=0)      #GEOMETRY MANAGER: GRID LAYOUT
                print('Geometry Managers: Grid Layout')
            elif val == 'Geometry Managers: Place Layout':
                self.topic4Frame.grid(row=0, column=0)      #GEOMETRY MANAGER: PLACE LAYOUT
                print('Geometry Managers: Place Layout')
            elif val == 'Widgets':
                self.topic5Frame.grid(row=0, column=0)      #WIDGETS
                print('Widgets')
            elif val == 'Label widget':
                self.topic6Frame.grid(row=0, column=0)      #LABEL WIDGET
                print('Label widget')
            elif val == 'Button widget':
                self.topic7Frame.grid(row=0, column=0)      #BUTTON WIDGET
                print('Button widget')
            elif val == 'Entry widget':
                self.topic8Frame.grid(row=0, column=0)      #ENTRY WIDGET
                print('Entry widget')
            elif val == 'Frame widget':
                self.topic9Frame.grid(row=0, column=0)      #FRAME WIDGET
                print('Frame widget')
            elif val == 'Canvas widget':
                self.topic10Frame.grid(row=0, column=0)     #CANVAS WIDGET
                print('Canvas widget')
            elif val == 'Menu widget':
                self.topic11Frame.grid(row=0, column=0)     #MENU WIDGET
                print('Menu widget')
            elif val == 'Listbox widget':
                self.topic12Frame.grid(row=0, column=0)     #LISTBOX WIDGET
                print('Listbox widget')
            elif val == 'Scrollbar widget':
                self.topic13Frame.grid(row=0, column=0)     #SCROLLBAR WIDGET
                print('Scrollbar widget')
            elif val == 'Notebook widget':
                self.topic14Frame.grid(row=0, column=0)     #NOTEBOOK WIDGET
                print('Notebook widget')
            elif val == 'File I/O':
                self.topic15Frame.grid(row=0, column=0)     #FILE I/O
                print('File I/O')
            elif val == 'A simple employee data managemet system':
                self.topic16Frame.grid(row=0, column=0)             #'A simple employee data managemet system'
                print('A simple employee data managemet system')
            elif val == 'A simple calculator application':
                self.topic17Frame.grid(row=0, column=0)
                print('A simple calculator application')
            else:
                print('Null')


    #function para pag hover sa button kay machange ang color eyy
    #on event
    def btn_on_enter(self, event):
        self.btn = event.widget

        if self.btn == self.viewTopicBtn:
            self.viewTopicBtn.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn0:
            self.goBackBtn0.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn1:
            self.goBackBtn1.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn2:
            self.goBackBtn2.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn3:
            self.goBackBtn3.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn4:
            self.goBackBtn4.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn5:
            self.goBackBtn5.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn6:
            self.goBackBtn6.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn7:
            self.goBackBtn7.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn7:
            self.goBackBtn7.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn8:
            self.goBackBtn8.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn9:
            self.goBackBtn9.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn10:
            self.goBackBtn10.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn11:
            self.goBackBtn11.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn12:
            self.goBackBtn12.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn13:
            self.goBackBtn13.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn14:
            self.goBackBtn14.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn15:
            self.goBackBtn15.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn16:
            self.goBackBtn16.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn17:
            self.goBackBtn17.config(bg='#2688ED', fg='white')
        else:
            print('null')


    def btn_on_leave(self, event):
        self.btn == event.widget

        if self.btn == self.viewTopicBtn:
            self.viewTopicBtn.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn0:
            self.goBackBtn0.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn1:
            self.goBackBtn1.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn2:
            self.goBackBtn2.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn3:
            self.goBackBtn4.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn4:
            self.goBackBtn4.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn5:
            self.goBackBtn5.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn6:
            self.goBackBtn6.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn7:
            self.goBackBtn7.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn8:
            self.goBackBtn8.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn9:
            self.goBackBtn9.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn10:
            self.goBackBtn10.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn11:
            self.goBackBtn11.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn12:
            self.goBackBtn12.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn13:
            self.goBackBtn13.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn14:
            self.goBackBtn14.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn15:
            self.goBackBtn15.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn16:
            self.goBackBtn16.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn17:
            self.goBackBtn17.config(bg='SystemButtonFace', fg='black')
        else:
            print('null')



    ############### function to display topics ###############
    def allTopics(self):

        ############### GETTING STARTED WITH TKINTER ###############
        #self.topic0Frame = 'GETTING STARTED WITH TKINTER'
        self.topic0Frame = Frame(self.main)
        # self.topic0Frame.grid(row=0, column=0, columnspan=7, rowspan=10)

        

        self.goBackBtn0 = Button(self.topic0Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn0.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn0.bind('<Leave>', self.btn_on_leave)
        self.goBackBtn0.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic0FrameTitle = Label(self.topic0Frame,
                                        text='Getting started with Tkinter',
                                        font=('Helvetica', '12'))
        self.topic0FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)


        #create notebook widget
        self.topic0noteBook = ttk.Notebook(self.topic0Frame)

        self.topic0tab1 = Frame(self.topic0noteBook)
        self.topic0tab2 = Frame(self.topic0noteBook)

        self.topic0noteBook.add(self.topic0tab1, text='Topic')
        self.topic0noteBook.add(self.topic0tab2, text='Sample Code Snippet')

        self.topic0noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        Label(self.topic0tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        Label(self.topic0tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)


        # self.topic0TextWidget = Text(self.topic0Frame,
        #                                 font=('Helvetica', '10'),
        #                                 state='normal')
        # self.topic0TextWidget.grid(row=0, column=0, columnspan=7)

        # self.topic0text0 = 'This is topic 1. Lorem ipsum dolor sit amet adipscing consectitur.\n'

        # self.topic0TextWidget.insert(END, self.topic0text0+self.topic0text0+self.topic0text0+self.topic0text0+self.topic0text0+self.topic0text0+self.topic0text0+self.topic0text0)

        # self.topic0TextWidget.config(state='disabled', height=20, width=60, wrap='word')

        


        ############### GEOMETRY MANAGERS ###############
        #self.topic1Frame = 'GEOMETRY MANAGERS'
        self.topic1Frame = Frame(self.main)
        # self.topic1Frame.grid(row=0, column=0, columnspan=7, rowspan=10)


        self.goBackBtn1 = Button(self.topic1Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn1.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn1.bind('<Leave>', self.btn_on_leave)
        self.goBackBtn1.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic1FrameTitle = Label(self.topic1Frame,
                                        text='Geometry Managers',
                                        font=('Helvetica', '12'))
        self.topic1FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic1noteBook = ttk.Notebook(self.topic1Frame)

        self.topic1tab1 = Frame(self.topic1noteBook)
        self.topic1tab2 = Frame(self.topic1noteBook)

        self.topic1noteBook.add(self.topic1tab1, text='Topic')
        self.topic1noteBook.add(self.topic1tab2, text='Sample Code Snippet')

        self.topic1noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        # Label(self.topic1tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        # Label(self.topic1tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)

        self.topic1tab1Canvas = Canvas(self.topic1tab1)
        



        ############### GEOMETRY MANAGERS: PACK LAYOUT ###############
        # self.topic2Frame = 'GEOMETRY MANAGERS: PACK LAYOUT'
        self.topic2Frame = Frame(self.main)
        # self.topic2Frame.grid(row=0, column=0)


        self.goBackBtn2 = Button(self.topic2Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn2.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn2.bind('<Leave>', self.btn_on_leave)
        self.goBackBtn2.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic2FrameTitle = Label(self.topic2Frame,
                                        text='Geometry Managers: Pack Layout',
                                        font=('Helvetica', '12'))
        self.topic2FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic2noteBook = ttk.Notebook(self.topic2Frame)

        self.topic2tab1 = Frame(self.topic2noteBook)
        self.topic2tab2 = Frame(self.topic2noteBook)

        self.topic2noteBook.add(self.topic2tab1, text='Topic')
        self.topic2noteBook.add(self.topic2tab2, text='Sample Code Snippet')

        self.topic2noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        Label(self.topic2tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        Label(self.topic2tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)



        ############### GEOMETRY MANAGERS: GRID LAYOUT ###############
        #self.topic3Frame = 'GEOMETRY MANAGERS: GRID LAYOUT'
        self.topic3Frame = Frame(self.main)
        # self.topic3Frame.grid(row=0, column=0)


        self.goBackBtn3 = Button(self.topic3Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn3.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn3.bind('<Leave>', self.btn_on_leave)
        self.goBackBtn3.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic3FrameTitle = Label(self.topic3Frame,
                                        text='Geometry Managers: Grid Layout',
                                        font=('Helvetica', '12'))
        self.topic3FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic3noteBook = ttk.Notebook(self.topic3Frame)

        self.topic3tab1 = Frame(self.topic3noteBook)
        self.topic3tab2 = Frame(self.topic3noteBook)

        self.topic3noteBook.add(self.topic3tab1, text='Topic')
        self.topic3noteBook.add(self.topic3tab2, text='Sample Code Snippet')

        self.topic3noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        Label(self.topic3tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        Label(self.topic3tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)



        ############### GEOMETRY MANAGERS: PLACE LAYOUT ###############
        # self.topic4Frame = 'GEOMETRY MANAGERS: PLACE LAYOUT'
        self.topic4Frame = Frame(self.main)
        # self.topic4Frame.grid(row=0, column=0)


        self.goBackBtn4 = Button(self.topic4Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn4.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn4.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn4.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic4FrameTitle = Label(self.topic4Frame,
                                        text='Geometry Managers: Place Layout',
                                        font=('Helvetica', '12'))
        self.topic4FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic4noteBook = ttk.Notebook(self.topic4Frame)

        self.topic4tab1 = Frame(self.topic4noteBook)
        self.topic4tab2 = Frame(self.topic4noteBook)

        self.topic4noteBook.add(self.topic4tab1, text='Topic')
        self.topic4noteBook.add(self.topic4tab2, text='Sample Code Snippet')

        self.topic4noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        Label(self.topic4tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        Label(self.topic4tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)



        ############### WIDGETS ###############
        # self.topic5Frame = 'WIDGETS'
        self.topic5Frame = Frame(self.main)
        # self.topic5Frame.grid(row=0, column=0)


        self.goBackBtn5 = Button(self.topic5Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn5.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn5.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn5.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic5FrameTitle = Label(self.topic5Frame,
                                        text='Widgets',
                                        font=('Helvetica', '12'))
        self.topic5FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic5noteBook = ttk.Notebook(self.topic5Frame)

        self.topic5tab1 = Frame(self.topic5noteBook)
        self.topic5tab2 = Frame(self.topic5noteBook)

        self.topic5noteBook.add(self.topic5tab1, text='Topic')
        self.topic5noteBook.add(self.topic5tab2, text='Sample Code Snippet')

        self.topic5noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        Label(self.topic5tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        Label(self.topic5tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)



        ############### LABEL WIDGET ###############
        # self.topic6Frame = 'WIDGET'
        self.topic6Frame = Frame(self.main)
        # self.topic6Frame.grid(row=0, column=0)


        self.goBackBtn6 = Button(self.topic6Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn6.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn6.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn6.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic6FrameTitle = Label(self.topic6Frame,
                                        text='Label widget',
                                        font=('Helvetica', '12'))
        self.topic6FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic6noteBook = ttk.Notebook(self.topic6Frame)

        self.topic6tab1 = Frame(self.topic6noteBook)
        self.topic6tab2 = Frame(self.topic6noteBook)

        self.topic6noteBook.add(self.topic6tab1, text='Topic')
        self.topic6noteBook.add(self.topic6tab2, text='Sample Code Snippet')

        self.topic6noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        Label(self.topic6tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        Label(self.topic6tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)



        ############### BUTTON WIDGET ###############
        # self.topic7Frame = 'BUTTON WIDGET'
        self.topic7Frame = Frame(self.main)
        # self.topic7Frame.grid(row=0, column=0)


        self.goBackBtn7 = Button(self.topic7Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn7.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn7.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn7.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic7FrameTitle = Label(self.topic7Frame,
                                        text='Button widget',
                                        font=('Helvetica', '12'))
        self.topic7FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic7noteBook = ttk.Notebook(self.topic7Frame)

        self.topic7tab1 = Frame(self.topic7noteBook)
        self.topic7tab2 = Frame(self.topic7noteBook)

        self.topic7noteBook.add(self.topic7tab1, text='Topic')
        self.topic7noteBook.add(self.topic7tab2, text='Sample Code Snippet')

        self.topic7noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        Label(self.topic7tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        Label(self.topic7tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)


        ############### ENTRY WIDGET ###############
        # self.topic8Frame = 'ENTRY WIDGET'
        self.topic8Frame = Frame(self.main)
        # self.topic8Frame.grid(row=0, column=0)


        self.goBackBtn8 = Button(self.topic8Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn8.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn8.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn8.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic8FrameTitle = Label(self.topic8Frame,
                                        text='Entry widget',
                                        font=('Helvetica', '12'))
        self.topic8FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic8noteBook = ttk.Notebook(self.topic8Frame)

        self.topic8tab1 = Frame(self.topic8noteBook)
        self.topic8tab2 = Frame(self.topic8noteBook)

        self.topic8noteBook.add(self.topic8tab1, text='Topic')
        self.topic8noteBook.add(self.topic8tab2, text='Sample Code Snippet')

        self.topic8noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        Label(self.topic8tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        Label(self.topic8tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)



        ############### FRAME WIDGET ###############
        # self.topic9Frame = 'FRAME WIDGET'
        self.topic9Frame = Frame(self.main)
        # self.topic9Frame.grid(row=0, column=0)


        self.goBackBtn9 = Button(self.topic9Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn9.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn9.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn9.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic9FrameTitle = Label(self.topic9Frame,
                                        text='Frame widget',
                                        font=('Helvetica', '12'))
        self.topic9FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic9noteBook = ttk.Notebook(self.topic9Frame)

        self.topic9tab1 = Frame(self.topic9noteBook)
        self.topic9tab2 = Frame(self.topic9noteBook)

        self.topic9noteBook.add(self.topic9tab1, text='Topic')
        self.topic9noteBook.add(self.topic9tab2, text='Sample Code Snippet')

        self.topic9noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        Label(self.topic9tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        Label(self.topic9tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)



        ############### CANVAS WIDGET ###############
        # self.topic10Frame = 'CANVAS WIDGET'
        self.topic10Frame = Frame(self.main)
        # self.topic10Frame.grid(row=0, column=0)


        self.goBackBtn10 = Button(self.topic10Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn10.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn10.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn10.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic10FrameTitle = Label(self.topic10Frame,
                                        text='Canvas widget',
                                        font=('Helvetica', '12'))
        self.topic10FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic10noteBook = ttk.Notebook(self.topic10Frame)

        self.topic10tab1 = Frame(self.topic10noteBook)
        self.topic10tab2 = Frame(self.topic10noteBook)

        self.topic10noteBook.add(self.topic10tab1, text='Topic')
        self.topic10noteBook.add(self.topic10tab2, text='Sample Code Snippet')

        self.topic10noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        Label(self.topic10tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        Label(self.topic10tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)


        ############### MENU WIDGET ###############
        # self.topic11Frame = 'MENU WIDGET'
        self.topic11Frame = Frame(self.main)
        # self.topic11Frame.grid(row=0, column=0)


        self.goBackBtn11 = Button(self.topic11Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn11.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn11.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn11.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic11FrameTitle = Label(self.topic11Frame,
                                        text='Menu widget',
                                        font=('Helvetica', '12'))
        self.topic11FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic11noteBook = ttk.Notebook(self.topic11Frame)

        self.topic11tab1 = Frame(self.topic11noteBook)
        self.topic11tab2 = Frame(self.topic11noteBook)

        self.topic11noteBook.add(self.topic11tab1, text='Topic')
        self.topic11noteBook.add(self.topic11tab2, text='Sample Code Snippet')

        self.topic11noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        Label(self.topic11tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        Label(self.topic11tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)



        ############### LISTBOX WIDGET ###############
        # self.topic12Frame = 'LISTBOX WIDGET'
        self.topic12Frame = Frame(self.main)
        # self.topic12Frame.grid(row=0, column=0)


        self.goBackBtn12 = Button(self.topic12Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn12.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn12.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn12.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic12FrameTitle = Label(self.topic12Frame,
                                        text='Listbox widget',
                                        font=('Helvetica', '12'))
        self.topic12FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic12noteBook = ttk.Notebook(self.topic12Frame)

        self.topic12tab1 = Frame(self.topic12noteBook)
        self.topic12tab2 = Frame(self.topic12noteBook)

        self.topic12noteBook.add(self.topic12tab1, text='Topic')
        self.topic12noteBook.add(self.topic12tab2, text='Sample Code Snippet')

        self.topic12noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        Label(self.topic12tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        Label(self.topic12tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)



        ############### SCROLLBAR WIDGET ###############
        # self.topic13Frame = 'SCROLLBAR WIDGET'
        self.topic13Frame = Frame(self.main)
        # self.topic13Frame.grid(row=0, column=0)


        self.goBackBtn13 = Button(self.topic13Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn13.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn13.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn13.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic13FrameTitle = Label(self.topic13Frame,
                                        text='Scrollbar widget',
                                        font=('Helvetica', '12'))
        self.topic13FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic13noteBook = ttk.Notebook(self.topic13Frame)

        self.topic13tab1 = Frame(self.topic13noteBook)
        self.topic13tab2 = Frame(self.topic13noteBook)

        self.topic13noteBook.add(self.topic13tab1, text='Topic')
        self.topic13noteBook.add(self.topic13tab2, text='Sample Code Snippet')

        self.topic13noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        Label(self.topic13tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        Label(self.topic13tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)


        ############### NOTEBOOK WIDGET ###############
        # self.topic14Frame = 'NOTEBOOK WIDGET'
        self.topic14Frame = Frame(self.main)
        # self.topic14Frame.grid(row=0, column=0)


        self.goBackBtn14 = Button(self.topic14Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn14.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn14.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn14.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic14FrameTitle = Label(self.topic14Frame,
                                        text='Notebook widget',
                                        font=('Helvetica', '12'))
        self.topic14FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic14noteBook = ttk.Notebook(self.topic14Frame)

        self.topic14tab1 = Frame(self.topic14noteBook)
        self.topic14tab2 = Frame(self.topic14noteBook)

        self.topic14noteBook.add(self.topic14tab1, text='Topic')
        self.topic14noteBook.add(self.topic14tab2, text='Sample Code Snippet')

        self.topic14noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        Label(self.topic14tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        Label(self.topic14tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)



        ############### FILE I/O ###############
        # self.topic15Frame = 'FILE I/O'
        self.topic15Frame = Frame(self.main)
        # self.topic15Frame.grid(row=0, column=0)


        self.goBackBtn15 = Button(self.topic15Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn15.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn15.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn15.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic15FrameTitle = Label(self.topic15Frame,
                                        text='FILE I/O',
                                        font=('Helvetica', '12'))
        self.topic15FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic15noteBook = ttk.Notebook(self.topic15Frame)

        self.topic15tab1 = Frame(self.topic15noteBook)
        self.topic15tab2 = Frame(self.topic15noteBook)

        self.topic15noteBook.add(self.topic15tab1, text='Topic')
        self.topic15noteBook.add(self.topic15tab2, text='Sample Code Snippet')

        self.topic15noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        Label(self.topic15tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        Label(self.topic15tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)



        ############### A SIMPLE EMPLOYEE DATA MANAGEMENT SYSTEM ###############
        # self.topic16Frame = 'A SIMPLE EMPLOYEE DATA MANAGEMENT SYSTEM'
        self.topic16Frame = Frame(self.main)
        # self.topic16Frame.grid(row=0, column=0)


        self.goBackBtn16 = Button(self.topic16Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn16.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn16.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn16.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic16FrameTitle = Label(self.topic16Frame,
                                        text='A simple employee data managemet system',
                                        font=('Helvetica', '12'))
        self.topic16FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic16noteBook = ttk.Notebook(self.topic16Frame)

        self.topic16tab1 = Frame(self.topic16noteBook)
        self.topic16tab2 = Frame(self.topic16noteBook)

        self.topic16noteBook.add(self.topic16tab1, text='Topic')
        self.topic16noteBook.add(self.topic16tab2, text='Sample Code Snippet')

        self.topic16noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        Label(self.topic16tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        Label(self.topic16tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)

        
        ############### A SIMPLE CALCULATOR APPLICATION ###############
        # self.topic17Frame = 'A SIMPLE CALCULATOR APPLICATION'
        self.topic17Frame = Frame(self.main)
        # self.topic17Frame.grid(row=0, column=0)


        self.goBackBtn17 = Button(self.topic17Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn17.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn17.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn17.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic17FrameTitle = Label(self.topic17Frame,
                                        text='A simple calculator application',
                                        font=('Helvetica', '12'))
        self.topic17FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic17noteBook = ttk.Notebook(self.topic17Frame)

        self.topic17tab1 = Frame(self.topic17noteBook)
        self.topic17tab2 = Frame(self.topic17noteBook)

        self.topic17noteBook.add(self.topic17tab1, text='Topic')
        self.topic17noteBook.add(self.topic17tab2, text='Sample Code Snippet')

        self.topic17noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        Label(self.topic17tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        Label(self.topic17tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)






def main():
    main = Tk()
    tukinter = Application(main)
    main.mainloop()


if __name__ == '__main__':
    main()