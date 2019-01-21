# miles per gallon calculator

import tkinter

class MilesGUI:
    def __init__(self):
        # create the main window
        self.main_window=tkinter.Tk()
        # set the title
        self.main_window.title("Miles Per Gallon Calculator")
        
        # create four frames for this GUI
        self.top_frame1=tkinter.Frame(self.main_window)
        self.top_frame2=tkinter.Frame(self.main_window)
        self.mid_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        
        # create widgets for the first question
        self.user_prompt1=tkinter.Label(self.top_frame1, \
                                       text="Enter the number of gallons of gas of your car's tank: ")
        self.entry_capacity=tkinter.Entry(self.top_frame1, \
                                 width=10)
        # pack them
        self.user_prompt1.pack(side="left")
        self.entry_capacity.pack(side="left")
        
        # create widgets for the second question
        self.user_prompt2=tkinter.Label(self.top_frame2, \
                                       text="Enter miles can be driven on full tank: ")
        # entry for input
        self.entry_miles_driven=tkinter.Entry(self.top_frame2, \
                                 width=10)
        
        # pack them
        self.user_prompt2.pack(side="left")
        self.entry_miles_driven.pack(side="left")
        
        # MID FRAME
        self.display_message=tkinter.Label(self.mid_frame, \
                                           text="Per gallon, you can drive in miles:")
        
        # create a StringVar to hold the converted value
        self.miles=tkinter.StringVar()
        
        # create a label to show this converted value.
        self.show_miles=tkinter.Label(self.mid_frame,\
                                      textvariable=self.miles)
        
        # pack them
        self.display_message.pack(side="left")
        self.show_miles.pack(side="left")
        
        # BOTTOM FRAME
        # button for calculate MPG
        self.calc_button=tkinter.Button(self.bottom_frame,\
                                        text="Calculate MPG", \
                                        command=self.convert_mpg)
        self.quit_button=tkinter.Button(self.bottom_frame, \
                                        text="Quit", bg="red", \
                                        command=self.main_window.destroy)
        
        # pack them
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")
        
        # pack the frames.
        self.top_frame1.pack()
        self.top_frame2.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        # enter into mainloop
        self.main_window.mainloop()
        
    def convert_mpg(self):
        # convert the given value
        # remember .get method returns "String" convert it into int or float
        # for mathematical expressions.
        mpg=(int(self.entry_miles_driven.get())/int(self.entry_capacity.get()))
        
        # set the calculate mpg back into StringVar object.
        self.miles.set(format(mpg, ",.2f"))

# create an instance of MilesGUI
converter=MilesGUI()