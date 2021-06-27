from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime


GUI = Tk()
GUI.title("Program บันทึกค่าใช้จ่าย By Yingnaja V.1.0")
#GUI.geometry('700x550+500+50')

w = 700
h = 550
ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2) - 50

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')


####################### MENU BAR #########################
menubar = Menu(GUI)
GUI.config(menu=menubar)

# File menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to googlesheet')
# Help menu
def About():
    print('About_menu')
    messagebox.showinfo('About','สวัสดีครับ \n สนใจติต่อ 0897513041')
    
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)
helpmenu.add_command(label='Read Me')
# Donate menu
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)

##########################################################
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH, expand=1)

icon_t1 = PhotoImage(file='list.png') # .subsample ใช้สำหรับย่อรูปคิดเป็นเท่า
icon_t2 = PhotoImage(file='list2.png')

Tab.add(T1, text=f'{"ค่าใช้จ่าย": ^{25}}', image=icon_t1,compound='top')
Tab.add(T2, text=f"{'ค่าใช้จ่ายทั้งหมด': ^{25}}", image=icon_t2,compound="top")

F1 = Frame(T1)
F1.pack(pady=10)

day = {'Mon':'จันทร์',
        'Tue':'อังคาร',
        'Wed':'พุธ',
        'Thu':'พฤหัสบดี',
        'Fri':'ศุกร์',
        'Sat':'เสาร์',
        'Sun':'อาทิตย์'
        }

def Save(event=None):
    expense = V_expense.get()
    price = V_price.get()
    pic = V_pic.get()

    if expense =="":
        messagebox.showwarning('Error','กรุณากรอกรายการ')
        return
    elif price == '':
        messagebox.showwarning('Error', 'กรูณากรอกราคา')
        return
    elif pic == '':
        messagebox.showwarning('Error', 'กรูณากรอกจำนวนสินค้า')

    try:
        total = int(price) * int(pic)
        # today = datetime.now().strftime('%a')
        # dt = datetime.now().strftime('%Y-%m-%d %H: %M: %S')
        # dt = day[today] + '' + dt
        print(f"รายการ: {expense} ราคา {price} บาท จำนวน {pic} จาน รวมเป็นเงิน {total} บาท")
        text = f'รายการ: {expense} ราคา: {price} บาท \n'
        text = text + f'จำนวน: {pic} รายการ รวมทั้งหมด: {total} บาท'
        v_rerult.set(text)
        V_expense.set("")
        V_price.set("")
        V_pic.set("")
        # บันทึกข้อมูลลง CSV
        today = datetime.now().strftime('%a')
        print(today)
        stamp = datetime.now()
        dt = stamp.strftime('%Y-%m-%d %H:%M:%S')
        transactionid = stamp.strftime('%Y%m%d%H%M%f')
        dt = day[today]+'-' + dt
        with open('savedata.csv', 'a',encoding='utf-8', newline='') as f:
            fw = csv.writer(f)
            data = [transactionid, dt, expense, price, pic, total]
            fw.writerow(data)
        #ทำให้เคอเซอร์ กลับไปตำแหน่งช่องกรอกแรก
        E1.focus()
        update_table()
    except:
        print('ERROR')
        #messagebox.showerror('Error', 'คุณกรอกตัวเลขผิด')
        messagebox.showwarning('Error', 'คุณกรอกข้อความผิด')
        V_expense.set("")
        V_price.set("")
        V_pic.set("")
# กด Enter
GUI.bind('<Return>', Save) #ต้องเพิ่ม def Save(event=None): 

def Show():
    pic = V_pic.get()
    result = int(price) * int(pic)
    print(f"รายการ: {expense} ราคา {price} บาท จำนวน {pic} จาน รวมเป็นเงิน {result} บาท")

FONT1 = (None, 16)
FONT2 = (None, 14)

shopping = PhotoImage(file='shop.png')
shoppic = ttk.Label(F1, image=shopping)
shoppic.pack()

#-------------------------------------
L = ttk.Label(F1, text="รายการค่าใช้จ่าย", font=FONT1).pack()
V_expense = StringVar() # ตัวแปรสำหรับเก็บข้อมูล
E1 = ttk.Entry(F1, textvariable=V_expense, font=FONT2)
E1.pack()
#-------------------------------------
#-------------------------------------
L = ttk.Label(F1, text="ราคา(บาท)", font=FONT1).pack()
V_price = StringVar() # ตัวแปรสำหรับเก็บข้อมูล
E2 = ttk.Entry(F1, textvariable=V_price, font=FONT2)
E2.pack()
#-------------------------------------
#-------------------------------------
L = ttk.Label(F1, text="จำนวน", font=FONT1).pack()
V_pic = StringVar() # ตัวแปรสำหรับเก็บข้อมูล
E3 = ttk.Entry(F1, textvariable=V_pic, font=FONT2)
E3.pack()
#-------------------------------------

saveicon = PhotoImage(file='save.png')
B2 = ttk.Button(F1, text='Save',command=Save, image=saveicon, compound='left')
B2.pack(ipadx=5, ipady=5, pady=10)

v_rerult = StringVar()
v_rerult.set('-------------rusult----------------')
result = ttk.Label(F1, textvariable=v_rerult,font=FONT1,foreground='green')
result.pack(pady=20)

###########################TAP 2############################

def read_csv():
    with open('savedata.csv', newline='',encoding='utf-8') as f:
        fr = csv.reader(f)
        data = list(fr)
    return data

# table
L = ttk.Label(T2, text='ตารางแสดงผลลัพธ์', font=FONT1).pack(pady=20)
header = ['ID','วัน-เวลา','รายการ','ราคา','จำนวน','รวมเงิน']
resultTable = ttk.Treeview(T2, columns=header, show='headings',height=15)
resultTable.pack()

# for i in range(len(header)):
#     resultTable.heading(header[0] ,text=header[0])

for h in header:
    resultTable.heading(h, text=h)

headerWidth = [120,150,180,80,50,80]
for h, w in zip(header, headerWidth):
    resultTable.column(h,width=w)

# ปุ่ม Delete (ตัวอย่าง)
# saveicon = PhotoImage(file='save.png')
# B2 = ttk.Button(F1, text='Save',command=Save, image=saveicon, compound='left')
# B2.pack(ipadx=5, ipady=5, pady=10)

alltransaction = {}

def UpdateCSV():
    with open('savedata.csv','w', newline='',encoding='utf-8') as f:
        fw = csv.writer(f)
        #เตรียมข้อมูลให้กลายเป็น list
        data = list(alltransaction.values())
        fw.writerows(data)
        print('Table was updated')
        

def DeleteRecord(event=None):
    check = messagebox.askyesno('Confirm','คุณต้องการลบข้อมูลใช่หรือไม่')
    if check==True:
        print('dedete')
        select = resultTable.selection()
        print(select)
        data = resultTable.item(select)
        data = data['values']
        transactionid = data[0]
        #print(transactionid)
        del alltransaction[str(transactionid)]
        UpdateCSV()
        update_table()
    else:
        print('Cancel')

BDelete = ttk.Button(T2, text='Delete',command=DeleteRecord)
BDelete.place(x=50, y=400)
#ใช้ปุ่ม Delete ลบ
resultTable.bind('<Delete>',DeleteRecord) 



def update_table():
    resultTable.delete(*resultTable.get_children())

    try:
        data = read_csv()
        for d in data:
            #create transaction data
            alltransaction[d[0]] = d
            resultTable.insert('',0, value=d)
        print('all  ', alltransaction)
    except:
        print('No file')

update_table()

###########################Right Click Menu############################

def EditRecord():
    POPUP = Toplevel()  #แทน Tk()
    POPUP.title('Edit Record')
    #POPUP.geometry('400x300')
    w = 400
    h = 300
    ws = POPUP.winfo_screenwidth()
    hs = POPUP.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2) - 50

    POPUP.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')

    #-------------------------------------
    L = ttk.Label(POPUP, text="รายการค่าใช้จ่าย", font=FONT1).pack()
    V_expense = StringVar() # ตัวแปรสำหรับเก็บข้อมูล
    E1 = ttk.Entry(POPUP, textvariable=V_expense, font=FONT2)
    E1.pack()
    #-------------------------------------
    #-------------------------------------
    L = ttk.Label(POPUP, text="ราคา(บาท)", font=FONT1).pack()
    V_price = StringVar() # ตัวแปรสำหรับเก็บข้อมูล
    E2 = ttk.Entry(POPUP, textvariable=V_price, font=FONT2)
    E2.pack()
    #-------------------------------------
    #-------------------------------------
    L = ttk.Label(POPUP, text="จำนวน", font=FONT1).pack()
    V_pic = StringVar() # ตัวแปรสำหรับเก็บข้อมูล
    E3 = ttk.Entry(POPUP, textvariable=V_pic, font=FONT2)
    E3.pack()
    #-------------------------------------

    def Edit():
        olddata = alltransaction[str(transactionid)]
        print('LOD: ', olddata)
        v1 = V_expense.get()
        v2 = float(V_price.get())
        v3 = int(V_pic.get())
        total = v2 * v3
        newdata = [olddata[0],olddata[1],v1,v2,v3,total]
        alltransaction[str(transactionid)] = newdata
        UpdateCSV()
        update_table()
        POPUP.destroy()  #คำสั่งปิดป๊อบอัพ


    saveicon = PhotoImage(file='save.png')
    B2 = ttk.Button(POPUP, text='Save',command=Edit, image=saveicon, compound='left')
    B2.pack(ipadx=5, ipady=5, pady=10)

    # -----get data in selected record---------
    select = resultTable.selection()
    #print(select)
    data = resultTable.item(select)
    data = data['values']
    print(data)
    transactionid = data[0]

    # set ค่าเก่าไว้ในกล่อง
    V_expense.set(data[2])
    V_price.set(data[3])
    V_pic.set(data[4])


    POPUP.mainloop()
    


rightclick = Menu(GUI,tearoff=0)
rightclick.add_command(label='Edit', command=EditRecord)
rightclick.add_command(label='Delete', command=DeleteRecord)

def menupopup(event):
    #print(event.x_root, event.y_root)
    rightclick.post(event.x_root, event.y_root) # คลิกขวาแล้วขึ้นป๊อบอัพ



resultTable.bind('<Button-3>', menupopup)  # ตำแหน่งที่คลิกขวาแล้วป๊อบอัพ




GUI.bind('<Tab>', lambda x: E2.focus())
GUI.mainloop()