# long distance calls
# Final question yaaaayyyy!

import tkinter
import tkinter.messagebox

class CallGUI:
    def __init__(self):
        # create the main window and set title
        self.main_window=tkinter.Tk()
        self.main_window.title("Long-Distance Calls")
        self.main_window.geometry("500x500")
        
        # create frames
        self.top_frame=tkinter.Frame(self.main_window)
        self.mid_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        
        # create an #DoubleVar object object to use with
        # the Radiobuttons.
        self.call_rate=tkinter.DoubleVar()
        
        # set the IntVar object to 1.
        self.call_rate.set(1)
        
        # create the Radiobutton widgets in the top frame.
        self.rb1=tkinter.Radiobutton(self.top_frame, \
                                     text="Daytime (6:00 A.M. through 5:59 P.M.): $0.07 per minute", variable=self.call_rate,\
                                     value=0.07)
        self.rb2=tkinter.Radiobutton(self.top_frame, \
                                     text="Evening (6:00 P.M. through 11:59 P.M): $0.12 per minute", variable=self.call_rate,\
                                     value=0.12)
        self.rb3=tkinter.Radiobutton(self.top_frame, \
                                     text="Off-peak (midnight through 5:50 A.M.): $0.05 per minute", variable=self.call_rate,\
                                     value=0.05)
        
        # pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        
        # MID FRAME 1 for minute-entry
        # create widgets for the top frame
        self.prompt_label=tkinter.Label(self.mid_frame, \
                                   text="How many minutes: ")
        self.entry=tkinter.Entry(self.mid_frame, \
                             width=10)
        # pack them
        self.prompt_label.pack(side="left")
        self.entry.pack(side="left")
        

        # BOTTOM FRAME for buttons.
        self.calc_button=tkinter.Button(self.bottom_frame,\
                                        text="Calculate the Cost", \
                                        command=self.CalculateCost)
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
        
    def CalculateCost(self):
        self.calculated_total=float(self.entry.get())*float(self.call_rate.get())
        
        tkinter.messagebox.showinfo("Total Cost", "$" + str(self.calculated_total))

# create an instance of CallGUI
example=CallGUI()
