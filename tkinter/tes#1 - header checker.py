
from tkinter import *
import requests as r


st= Tk()


hed = Label(text="-= HOST CHECKER =-")
hed.pack()

e = Entry(st,width=30,borderwidth=5)
e.pack()

# show help (pengguna pydroid)
def h(v):
       with open('/sdcard/dir.txt','w') as w:
       	        w.write(help(v))
       	        
def di():
	      lab = Label(text=f'GET http://{e.get()} HTTP/1.1 ')
	      lab.pack()
	      res  = r.get(url='http://'+e.get(),
	      allow_redirects=False)
	      r_code = res.status_code
	      r_rea = res.reason
	      lab2 = Label(bg='green',text='Response: {} {} '.format(
	      str(r_code),
	      str(r_rea)))
	      lab2.pack()
	      for i in res.headers:
	            h = Label(text=f'{i}: {res.headers[i]}')
	            h.pack()
	     

bt = Button(padx=50,text='Check', borderwidth=2,command=di)
bt.pack()


st.mainloop()
