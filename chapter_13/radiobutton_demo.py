# this program demonstrates a group of RadioButton widgets.

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # create the main window.
        self.main_window=tkinter.Tk()
        
        # create two frames. one for the Radiobuttons
        # and another for the regular Button widgets.
        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        
        # create an IntVar object to use with
        # the Radiobuttons.
        self.radio_var=tkinter.IntVar()
        
        # set the IntVar object to 1.
        self.radio_var.set(1)
        
        # create the Radiobutton widgets in the top frame.
        self.rb1=tkinter.Radiobutton(self.top_frame, \
                                     text="Option 1", variable=self.radio_var,\
                                     value=1)
        self.rb2=tkinter.Radiobutton(self.top_frame, \
                                     text="Option 2", variable=self.radio_var,\
                                     value=2)
        self.rb3=tkinter.Radiobutton(self.top_frame, \
                                     text="Option 3", variable=self.radio_var,\
                                     value=3)
        
        # pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        
        # create an OK button and a Quit button.
        self.ok_button=tkinter.Button(self.bottom_frame,\
                                      text="OK", command=self.show_choice)
        self.quit_button=tkinter.Button(self.bottom_frame,\
                                        text="Quit", command=self.main_window.destroy)
        
        # pack the buttons.
        self.ok_button.pack(side="left")
        self.quit_button.pack(side="left")
        
        # pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        # start the mainloop.
        tkinter.mainloop()
        
    # the show_choice method is the callback function for the
    # OK button.
    def show_choice(self):
        tkinter.messagebox.showinfo("Selection", "You selected option " + \
                                    str(self.radio_var.get()))
        
# create an instance of the MyGUI class.
my_gui=MyGUI()