from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql
from tkinter import ttk,messagebox
import pymysql
import datetime

class inventoryClass:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("650x525+200+40")
        self.root.title("Madumal Management System")
        self.root.resizable(False,False)


        # Heading
        title=Label(self.root,text="Bike Inventory",font=('times',25,'bold'),bg='#30E3DF',fg='black',anchor='w',padx=20)
        title.place(x=0,y=30,relwidth=1,height=40)

       # Treeview
        # set treeview geography 
        Treeview_frame=Frame(self.root,bd=2,relief=RIDGE)
        Treeview_frame.place(x=10,y=100,width=600,height=200)

        scrolly=Scrollbar(Treeview_frame,orient=VERTICAL)
        scrollx=Scrollbar(Treeview_frame,orient=HORIZONTAL)

        self.treeviewtable=ttk.Treeview(Treeview_frame,columns=("code","make","model","avail","price","date"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.config(command=self.treeviewtable.xview)
        scrolly.config(command=self.treeviewtable.yview)

        self.treeviewtable.heading("code",text="Code")
        self.treeviewtable.heading("make",text="Make")
        self.treeviewtable.heading("model",text="Model")
        self.treeviewtable.heading("avail",text="Available")
        self.treeviewtable.heading("price",text="Price (Rs)")
        self.treeviewtable.heading("date",text="Date")

        self.treeviewtable["show"]="headings"
        self.treeviewtable.column("code",width=10,anchor='center')
        self.treeviewtable.column("make",width=30,anchor='center')
        self.treeviewtable.column("model",width=30,anchor='center')
        self.treeviewtable.column("avail",width=30,anchor='center')
        self.treeviewtable.column("price",width=30,anchor='center')
        self.treeviewtable.column("date",width=30,anchor='center')

        self.treeviewtable.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.treeviewtable.yview)
       # self.treeviewtable.bind("<ButtonRelease-1>",self.getdata)
        self.displaydata()

    def displaydata(self):
        sqlcon=pymysql.connect(host="localhost", user="root", password="", database="madumal_009")
        cur=sqlcon.cursor()
        cur.execute("select * from bike")
        result=cur.fetchall()

        self.treeviewtable.delete(*self.treeviewtable.get_children())
        for row in result:
            self.treeviewtable.insert("",END,value=row)
        # End get data to treeview


# gui
if __name__=="__main__":
    root=Tk()
    obj=inventoryClass(root)
    root.mainloop()