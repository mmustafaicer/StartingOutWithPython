# property tax

import tkinter

class PropertyTaxGUI():       # :D
    def __init__(self):
        # create the main window
        self.main_window=tkinter.Tk()
        # set the title
        self.main_window.title("Property Tax Calculator")
        self.main_window.geometry("500x500")
    
        # create four frames for this GUI
        self.top_frame=tkinter.Frame(self.main_window)
        self.mid_frame1=tkinter.Frame(self.main_window)
        self.mid_frame2=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
    
        # create widgets for the top frame
        self.prompt_label=tkinter.Label(self.top_frame, \
                                   text="Enter the actual value of the property: ")
        self.entry_act_value=tkinter.Entry(self.top_frame, \
                             width=10)
        # pack them
        self.prompt_label.pack(side="left")
        self.entry_act_value.pack(side="left")
    
        # MID FRAME 1
        # create displays for assessment value
        self.display_message1=tkinter.Label(self.mid_frame1, \
                                           text="Assessment value is: $")
    
        # create a StringVar to hold the converted value
        self.assessment_value=tkinter.StringVar()
        
        # create a label to show this converted value.
        self.show_assess_value=tkinter.Label(self.mid_frame1,\
                                      textvariable=self.assessment_value)
        
        # pack them
        self.display_message1.pack(side="left")
        self.show_assess_value.pack(side="left")
        
        # MID FRAME 2
        # create displays for property tax value
        self.display_message2=tkinter.Label(self.mid_frame2, \
                                           text="Property tax is: $")
    
        # create a StringVar to hold the converted value
        self.tax_value=tkinter.StringVar()
        
        # create a label to show this converted value.
        self.show_tax_value=tkinter.Label(self.mid_frame2,\
                                      textvariable=self.tax_value)
        
        # pack them
        self.display_message2.pack(side="left")
        self.show_tax_value.pack(side="left")
        
        # BOTTOM FRAME
        # button for calculation
        self.calc_button=tkinter.Button(self.bottom_frame,\
                                        text="Calculate the values", \
                                        command=self.convert)
        self.quit_button=tkinter.Button(self.bottom_frame, \
                                        text="Quit", bg="red", \
                                        command=self.main_window.destroy)
        
        # pack them
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")
        
        # pack the frames.
        self.top_frame.pack()
        self.mid_frame1.pack()
        self.mid_frame2.pack()
        self.bottom_frame.pack()
            
        # enter into mainloop
        self.main_window.mainloop()
        
    def convert(self):
        # convert the given value
        # remember .get method returns "String" convert it into int or float
        # for mathematical expressions.
        self.assessed_value=float(self.entry_act_value.get())*0.60
        self.calculated_tax=self.assessed_value*(0.75/100)
        
        # return calculated values back into StringVar object using .set() method
        self.assessment_value.set(format(self.assessed_value, ",.2f"))
        self.tax_value.set(format(self.calculated_tax, ",.2f"))
        
# create an instance of Fahrenheiter
example = PropertyTaxGUI()