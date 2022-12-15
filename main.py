from tkinter import *
from modulos_Proyecto import *
def destructor(nombre_raiz):
    '''Destruye la raiz

    :param nombre_raiz: Nombre de la Raiz
    :type nombre_raiz: Tkinter
    :return: None
    :rtype: None
    '''
    nombre_raiz.destroy()

def consultar_libro_proceso(libro,frame):
    '''Retorna una interfaz con la lista de libros que está disponible

    :param libro: Código del libro
    :type libro: str
    :param frame: Colocar mensajes
    :type frame: Tkinter
    :return: None
    :rtype: None
    '''
    a=persona.ConsultarLibro(libro)
    if a!= 0 and a!= None and a!=[]:
        lola = Tk()
        lola.title("Modulo Estudiante")
        lola.geometry("650x600")
        lol = Frame(lola, width="450", height="450")
        lol.pack()
        Nombre = Label(lol, text="libros disponibles", pady=10)
        Nombre.grid(row=0, column=0, sticky="w")
        contador =2
        for x in range(len(a)):
                nombre = Label(lol, text=" nombre: " + a[x][0])
                nombre.grid(row=contador, column=0, sticky="w")
                autor = Label(lol, text="Genero: " + a[x][1])
                autor.grid(row=contador + 1, column=0, sticky="w")
                Estado = Label(lol, text="Autor: " + a[x][2])
                Estado.grid(row=contador + 2, column=0, sticky="w")
                codigo = Label(lol, text="estado: " + a[x][3])
                codigo.grid(row=contador + 3, column=0, sticky="w")
                codigo = Label(lol, text="Codigo: " + a[x][4])
                codigo.grid(row=contador + 4, column=0, sticky="w")
                espacio=Label(lol, text="")
                espacio.grid(row=contador + 5, column=0, sticky="w")
                contador=contador+6
    else:
        Nombre = Label(frame, text="No disponible")
        Nombre.grid(row=2, column=2)

def consultar_libros():
    '''Interfaz de consultar libros

    :return: Interfaz para búsqueda de los libros
    :rtype: None
    '''
    consultar = Tk()
    consultar.title("Modulo Estudiante")
    consultar.geometry("650x600")
    frameconsultar = Frame(consultar, width="450", height="450")
    frameconsultar.pack()
    var_libro= StringVar(consultar)
    Nombre = Label(frameconsultar, text="Indicame el nombre del libro que deseas consultar")
    Nombre.grid(row=1, column=1, pady=10)
    pregunta = Entry(frameconsultar, textvariable=var_libro)
    pregunta.grid(row=2, column=1, pady=10)
    boton_actualizar_informacion = Button(frameconsultar, text="consultar", width=21,command=lambda :consultar_libro_proceso(var_libro.get(),frameconsultar))
    boton_actualizar_informacion.grid(row=7, column=1)
    boton_actualizar_informacion.config(cursor="hand2")
    boton_salir = Button(frameconsultar, text="Salir", width=21,command=lambda :destructor(consultar))
    boton_salir.grid(row=8, column=1, pady=10)
    boton_salir.config(cursor="hand2")
    consultar.mainloop()

def eliminar_Libro_Proceso(frame,codigo):
    '''Elimina un libro de la lista

    :param frame: Contenedor de un mensaje
    :type frame: Tkinter
    :param codigo: Código del libro
    :type codigo: str
    :return: None
    :rtype: None
    '''
    a=Funcionario.EliminarLibros(codigo)
    if a!=0 and a!= None:
        afirmativo= Label(frame,text="El libro "+a[0][0]+" sido eliminado correctamente")
        afirmativo.grid(row=9, column=1)
    else:
        Negativo = Label(frame, text="El libro no se encuentra en existencia valida nuevamente")
        Negativo.grid(row=9, column=1)

def elimininar_Libro():
    '''Permite ingresar el código para eliminar el libro

    :return: None
    :rtype: None
    '''
    lola = Tk()
    lola.title("Modulo Estudiante")
    lola.geometry("650x600")
    framelola = Frame(lola, width="450", height="450")
    framelola.pack()
    Nombre = Label(framelola, text="Indicame el codigo  del libro que deseas eliminar")
    Nombre.grid(row=1, column=1, pady=10)
    Libro2 = StringVar(lola)
    pregunta = Entry(framelola, textvariable=Libro2)
    pregunta.grid(row=2, column=1, pady=10)
    boton_actualizar_informacion = Button(framelola, text="eliminar", width=21,command=lambda:eliminar_Libro_Proceso(framelola, Libro2.get()))
    boton_actualizar_informacion.grid(row=7, column=1)
    boton_actualizar_informacion.config(cursor="hand2")
    boton_salir = Button(framelola, text="Salir", width=21, command=lambda: destructor(lola))
    boton_salir.grid(row=8, column=1, pady=10)
    boton_salir.config(cursor="hand2")
    lola.mainloop()

def inicio_sesion_estudiante(raiz):
        '''Interfaz para iniciar sesión del estudiante

        :param raiz: Raiz Anterior
        :type raiz: Tkinter
        :return: None
        :rtype: None
        '''
        destructor(raiz)
        estu = Tk()
        estu.title("proyecto final poo")
        estu.geometry("650x600")
        frame = Frame(estu, width="450", height="450")
        frame.pack()
        titulo_validacion = Label(frame, text="validacion de estudiante ")
        titulo_validacion.grid(row=3, column=1, pady=40)
        codigo=Label(frame,text="ingresa tu codigo")
        codigo.grid(row=4, column=0)
        varcod_Estu= StringVar()
        ingreso_codigo=Entry(frame,textvariable=varcod_Estu)
        ingreso_codigo.grid(row=4, column=1)
        varcon_Estu=StringVar()
        contraseña=Label(frame,text="ingresa tu contraseña")
        contraseña.grid(row=5, column=0)
        ingreso_contraseña=Entry(frame,textvariable=varcon_Estu)
        ingreso_contraseña.grid(row=5,column=1)
        ingreso_contraseña.config(show="*")
        Boton_ingreso=Button(frame,text="ingresar",command=lambda:validar_estudiante_Interfaz(frame,estu,varcod_Estu.get(),varcon_Estu.get()))
        Boton_ingreso.grid(row=6,column=1,pady=5)
        Boton_salir = Button(frame, text="salir", command=lambda: volver_Menu(estu))
        Boton_salir.grid(row=7, column=1, pady=5)
        estu.mainloop()

def devolver_libro(frame,posicion):
    '''Devuelve el libro

    :param frame: Contenedor de un mensaje
    :type frame: Tkinter
    :param posicion: Posición del usuario en el fichero
    :type posicion: int
    :return: None
    :rtype: None
    '''
    Var_int_devolver=Estudiante.devolver_libro(posicion)
    if Var_int_devolver==1:
        No_Reserva= Label(frame,text="no tienes libros reservados")
        No_Reserva.grid(row=5, column=2)
    elif Var_int_devolver==3:
        Reserva = Label(frame, text="Haz devuelto el libro con exito")
        Reserva.grid(row=5, column=2)
    elif Var_int_devolver==0:
        No_Existen=Label(frame, text="Haz devuelto el libro con exito")
        No_Existen.grid(row=5, column=2)

def validar_estudiante_Interfaz(frame,raiz,opcion, contraseña):
            '''Valida la información del estudiante para poder iniciar sesión del estudiante

            :param frame: Da un mensaje en caso de ingresar los datos erroneamente
            :type frame: Tkinter
            :param raiz: Destruir la raiz anterior
            :type raiz: Tkinter
            :param opcion: Código del Estudiante
            :type opcion: str
            :param contraseña: Contraseña para iniciar sesión
            :type contraseña: str
            :return: None
            :rtype: None
            '''
            lista = Estudiante.validar_Estudiante(opcion, contraseña)
            if lista != 0 and lista != None:
                destructor(raiz)
                origen = Tk()
                origen.title("Modulo Estudiante")
                origen.geometry("650x600")
                frameF = Frame(origen, width="450", height="450")
                frameF.pack()
                Nombre = Label(frameF, text="Bienvenid@ " + lista[0][0] + " " + lista[0][1])
                Nombre.grid(row=1, column=1, pady=10)
                pregunta = Label(frameF, text="¿Que deseas hacer el dia de hoy?")
                pregunta.grid(row=2, column=1, pady=10)
                boton_agregar = Button(frameF, text="pedir un libro", width=21, command=lambda:Pedir_Libros(lista[1]))
                boton_agregar.grid(row=4, column=1, pady=10)
                boton_agregar.config(cursor="hand2")
                boton_eliminar = Button(frameF, text="devolver un libro", width=21, command=lambda:devolver_libro(frameF,lista[1]))
                boton_eliminar.grid(row=5, column=1, pady=10)
                boton_eliminar.config(cursor="hand2")
                boton_consultar = Button(frameF, text="consultar un libro", width=21, command=lambda:consultar_libros())
                boton_consultar.grid(row=6, column=1, pady=10)
                boton_consultar.config(cursor="hand2")
                boton_salir = Button(frameF, text="Salir", width=21,command=lambda :volver_Menu(origen))
                boton_salir.grid(row=7, column=1, pady=10)
                boton_salir.config(cursor="hand2")
                origen.mainloop()
            else:
                error = Label(frame, text="Digitaste erroneamente el codigo o contraseña")
                error.grid(row=4, column=2, padx=5)
                error.config(fg="red")
                error1 = Label(frame, text="Digitaste erroneamente el codigo o contraseña")
                error1.grid(row=5, column=2, padx=5)
                error1.config(fg="red")

def validar_Funcionario_Interfaz(frame,raiz,opcion,contraseña):
            '''Valida la información del estudiante para poder iniciar sesión del funcionario:

            :param frame: Da un mensaje en caso de ingresar los datos erroneamente
            :type frame: Tkinter
            :param raiz: Destruir la raiz anterior
            :type raiz: Tkinter
            :param opcion: Código del Funcionario
            :type opcion: str
            :param contraseña: Contraseña Del Funcionario
            :type contraseña: str
            :return: None
            :rtype: None
            '''
            lista=Funcionario.validar_Funcionario(opcion,contraseña)
            if lista != 0 and lista!= None:
                destructor(raiz)
                origen=Tk()
                origen.title("Modulo funcionario")
                origen.geometry("650x600")
                frameF = Frame(origen, width="450", height="450")
                frameF.pack()
                Nombre=Label(frameF,text="Bienvenid@ "+lista[0][0]+" "+lista[0][1])
                Nombre.grid(row=1,column=1,pady=10)
                pregunta=Label(frameF,text="¿Que deseas hacer el dia de hoy?")
                pregunta.grid(row=2, column=1,pady=10)
                boton_agregar=Button(frameF,text="Agregar un libro",width=21,command=lambda :registro_Libros(origen,opcion,contraseña))
                boton_agregar.grid(row=4, column=1,pady=10)
                boton_agregar.config(cursor="hand2")
                boton_eliminar = Button(frameF, text="Eliminar un libro",width=21,command= lambda: elimininar_Libro())
                boton_eliminar.grid(row=5, column=1,pady=10)
                boton_eliminar.config(cursor="hand2")
                boton_consultar = Button(frameF, text="consultar libros",width=21,command=lambda :consultar_libros())
                boton_consultar.grid(row=6, column=1,pady=10)
                boton_consultar.config(cursor="hand2")
                boton_actualizar_informacion = Button(frameF, text="actualizar informacion",width=21)
                boton_actualizar_informacion.grid(row=7, column=1,pady=10)
                boton_actualizar_informacion.config(cursor="hand2")
                boton_salir=Button(frameF,text="Salir",width=21)
                boton_salir.grid(row=8, column=1,pady=10)
                boton_salir.config(cursor="hand2",command=lambda :volver_Menu(origen))
                origen.mainloop()
            else :
                error=Label(frame,text="Digitaste erroneamente el codigo o contraseña")
                error.grid(row=4, column=2, padx=5)
                error.config(fg="red")
                error1 = Label(frame, text="Digitaste erroneamente el codigo o contraseña")
                error1.grid(row=5, column=2, padx=5)
                error1.config(fg="red")

def inicio_sesion_Funcionario(raiz):
    '''Interfaz para iniciar sesión del funcionario

    :param raiz: Destruye La Raiz Anterior
    :return: None
    :rtype: None
    '''
    destructor(raiz)
    root = Tk()
    codigo_carac = StringVar()
    contraseña_carac = StringVar()
    root.title("proyecto final poo")
    root.geometry("650x600")
    frame = Frame(root, width="450", height="450")
    frame.pack()
    titulo_validacion = Label(frame, text="validacion de Funcionario ")
    titulo_validacion.grid(row=3, column=1, pady=40)
    lab_codigo = Label(frame, text="ingresa tu codigo")
    lab_codigo.grid(row=4, column=0)
    ingreso_codigo = Entry(frame, textvariable=codigo_carac)
    ingreso_codigo.grid(row=4, column=1)
    lab_contraseña = Label(frame, text="ingresa tu contraseña")
    lab_contraseña.grid(row=5, column=0)
    ingreso_contraseña = Entry(frame, textvariable=contraseña_carac)
    ingreso_contraseña.grid(row=5, column=1)
    ingreso_contraseña.config(show="*")
    Boton_ingreso = Button(frame, text="ingresar",command=lambda: validar_Funcionario_Interfaz(frame,root,codigo_carac.get(), contraseña_carac.get()))
    Boton_ingreso.grid(row=6, column=1, pady=5)
    Boton_ingreso.config(cursor="hand2")
    Boton_salir=Button(frame, text="salir",command=lambda: volver_Menu(root))
    Boton_salir.grid(row=7, column=1, pady=5)
    root.mainloop()

def registro_funcionario(raiz):
        '''Interfaz para el registro de un funcionario

        :param raiz: Destruye la raiz anterior
        :return: None
        :rtype: None
        '''
        destructor(raiz)
        marco = Tk()
        marco.geometry("650x600")
        frameM = Frame(marco, width="450", height="450")
        frameM.pack()
        cargo = Label(frameM, text="indicame el cargo que desempeñas ", font=2)
        cargo.grid(row=0, column=0)
        varcargo = IntVar()
        pregunta_cargo0 = Radiobutton(frameM, text="Jefe de Biblioteca", variable=varcargo, value=0)
        pregunta_cargo0.grid(row=1, column=0, sticky="w")
        pregunta_cargo1 = Radiobutton(frameM, text="Bibliotecario", variable=varcargo, value=1)
        pregunta_cargo1.grid(row=2, column=0, sticky="w")
        pregunta_cargo2 = Radiobutton(frameM, text="secretaria", variable=varcargo, value=2)
        pregunta_cargo2.grid(row=3, column=0, sticky="w")
        genero = Label(frameM, text="indicame tu genero ", font=2)
        genero.grid(row=4, column=0, sticky="w")

        vargenero = IntVar()
        pregunta_genero0 = Radiobutton(frameM, text="Maculino", variable=vargenero, value=0)
        pregunta_genero0.grid(row=5, column=0, sticky="w")
        pregunta_genero1 = Radiobutton(frameM, text="Femenino", variable=vargenero, value=1)
        pregunta_genero1.grid(row=6, column=0, sticky="w")
        pregunta_genero2 = Radiobutton(frameM, text="No especificado", variable=vargenero, value=2)
        pregunta_genero2.grid(row=7, column=0, sticky="w")

        var_codigo = StringVar()
        codigo = Label(frameM, text="indicame tu codigo ", font=2)
        codigo.grid(row=8, column=0, sticky="w")
        preguntacodigoF = Entry(frameM, textvariable=var_codigo)
        preguntacodigoF.grid(row=9, column=0, sticky="w")

        var_nombre = StringVar()
        nombre = Label(frameM, text="indicame tu nombre ", font=2)
        nombre.grid(row=10, column=0, sticky="w")
        preguntanombreF = Entry(frameM, textvariable=var_nombre)
        preguntanombreF.grid(row=11, column=0, sticky="w")

        var_apellido = StringVar()
        nombre = Label(frameM, text="indicame tu apellido ", font=2)
        nombre.grid(row=12, column=0, sticky="w")
        preguntanombreF = Entry(frameM, textvariable=var_apellido)
        preguntanombreF.grid(row=13, column=0, sticky="w")

        var_contraseña = StringVar()
        contraseña = Label(frameM, text="indicame contraseña ", font=2)
        contraseña.grid(row=14, column=0, sticky="w")
        preguntacontraseña = Entry(frameM, textvariable=var_contraseña)
        preguntacontraseña.grid(row=15, column=0, sticky="w")
        boton_Validar = Button(frameM, text="Registrar",command=lambda: registrar_funcionario(frameM,varcargo.get(), vargenero.get(), var_codigo.get(),var_nombre.get(), var_apellido.get(),var_contraseña.get()))
        boton_Validar.grid(row=16, column=0, pady=15)

        def registrar_funcionario(frame,cargo, genero, codigo, nombre, apellido, contraseña):
            cont_name = 0
            cont_last_name = 0
            cont_code = 0
            cont_password = 0
            for i in nombre:
                if i != " " and nombre!= None:
                    cont_name = cont_name + 1
            for i in apellido:
                if i != " "and apellido!= None:
                    cont_last_name = cont_last_name + 1
            for i in codigo:
                if i != " " and codigo != None:
                    cont_code = cont_code + 1
            for i in contraseña:
                    if i != " " and  i != "":
                        cont_password = cont_password + 1
            if cont_name !=0  and cont_last_name !=0  and cont_code !=0  and cont_password !=0 :
                if cont_name == len(nombre) and cont_last_name == len(apellido) and cont_code == len(codigo) and cont_password == len(contraseña):
                    if cargo == 0:
                        variable_cargos = "Jefe de Biblioteca"
                    elif cargo == 1:
                        variable_cargos = "Bibliotecario"
                    elif cargo == 2:
                        variable_cargos = "secretaria"
                    if genero == 0:
                        variable_generos = "Maculino"
                    elif genero == 1:
                        variable_generos = "Femenino"
                    elif genero == 2:
                        variable_generos = "No especificado"
                    Funcionario.almacenamiento_Funcionario(nombre, apellido, codigo, contraseña, variable_cargos, variable_generos)
                    marco.destroy()
                    inicio()
                else:
                    Invalido=Label(frame, text= "No has digitado algun dato valido\n recuerda que no puedes incluir espacios  ")
                    Invalido.grid(row=17, column=0)
            else:
                Invalido = Label(frame,
                                 text="No has digitado algun dato valido\n recuerda que no puedes incluir espacios  ")
                Invalido.grid(row=17, column=0)

def registro_Estudiantes(raiz):
        '''Interfaz para el registro de un estudiante

        :param raiz: Destruye la raiz anterior
        :return: None
        :rtype: None
        '''
        destructor(raiz)
        marco = Tk()
        marco.geometry("650x600")
        frameM = Frame(marco, width="450", height="450")
        frameM.pack()
        cargo = Label(frameM, text="indicame la facultad a la cual perteneces ", font=2)
        cargo.grid(row=0, column=0)

        varfacultad = IntVar()
        pregunta_cargo0 = Radiobutton(frameM, text="ciencias y educacion", variable=varfacultad, value=0)
        pregunta_cargo0.grid(row=1, column=0, sticky="w")
        pregunta_cargo1 = Radiobutton(frameM, text="artes", variable=varfacultad, value=1)
        pregunta_cargo1.grid(row=2, column=0, sticky="w")
        pregunta_cargo2 = Radiobutton(frameM, text="ingenieria", variable=varfacultad, value=2)
        pregunta_cargo2.grid(row=3, column=0, sticky="w")
        genero = Label(frameM, text="indicame tu genero ", font=2)
        genero.grid(row=4, column=0, sticky="w")

        vargenero = IntVar()
        pregunta_genero0 = Radiobutton(frameM, text="Maculino", variable=vargenero, value=0)
        pregunta_genero0.grid(row=5, column=0, sticky="w")
        pregunta_genero1 = Radiobutton(frameM, text="Femenino", variable=vargenero, value=1)
        pregunta_genero1.grid(row=6, column=0, sticky="w")
        pregunta_genero2 = Radiobutton(frameM, text="No especificado", variable=vargenero, value=2)
        pregunta_genero2.grid(row=7, column=0, sticky="w")

        var_codigo = StringVar()
        codigo = Label(frameM, text="indicame tu codigo ", font=2)
        codigo.grid(row=8, column=0, sticky="w")
        preguntacodigoF = Entry(frameM, textvariable=var_codigo)
        preguntacodigoF.grid(row=9, column=0, sticky="w")

        var_nombre = StringVar()
        nombre = Label(frameM, text="indicame tu nombre ", font=2)
        nombre.grid(row=10, column=0, sticky="w")
        preguntanombreF = Entry(frameM, textvariable=var_nombre)
        preguntanombreF.grid(row=11, column=0, sticky="w")

        var_apellido = StringVar()
        nombre = Label(frameM, text="indicame tu apellido ", font=2)
        nombre.grid(row=12, column=0, sticky="w")
        preguntanombreF = Entry(frameM, textvariable=var_apellido)
        preguntanombreF.grid(row=13, column=0, sticky="w")

        var_con = StringVar()
        nombre = Label(frameM, text="indicame tu contraseña ", font=2)
        nombre.grid(row=14, column=0, sticky="w")
        preguntacon = Entry(frameM, textvariable=var_con)
        preguntacon.grid(row=15, column=0, sticky="w")

        boton_Validar = Button(frameM, text="Registrar",
                               command=lambda: registrar_Estudiante(frameM,varfacultad.get(), vargenero.get(),
                                                                    var_codigo.get(), var_con.get(), var_nombre.get(),
                                                                    var_apellido.get()))
        boton_Validar.grid(row=16, column=0, pady=15)

        def registrar_Estudiante(frame,facultad, genero, codigo, contraseña, nombre, apellido):
            cont_name = 0
            cont_last_name = 0
            cont_code = 0
            cont_password = 0
            for i in nombre:
                if i != " " and nombre != None:
                    cont_name = cont_name + 1
            for i in apellido:
                if i != " " and apellido != None:
                    cont_last_name = cont_last_name + 1
            for i in codigo:
                if i != " " and codigo != None:
                    cont_code = cont_code + 1
            for i in contraseña:
                if i != " " and i != "":
                    cont_password = cont_password + 1
            if cont_name != 0 and cont_last_name != 0 and cont_code != 0 and cont_password != 0:
                if cont_name == len(nombre) and cont_last_name == len(apellido) and cont_code == len(codigo) and cont_password == len(contraseña):
                    if facultad == 0:
                        variable_facultad = "ciencias y educacion"
                    elif facultad == 1:
                        variable_facultad = "artes"
                    elif facultad == 2:
                        variable_facultad = "ingenieria"
                    if facultad == 0:
                        variable_generos = "Maculino"
                    elif genero == 1:
                        variable_generos = "Femenino"
                    elif genero == 2:
                        variable_generos = "No especificado"
                    Estudiante.almacenamiento_Estudiantes(nombre, apellido, codigo, contraseña, variable_facultad,variable_generos)
                    marco.destroy()
                    inicio()
                else:
                    Invalido = Label(frame,text="No has digitado algun dato valido\n recuerda que no puedes incluir espacios  ")
                    Invalido.grid(row=17, column=0)
            else:
                Invalido = Label(frame,text="No has digitado algun dato valido\n recuerda que no puedes incluir espacios  ")
                Invalido.grid(row=17, column=0)

def registro_Libros(raiz,opcion,contraseña):
    '''Interfaz para el registro de libros

    :param raiz: Destruye la raiz Anterior
    :type raiz: Tkinter
    :param opcion: Código del Funcionario
    :type opcion: str
    :param contraseña: Contraseña Del Funcionario
    :type contraseña: str
    :return: None
    :rtype: None
    '''
    destructor(raiz)
    marco = Tk()
    marco.geometry("650x600")
    frameM = Frame(marco, width="450", height="450")
    frameM.pack()
    genero = Label(frameM, text="indicame el genero del libro ", font=2)
    genero.grid(row=0, column=0)
    var_genero = IntVar()
    pregunta_genero0 = Radiobutton(frameM, text="Accion", variable=var_genero, value=0)
    pregunta_genero0.grid(row=1, column=0, sticky="w")
    pregunta_genero1 = Radiobutton(frameM, text="Comedia", variable=var_genero, value=1)
    pregunta_genero1.grid(row=2, column=0, sticky="w")
    pregunta_genero2 = Radiobutton(frameM, text="Drama", variable=var_genero, value=2)
    pregunta_genero2.grid(row=3, column=0, sticky="w")

    var_nombre = StringVar()
    nombre = Label(frameM, text="indicame el nombre del libro", font=2)
    nombre.grid(row=10, column=0, sticky="w")
    preguntanombreF = Entry(frameM, textvariable=var_nombre)
    preguntanombreF.grid(row=11, column=0, sticky="w")

    var_autor = StringVar()
    autor = Label(frameM, text="indicame el autor del libro", font=2)
    autor.grid(row=12, column=0, sticky="w")
    pregunta_autor = Entry(frameM, textvariable=var_autor)
    pregunta_autor.grid(row=13, column=0, sticky="w")

    var_codigo = StringVar()
    codigo = Label(frameM, text="indicame el codigo del libro ", font=2)
    codigo.grid(row=14, column=0, sticky="w")
    pregunta_codigo = Entry(frameM, textvariable=var_codigo)
    pregunta_codigo.grid(row=15, column=0, sticky="w")

    boton_Validar = Button(frameM, text="Registrar",command=lambda: registrar_Libro(var_nombre.get(),var_genero.get(),var_autor.get(),var_codigo.get()))
    boton_Validar.grid(row=16, column=0, pady=15)

    def registrar_Libro(nombre,var_genero, autor, codigo):

        if var_genero == 0:
            variable_generos = "accion"
        elif var_genero == 1:
            variable_generos = "comedia"
        elif var_genero == 2:
            variable_generos = "Drama"

        Funcionario.AgregarLibros(nombre,variable_generos, autor, codigo)

        validar_Funcionario_Interfaz(None,marco,opcion,contraseña)

def registrar(raiz):
        '''Interfaz que permite elegir el tipo de usuario

        :param raiz: Destruye la raiz anterior
        :type raiz: Tkinter
        :return:
        '''
        destructor(raiz)
        fuente=Tk()
        fuente.geometry("650x600")
        fuente.title("Registro")
        frameO=Frame(fuente,width="450",height="450")
        frameO.pack()
        tipodep=Label(frameO, text="indicame el tipo de persona")
        tipodep.grid(row=1,column=1,pady=10)
        espacio=Label(frameO,text="")
        espacio.grid(row=2, column=1, pady=10)
        boton_estu=Button(frameO,text="Estudiante ",width=21,command=lambda :registro_Estudiantes(fuente))
        boton_estu.grid(row=3,column=1,pady=10)
        boton_Funcio = Button(frameO, text="Funcionario ", width=21,command= lambda :registro_funcionario(fuente))
        boton_Funcio.grid(row=4, column=1,pady=10)
        boton_salir_menu=Button(frameO, text="Menu Principal ", width=21,command= lambda :volver_Menu(fuente))
        boton_salir_menu.grid(row=5, column=1,pady=10)

def Pedir_Libros(posicion):
    '''Interfaz que permite pedir un libro

    :param posicion: Posición de usuario dentro del fichero
    :type posicion: int
    :return: None
    :rtype: None
    '''
    Pedir = Tk()
    Pedir.title("Modulo Estudiante")
    Pedir.geometry("650x600")
    framePedir = Frame(Pedir, width="450", height="450")
    framePedir.pack()
    Nombre = Label(framePedir, text="Indicame el codigo del libro que deseas solicitar")
    Nombre.grid(row=1, column=1, pady=10)
    Libro2 = StringVar(Pedir)
    pregunta = Entry(framePedir, textvariable=Libro2)
    pregunta.grid(row=2, column=1, pady=10)
    boton_actualizar_informacion = Button(framePedir, text="solicitar", width=21,command=lambda:Pedir_Libros_Proceso(framePedir,posicion,Libro2.get()))
    boton_actualizar_informacion.grid(row=7, column=1)
    boton_actualizar_informacion.config(cursor="hand2")
    boton_salir = Button(framePedir, text="Consultar libro", width=21, command=lambda: consultar_libro_proceso(Libro2.get(),framePedir))
    boton_salir.grid(row=8, column=1)
    boton_salir.config(cursor="hand2")
    boton_salir = Button(framePedir, text="Salir", width=21, command=lambda: destructor(Pedir))
    boton_salir.grid(row=9, column=1, pady=10)
    boton_salir.config(cursor="hand2")
    Pedir.mainloop()

def Pedir_Libros_Proceso(frame,posicion,codigo_Libro):
    '''Toma los datos del libro que se quiere pedir

    :param frame: Da un Mensaje en caso de que el libro se encuentre reservado, no exista o el usuario tenga un libro reservado
    :type frame: Tkinter
    :param posicion: Posición del usuario en el fichero
    :type posicion: int
    :param codigo_Libro: Código Del Libro
    :type codigo_Libro: str
    :return: None
    :rtype: None
    '''
    a=Estudiante.pedir_libro(posicion,codigo_Libro)
    if a==1 :
       reserva_ok=Label(frame,text="¡El libro ha sido reservado exitosamente!")
       reserva_ok.grid(row=2,column=2)
       reserva_ok.config(fg="green")
       del reserva_ok
    elif a==2:
       reservado=Label(frame,text="El libro ya se encuentra reservado")
       reservado.grid(row=2,column=2)
       reservado.config(fg="Red")
       del reservado
    elif a==3:
       no_Existe=Label(frame,text="El libro no existe valida nuevamente")
       no_Existe.grid(row=2,column=2)
       no_Existe.config(fg="Red")
       del no_Existe
    elif a==4:
       sin_Libros = Label(frame, text="No hay libros disponibles en este momento")
       sin_Libros.grid(row=2, column=2)
       sin_Libros.config(fg="Red")
       del sin_Libros
    elif type(a)==str:
       reserva_Activa= Label(frame, text="ya tienes reserva, busca por el codigo: "+a)
       reserva_Activa.grid(row=11, column=1)
       reserva_Activa.config(fg="Red")

def inicio():
    '''Interfaz menú Principal

    :return: None
    :rtype: None
    '''
    raiz=Tk()
    raiz.title("Proyecto Final POO")
    raiz.geometry("650x600")
    frame=Frame(raiz,width="450",height="450")
    frame.pack()
    Bienvenida_Modulo=Label(frame,text="Hola Bienvenido al modulo de la biblioteca")
    Bienvenida_Modulo.grid(row=3,column=1, pady=80)
    Estudiante_Boton=Button(frame,text="ingresar como estudiante",width=21,command=lambda :inicio_sesion_estudiante(raiz))
    Estudiante_Boton.grid(row=4,column=1, pady=10)
    Estudiante_Boton.config(cursor="hand2")
    Funcionario_Boton=Button(frame,text="ingresar como Funcionario",width=21,command=lambda :inicio_sesion_Funcionario(raiz))
    Funcionario_Boton.grid(row=5,column=1, pady=10)
    Funcionario_Boton.config(cursor="hand2")
    Registro_Boton=Button(frame,text="Registrarte",width=21,command=lambda:registrar(raiz))
    Registro_Boton.grid(row=6,column=1, pady=10)
    Registro_Boton.config(cursor="hand2")
    salir=Button(frame,text="salir",width=21,command=lambda:destructor(raiz))
    salir.grid(row=7,column=1, pady=10)
    salir.config(cursor="hand2")
    raiz.mainloop()

def volver_Menu(raiz):
    '''Vuelve al menú principal

    :param raiz: Destruye la raiz anterior
    :return: None
    :rtype: None
    '''
    destructor(raiz)
    inicio()

inicio()
