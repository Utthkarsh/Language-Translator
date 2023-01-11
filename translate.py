from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox
root = Tk()
root.title('Translate Languages')
root.geometry('880x300')
def tran():
    transTxt.delete(1.0,END)
    try:
        for key,values in language.items():
            if(values == originalCom.get()):
                origKey = key
        for key,values in language.items():
            if(values == transCom.get()):
                transKey = key
    except Exception as e:
        messagebox.showerror('translator ' + e)
    word = textblob.TextBlob(orignialTxt.get(1.0,END))
    word = word.translate(from_lang=origKey,to=transKey)
    transTxt.insert(1.0,word)
def clear():
    orignialTxt.delete(1.0,END)
    transTxt.delete(1.0,END)
language = googletrans.LANGUAGES
langL = list(language.values())
orignialTxt = Text(root, height=10,width=40)
orignialTxt.grid(row=0,column=0,padx=10,pady=20)

translateB = Button(root,text='Translate',font=('Helvetica',24),command=tran)
translateB.grid(row=0,column=1,padx=10)

transTxt = Text(root, height=10,width=40)
transTxt.grid(row=0,column=2,padx=10,pady=20)

originalCom = ttk.Combobox(root,width=50,value=langL)
originalCom.current(21)
originalCom.grid(row=1,column=0)

transCom = ttk.Combobox(root,width=50,value=langL)
transCom.current(21)
transCom.grid(row=1,column=2)

clearB = Button(root, text='clear',command=clear)
clearB.grid(row=2,column=1)

root.mainloop()