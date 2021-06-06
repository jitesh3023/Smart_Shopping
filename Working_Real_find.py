from Tkinter import * 
import os
def show_entry_fields():
	a = e.get()
	if a=="Fruits":
		location="First Column"
		price=50
        #availability="Yes"
        
	elif a == "Medicines":
		location="Second Column"
		price=1000
	elif a == "Grocery":
		location="Third Column"
		price=500
	elif a == "Vegetable":
		location="Fourth Column"
		price=600
	elif a == "Stationary":
		location="Fifth Column"
		price=30
	else:
		location=0
		price=0
		print("Please enter valid item name")
	print("Item: %s\nLocation: %s\nPrice: %s" % (e.get(), location,price))

m=Tk()
m.title('Find commodity')
Label(m, text='Item Name').grid(row=0)
e = Entry(m)
e.grid(row=0, column=1)
#Button(m, text='Quit', command=m.quit).grid(row=3,column=0, sticky=W,pady=4)
Button(m,text='Show', command=show_entry_fields).grid(row=3, column=1,sticky=W, pady=4)
menus=Tk()
menus.title("Items available with us are :-")  
#Label  
Label(menus, text="Items available with us are as follows:\n1)Fruits,\n 2)Medicines,\n 3)Grocery,\n 4)Vegetable and \n 5)Stationary\n Please type the required item name in the other dialog box.").grid(column=3,row=5,padx=20,pady=30) 

m.mainloop()