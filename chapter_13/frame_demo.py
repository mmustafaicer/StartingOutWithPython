# this program creates labels in two different frames.
import tkinter 

class MyGUI:
    def __init__(self):
        # create the main window widget.
        self.main_window=tkinter.Tk()
        
        # create two frames, one for the top of the 
        # windows, and one for the bottom.
        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        
        # create three Label widgets for the top frame.
        self.label1=tkinter.Label(self.top_frame, \
                                  text="Winken")
        self.label2=tkinter.Label(self.top_frame, \
                                  text="Blinken")
        self.label3=tkinter.Label(self.top_frame, \
                                  text="Nod")
        
        # pack the labels that are in the top frame.
        # use the side="top" argument to stack them one 
        # on top of the other.
        self.label1.pack(side="top")
        self.label2.pack(side="top")
        self.label3.pack(side="top")
        
        # create three Label widgets for the bottom frame.
        self.label4=tkinter.Label(self.top_frame, \
                                  text="Winken")
        self.label5=tkinter.Label(self.top_frame, \
                                  text="Blinken")
        self.label6=tkinter.Label(self.top_frame, \
                                  text="Nod")
        
        # pack the labels that are in the bottom frame.
        # use the side="left" argument to arrange them 
        # horizontally from the left of the frame.
        self.label4.pack(side="left")
        self.label5.pack(side="left")
        self.label6.pack(side="left")
        
        # yes, we have to pack the frames too!
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        # enter the tkinter main loop.
        tkinter.mainloop()
        
# create an instance of the MyGUI class.
my_gui=MyGUI()