# this program demonstrates a Button Widget
# when the user clicks the Button, an
# info dialog box is displayed.

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # create the main window gadget.
        self.main_window=tkinter.Tk()
        
        # create a Button widget. The text "Click me!"
        # should appear on the face of the Button. The
        # do_something method should be executed when
        # the user clicks the Button.
        self.my_button=tkinter.Button(self.main_window, \
                                      text="Click me!", \
                                      command=self.do_something)
        
        # pack the button.
        self.my_button.pack()
        
        # enter the tkinter main loop.
        tkinter.mainloop()
        
    # the do_something method is a callback function
    # for the Button widget.
    
    def do_something(self):
        # display an info dialog box.
        tkinter.messagebox.showinfo("Response",\
                                    "Thanks for clicking the button.")
        
# create an instance of the MyGUI class.
my_gui=MyGUI()