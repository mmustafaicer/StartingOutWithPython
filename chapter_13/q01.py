# name and address
import tkinter

class NameAddressGUI:
    def __init__(self):
        # open a main window.
        self.main_window=tkinter.Tk()
        
        # create two frames for 1 info and buttons below
        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        
        # TOP FRAME
        # create a address string variable
        self.address=tkinter.StringVar()
        
        # create display label
        self.address_label=tkinter.Label(self.top_frame, \
                                         textvariable=self.address)
        
        # pack the widget
        self.address_label.pack(side="left")
        
        # BOTTOM FRAME
        # create buttons.
        self.show_button=tkinter.Button(self.bottom_frame, \
                                      text="Show Info", \
                                      command=self.show_info)
        self.quit_button=tkinter.Button(self.bottom_frame,\
                                        text="Quit", \
                                        command=self.main_window.destroy)
        
        # pack the widgets.
        self.show_button.pack(side="left")
        self.quit_button.pack(side="left")
        
        # pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        # enter the mainloop.
        self.main_window.mainloop()
        
    def show_info(self):
        # create address text
        self.text="Test User\n145 Python Drive\nDallas, TX 76201"
        
        # set address text to address_label
        self.address.set(self.text)
    
# create an instance
my_info=NameAddressGUI()