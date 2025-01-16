from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql
from tkinter import ttk,messagebox
import pymysql
import datetime

class searchClass:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("800x480+200+40")
        self.root.title("Madumal Management System")
        self.root.resizable(False,False)
   
        # Heading
        title=Label(self.root,text="Search Model or Make",font=('times',25,'bold'),bg='#30E3DF',fg='black',anchor='w',padx=20)
        title.place(x=0,y=30,relwidth=1,height=40)


        #......search frame..........
        searchframe=LabelFrame(self.root,text="Search",font=('time',10,'bold'),bd=1,relief=RIDGE,bg='lightgray')
        searchframe.place(x=10,y=90,width=400,height=60)

        self.var_searchtxt=StringVar()
        self.var_searchby=StringVar()

        cmd_search=ttk.Combobox(searchframe,textvariable=self.var_searchby,values=("-- Select --","make","model"),state='readonly',justify=LEFT,font=('times',12,'bold'))
        cmd_search.place(x=5,y=5,width=100,height=25)
        cmd_search.current(0)
        
        txt_search=Entry(searchframe,textvariable=self.var_searchtxt,font=('times',12,'bold'),fg='black').place(x=115,y=5,width=120)
        btn_search=Button(searchframe,text='Search',command=self.search,font=('times',12,'bold'),fg='black').place(x=250,y=5,width=70,height=25)
        btn_clear=Button(searchframe,text='Clear',command=self.clear,font=('times',12,'bold'),fg='black').place(x=325,y=5,width=70,height=25)
        
        # ......Treeview..........
        # set treeview geography 
        Treeview_frame=Frame(self.root,bd=2,relief=RIDGE)
        Treeview_frame.place(x=10,y=170,width=780,height=270)

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
        self.treeviewtable.heading("date_today",text="Date")

        self.treeviewtable["show"]="headings"
        self.treeviewtable.column("nic",width=30,anchor='center')
        self.treeviewtable.column("name",width=70,anchor='center')
        self.treeviewtable.column("code",width=20,anchor='center')
        self.treeviewtable.column("make",width=70,anchor='center')
        self.treeviewtable.column("model",width=30,anchor='center')
        self.treeviewtable.column("price",width=50,anchor='center')
        self.treeviewtable.column("date_today",width=70,anchor='center')

        self.treeviewtable.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.treeviewtable.yview)
        self.displaydata()

    def search(self):
        try:
            if self.var_searchby.get()=="select":
                messagebox.showerror("Error","Select search option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Select input",parent=self.root)
            else:
                sqlcon=pymysql.connect(host="localhost", user="root", password="", database="madumal_009")
                cur=sqlcon.cursor()
                cur.execute("select nic,name,code,model,make,price,date_today from issueinvoice where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                result=cur.fetchall()
                if len(result)!=0:
                    self.treeviewtable.delete(*self.treeviewtable.get_children())
                    for row in result:
                        self.treeviewtable.insert('',END,value=row)
                else:
                    messagebox.showerror("Error","No data",parent=self.root)
                sqlcon.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            

    def clear(self):
        self.var_searchtxt.set("")
        self.var_searchby.set("-- Select --")
    

    def displaydata(self):
        sqlcon=pymysql.connect(host="localhost", user="root", password="", database="madumal_009")
        cur=sqlcon.cursor()
        cur.execute("select nic,name,code,make,model,price,date_today from issueinvoice")
        result=cur.fetchall()
        self.treeviewtable.delete(*self.treeviewtable.get_children())
        for row in result:
            self.treeviewtable.insert("",END,value=row)
      

# gui
if __name__=="__main__":
    root=Tk()
    obj=searchClass(root)
    root.mainloop()