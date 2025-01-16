from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql
from tkinter import ttk,messagebox


from addBike import addBikeClass
from member import memberClass
from issueInvoice import issueInvoiceClass
from search import searchClass
from inventory import inventoryClass


class dashboard:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1100x525+150+75")
        self.root.title("Madumal Motor Management System")

        bg_image = Image.open("bg.jpg").resize((1100,525)) 
        self.photo_image=ImageTk.PhotoImage(bg_image)
        self.lbl_photo_image=Label(self.root,image=self.photo_image,bd=0).place(x=0,y=0)

        title=Label(self.root,text="Madumal Motor - Rathnapura",font=('times',25,'bold'),bg='lightblue',fg='black',anchor='w',padx=20)
        title.place(x=0,y=30,relwidth=1,height=40)

         # label
        btn_bike=Button(self.root,text="Add Bike",command=self.addbike,font=('times',20,'bold'),bg='lightblue',fg='black',cursor='hand2', bd=0).place(x=15,y=120,height=35,width=250)
        btn_member=Button(self.root,text="Customer",command=self.member,font=('times',20,'bold'),bg='lightblue',fg='black',cursor='hand2', bd=0).place(x=15,y=170,height=35,width=250)
        btn_invoice=Button(self.root,text="Invoice",command=self.issueInvoice,font=('times',20,'bold'),bg='lightblue',fg='black',cursor='hand2', bd=0).place(x=15,y=220,height=35,width=250)
        btn_search=Button(self.root,text="Search",command=self.search,font=('times',20,'bold'),bg='lightblue',fg='black',cursor='hand2', bd=0).place(x=15,y=270,height=35,width=250)
        btn_inventory=Button(self.root,text="Inventory",command=self.inventory,font=('times',20,'bold'),bg='lightblue',fg='black',cursor='hand2', bd=0).place(x=15,y=320,height=35,width=250)

    def addbike(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=addBikeClass(self.new_win)

    def member(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=memberClass(self.new_win)

    def issueInvoice(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=issueInvoiceClass(self.new_win)

    def search(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=searchClass(self.new_win)

    def inventory(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=inventoryClass(self.new_win)

# gui
if __name__=="__main__":
    root=Tk()
    obj=dashboard(root)
    root.mainloop()