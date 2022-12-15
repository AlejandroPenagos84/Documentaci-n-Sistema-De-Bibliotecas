class Libro:
  '''La clase Libro define los atributos que va a tener cada libro

  :param nombreLibro: Nombre Del Libro
  :type nombreLibro: str
  :param genero: Género Del Libro
  :type genero: str
  :param autor: Nombre Del Autor
  :type autor: str
  :param codigo: Código del libro
  :type codigo: str
  '''
  def __init__(self, nombreLibro,genero, autor,codigo):
    self.nombreLibro = nombreLibro
    self.autor = autor
    self.estado = "Disponible"
    self.codigo=codigo
    self.genero=genero

class persona:
  '''Representa una persona

  :param nombre: Nombre De La Persona
  :type nombre: str
  :param apellido: Apellido De La Persona
  :type apellido: str
  :param codigo: Código De La Persona
  :type codigo: str
  '''
  def __init__(self, nombre, apellido, codigo):
    self.nombre = nombre
    self.apellido = apellido
    self.codigo = codigo

  def ConsultarLibro(libro):
    '''Consulta si está registrado un libro

    :param libro: Es el parametro con el cual se busca el libro. Puede ser nombre, autor, género, o código
    :type libro: str
    :return: Lista De Libros
    :rtype: list
    '''
    libro.lower()
    print(libro)
    a=open("objetos_Libros","a")
    a.close()
    a=open("objetos_Libros","r")
    b=a.readlines()
    a.close()
    texto_Final=""
    lista=[]
    lista_libros=[]
    t=0
    contador=2
    if t == len(b):
        return 0
    if libro != None and len(libro)!=0:
        if len(b)!=0:
          if len(b)!=0:
            for i in range(len(b)):
              for x in b[i]:
                #print("linea 40 consultar prueba", i)
                if x!="\n":
                  if x != ",":
                    texto_Final=texto_Final+x
                  elif x==",":
                    lista.append(texto_Final)
                    texto_Final=""
                if x=="\n":
                  lista.append(texto_Final)
                  texto_Final = ""
                  if lista.count(libro)>=1:
                      lista_libros.append(lista)
                  else:
                    t=t+1
                  lista=[]
        else:
            lista_libros=0
            return lista_libros
    else:
        lista_libros=0
        return lista_libros
    return lista_libros

class Funcionario(persona):
  '''Representa un Funcionario, la persona encargada de administrar el inventario de libros
  
  :param nombre: Nombre de la Persona
  :type nombre: str
  :param apellido: Apellido de la persona
  :type apellido: str
  :param codigo: Codigo de la persona
  :type codigo: str
  :param contraseña: Contraseña que usará el funcionario para iniciar sesión
  :type contraseña: str
  :param cargo: Cargo del Funcionario
  :type cargo: str
  :param genero: Género del Funcionario
  :type genero: str
  '''
  def __init__(self, nombre, apellido, codigo,contraseña,cargo,genero):
    
    super().__init__(nombre, apellido, codigo)
    self._cargo = cargo
    self._genero = genero
    self._contraseña = contraseña

  def almacenamiento_Funcionario(nombre, apellido, codigo,contraseña,cargo,genero):
    '''Almacenamiento del Funcionario en el archivos "objetos_Funcionario"

    :param nombre: Nombre del Funcionario
    :type nombre: str
    :param apellido: Apellido Del Funcionario
    :type apellido: str
    :param codigo: Código Del Funcionario
    :type codigo: str
    :param contraseña: Contraseña para iniciar sesión
    :type contraseña: str
    :param cargo: Cargo del Funcionario
    :type cargo: str
    :param genero: Género del Funcionario (Masculino, Femenino, No Especificado)
    :type genero: str
    :return: Guarda al Funcionario en el archivo "objetos_Funcionario"
    :rtype: None
    '''
    cont_name = 0
    cont_last_name =0
    cont_code = 0
    cont_password =0
    for i in nombre:
        if i!=" ":
            cont_name=cont_name+1
    for i in apellido:
        if i!=" ":
            cont_last_name=cont_last_name+1
    for i in codigo:
        if i!=" " and i!= None:
            cont_code=cont_code+1
    for i in contraseña:
        if i!=" ":
            cont_password=cont_password+1
    if cont_name==len(nombre)and cont_last_name==len(apellido) and cont_code==len(codigo) and cont_password==len(contraseña):
        lista_objetos = open("objetos_Funcionario", "a")
        personF = Funcionario(nombre, apellido, codigo,contraseña,cargo,genero)
        lista_objetos.write(personF.nombre + "," +personF.apellido + "," +personF.codigo +","+personF._contraseña+","+ personF._cargo+","+personF._genero+"\n")
        lista_objetos.close()

  def AgregarLibros(nombre,genero,autor,codigo):
    '''Guardar Libros en el archivo "objetos_Libros"

    :param nombre: Nombre Del Libro
    :type nombre: str
    :param genero: Genenero Del Libro
    :type genero: str
    :param autor: Autor Del Libro
    :type autor: str
    :param codigo: Código Del Libro
    :type codigo: str
    :return: Guarda el libro con sus respectivos datos en el archivo "objetos_Libros"
    '''
    lista_libros = open("objetos_Libros", "a")
    libroAgregar = Libro(nombre.lower(),genero.lower(),autor.lower(),codigo.lower())
    lista_libros.write(libroAgregar.nombreLibro + "," +libroAgregar.genero + "," + libroAgregar.autor +","+libroAgregar.estado + ","+libroAgregar.codigo+"\n")
    lista_libros.close()


  def validar_Funcionario(opcion,contraseña):
      '''Valida si el usuario se encuentra en el archivo "objetos_Funcionario"

      :param opcion: Código Del Funcionario
      :param contraseña: Contraseña del Funcionario
      :return: None
      :rtype: None
      '''
      a = open("objetos_Funcionario", "a")
      a.close()
      a = open("objetos_Funcionario", "r")
      b = a.readlines()
      a.close()
      texto_Final = ""
      lista = []
      t = 0
      if len(b) != 0:
        for i in range(len(b)):
            for x in b[i]:
                if x != "\n":
                    if x != ",":
                        texto_Final = texto_Final + x
                    elif x == ",":
                              lista.append(texto_Final)
                              texto_Final = ""
                if x == "\n":
                    lista.append(texto_Final)
                    texto_Final = ""
                    if lista.count(opcion)!=0:
                        if lista[2] == opcion :
                            if lista[3]==contraseña:
                                return lista,i
                            else:
                                return 0
                        else:
                            t = t + 1
                    lista = []
                if t == len(b):
                        return 0
      else:
          return 0

  def EliminarLibros(codigo):
      '''Elimina el Libro del Archivo "objetos_Libros"

      :param codigo: Codigo del Libro que será eliminado
      :type codigo: str
      :return: None
      '''
      opcion = codigo
      a=open("objetos_Libros","a")
      a.close()
      a=open("objetos_Libros","r")
      b=a.readlines()
      a.close()
      a=open("objetos_Libros","r")
      c=a.readlines()
      a.close()
      temp=[]
      texto_Final=""
      lista=[]
      t=0
      lista2=[]
      if len(b)!=0 and t!=len(b):
        if len(b)!=0:
          for i in range(len(b)):
            for x in b[i]:
              if x!="\n":
                if x != ",":
                  texto_Final=texto_Final+x
                elif x==",":
                  lista.append(texto_Final)
                  texto_Final=""
              if x=="\n":
                lista.append(texto_Final)
                texto_Final = ""
                if lista[4]==opcion:
                  lista2.append(lista)
                  temp.append(i)
                else:
                  t=t+1
                lista=[]
      else:
        return 0
      if len(temp)!=0:
        archivo_Final=open("objetos_Libros","w")
        archivo_Final.close()
        archivo_Final=open("objetos_Libros","a")
        for i in temp:
          c[i]=""
        for i in range(len(c)):
          if c[i]!="":
            archivo_Final.write(c[i])
        archivo_Final.close()
        return lista2

class Estudiante(persona):
  '''Representa al estudiante

  :param nombre: Nombre Del Estudiante
  :type nombre: str
  :param apellido: Apellido Del Estudiante
  :type apellido: str
  :param codigo: Código Del Estudiante
  :type codigo: str
  :param contraseña: Contraseña para iniciar sesión del Estudiante
  :type contraseña: str
  :param facultad: Facultad a la que pertenece el estudiante
  :type facultad: str
  :param genero: Género Del Estudiante
  :type genero: str
  '''
  def __init__(self, nombre, apellido, codigo,contraseña,facultad,genero):

    super().__init__(nombre, apellido, codigo)
    self.facultad = facultad
    self.genero= genero
    self._contraseña= contraseña
    self.reserva= " "

  def almacenamiento_Estudiantes(nombre,apellido,codigo,contraseña,facultad,genero):
    '''Almacena Estudiantes en el archivo "objetos_Estudiantes"

    :param nombre: Nombre Del Estudiante
    :type nombre: str
    :param apellido: Apellido Del Estudiante
    :type apellido: str
    :param codigo: Código Del Estudiante
    :type codigo: str
    :param contraseña: Contraseña para iniciar sesión del Estudiante
    :type contraseña: str
    :param facultad: Facultad a la que pertenece el estudiante
    :type facultad: str
    :param genero: Género Del Estudiante
    :type genero: str
    :return: None
    '''
    lista_objetos = open("objetos_Estudiantes", "a")
    personE = Estudiante(nombre,apellido,codigo,contraseña,facultad,genero)
    lista_objetos.write(personE.nombre + "," + personE.apellido + "," + personE.codigo +"," + personE._contraseña +","+ personE.facultad + ","+ personE.genero +","+personE.reserva+"\n")
    lista_objetos.close()

  def pedir_libro(posicion,codigo_Libro):
      '''Le permite al usuario pedir un libro, cambiando su estado de "Disponible" a "Reservado"

      :param posicion: Posición del Usuario En El Fichero
      :type posicion: int
      :param codigo_Libro: Código del Libro
      :type codigo_Libro: str
      :return: Pedir Libro
      :rtype: bool
      '''
      f=int(posicion)
      a=open("objetos_Estudiantes","a")
      a.close()
      a=open("objetos_Estudiantes","r")
      b=a.readlines()
      a.close()
      texto_Final=""
      lista=[]
      for i in b[f]:
        if i!=",":
          texto_Final=texto_Final+i
        if i==",":
          lista.append(texto_Final)
          texto_Final=""
        if i=="\n":
          lista.append(texto_Final)
          texto_Final=""
      if lista[6]==""+"\n":
            l=open("objetos_Libros","a")
            l.close()
            l=open("objetos_Libros","r")
            ñ=l.readlines()
            l.close()
            lista_Libros=[]
            temp=[]
            contador1=0
            w=""
            if len(ñ)!=0:
                for i in range(len(ñ)):
                  for x in ñ[i]:
                    if x!="\n":
                      if x != ",":
                        w= w+ x
                      elif x==",":
                        lista_Libros.append(w)
                        w=""
                    if x=="\n":
                      lista_Libros.append(w)
                      w = ""
                      if lista_Libros.count(codigo_Libro)>=1:
                        temp.append(int(i))
                        contador1+=1
                      lista_Libros=[]

                if contador1>0:
                  lista_Libros_c=[]
                  textoFinal_Libros=""
                  textoFinal=""
                  for per in temp:
                    for x in ñ[per]:
                      if x!=",":
                          textoFinal_Libros= textoFinal_Libros+x
                      if x==",":
                          lista_Libros_c.append(textoFinal_Libros)
                          textoFinal_Libros=""
                      if x=="\n":
                          lista_Libros_c.append(textoFinal_Libros)
                          textoFinal_Libros=""
                    if  lista_Libros_c[3]!="Reservado":
                      if lista_Libros_c[4]==codigo_Libro+"\n":
                          lista_Libros_c[3]= "Reservado"
                          cont=1
                          for i in lista_Libros_c:
                            if cont!=len(lista_Libros_c):
                              textoFinal=textoFinal+i+","
                            if cont==len(lista_Libros_c):
                              textoFinal=textoFinal+i
                            cont=cont+1                        
                          ñ[per]=textoFinal
                          a=open("objetos_Libros","w")
                          a.close()    
                          a=open("objetos_Libros","a")
                          for i in ñ:
                            a.write(i)
                          a.close()              
                          lista[6]=codigo_Libro+"\n"
                          cont=1
                          textoFi=""
                          for i in lista:
                            if cont!=len(lista):
                              textoFi=textoFi+i+","
                            if cont==len(lista):
                              textoFi=textoFi+i
                            cont=cont+1  
                          b[f]=textoFi
                          a=open("objetos_Estudiantes","w")
                          a.close()    
                          a=open("objetos_Estudiantes","a")
                          for i in b:
                            a.write(i)
                          a.close()
                          return 1
                      else:                    
                        lista_Libros_c=[]
                    else:
                      return 2
                elif contador1==0:
                  return 3
            else:
              return 4
      else:
        return lista[6]


  def validar_Estudiante(opcion,contraseña):
      '''Valida si un estudiante se encuentra registrado en el momento de iniciar sesión

      :param opcion: Código del Estudiante
      :param contraseña: Contraseña del Usuario Para Iniciar Sesión
      :type contraseña: str
      :return: None
      :rtype: None
      '''
      a=open("objetos_Estudiantes","a")
      a.close()
      a=open("objetos_Estudiantes","r")
      b=a.readlines()
      a.close()
      texto_Final=""
      lista=[]
      t=1

      if len(b) != 0:
          for i in range(len(b)):
              for x in b[i]:
                  if x != "\n":
                      if x != ",":
                          texto_Final = texto_Final + x
                      elif x == ",":
                          lista.append(texto_Final)
                          texto_Final = ""
                  if x == "\n":
                      lista.append(texto_Final)
                      #print(lista, "prueba linea 364 modulos_proyecto, aceptar usuario")
                      texto_Final = ""
                      if lista.count(opcion) != 0:
                          #print(lista, "prueba linea 367 modulos_proyecto, aceptar usuario")
                          if lista[2] == opcion:
                              #print(lista, "prueba linea 388 modulos_proyecto, aceptar usuario")
                              if lista[3] == contraseña:
                                  return lista,i
                              else:
                                  return 0
                          else:
                              t = t + 1
                      lista = []
                  if t == len(b):
                      #print(lista, "prueba linea 380 modulos_proyecto, aceptar usuario")
                      return 0
      else:
          print(lista)
          return 0

  def devolver_libro(posicion):
      '''Devolver el libro que tenga reservado el usuariow

      :param posicion: Posición del Usuario en el fichero
      :type posicion: int
      :return: Devuelve el libro
      :rtype: bool
      '''
      a=open("objetos_Estudiantes","a")
      a.close()
      a=open("objetos_Estudiantes","r")
      b=a.readlines()
      a.close()
      texto_Final=""
      lista=[]
      for i in b[posicion]:
        if i!=",":
          texto_Final=texto_Final+i
        if i==",":
          lista.append(texto_Final)
          texto_Final=""
        if i=="\n":
          lista.append(texto_Final)
          texto_Final=""
      if lista[5]!="\n" :
            opcion = lista[6]
            l=open("objetos_Libros","a")
            l.close()
            l=open("objetos_Libros","r")
            ñ=l.readlines()
            l.close()
            lista_Libros=[]
            temp=[]
            w=""
            if len(ñ)!=0:
                for i in range(len(ñ)):
                  for x in ñ[i]:
                    if x!="\n":
                      if x != ",":
                        w= w+ x
                      elif x==",":
                        lista_Libros.append(w)
                        w=""
                    if x=="\n":
                      lista_Libros.append(w)
                      w = ""
                      if lista_Libros[4]+"\n"==opcion:
                          temp.append(int(i))
                      lista_Libros=[]
                codigo_Libro=lista[6]
                lista_Libros_c=[]
                textoFinal_Libros=""
                textoFinal=""
                for per in temp:
                  for x in ñ[per]:
                    if x!=",":
                        textoFinal_Libros= textoFinal_Libros+x
                    if x==",":
                        lista_Libros_c.append(textoFinal_Libros)
                        textoFinal_Libros=""
                    if x=="\n":
                        lista_Libros_c.append(textoFinal_Libros)
                        textoFinal_Libros=""
                  if lista_Libros_c[4]==codigo_Libro:
                      lista_Libros_c[3]= "Disponible"
                      cont=1
                      for i in lista_Libros_c:
                        if cont!=len(lista_Libros_c):
                          textoFinal=textoFinal+i+","
                        if cont==len(lista_Libros_c):
                          textoFinal=textoFinal+i
                        cont=cont+1
                      ñ[per]=textoFinal
                      a=open("objetos_Libros","w")
                      a.close()
                      a=open("objetos_Libros","a")
                      for i in ñ:
                        a.write(i)
                      a.close()
                      lista[6]="\n"
                      cont=1
                      textoFi=""
                      for i in lista:
                        if cont!=len(lista):
                          textoFi=textoFi+i+","
                        if cont==len(lista):
                          textoFi=textoFi+i
                        cont=cont+1
                      b[posicion]=textoFi
                      a=open("objetos_Estudiantes","w")
                      a.close()
                      a=open("objetos_Estudiantes","a")
                      for i in b:
                        a.write(i)
                      a.close()
                      return 3
            else:
              return  0
      else:
        return 1
