# celcius to fahrenheit
import tkinter

class FahrenheiterGUI():       # :D
    def __init__(self):
        # create the main window
        self.main_window=tkinter.Tk()
        # set the title
        self.main_window.title("Celcius to Fahrenheit")
    
        # create three frames for this GUI
        self.top_frame=tkinter.Frame(self.main_window)
        self.mid_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
    
        # create widgets for the top frame
        self.prompt_label=tkinter.Label(self.top_frame, \
                                   text="Enter the Celcius temperature: ")
        self.entry_celcius=tkinter.Entry(self.top_frame, \
                             width=10)
        # pack them
        self.prompt_label.pack(side="left")
        self.entry_celcius.pack(side="left")
    
        # MID FRAME
        self.display_message=tkinter.Label(self.mid_frame, \
                                           text="In Fahrenheit it equals to:")
    
        # create a StringVar to hold the converted value
        self.fahrenheit=tkinter.StringVar()
        
        # create a label to show this converted value.
        self.show_fahrenheit=tkinter.Label(self.mid_frame,\
                                      textvariable=self.fahrenheit)
        
        # pack them
        self.display_message.pack(side="left")
        self.show_fahrenheit.pack(side="left")
        
        # BOTTOM FRAME
        # button for calculate MPG
        self.calc_button=tkinter.Button(self.bottom_frame,\
                                        text="Convert to Fahrenheit", \
                                        command=self.convert)
        self.quit_button=tkinter.Button(self.bottom_frame, \
                                        text="Quit", bg="red", \
                                        command=self.main_window.destroy)
        
        # pack them
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")
        
        # pack the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
            
        # enter into mainloop
        self.main_window.mainloop()
        
    def convert(self):
        # convert the given value
        # remember .get method returns "String" convert it into int or float
        # for mathematical expressions.
        self.calculated_fahrenheit=((9/5)*float(self.entry_celcius.get())+32)
        
        # return fahrenheit back into StringVar object using .set() method
        self.fahrenheit.set(format(self.calculated_fahrenheit, ",.2f"))
        
# create an instance of Fahrenheiter
example = FahrenheiterGUI()