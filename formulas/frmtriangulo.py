from tkinter import * #Cargar módulo

def calcular(): #Método para hallar el triángulo
    la=int(txtlado.get())
    are = la * la
    return areatri.set(are)
    #print(str(are))

raiz = Tk() #define la ventana principal
raiz.title('Triangulo')
raiz.geometry('300x300') #anchura y altura
raiz.configure(bg='beige')

areatri= StringVar()

lblnombre = Label(raiz, text="Ingrese el lado:")
lblnombre.pack()

txtlado=Entry(raiz)
txtlado.pack()

btnmostrar =Button(raiz, text="Calcular", command=calcular)
btnmostrar.pack()

lblresultado= Label(raiz, textvariable=areatri)
lblresultado.pack()

raiz.mainloop()

