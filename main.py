from tkinter import *
from tkinter import messagebox
import random, os, tempfile, smtplib


#functionality Part

def print_bill():
    if textarea.get(1.0,END) =='\n':
        messagebox.showerror("Error", "Bill is empty Details are requried")
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnumberEntry.get():
            f = open(f'bills/{i}','r')
            textarea.delete(1.0,END)

            for data in f:
                textarea.insert(END,data)
            f.close()  
            break

    else:
        messagebox.showerror("Error","Bill not found")

    pass

if not os .path.exists('bills'):
    os.mkdir('bills')


def save_bill():
    result = messagebox.askyesno('Confirm','Do you want to save the bill')
    
    if result:
        bill_content = textarea.get(1.0,END)
        file = open(f"bills/{billnumber}.txt","w") 
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill {billnumber} saved successfully')
    



billnumber=random.randint(500,1000)
# Total 
def total():
    global soapprice,hairsprayprice,facecreamprice,facewashprice,hairgelprice,bodylotionprice  
    global riceprice,oilprice,daalprice,wheetprice,sugarprice,teaprice    
    global mazzaprice,pepsiprice,spriteprice,dewprice,frootyprice,cococolaprice 
    global totalbill

    #cosmatic Price Calculation
    soapprice=int(bathsoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*50
    facewashprice=int(facewashEntry.get())*100
    hairgelprice=int(hairgelEntry.get())*80
    hairsprayprice=int(hairsprayEntry.get())*150
    bodylotionprice= int(bodylotionEntry.get())*60

    totalcosmaticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmaticpriceEntry.delete(0,END)
    cosmaticpriceEntry.insert(0,f'{totalcosmaticprice} Rs')
    cosmatictax=totalcosmaticprice * 0.12
    cosmatictaxEntry.delete(0,END)
    cosmatictaxEntry.insert(0,f'{cosmatictax} Rs')
    
    #Grocery Price Calculation
    riceprice=int(riceEntry.get())*30
    oilprice=int(oilEntry.get())*100
    daalprice=int(daalEntry.get())*120
    wheetprice=int(wheetEntry.get())*50
    sugarprice=int(sugarEntry.get())*140
    teaprice=int(teaEntry.get())*80

    totalgroceryprice=riceprice+oilprice+daalprice+wheetprice+sugarprice+teaprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'{totalgroceryprice} Rs')
    grocerytax=totalgroceryprice*0.05
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,str(grocerytax)+ " Rs")
    
    #Cold Drink Price Calculation
    mazzaprice=int(mazzaEntry.get())*50
    pepsiprice=int(pepsiEntry.get())*20
    spriteprice=int(spriteEntry.get())*30
    dewprice=int(dewEntry.get())*20
    frootyprice=int(frootiEntry.get())*45
    cococolaprice=int(cococolaEntry.get())*50

    totaldrinksprice=mazzaprice+pepsiprice+spriteprice+dewprice+frootyprice+cococolaprice
    drinkpriceEntry.delete(0,END)
    drinkpriceEntry.insert(0,f'{totaldrinksprice} Rs')

    drinktax=totalgroceryprice*0.08
    drinktaxEntry.delete(0,END)
    drinktaxEntry.insert(0,str(drinktax)+ " Rs")


    totalbill=totalcosmaticprice+totalgroceryprice+totaldrinksprice+cosmatictax+grocerytax+drinktax
# Bill Show button
def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror("Error","Please Enter Customer Name and Phone Number")
    elif cosmaticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and drinkpriceEntry.get()=='':
        messagebox.showerror("Error","No Products Are Selected")
    elif cosmaticpriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs' and drinkpriceEntry.get()=='0 Rs':    
        messagebox.showerror("Error","No Products Are Selected")
    else:
        textarea.delete(1.0,END)

        textarea.insert(END, '\t\t** Welcome Customer **\n')
        textarea.insert(END, f'\nBillNumber: {billnumber}')
        textarea.insert(END, f'\nCustomer Name : {nameEntry.get()}')
        textarea.insert(END, f'\nCustomer Phone Number: {phoneEntry.get()}')
        textarea.insert(END,'\n===============================================================\n')
        textarea.insert(END,'Product\t\t\tQuality\t\t\tPrice')
        textarea.insert(END,'\n===============================================================\n')
        if bathsoapEntry.get()!='0':
            textarea.insert(END,f'Bath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs\n') 
        if facecreamEntry.get()!='0':
            textarea.insert(END,f'Face Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs\n')    
        if facewashEntry.get()!='0':
            textarea.insert(END,f'Face Wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs\n')
        if hairsprayEntry.get()!='0':
            textarea.insert(END,f'hair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs\n')
        if hairgelEntry.get()!='0':
            textarea.insert(END,f'Hair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs\n')
        if bodylotionEntry.get()!='0':
            textarea.insert(END,f'Body Lotion \t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs\n')


        if riceEntry.get()!='0':
            textarea.insert(END,f'Rice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs\n')   
        if oilEntry.get()!='0':
            textarea.insert(END,f'Oil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs\n')  
        if daalEntry.get()!='0':
            textarea.insert(END,f'Daal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs\n') 
        if wheetEntry.get()!='0':
            textarea.insert(END,f'Wheet\t\t\t{wheetEntry.get()}\t\t\t{wheetprice} Rs\n')   
        if sugarEntry.get()!='0':
            textarea.insert(END,f'Sugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs\n') 
        if teaEntry.get()!='0':
            textarea.insert(END,f'Tea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs\n')

        
        if mazzaEntry.get()!='0':
            textarea.insert(END,f'Mazza\t\t\t{mazzaEntry.get()}\t\t\t{mazzaprice} Rs\n')   
        if pepsiEntry.get()!='0':
            textarea.insert(END,f'Pepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs\n')  
        if spriteEntry.get()!='0':
            textarea.insert(END,f'Sprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rs\n') 
        if dewEntry.get()!='0':
            textarea.insert(END,f'Dew\t\t\t{dewEntry.get()}\t\t\t{dewprice} Rs\n')   
        if frootiEntry.get()!='0':
            textarea.insert(END,f'Frooty\t\t\t{frootiEntry.get()}\t\t\t{frootyprice} Rs\n') 
        if cococolaEntry.get()!='0':
            textarea.insert(END,f'Coco Cola\t\t\t{cococolaEntry.get()}\t\t\t{cococolaprice} Rs\n')
        textarea.insert(END,'\n---------------------------------------------------------------\n')
        
        if cosmatictaxEntry.get()!='0,0 Rs':
            textarea.insert(END,f'\nCosmatic Tax: \t\t\t{cosmatictaxEntry.get()}')
        if grocerytaxEntry.get()!='0,0 Rs':
            textarea.insert(END,f'\nGrocery Tax: \t\t\t{grocerytaxEntry.get()}')
        if drinktaxEntry.get()!='0,0 Rs':
            textarea.insert(END,f'\nDrink Tax: \t\t\t{drinktaxEntry.get()}')

        textarea.insert(END,f'\nTotal Bill: \t\t\t{totalbill}')
        save_bill()


def send_email():
    def send():
        try:
            obj = smtplib.SMTP('smtp.gmail.com', 587)
            obj.starttls()
            obj.login(senderEntry.get(),password.get())
            message = emailtextarea.get(.0,END)
            reciever_address = reciverEntry.get()
            obj.sendmail(senderEntry.get(), reciever_address, message)
            obj.quit()
            messagebox.showinfo("Success", "Email sent successfully",parent = emailwindow)
            emailwindow.destroy()
        except:
            messagebox.showerror("Error", "Failed to send email",parent = emailwindow)


    if textarea.get(1.0,END) == '\n':
        messagebox.showerror("Error", "Bill is empty")
    else:
        emailwindow = Toplevel()
        emailwindow.title("Send Email")
        emailwindow.resizable(0,0)
        emailwindow.config(bg='gray20')
        emailwindow.grab_set()

        sender_frame = LabelFrame(emailwindow,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='gold')
        sender_frame.grid(row=0,column=0,padx=40,pady=20)

        senderlebel = Label(sender_frame,text="Sender's Email",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        senderlebel.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        senderEntry = Entry(sender_frame,font=('arial',12,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=10)


        password = Label(sender_frame,text="Password",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        password.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        password = Entry(sender_frame,font=('arial',12,'bold'),bd=2,width=23,relief=RIDGE,show='x')
        password.grid(row=1,column=1,padx=10,pady=10)


        recipentframe = LabelFrame(emailwindow,text='RECIPIENT',font=('arial',16,'bold'),bd=6,bg='gray20',fg='gold')
        recipentframe.grid(row=1,column=0,padx=40,pady=20)

        reciverlebel = Label(recipentframe,text="Email Address",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        reciverlebel.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        reciverEntry = Entry(recipentframe,font=('arial',12,'bold'),bd=2,width=24,relief=RIDGE)
        reciverEntry.grid(row=0,column=1,padx=10,pady=10)

        messagelebel = Label(recipentframe,text="Message",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        messagelebel.grid(row=1,column=0,padx=10,pady=5,sticky=W)


        emailtextarea = Text(recipentframe,bd=2,width=48,height=16)
        emailtextarea.grid(row=2,column=0,padx=10,pady=5,columnspan=2)
        emailtextarea.delete(1.0,END)
        emailtextarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-',''))

        sendbutton = Button(emailwindow,text='SEND',font=('arial',16,'bold'),width=15,background='gold',activebackground='gold',command=send)
        sendbutton.grid(row=2,column=0,padx=10,pady=10)



#GUI Part
root=Tk()
root.title("Retail Billing System")
root.geometry('1270x680')
root.iconbitmap('icon.ico')

headinglabel=Label(root,text='Retail Billing System',font=('time new roman',30,'bold')
                   ,bg='gray20',fg='gold',bd=12,relief=GROOVE)
headinglabel.pack(fill=X)

# Customer Deatils Section

customer_details_Frame=LabelFrame(root, text='Customer Details',
                                  font=('time new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
customer_details_Frame.pack(fill=X)

nameLabel=Label(customer_details_Frame,text='Name',
                font=('time new roman',15,'bold'),fg='white',bg='gray20')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_Frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_Frame,text='Phone Number',
                font=('time new roman',15,'bold'),fg='white',bg='gray20')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_Frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_Frame,text='Bill Number',
                font=('time new roman',15,'bold'),fg='white',bg='gray20')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_Frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_Frame,text='Search',
                font=('arial',12,'bold'),bd=7,width=10, command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productFrame=Frame(root)
productFrame.pack()

# Cosmatic Section

cosmaticsFrame=LabelFrame(productFrame,text='Cosmatics',
                          font=('time new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
cosmaticsFrame.grid(row=0,column=0)

bathsoapLable=Label(cosmaticsFrame,text='Bath Soap',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
bathsoapLable.grid(row=0,column=0,pady=9,padx=10,sticky='W')

bathsoapEntry=Entry(cosmaticsFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)

facecreamLable=Label(cosmaticsFrame,text='Face Cream',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
facecreamLable.grid(row=1,column=0,pady=9,padx=10,sticky='W')

facecreamEntry=Entry(cosmaticsFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)

facewashLable=Label(cosmaticsFrame,text='Face Wash',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
facewashLable.grid(row=2,column=0,pady=9,padx=10,sticky='W')

facewashEntry=Entry(cosmaticsFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)

hairsprayLable=Label(cosmaticsFrame,text='Hair Spray',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
hairsprayLable.grid(row=3,column=0,pady=9,padx=10,sticky='W')

hairsprayEntry=Entry(cosmaticsFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairsprayEntry.insert(0,0)

hairgelLable=Label(cosmaticsFrame,text='Hair Gel',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
hairgelLable.grid(row=4,column=0,sticky='W',pady=9,padx=10)

hairgelEntry=Entry(cosmaticsFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)
hairgelEntry.insert(0,0)

bodylotionLable=Label(cosmaticsFrame,text='Body Lotion',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
bodylotionLable.grid(row=5,column=0, pady=9,padx=10,sticky='W')

bodylotionEntry=Entry(cosmaticsFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)

# Grocery Section

groceryFrame=LabelFrame(productFrame,text='Grocery',
                          font=('time new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
groceryFrame.grid(row=0,column=1)

riceLable=Label(groceryFrame,text='Rice',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
riceLable.grid(row=0,column=0,pady=9,padx=10,sticky='W')

riceEntry=Entry(groceryFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)

oilLable=Label(groceryFrame,text='Oil',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
oilLable.grid(row=1,column=0,pady=9,padx=10,sticky='W')

oilEntry=Entry(groceryFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,0)

daalLable=Label(groceryFrame,text='Daal',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
daalLable.grid(row=2,column=0,pady=9,padx=10,sticky='W')

daalEntry=Entry(groceryFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=9,padx=10)
daalEntry.insert(0,0)

wheetLable=Label(groceryFrame,text='Wheet',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
wheetLable.grid(row=3,column=0,pady=9,padx=10,sticky='W')

wheetEntry=Entry(groceryFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
wheetEntry.grid(row=3,column=1,pady=9,padx=10)
wheetEntry.insert(0,0)

sugerLable=Label(groceryFrame,text='Suger',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
sugerLable.grid(row=4,column=0,pady=9,padx=10,sticky='W')

sugarEntry=Entry(groceryFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=4,column=1,pady=9,padx=10)
sugarEntry.insert(0,0)

teaLable=Label(groceryFrame,text='Tea',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
teaLable.grid(row=5,column=0,pady=9,padx=10,sticky='W')

teaEntry=Entry(groceryFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10)
teaEntry.insert(0,0)



# Cold Drink Section

colddrinkFrame=LabelFrame(productFrame,text='Cold Drink',
                          font=('time new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
colddrinkFrame.grid(row=0,column=2)

mazzaLable=Label(colddrinkFrame,text='Mazza',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
mazzaLable.grid(row=0,column=0,pady=9,padx=10,sticky='W')

mazzaEntry=Entry(colddrinkFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
mazzaEntry.grid(row=0,column=1,pady=9,padx=10)
mazzaEntry.insert(0,0)

pepsiLable=Label(colddrinkFrame,text='Pepsi',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
pepsiLable.grid(row=1,column=0,pady=9,padx=10,sticky='W')

pepsiEntry=Entry(colddrinkFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)
pepsiEntry.insert(0,0)

spriteLable=Label(colddrinkFrame,text='Sprite',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
spriteLable.grid(row=2,column=0,pady=9,padx=10,sticky='W')

spriteEntry=Entry(colddrinkFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)

dewLable=Label(colddrinkFrame,text='Dew',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
dewLable.grid(row=3,column=0,pady=9,padx=10,sticky='W')

dewEntry=Entry(colddrinkFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
dewEntry.grid(row=3,column=1,pady=9,padx=10)
dewEntry.insert(0,0)

frootiLable=Label(colddrinkFrame,text='Frooti',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
frootiLable.grid(row=4,column=0,pady=9,padx=10,sticky='W')

frootiEntry=Entry(colddrinkFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
frootiEntry.grid(row=4,column=1,pady=9,padx=10)
frootiEntry.insert(0,0)

cococolaLable=Label(colddrinkFrame,text='Coco Cola',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
cococolaLable.grid(row=5,column=0,pady=9,padx=10,sticky='W')

cococolaEntry=Entry(colddrinkFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
cococolaEntry.grid(row=5,column=1,pady=9,padx=10)
cococolaEntry.insert(0,0)


# Bill Area Section

billFrame=Frame(productFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=3,padx=6)

billarealabel=Label(billFrame,text='Bill Area',font=('time new roman',15,'bold'),bd=7,relief=GROOVE)
billarealabel.pack(fill=X)

Scrollbar=Scrollbar(billFrame,orient=VERTICAL)
Scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billFrame,height=19,width=63,yscrollcommand=Scrollbar.set)
textarea.pack()
Scrollbar.config(command=textarea.yview)

# Bill Menu Section

billmenuFrame=LabelFrame(root,text='Bill Menu',
                          font=('time new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
billmenuFrame.pack()


# row=5,column=1,pady=9,padx=10

cosmaticpriceLable=Label(billmenuFrame,text='Cosmatic Price',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
cosmaticpriceLable.grid(row=0,column=0,pady=9,padx=35)

cosmaticpriceEntry=Entry(billmenuFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
cosmaticpriceEntry.grid(row=0,column=1,pady=6,padx=15)

grocerypriceLable=Label(billmenuFrame,text='Grocery Price',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
grocerypriceLable.grid(row=1,column=0,pady=6,padx=35,sticky='W')

grocerypriceEntry=Entry(billmenuFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10)

drinkpriceLable=Label(billmenuFrame,text='Cold Drink Price',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
drinkpriceLable.grid(row=2,column=0,pady=6,padx=35,sticky='W')

drinkpriceEntry=Entry(billmenuFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
drinkpriceEntry.grid(row=2,column=1,pady=6,padx=10)

cosmatictaxLable=Label(billmenuFrame,text='Cosmatic Tax',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
cosmatictaxLable.grid(row=0,column=3,pady=6,padx=10,sticky='W')

cosmatictaxEntry=Entry(billmenuFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
cosmatictaxEntry.grid(row=0,column=4,pady=6,padx=10)

grocerytaxLable=Label(billmenuFrame,text='Grocery Tax',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
grocerytaxLable.grid(row=1,column=3,pady=6,padx=10,sticky='W')

grocerytaxEntry=Entry(billmenuFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=4,pady=6,padx=10)

drinktaxLable=Label(billmenuFrame,text='Cold Drink Tax',
                    font=('time new roman',15,'bold'),fg='white',bg='gray20')
drinktaxLable.grid(row=2,column=3,pady=6,padx=10,sticky='W')

drinktaxEntry=Entry(billmenuFrame,
                    font=('time new roman',15,'bold'),width=10,bd=5)
drinktaxEntry.grid(row=2,column=4,pady=6,padx=10)


#Buttonframe

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=5,rowspan=3)

totalButton=Button(buttonFrame,text='Total',
                   font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text='Bill',
                   font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',
                   font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',
                   font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',
                   font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
clearButton.grid(row=0,column=4,pady=20,padx=5)





root.mainloop()

