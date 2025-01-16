from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql
from tkinter import ttk,messagebox
import pymysql
import datetime

class addBikeClass:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1100x525+200+40")
        self.root.title("Madumapl Management System")
        self.root.resizable(False,False)


        # Heading
        title=Label(self.root,text="Add New Bike",font=('times',25,'bold'),bg='#30E3DF',fg='black',anchor='w',padx=20)
        title.place(x=0,y=30,relwidth=1,height=40)

        # variable
        self.var_code=StringVar()
        self.var_make=StringVar()
        self.var_model=StringVar()
        self.var_avail=StringVar()
        self.var_price=StringVar()
        self.var_date=StringVar()

        self.var_date.set(datetime.date.today())

        #lables
        lbl_code=Label(self.root,text="Bike Code",font=('times',20,'bold'),fg='black').place(x=10,y=100)
        lbl_make=Label(self.root,text="Bike Make",font=('times',20,'bold'),fg='black').place(x=10,y=140)
        lbl_model=Label(self.root,text="Bike Model",font=('times',20,'bold'),fg='black').place(x=10,y=180)
        lbl_avail=Label(self.root,text="Available Now",font=('times',20,'bold'),fg='black').place(x=10,y=220)
        lbl_price=Label(self.root,text="Bike Price",font=('times',20,'bold'),fg='black').place(x=10,y=260)
        lbl_date=Label(self.root,text="Date",font=('times',20,'bold'),fg='black').place(x=10,y=300)

        # Entry
        entry_code=Entry(self.root,textvariable=self.var_code,font=("times",20,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=200,y=106,width=150,height=30)
        entry_make=Entry(self.root,textvariable=self.var_make,font=("times",20,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=200,y=146,width=150,height=30)
        entry_model=Entry(self.root,textvariable=self.var_model,font=("times",20,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=200,y=186,width=150,height=30)
        entry_avail=Entry(self.root,textvariable=self.var_avail,font=("times",20,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=200,y=226,width=150,height=30)
        entry_price=Entry(self.root,textvariable=self.var_price,font=("times",20,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=200,y=266,width=150,height=30)
        entry_date=Entry(self.root,textvariable=self.var_date,font=("times",20,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=200,y=306,width=150,height=30)

         # button

        btn_save=Button(self.root,text="SAVE",command=self.save,font=('times',18),bg="#30E3DF",fg="black",cursor="hand2").place(x=10,y=400,height=30,width=100)
        btn_update=Button(self.root,text="UPDATE",command=self.update, font=('times',18),bg="#30E3DF",fg="black",cursor="hand2").place(x=150,y=400,height=30,width=110)
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=('times',18),bg="#30E3DF",fg="black",cursor="hand2").place(x=300,y=400,height=30,width=110)
        btn_clear=Button(self.root,text="CLEAR",command=self.clear,font=('times',18),bg="#30E3DF",fg="black",cursor="hand2").place(x=450,y=400,height=30,width=100)


       # Treeview
        # set treeview geography 
        Treeview_frame=Frame(self.root,bd=2,relief=RIDGE)
        Treeview_frame.place(x=470,y=100,width=600,height=200)

        scrolly=Scrollbar(Treeview_frame,orient=VERTICAL)
        scrollx=Scrollbar(Treeview_frame,orient=HORIZONTAL)

        self.treeviewtable=ttk.Treeview(Treeview_frame,columns=("code","make","model","avail","price","date"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.config(command=self.treeviewtable.xview)
        scrolly.config(command=self.treeviewtable.yview)

        self.treeviewtable.heading("code",text="Code")
        self.treeviewtable.heading("make",text="Make")
        self.treeviewtable.heading("model",text="Model")
        self.treeviewtable.heading("avail",text="Available")
        self.treeviewtable.heading("price",text="Price")
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
        self.treeviewtable.bind("<ButtonRelease-1>",self.getdata)
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

    def getdata(self,ev):
        viewinfo=self.treeviewtable.focus()
        learnerdata=(self.treeviewtable.item(viewinfo))
        row=learnerdata['values']

        self.var_code.set(row[0])
        self.var_make.set(row[1])
        self.var_model.set(row[2])
        self.var_avail.set(row[3])
        self.var_price.set(row[4])
        self.var_date.set(row[5])
        # End get data to treeview

    # save button function
    def save(self):
        # pass
        sqlcon=pymysql.connect(host="localhost", user="root", password="", database="madumal_009")
        cur=sqlcon.cursor()

        try:
            if self.var_code.get()=="":
                messagebox.showerror("Error", "All field required ... !!!")
            else:
                cur.execute("insert into bike(code,make,model,avail,price,date) values (%s,%s,%s,%s,%s,%s)",
                (
                    self.var_code.get(),
                    self.var_make.get(),
                    self.var_model.get(),
                    self.var_avail.get(),
                    self.var_price.get(),
                    self.var_date.get(),
                ))
                sqlcon.commit()
                self.displaydata()
                messagebox.showinfo("Success", "All field recorded successfully ... !!!",parent=self.root)
            sqlcon.close()
            self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")


    def update(self):
        sqlcon=pymysql.connect(host="localhost", user="root", password="", database="madumal_009")
        cur=sqlcon.cursor()
        cur.execute("update bike set make=%s,model=%s,avail=%s,price=%s,date=%s where code=%s",
        (
            self.var_make.get(),
            self.var_model.get(),
            self.var_avail.get(),
            self.var_price.get(),
            self.var_date.get(),
            self.var_code.get()
        ))
        sqlcon.commit()
        self.displaydata()
        messagebox.showinfo("Success", "Bike Updated successfully ... !!!",parent=self.root)
        sqlcon.close()
        self.clear()
    
    def delete(self):
        sqlcon=pymysql.connect(host="localhost", user="root", password="", database="madumal_009")
        cur=sqlcon.cursor()
        cur.execute("delete from bike where code=%s",self.var_code.get())
        sqlcon.commit()
        self.displaydata()
        messagebox.showinfo("Success", "Bike Deleted successfully ... !!!",parent=self.root)
        sqlcon.close()
        self.clear()

    def clear(self):
        self.var_code.set("")
        self.var_make.set("")
        self.var_model.set("")
        self.var_avail.set("")
        self.var_price.set("")
      #  self.var_date.set("")



# gui
if __name__=="__main__":
    root=Tk()
    obj=addBikeClass(root)
    root.mainloop()