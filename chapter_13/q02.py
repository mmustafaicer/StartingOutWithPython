# Latin translator

import tkinter

class LatinTranslatorGUI:
    def __init__(self):
        # create the main window
        self.main_window=tkinter.Tk()
        # set the title
        self.main_window.title("Latin to English Translator")
        
        # create three frames.
        self.top_frame=tkinter.Frame(self.main_window)
        self.mid_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        
        # we need a StringVar object to associate with
        # an output label
        self.translation1=tkinter.StringVar()
        self.translation2=tkinter.StringVar()
        self.translation3=tkinter.StringVar()
        
        # create labels for each button
        self.translation_label1=tkinter.Label(self.top_frame, bg="green", fg="white", \
                                       textvariable=self.translation1)
        self.translation_label2=tkinter.Label(self.mid_frame, bg="green", fg="white", \
                                       textvariable=self.translation2)
        self.translation_label3=tkinter.Label(self.bottom_frame, bg="green", fg="white", \
                                       textvariable=self.translation3)
        
        # create button widgets on the top frame
        self.b1=tkinter.Button(self.top_frame,\
                               text="sinister",\
                               command=self.answer1)
        self.b2=tkinter.Button(self.mid_frame,\
                               text="dexter",\
                               command=self.answer2)
        self.b3=tkinter.Button(self.bottom_frame,\
                               text="medium",\
                               command=self.answer3)
        
        # pack the buttons and displays
        self.b1.pack(side="left")
        self.b2.pack(side="left")
        self.b3.pack(side="left")
        self.translation_label1.pack(side="right")
        self.translation_label2.pack(side="right")
        self.translation_label3.pack(side="right")
        
        # pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        # enter the mainloop.
        self.main_window.mainloop()
    
    
    # setter functions for each translation
    def answer1(self):
        self.translation1.set("left")
    def answer2(self):
        self.translation2.set("right")
    def answer3(self):
        self.translation3.set("center")
# create an instance of LatinTranslatorGUI
example = LatinTranslatorGUI()
