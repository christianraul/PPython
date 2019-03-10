from tkinter import *
raiz=Tk()
raiz.title("Ventana de Prueba")
# raiz.iconbitmap("") para icono de ventana
# raiz.geometry("650x350")
raiz.config(bg="blue")

nframe=Frame()
nframe.pack()
nframe.config(bg="red")
nframe.config(width="650", height="350")
nframe.config(bd=10)
nframe.config(cursor="hand2")
nframe.config(relief="groove")



raiz.mainloop()