from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql
from tkinter import ttk,messagebox
import pymysql
import datetime
import openpyxl
from openpyxl import Workbook

class issueInvoiceClass:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("850x525+200+40")
        self.root.title("Madumal Management System")
        self.root.resizable(False,False)
   
        # Heading
        title=Label(self.root,text="Invoice",font=('times',25,'bold'),bg='#30E3DF',fg='black',anchor='w',padx=20)
        title.place(x=0,y=30,relwidth=1,height=40)

        # variable
        # invoice
        self.var_invoiceNo=StringVar()
        self.var_date_today=StringVar()


        # member
        self.var_nic=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_address=StringVar()
        self.var_email=StringVar()

        # addbike
        self.var_code=StringVar()
        self.var_make=StringVar()
        self.var_model=StringVar()
        self.var_price=StringVar()
        self.var_date=StringVar()

        self.var_date_today.set(datetime.date.today())

        #lables
        lbl_code=Label(self.root,text="CODE",font=('times',16,'bold'),fg='black').place(x=60,y=100)
        lbl_nic=Label(self.root,text="NIC",font=('times',16,'bold'),fg='black').place(x=60,y=140)
        # Bike
        lbl_make=Label(self.root,text="Bike Make",font=('times',12,'bold'),fg='black').place(x=500,y=90,height=15)
        lbl_model=Label(self.root,text="Bike Model",font=('times',12,'bold'),fg='black').place(x=500,y=110,height=15)
        lbl_price=Label(self.root,text="Bike Price",font=('times',12,'bold'),fg='black').place(x=500,y=130,height=15)
        lbl_date=Label(self.root,text="Date",font=('times',12,'bold'),fg='black').place(x=500,y=150,height=15)
        # Member
        lbl_name=Label(self.root,text="Name",font=('times',12,'bold'),fg='black').place(x=500,y=200,height=15)
        lbl_address=Label(self.root,text="Address",font=('times',12,'bold'),fg='black').place(x=500,y=220,height=15)
        lbl_contact=Label(self.root,text="Contact",font=('times',12,'bold'),fg='black').place(x=500,y=240,height=15)
        lbl_email=Label(self.root,text="Email",font=('times',12,'bold'),fg='black').place(x=500,y=260,height=15)
      
        # Entry
        entry_code=Entry(self.root,textvariable=self.var_code,font=("times",12,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=160,y=98,width=170,height=30)
        entry_nic=Entry(self.root,textvariable=self.var_nic,font=("times",12,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=160,y=138,width=170,height=30)
        # Bike
        entry_make=Entry(self.root,textvariable=self.var_make,font=("times",12,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=600,y=90,width=160,height=15)
        entry_model=Entry(self.root,textvariable=self.var_model,font=("times",12,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=600,y=110,width=160,height=15)
        entry_price=Entry(self.root,textvariable=self.var_price,font=("times",12,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=600,y=130,width=160,height=15)
        entry_date=Entry(self.root,textvariable=self.var_date,font=("times",12,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=600,y=150,width=160,height=15)
        # Member
        entry_name=Entry(self.root,textvariable=self.var_name,font=("times",12,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=600,y=200,width=160,height=15)
        entry_address=Entry(self.root,textvariable=self.var_address,font=("times",12,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=600,y=220,width=160,height=15)
        entry_contact=Entry(self.root,textvariable=self.var_contact,font=("times",12,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=600,y=240,width=160,height=15)
        entry_email=Entry(self.root,textvariable=self.var_email,font=("times",12,"bold"),bg="#30E3DF",fg="black",bd=0).place(x=600,y=260,width=160,height=15)
       
        # button

        btn_code=Button(self.root,text="Search",command=self.search1,font=('times',12),bg="#30E3DF",fg="black",cursor="hand2").place(x=350,y=100,height=23,width=70)
        btn_nic=Button(self.root,text="Search",command=self.search2, font=('times',12),bg="#30E3DF",fg="black",cursor="hand2").place(x=350,y=140,height=23,width=70)
        
        btn_save=Button(self.root,text="SAVE",command=self.save,font=('times',12),bg="#30E3DF",fg="black",cursor="hand2").place(x=17,y=190,height=30,width=80)
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=('times',12),bg="#30E3DF",fg="black",cursor="hand2").place(x=120,y=190,height=30,width=80)
        btn_clear=Button(self.root,text="CLEAR",command=self.clear,font=('times',12),bg="#30E3DF",fg="black",cursor="hand2").place(x=220,y=190,height=30,width=80)
        btn_print = Button(self.root, text="Print to Excel", command=self.export_to_excel,bg="#30E3DF").place(x=320,y=190,height=30,width=80)
 
        
        # ......Treeview..........
        # set treeview geography 
        Treeview_frame=Frame(self.root,bd=2,relief=RIDGE)
        Treeview_frame.place(x=10,y=300,width=780,height=170)

        scrolly=Scrollbar(Treeview_frame,orient=VERTICAL)
        scrollx=Scrollbar(Treeview_frame,orient=HORIZONTAL)

        self.treeviewtable=ttk.Treeview(Treeview_frame,columns=("nic","name","code","make","model","price","date_today"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.config(command=self.treeviewtable.xview)
        scrolly.config(command=self.treeviewtable.yview)
        
        self.treeviewtable.heading("nic",text="NIC")
        self.treeviewtable.heading("name",text="Name")
        self.treeviewtable.heading("code",text="Code")
        self.treeviewtable.heading("make",text="Make")
        self.treeviewtable.heading("model",text="Model")
        self.treeviewtable.heading("price",text="Price (Rs)")
        self.treeviewtable.heading("date_today",text="Date Today")

        self.treeviewtable["show"]="headings"
        self.treeviewtable.column("nic",width=70)
        self.treeviewtable.column("name",width=70)
        self.treeviewtable.column("code",width=70)
        self.treeviewtable.column("make",width=70)
        self.treeviewtable.column("model",width=100)
        self.treeviewtable.column("price",width=70)
        self.treeviewtable.column("date_today",width=70)

        self.treeviewtable.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.treeviewtable.yview)
        self.treeviewtable.bind("<ButtonRelease-1>",self.getdata)
        self.displaydata()

    
    def search1(self):
        sqlcon=pymysql.connect(host="localhost", user="root", password="", database="madumal_009")
        cur=sqlcon.cursor()
        cur.execute("select * from bike where code=%s",self.var_code.get())
        result=cur.fetchall()

        for row in result:
            self.var_make.set(row[1])
            self.var_model.set(row[2])
            self.var_price.set(row[4])
            self.var_date.set(row[5])

    def search2(self):
        sqlcon=pymysql.connect(host="localhost", user="root", password="", database="madumal_009")
        cur=sqlcon.cursor()
        cur.execute("select * from member where nic=%s",self.var_nic.get())
        result=cur.fetchall()

        for row in result:
            self.var_name.set(row[1])
            self.var_address.set(row[2])
            self.var_contact.set(row[3])
            self.var_email.set(row[4])

    def displaydata(self):
        sqlcon=pymysql.connect(host="localhost", user="root", password="", database="madumal_009")
        cur=sqlcon.cursor()
        cur.execute("select nic,name,code,make,model,price,date_today from issueinvoice")
        result=cur.fetchall()

        self.treeviewtable.delete(*self.treeviewtable.get_children())
        for row in result:
            self.treeviewtable.insert("",END,value=row)
        # End get data to treeview

    def getdata(self,ev):
        viewinfo=self.treeviewtable.focus()
        learnerdata=(self.treeviewtable.item(viewinfo))
        row=learnerdata['values']

        self.var_nic.set(row[1])
        self.var_name.set(row[2])
        self.var_code.set(row[3])
        self.var_make.set(row[4])
        self.var_model.set(row[5])
        self.var_price.set(row[6])
        self.var_date_today.set(row[7])
        # End get data to treeview

    # save button function
    def save(self):
        sqlcon=pymysql.connect(host="localhost", user="root", password="", database="madumal_009")
        cur=sqlcon.cursor()

        try:
            if self.var_nic.get()=="" and self.var_code.get()=="":
                messagebox.showerror("Error", "NIC & CODE fields required ... !!!")
            else:
                cur.execute("insert into issueinvoice(nic,name,code,make,model,price,date_today) values (%s,%s,%s,%s,%s,%s,%s)",
                (
                  #  self.var_invoceNo.get(),
                    self.var_nic.get(),
                    self.var_name.get(),
                    self.var_code.get(),
                    self.var_make.get(),
                    self.var_model.get(),
                    self.var_price.get(),
                    self.var_date_today.get(),
                ))

                cur.execute("update bike set avail = avail-1 where code = %s", (self.var_code.get(),))

                sqlcon.commit()
                self.displaydata()
                messagebox.showinfo("Success", "All field recorded successfully ... !!!",parent=self.root)
            sqlcon.close()
            self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")    
    # part 07
    def delete(self):
        if len(self.var_invoiceNo.get())==0:
            messagebox.showerror('Error',"Please select a record",parent=self.root)
        else:
            sqlcon=pymysql.connect(host="localhost", user="root", password="", database="madumal_009")
            cur=sqlcon.cursor()
            cur.execute("delete from issueinvoice where invoiceNo=%s",self.var_invoiceNo.get())
            sqlcon.commit()
            self.displaydata()
            messagebox.showinfo("Success", "Invoice Deleted successfully ... !!!",parent=self.root)
            sqlcon.close()
            self.clear()

    def clear(self):
        self.var_nic.set("")
        self.var_name.set("")
        self.var_code.set("")
        self.var_make.set("")
        self.var_model.set("")
        self.var_price.set("")
        self.var_date_today.set("")

    def export_to_excel(self):
        # Create a new Excel workbook and select the active sheet
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Inventory Data"

        # Add column headers
        headers = ["NIC", "Name", "Code", "Make", "Model", "Price", "Date"]
        sheet.append(headers)

        # Insert each row of data
        for row_id in self.treeviewtable.get_children():
            row = self.treeviewtable.item(row_id)['values']
            sheet.append(row)

        # Save the workbook to a file
        workbook.save("InventoryData.xlsx")
        print("Data exported to InventoryData.xlsx")
      

# gui
if __name__=="__main__":
    root=Tk()
    obj=issueInvoiceClass(root)
    root.mainloop()