# this exercise is not a part of the book.
# just challenge for ourselves. Try not to look at
# examples. comment every step

# lets create a program with GUI

#===============================================================================
# program should look like this 
# 
#     Enter integer    [entry block]
#     
#     Enter integer    [entry block]
#     
#     Enter integer    [entry block]
#     
#     Their total = (Shows total)
# 
# GET_TOTAL button            "Quit" Button
#===============================================================================

import tkinter

class TotalGUI:
    def __init__(self):
        # open GUI window
        self.main_window=tkinter.Tk()
        
        # create five frames.
        self.num1_frame=tkinter.Frame(self.main_window)
        self.num2_frame=tkinter.Frame(self.main_window)
        self.num3_frame=tkinter.Frame(self.main_window)
        self.total_frame=tkinter.Frame(self.main_window)
        self.button_frame=tkinter.Frame(self.main_window)
        
        # create and pack the widgets for num1
        self.num1_label=tkinter.Label(self.num1_frame,\
                                   text="Enter an integer:")
        # entry block
        self.num1_entry=tkinter.Entry(self.num1_frame,\
                                   width=10)
        
        # pack them
        self.num1_label.pack(side="left")
        self.num1_entry.pack(side="left")
        
        # create and pack the widgets for num2
        self.num2_label=tkinter.Label(self.num2_frame,\
                                   text="Enter an integer:")
        # entry block
        self.num2_entry=tkinter.Entry(self.num2_frame,\
                                   width=10)
        
        # pack them
        self.num2_label.pack(side="left")
        self.num2_entry.pack(side="left")
        
        # create and pack the widgets for num3
        self.num3_label=tkinter.Label(self.num3_frame,\
                                   text="Enter an integer:")
        # entry block
        self.num3_entry=tkinter.Entry(self.num3_frame,\
                                   width=10)
        
        # pack them
        self.num3_label.pack(side="left")
        self.num3_entry.pack(side="left")
        
        # create and pack the widgets for total.
        self.result_label=tkinter.Label(self.total_frame,\
                                        text="Total:")
        self.total=tkinter.StringVar()  # to update total_label
        self.total_label=tkinter.Label(self.total_frame,\
                                       textvariable=self.total)
        
        self.result_label.pack(side="left")
        self.total_label.pack(side="left")
        
        # create and pack the button widgets.
        self.total_button=tkinter.Button(self.button_frame, \
                                         text="Total", \
                                         command=self.get_total)
        self.quit_button=tkinter.Button(self.button_frame, \
                                        text="Quit", \
                                        command=self.main_window.destroy)
        
        self.total_button.pack(side="left")
        self.quit_button.pack(side="left")
        
        # pack the frames.
        self.num1_frame.pack()
        self.num2_frame.pack()
        self.num3_frame.pack()
        self.total_frame.pack()
        self.button_frame.pack()
        
        # get into mainloop function
        tkinter.mainloop()
    
    # the get_total method is callback function for
    # total_button widget.
        
    def get_total(self):
        # get the values from entry blocks
        self.num1=float(self.num1_entry.get())
        self.num2=float(self.num2_entry.get())
        self.num3=float(self.num3_entry.get())
        
        # calculate the sum
        self.sum=self.num1+self.num2+self.num3   # do not use self.total
                                                        # we already used self.total above
                                                        # that gave error.
        # assign total to total displayer label
        self.total.set(self.sum)
                
# create an instance of Total class
sum_example = TotalGUI()
        
        