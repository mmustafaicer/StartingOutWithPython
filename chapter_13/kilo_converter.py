# this program converts distances in kilometres
# to miles. the result is displayed in an info
# dialog box.

import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
        # create the main window.
        self.main_window=tkinter.Tk()
        
        # create two frames to group widgets.
        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        
        # create widgets for the top frame.
        self.prompt_label=tkinter.Label(self.top_frame,\
                                        text="Enter a distance in kilometers: ")
        self.kilo_entry=tkinter.Entry(self.top_frame, \
                                      width=10)

        # pack the top frame's widgets.
        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")
        
        # create the button widgets for the bottom frame.
        self.calc_button=tkinter.Button(self.bottom_frame,\
                                        text="Convert",
                                        command=self.convert)
        self.quit_button=tkinter.Button(self.bottom_frame,\
                                        text="Quit",
                                        command=self.main_window.destroy)
        
        # pack the bottom frame's widgets.
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")
        
        # pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        # enter the tkinter main loop.
        tkinter.mainloop()
        
    # the convert method is a callback function for
    # the Calculate button.
    
    def convert(self):
        # get the value entered by the user into the
        # kilo_entry widget.
        kilo=float(self.kilo_entry.get())
        
        # convert kilometers to miles
        miles=kilo*0.6214
        
        # display the results in an info dialog box.
        tkinter.messagebox.showinfo("Results",\
                                    str(kilo) + " kilometers is equal to " +\
                                    str(miles) + " miles.")
        
# create an instance of the KiloConverterGUI class.
kilo_conv=KiloConverterGUI()
        
        