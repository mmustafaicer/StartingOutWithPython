# Joe's Automotive
# learn onvalue and off value for Checkbuttons
# it helped a lot.


import tkinter
import tkinter.messagebox

class JoeAutomotiveGUI:
    def __init__(self):
        # create the main window and set title
        self.main_window=tkinter.Tk()
        self.main_window.title("Joe's Automotive")
        self.main_window.geometry("500x500")
        
        # create two frames
        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        
        # create IntVar variables to hold costs
        self.oil_checked = tkinter.IntVar()
        self.lube_checked = tkinter.IntVar()
        self.radiator_checked = tkinter.IntVar()
        self.transmission_checked = tkinter.IntVar()
        self.inspection_checked = tkinter.IntVar()
        self.muffler_checked = tkinter.IntVar()
        self.tire_checked = tkinter.IntVar()
        
        # set IntVar variables to 0
        self.oil_checked.set(0)
        self.lube_checked.set(0)
        self.radiator_checked.set(0)
        self.transmission_checked.set(0)
        self.inspection_checked.set(0)
        self.muffler_checked.set(0)
        self.tire_checked.set(0)
        
        # create Checkbuttons.
        self.cb1=tkinter.Checkbutton(self.top_frame, \
                                     text="Oil Change-$30.00", variable=self.oil_checked, onvalue=30, offvalue=0)  
        self.cb2=tkinter.Checkbutton(self.top_frame, \
                                     text="Lube Job-$20.00", variable=self.lube_checked, onvalue=20, offvalue=0)
        self.cb3=tkinter.Checkbutton(self.top_frame, \
                                     text="Radiator Flush-$40.00", variable=self.radiator_checked, onvalue=40, offvalue=0)
        self.cb4=tkinter.Checkbutton(self.top_frame, \
                                     text="Transmission Flush-$100.00", variable=self.transmission_checked, onvalue=100, offvalue=0)
        self.cb5=tkinter.Checkbutton(self.top_frame, \
                                     text="Inspection-$35.00", variable=self.inspection_checked, onvalue=35, offvalue=0)
        self.cb6=tkinter.Checkbutton(self.top_frame, \
                                     text="Muffler Replacement-$200.00", variable=self.muffler_checked, onvalue=200, offvalue=0)
        self.cb7=tkinter.Checkbutton(self.top_frame, \
                                     text="Tire Rotation-$30.00", variable=self.tire_checked, onvalue=30, offvalue=0)
        
        # pack the Checkbuttons
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()
        
        # bottom frame for buttons.
        self.calc_button=tkinter.Button(self.bottom_frame, \
                                       text="Calculate Total",\
                                       command=self.show_total)
        self.quit_button=tkinter.Button(self.bottom_frame,\
                                        text="Quit", bg="red",\
                                        command=self.main_window.destroy)
        
        # pack the buttons
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")
        
        # finally pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # create the main loop
        self.main_window.mainloop()
        
    def show_total(self):
        # calculate the total
        self.total=self.oil_checked.get() + self.lube_checked.get() + self.radiator_checked.get() + \
                    self.transmission_checked.get() + self.inspection_checked.get() + \
                    self.muffler_checked.get() + self.tire_checked.get()
        
        # create total message.
        self.total_message="$"+format(float(self.total), ",.2f")
        
        tkinter.messagebox.showinfo("Your Total", self.total_message)
        
# create an instance of JoeAutomotiveGUI
example=JoeAutomotiveGUI()