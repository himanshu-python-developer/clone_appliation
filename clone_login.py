from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox  

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == 'hsdevp@gmail.com' and password == '1234':
        messagebox.showinfo('Yayyy','Login Successful')
    else:
        messagebox.showerror('Error','Login Failed')


root = Tk()

root.title('logIn') #this method use the title bar name change 

root.iconbitmap('') # this root using icon include

# root.minsize(400,400) # method using the minsizie side 

root.geometry('350x500') # this method usethe as a look the size of any manypulate

root.configure(background='#0096DC') # This Method using a Background color 

#This Menthod Using a Import a logo and photo 
# img = builtins.open(filename=("Flipkart"))
img = Image.open('Flipkart/img1.jpeg')
risezed_img = img.resize((100,100))
img = ImageTk.PhotoImage(risezed_img)

img_label = Label(root,image=img)
img_label.pack(pady=(10,10))

#Unsing Front Size Showing Name 
text_lable = Label(root,text='Flipkart',fg='white',bg='#0096DC')
text_lable.pack()
text_lable.config(font=('verdana',24))

# Using this Method Showing this the block of Email  
email_lable = Label(root,text= 'Enter Email',fg='white',bg='#0096DC')
email_lable.pack(pady=(20,5))
email_lable.config(font=('verdana',11))

email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(20,5))

#Using this Method Useing a Password As a Password 
password_lable =Label (root , text ='Password ', fg ='white', bg='#0096DC')
password_lable.config(font=(20,5))
password_lable.pack(pady=(1,15))

password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(20,5))

#Using this Method Show the logIn Botten  
login_btn = Button(root,text='Login Here',bg='white',fg='black',width=20,height=2,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))




root.mainloop()
