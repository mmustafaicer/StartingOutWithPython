# this program uses the side="left" argument with
# the pack method to change the layout of the widgets.

import tkinter

class MyGUI:
    def __init__(self):
        # create the main windows widget.
        self.main_window=tkinter.Tk()
        
        # create two Label widgets
        self.label1=tkinter.Label(self.main_window,\
                                 text="Hello World!")
        self.label2=tkinter.Label(self.main_window,\
                                 text="This is my GUI program.")
        # call the Label widget's pack method.
        self.label1.pack(side="left")
        self.label2.pack(side="left")
        
        # enter the tkinter main loop.
        tkinter.mainloop()
        
# create an instance of the MyGUI class.
my_gui=MyGUI()