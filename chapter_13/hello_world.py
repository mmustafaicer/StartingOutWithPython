# this program displays a label with text.
import tkinter


class MyGUI:
    def __init__(self):
        # create the main windows widget.
        self.main_window=tkinter.Tk()
        
        # create a Label widget containing the
        # text "Hello World!"
        self.label=tkinter.Label(self.main_window,\
                                 text="Hello World!")
        
        # call the Label widget's pack method.
        self.label.pack()
        
        # enter the tkinter main loop.
        tkinter.mainloop()
        
# create an instance of the MyGUI class.
my_gui=MyGUI()