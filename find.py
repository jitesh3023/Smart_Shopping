import os
import pickle

details_list=[]
l2=[]
G = []
def file_save():
    PRODUCT_PRO = details_list[0]
    PRICE_PRO = details_list[1]
    LOCATION_PRO = details_list[2]
    AVAILABILITY_PRO = details_list[3]
   
    f = open("data.ods", "ab")
    a=save(PRODUCT_PRO,PRICE_PRO,LOCATION_PRO,AVAILABILITY_PRO)
    pickle.dump(a,f, protocol=2)
    f.close()
    restart_program()


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)






class save:
    def __init__(self, PRODUCT_PRO, PRICE_PRO, LOCATION_PRO, AVAILABILITY_PRO):
        self.product=PRODUCT_PRO
        self.price=PRICE_PRO
        self.location=LOCATION_PRO
        self.availability=AVAILABILITY_PRO
    
        print(self.product, self.price, self.location, self.availability)

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


class SMART_SHOPPING:
    def __init__(self):
        def gotinfo():
            self.gettininfo = str(self.gather.get())
            print(self.gettininfo)
            print("\n")
            if len(self.gettininfo) != 0:
                self.Text1.insert(INSERT, " valid product name ""\n")
            else :
                self.Text1.insert(INSERT,"invalid product name""\n")

            try:
                n = 0
                f2 = open("data.ods", "rb")
                while True:
                    s = pickle.load(f2)
                    a = str(s.product)
                    print (a)
                    if self.gettininfo == a:
                        n = 1
                        # print("PRODUCT-", "\t", "\t", s.product)
                        # print("\n")
                        print("PRICE-", "\t", s.price)
                        print("\n")
                        print("LOCATION-", "  ", s.location)
                        print("\n")
                        print("AVAILABILITY", s.availability)
                    elif EOFError:
                        if n == 0:
                            print("INVALID PRODUCT ", self.gettininfo)
                        else:
                            n = 0
                            continue
            except EOFError:
                pass
                f2.close()

        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {Segoe UI} -size 17 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 28 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 23 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
        font5 = "-family {Segoe UI} -size 18 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        root.geometry("881x582+249+104")
        root.title("SMART SHOPPING")
        root.configure(background="#d9d9d9")



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.94)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=825)

        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.04, rely=0.46, relheight=0.48, relwidth=0.93)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=764)
        self.Text1.configure(wrap=WORD)



        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.12, rely=0.15, height=48, width=280)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font5)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text=''' Product Name   :''')

        self.Entry1 = Entry(self.Frame1)
        self.gather=StringVar()
        self.Entry1.place(relx=0.65, rely=0.17,height=40, relwidth=0.1)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=84)
        self.Entry1.configure(textvariable=self.gather)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.39, rely=0.29, height=74, width=197)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font10)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''SUBMIT''')
        self.Button1.configure(width=197)
        self.Button1.configure(command=gotinfo)

        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0.22, rely=0.02, relheight=0.12, relwidth=0.56)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(font=font10)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''INFO OF ANY MATERIAL ..!!''')
        self.Message1.configure(width=360)
        root.mainloop()






if __name__ == '__main__':
    GETINFO=SMART_SHOPPING()
