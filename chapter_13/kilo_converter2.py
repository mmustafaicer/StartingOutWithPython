# this program converts distances in kilometers
# to miles. the result is displayed in a label
# on the main window.

import tkinter

class KiloConverterGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        
        # create three frames to group widgets.
        self.top_frame=tkinter.Frame()
        self.mid_frame=tkinter.Frame()
        self.bottom_frame=tkinter.Frame()
        
        # TOP FRAME widgets
        self.prompt_label=tkinter.Label(self.top_frame,
                                        text="Enter a distance in kilometers:")
        self.kilo_entry=tkinter.Entry(self.top_frame,\
                                      width=10)
        
        # pack the TOP FRAME widgets.
        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")
        
        # MIDDLE FRAME widgets
        self.descr_label=tkinter.Label(self.mid_frame,\
                                       text="Converted to miles: ")
        
        # we need a StringVar object to associate with
        # an output label. use the object's set method to
        # store a string of blank characters.
        self.value=tkinter.StringVar() 
        
        # create a label and associate it with the
        # StringVar object. Any value stored in the
        # StringVar object will automatically be displayed
        # in the label.
        self.miles_label=tkinter.Label(self.mid_frame,\
                                       textvariable=self.value)
        
        # pack the MIDDLE FRAME widgets
        self.descr_label.pack(side="left")
        self.miles_label.pack(side="left")
        
        # BOTTOM FRAMES
        self.calc_button=tkinter.Button(self.bottom_frame,\
                                        text="Convert",
                                        command=self.convert)
        self.quit_button=tkinter.Button(self.bottom_frame,\
                                        text="Quit", \
                                        command=self.main_window.destroy)
        
        # pack the buttons.
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")
        
        # pack the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        # enter the tkinter main loop.
        tkinter.mainloop()
        
    # the convert method is a callback function for the
    # Calculate button.
    
    def convert(self):
        # get the value entered by the user into
        # the kilo_entry widget.
        kilo=float(self.kilo_entry.get())       # remember .get method
        
        # convert kilometers to miles.
        miles=kilo*0.6214
        
        # convert miles to a string and store it in
        # the StringVar object. this will automatically 
        # update the miles_label widget.
        self.value.set(miles)
        
# create an instance of the KiloConverterGUI class.
kilo_conv=KiloConverterGUI()                            