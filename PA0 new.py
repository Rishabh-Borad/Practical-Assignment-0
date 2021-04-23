#importing necessary libraries
from tkinter import *
from tkinter import ttk

#generate and configure the root node of ui
root=Tk()
ttk.Style().configure("TButton", padding=6, relief="flat", background="#ffffff")
root.title("PA0")
root.configure(background="#abcfef")



#function to encrypt data, since algorithm to encrypt and decrypt is same, this function can be use to both encrypt and decrypt data
#text : data to be encrypted
def encryptData(text):
	n=len(text)
	out=''
	for i in range(n):
		if(ord(text[i])>=ord('A') and ord(text[i])<=ord('Z')):
			diff = ord(text[i])-ord('A')
			out+=chr(ord('Z')-diff)
		elif(ord(text[i])>=ord('a')and ord(text[i])<=ord('z')):
			diff=ord(text[i])-ord('a')
			out+=chr(ord('z')-diff)
		else:
		 out+=text[i]
	return out
	

#command to be called on pressing encipher/decipher button
#text : data to be encrypted/decrypted
#te : text field which will be containing output of encryption/decryption
def edButton(text,te):
	out=encryptData(text)
	te.delete("1.0",END)
	te.insert("1.0",out)

#frame
frame=LabelFrame(root,text="",padx=10,pady=10)
frame.configure(background="#222930")


#plain text label
ptl=Label(frame,text="PLAINTEXT",bg="#222930",font=("Times New Roman",14),fg="white")
#cipher text label
ctl=Label(frame,text="CIPHERTEXT",bg="#222930",font=("Times New Roman",14),fg="white")


#plain text entry
pte=Text(frame,width=50,height=10,bg="#4EB1BA")
#cipher text entry
cte=Text(frame,width=50,height=10,bg="#4EB1BA")

#Encryption Button
ptb=Button(frame,text=">>Encipher>>",font=("Times New Roman",14),bg="#E9E9E9",command=lambda:edButton(pte.get("1.0",END),cte),bd=10,relief="solid")
#Decryption Button
ctb=Button(frame,text="<<Decipher<<",font=("Times New Roman",14),bg="#E9E9E9",command=lambda:edButton(cte.get("1.0",END),pte),bd=10,relief="solid")

frame.pack(padx=10,pady=10)

#positioning
ptl.grid(row=0,column=0,pady=10)
ctl.grid(row=0,column=2,pady=10)

pte.grid(row=1,column=0,rowspan=2)
cte.grid(row=1,column=2,rowspan=2)

ptb.grid(row=1,column=1,padx=15)
ctb.grid(row=2,column=1,padx=15)

root.mainloop()
