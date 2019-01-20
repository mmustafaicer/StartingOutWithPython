# this program has a Quit button that calls
# the Tk class's destroy method when clicked.

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
        
        # create a Quit button. When this button is clicked
        # the root widget's destroy method is called.
        # (The main_window variable references the root widget,
        # so the callback function is self.main_window.destroy.)
        self.quit_button=tkinter.Button(self.main_window, \
                                        text="Quit",
                                        command=self.main_window.destroy)
        
        # pack the buttons.
        self.my_button.pack()
        self.quit_button.pack()
        
        # enter the tkinter main loop.
        tkinter.mainloop()
        
    # the do_something method is a callback function
    # for the Button widget.
    
    def do_something(self):
        # display an info dialog box.
        tkinter.messagebox.showerror("Response", \
                                     "Thanks for clicking the button.")
        
# create an instance of the MyGUI class.
my_gui=MyGUI()