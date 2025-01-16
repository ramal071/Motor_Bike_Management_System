from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql
from tkinter import ttk,messagebox
import pymysql
import datetime

class memberClass:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1100x525+200+40")
        self.root.title("Madumal Management System")
        self.root.resizable(False,False)
    
        # Heading
        title=Label(self.root,text="Customer / Memeber Details",font=('times',25,'bold'),bg='#30E3DF',fg='black',anchor='w',padx=20)
        title.place(x=0,y=30,relwidth=1,height=40)

        # variable

        self.var_nic=StringVar()
        self.var_name=StringVar()
        self.var_address=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_date=StringVar()

        self.var_date.set(datetime.date.today())

        #lables
        lbl_nic=Label(self.root,text="NIC",font=('times',20,'bold'),fg='black').place(x=10,y=100)
        lbl_name=Label(self.root,text="Name",font=('times',20,'bold'),fg='black').place(x=10,y=140)
        lbl_address=Label(self.root,text="Address",font=('times',20,'bold'),fg='black').place(x=10,y=180)
        lbl_contact=Label(self.root,text="Contact",font=('times',20,'bold'),fg='black').place(x=10,y=220)
        lbl_email=Label(self.root,text="Email",font=('times',20,'bold'),fg='black').place(x=10,y=260)
        lbl_date=Label(self.root,text="Date",font=('times',20,'bold'),fg='black').place(x=10,y=300)
        # Entry
        entry_nic=Entry(self.root,textvariable=self.var_nic,font=("times",20,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=190,y=106,width=250,height=30)
        entry_name=Entry(self.root,textvariable=self.var_name,font=("times",20,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=190,y=146,width=250,height=30)
        entry_address=Entry(self.root,textvariable=self.var_address,font=("times",20,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=190,y=186,width=250,height=30)
        entry_contact=Entry(self.root,textvariable=self.var_contact,font=("times",20,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=190,y=226,width=250,height=30)
        entry_email=Entry(self.root,textvariable=self.var_email,font=("times",20,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=190,y=266,width=250,height=30)
        entry_date=Entry(self.root,textvariable=self.var_date,font=("times",20,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=190,y=306,width=250,height=30)

        # button

        btn_save=Button(self.root,text="SAVE",command=self.save,font=('times',18),bg="#30E3DF",fg="black",cursor="hand2").place(x=10,y=400,height=30,width=100)
        btn_update=Button(self.root,text="UPDATE",command=self.update, font=('times',18),bg="#30E3DF",fg="black",cursor="hand2").place(x=150,y=400,height=30,width=110)
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=('times',18),bg="#30E3DF",fg="black",cursor="hand2").place(x=300,y=400,height=30,width=110)
        btn_clear=Button(self.root,text="CLEAR",command=self.clear,font=('times',18),bg="#30E3DF",fg="black",cursor="hand2").place(x=450,y=400,height=30,width=100)


       # Treeview
        # set treeview geography 
        Treeview_frame=Frame(self.root,bd=2,relief=RIDGE)
        Treeview_frame.place(x=520,y=100,width=520,height=250)

        scrolly=Scrollbar(Treeview_frame,orient=VERTICAL)
        scrollx=Scrollbar(Treeview_frame,orient=HORIZONTAL)

        self.treeviewtable=ttk.Treeview(Treeview_frame,columns=("nic","name","address","contact","email"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.config(command=self.treeviewtable.xview)
        scrolly.config(command=self.treeviewtable.yview)

        self.treeviewtable.heading("nic",text="NIC")
        self.treeviewtable.heading("name",text="Name")
        self.treeviewtable.heading("address",text="Address")
        self.treeviewtable.heading("contact",text="Contact")
        self.treeviewtable.heading("email",text="E-mail")

        self.treeviewtable["show"]="headings"
        self.treeviewtable.column("nic",width=30,anchor='center')
        self.treeviewtable.column("name",width=30,anchor='center')
        self.treeviewtable.column("address",width=30,anchor='center')
        self.treeviewtable.column("contact",width=30,anchor='center')
        self.treeviewtable.column("email",width=30,anchor='center')

        self.treeviewtable.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.treeviewtable.yview)
        self.treeviewtable.bind("<ButtonRelease-1>",self.getdata)
        self.displaydata()

    def displaydata(self):
        sqlcon=pymysql.connect(host="localhost", user="root", password="", database="madumal_009")
        cur=sqlcon.cursor()
        cur.execute("select * from member")
        result=cur.fetchall()

        self.treeviewtable.delete(*self.treeviewtable.get_children())
        for row in result:
            self.treeviewtable.insert("",END,value=row)
        # End get data to treeview

    def getdata(self,ev):
        viewinfo=self.treeviewtable.focus()
        learnerdata=(self.treeviewtable.item(viewinfo))
        row=learnerdata['values']

        self.var_nic.set(row[0])
        self.var_name.set(row[1])
        self.var_address.set(row[2])
        self.var_contact.set(row[3])
        self.var_email.set(row[4])
        self.var_date.set(row[5])
        # End get data to treeview

    # save button function
    def save(self):
        # pass
        sqlcon=pymysql.connect(host="localhost", user="root", password="", database="madumal_009")
        cur=sqlcon.cursor()

        try:
            if self.var_nic.get()=="":
                messagebox.showerror("Error", "All field required ... !!!")
            else:
                cur.execute("insert into member(nic,name,address,contact,email,date) values (%s,%s,%s,%s,%s,%s)",
                (
                    self.var_nic.get(),
                    self.var_name.get(),
                    self.var_address.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
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
        cur.execute("update member set name=%s,address=%s,contact=%s,email=%s,date=%s where nic=%s",
        (
            self.var_name.get(),
            self.var_address.get(),
            self.var_contact.get(),
            self.var_email.get(),
            self.var_date.get(),
            self.var_nic.get()
        ))
        sqlcon.commit()
        self.displaydata()
        messagebox.showinfo("Success", "Member Updated successfully ... !!!",parent=self.root)
        sqlcon.close()
        self.clear()
    
    
    def delete(self):
        sqlcon=pymysql.connect(host="localhost", user="root", password="", database="madumal_009")
        cur=sqlcon.cursor()
        cur.execute("delete from member where nic=%s",self.var_nic.get())
        sqlcon.commit()
        self.displaydata()
        messagebox.showinfo("Success", "Member Deleted successfully ... !!!",parent=self.root)
        sqlcon.close()
        self.clear()

    def clear(self):
        self.var_nic.set("")
        self.var_name.set("")
        self.var_address.set("")
        self.var_contact.set("")
        self.var_email.set("")
      #  self.var_date.set("")



# gui
if __name__=="__main__":
    root=Tk()
    obj=memberClass(root)
    root.mainloop()