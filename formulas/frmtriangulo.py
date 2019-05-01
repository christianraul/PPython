from tkinter import * #Cargar módulo

def calcular(): #Método para hallar el triángulo
    la=int(txtlado.get())
    are = la * la
    return areatri.set(are)
    #print(str(are))

raiz = Tk() #define la ventana principal
raiz.title('Triangulo')
raiz.geometry('300x200') #anchura y altura
raiz.configure(bg='gold')

areatri= StringVar()

colorfondo="gold"
colorboton="yellow"
colorletra="red"

lblti=Label(raiz, text="Área de un Triángulo", bg=colorfondo, fg=colorletra, font=("Ebrima", 22)).place(x=20, y=10)
lblnombre = Label(raiz, text="Ingrese el lado:", bg=colorfondo, fg=colorletra, font=("Helvetica", 16)).place(x=10, y=60)
txtlado=Entry(raiz, font=("Arial", 12), justify=CENTER, width=10)
txtlado.place(x=160, y=65)
btnmostrar =Button(raiz, text="Calcular", bg=colorboton, fg="blue", command=calcular, font=("Ebrima", 14), anchor="center", activebackground="red").place(x=70, y=100)
btncerrar =Button(raiz, text="Cerrar", bg="red", fg="white", command=raiz.quit, font=("Ebrima", 14), anchor="center", activebackground="yellow").place(x=170, y=100)
lbltitulo=Label(raiz, text="El resultado es: ", bg=colorfondo, font=("Ebrima", 20)).place(x=10, y=150)
lblresultado= Label(raiz, textvariable=areatri, bg="black", fg="white", font=("Ebrima", 20))
lblresultado.place(x=200, y=150)

raiz.mainloop()

