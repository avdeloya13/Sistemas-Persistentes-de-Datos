import csv

"""
Fundamentos de Bases de Datos
Práctica 1
Alumna: Ana Valeria Deloya Andrade
"""

def lectura(archivo):
  """Realiza la lectura e impresion de archivos csv"""
  
  with open(archivo,mode = 'r') as csv_file:
      reader = csv.reader(csv_file)
      contador = 0
  
      for row in reader:
          contador = contador + 1
          print(row)
          if contador > 30:
              break


def agregar_productos(producto):
  """Agrega nuevos productos al archivo csv"""
  
  with open('inventario.csv',mode = 'a') as csv_file:
      writer = csv.writer(csv_file)

      writer.writerow(producto)
  print('\n------------------------------------------------')
  lectura('inventario.csv')
  print('------------------------------------------------\n')


def crea_productos(id,nombre,categoria,precio,existencia):
  """Crea los productos para despues agregarlos al inventario"""
  
  if id.isnumeric() == False:  
    print('\n***Id no valido***\n')
    return
  
  if nombre.isnumeric():
    print('\n***Nombre no valido***\n')
    return

  if categoria.isnumeric():
    print('\n***Categoria no valida***\n')
    return
    
  if precio.isnumeric() == False:   
    print('\n***Precio no valido***\n')
    return

  if existencia.isnumeric() == False:  
    print('\n***Cantidad no valida***\n')
    return


  nuevo = [id, nombre,categoria,precio,existencia]
  agregar_productos(nuevo)


def busqueda_cadenas(dato,indice):
  """Busqueda de productos por: nombre, categoria"""

  contador = 0
  if dato.isnumeric() == False:
    with open('inventario.csv','r') as file:
      csv_file = csv.reader(file)
      for row in csv_file:
        if dato == row[indice]:
          contador = contador +1
          print(row)
  else:
    print('\n***Dato no valido***\n')

  if contador == 0:
    print('\n***Producto no encontrado***\n')


def busqueda_numeros(dato,indice):
  """Busqueda de productos por: id, precio, cant. en existencia"""
  
  contador = 0
  if dato.isnumeric():
    with open('inventario.csv','r') as file:
      csv_file = csv.reader(file)
      for row in csv_file:
        if dato == row[indice]:
          contador = contador + 1
          print(row) 
  else:
    print('\n***Dato no valido***\n')

  if contador == 0:
    print('\n***Producto no encontrado***\n')


def repetidos(dato,indice):
  """Auxiliar que verifica que no se repitan datos, recibe el dato 
  y el indice de acuerdo a su posicion: 0 para id, 1 nombre, 2       categoria, 3 precio, 4 cant. en existencia"""
  
  with open('inventario.csv',mode = 'r') as file:
    reader = csv.reader(file)
    
    for row in reader:
        if row[indice] == dato:
          return True
    return False
  

def modifica(indice,id,archivo,new):
  """Modifica el inventario, recibe un indice de acuerdo a la     
  posicion: 0 id, 1 nombre, 2 categoria, 3 precio, 4 cant. en   
  existencia
  Tambien recibe el id del archivo a modificar, el archivo csv y     el nuevo dato
  """
  
  with open(archivo,mode = 'r') as file:
    reader = csv.reader(file)
    l = []
    encontrado = False
    
    for row in reader:
      if row[0] == id:
        encontrado=True
       
        if indice == 1 or indice == 0:
          rep = repetidos(new,indice)
          if rep:
            print('\n**El nuevo dato ya existia en inventario**\n')
            return  
             
        row[indice] = new
      l.append(row)
    file.close()
        
    if encontrado == False:
      print('\n***Dato no encontrado***\n')    
    else:
      print('\n------------------------------------------------')
      file = open(archivo,'w+',newline='')
      writer = csv.writer(file)
      writer.writerows(l)
      file.seek(0)
      reader = csv.reader(file)
      for row in reader:
        print(row)
      file.close()
      print('------------------------------------------------\n')


def elimina(id):
  """Elimina productos"""
  
  with open('inventario.csv',mode = 'r') as file:
    reader = csv.reader(file)
    l = []
    
    encontrado = False
    
    for row in reader:
      if row[0] == id:
        encontrado = True
      else:
          l.append(row)
      
    file.close()
        
    if encontrado == False:
      print('\n***Producto no encontrado***\n')    
      
    else:
      print('\n------------------------------------------------')
      file = open('inventario.csv','w+',newline='')
      writer = csv.writer(file)
      writer.writerows(l)
      file.seek(0)
      reader = csv.reader(file)
      for row in reader:
        print(row)
      file.close()
      print('------------------------------------------------\n')


def elimina_ventas_totales():
  """Elimina ventas totales del archivo: ventas_totales.csv"""
  
  with open('ventas_totales.csv',mode = 'r') as file:
    reader = csv.reader(file)
    l = []
    dia=str(input('\n**Escribe el dia de la venta a eliminar**\n'))
    mes=str(input('\n**Escribe el mes de la venta a eliminar**\n'))
    a=str(input('\n**Escribe el anio de la venta a eliminar**\n'))
    encontrado = False
    
    for row in reader:
      if row[0] == dia and row[1] == mes and a == row[2]:
        encontrado = True
      else:
          l.append(row)
      
    file.close()
        
    if encontrado == False:
      print('\n***Producto no encontrado***\n')    
      
    else:
      print('\n------------------------------------------------')
      file = open('ventas_totales.csv','w+',newline='')
      writer = csv.writer(file)
      writer.writerows(l)
      file.seek(0)
      reader = csv.reader(file)
      for row in reader:
        print(row)
      file.close()
      print('------------------------------------------------\n')


def modifica_ventas(indice,dato,archivo):
  """Modifica las ventas, recibe un indice de acuerdo a la     
  posicion: 0 dia, 1 mes, 2 anio, 3 total
  Tambien recibe el dato a modificar y el archivo csv
  """
  
  with open(archivo,mode = 'r') as file:
    reader = csv.reader(file)
    l = []
    encontrado = False
    
    for row in reader:
      if row[indice] == dato:
        encontrado=True
        n = input('Escribe el nuevo dato: ')
        new = n.lower()
             
        row[indice] = new
      l.append(row)
    file.close()
        
    if encontrado == False:
      print('\n***Dato no encontrado***\n')    
    else:
      print('\n------------------------------------------------')
      file = open(archivo,'w+',newline='')
      writer = csv.writer(file)
      writer.writerows(l)
      file.seek(0)
      reader = csv.reader(file)
      for row in reader:
        print(row)
      file.close()
      print('------------------------------------------------\n')


def ventas_del_dia():
  """Registra ventas del dia"""

  with open('inventario.csv',mode = 'r') as file:
    reader = csv.reader(file)
    
    id= str(input('\n**Escribe el id del producto a comprar**\n'))
    encontrado = False
    precio = 0
    
    for row in reader:
      if row[0] == id:
        encontrado = True
        precio = row[3]
        
    file.close()
        
    if encontrado == False:
      print('\n***Producto no encontrado***\n') 
      return

    reduce_existencia(id)
    
    venta = [id,precio]
    
    with open('ventas.csv',mode = 'a') as csv_file:
      writer = csv.writer(csv_file)
      writer.writerow(venta)


def reduce_existencia(id):
  """Reduce cantidad en existencia de un producto y lo elimina si llega a 0 la cantidad en existencia"""

  with open('inventario.csv', mode = 'r') as file:
    reader = csv.reader(file)
    nuevo = 0

    for row in reader:
        if row[0] == id:
          nuevo = nuevo + (int(row[4]) - 1)
          modifica(4,id,'inventario.csv',nuevo)
          if nuevo == 0:
            #si el producto llega a 0 cant. en exist. ,se elimina
            print('\n***Inventario actualizado sin la compra reciente: \n')
            elimina(id)

    file.close()


def venta_total(fecha):
  """Registra y muestra las ventas totales del dia"""

  with open('ventas.csv', mode = 'r') as file:
    reader = csv.reader(file)
    total = 0
    dia, mes, anio = map(int, fecha.split("/"))
    
    for row in reader:
        if row[1].isnumeric():
          total = total + int(row[1])

    file.close()
    print('\n***VENTA TOTAL DEL DIA:')
    print(total)
    venta = [dia,mes,anio,total]
    with open('ventas_totales.csv',mode = 'a') as csv_file:
      writer = csv.writer(csv_file)
      writer.writerow(venta)
      
  elimina_ventas()
  
  print('\n------------------------------------------------')
  lectura('ventas_totales.csv')
  print('------------------------------------------------\n')


def elimina_ventas():
  """Elimina ventas al finalizar el dia"""
   
  with open('ventas.csv',mode = 'r') as file:
    reader = csv.reader(file)
    l = []
    c = ''
    
    for row in reader:
      if (row[0].isnumeric()) == False:
          l.append(row)
      
    file.close()
  
  file = open('ventas.csv','w+',newline='')
  writer = csv.writer(file)
  writer.writerows(l)
  writer.writerows(c)
  file.seek(0)
  file.close()


try:
  def main():
    """Menu con opciones para el usuario"""
    
    print('MENU DE INICIO:')
    print('1 Para ver el inventario')
    print('2 Para agregar productos')
    print('3 Para buscar productos')
    print('4 Para modificar el inventario')
    print('5 Para eliminar un producto')
    print('6 Para registrar una compra')
    print('7 Para ver las ventas totales del dia')
    print('8 Para modificar ventas')
    print('9 Para eliminar ventas')
    print('10 Para salir')
    print('*******************************************')
    src=int(input('Selecciona una opcion: '))

    if src == 1:
      #Ver inventario
      print('\n------------------------------------------------')
      lectura('inventario.csv')
      print('------------------------------------------------\n')
      main()

    if src == 2:
      #Agregar productos
    
      id =str(input('Escribe el id del producto: '))
      rep = repetidos(id,0)
      if rep:
        print('\n**No se pudo completar agregar productos**\n')
        print('\n**El id ya existia en el inventario**\n')
        return  
    
      new1 =str(input('Escribe el nombre del producto: '))
      nombre = new1.lower()
      rept = repetidos(nombre,1)
      if rept:
        print('\n**No se pudo completar agregar productos**\n')
        print('\n**El nombre ya existia en el inventario**\n')
        return  
 
      new2=str(input('Escribe la categoria: '))
      cat = new2.lower()
    
      precio=str(input('Escribe el precio: '))
    
      exist=str(input('Escribe la cantidad en existencia: '))
    
      crea_productos(id,nombre,cat,precio,exist)
      main()

    if src == 3:
      #Buscar productos
      print('1 Busqueda por id')
      print('2 Busqueda por nombre')
      print('3 Busqueda por categoria')
      print('4 Busqueda por precio')
      print('5 Busqueda por cantidad en existencia')
      print('*******************************************')
      src3=int(input('Selecciona una opcion: '))
      if src3 == 1:
        id = input('Escribe el id: ')
        print('\n')
        busqueda_numeros(id,0)
        print('\n')
        main()
      
      if src3 == 2:
        n = str(input('Escribe el nombre del producto: '))
        nombre = n.lower()
        print('\n')
        busqueda_cadenas(nombre,1)
        print('\n')
        main()
      
      if src3 == 3:
        c = str(input('Escribe la categoria: '))
        categoria = c.lower()
        print('\n')
        busqueda_cadenas(categoria,2)
        print('\n')
        main()
      
      if src3 == 4:
        precio = input('Escribe el precio: ')
        print('\n')
        busqueda_numeros(precio,3)
        print('\n')
        main()
      
      if src3 == 5:
        cantidad = input('Escribe la cantidad: ')
        print('\n')
        busqueda_numeros(cantidad,4)
        print('\n')
        main()

    if src == 4:
      #Modificar inventario
      print('1 Modificar id')
      print('2 Modificar nombre')
      print('3 Modificar categoria')
      print('4 Modificar precio')
      print('5 Modificar cantidad en existencia')
      print('*******************************************')
      modif = int(input('Selecciona una opcion: '))
      if modif == 1:
        print('\n------------------------------------------------')
        lectura('inventario.csv')
        print('------------------------------------------------\n')
        id = str(input('Escribe el id del dato a modificar: '))
        n = input('Escribe el nuevo dato: ')
        new = n.lower()
        modifica(0,id,'inventario.csv',new)
        main()
      
      if modif == 2:
        print('\n------------------------------------------------')
        lectura('inventario.csv')
        print('------------------------------------------------\n')
        id = str(input('Escribe el id del dato a modificar: '))
        n = input('Escribe el nuevo dato: ')
        new = n.lower()
        modifica(1,id,'inventario.csv',new)
        main()
      
      if modif == 3:
        print('\n------------------------------------------------')
        lectura('inventario.csv')
        print('------------------------------------------------\n')
        id = str(input('Escribe el id del dato a modificar: '))
        n = input('Escribe el nuevo dato: ')
        new = n.lower()
        modifica(2,id,'inventario.csv',new)
        main()
      
      if modif == 4:
        print('\n------------------------------------------------')
        lectura('inventario.csv')
        print('------------------------------------------------\n')
        id = str(input('Escribe el id del dato a modificar: '))
        n = input('Escribe el nuevo dato: ')
        new = n.lower()
        modifica(3,id,'inventario.csv',new)
        main()
      
      if modif == 5:
        print('\n------------------------------------------------')
        lectura('inventario.csv')
        print('------------------------------------------------\n')
        id = str(input('Escribe el id del dato a modificar: '))
        n = input('Escribe el nuevo dato: ')
        new = n.lower()
        modifica(4,id,'inventario.csv',new)
        main()
    
    if src == 5:
      #Eliminar producto
      print('\n------------------------------------------------')
      lectura('inventario.csv')
      print('------------------------------------------------\n')
      id= str(input('\n**Escribe el id del producto a eliminar**\n'))
      elimina(id)
      main()

    if src == 6:
      #Registrar compra
      print('\n------------------------------------------------')
      lectura('inventario.csv')
      print('------------------------------------------------\n')
      ventas_del_dia()
      print('\n')
      main()

    if src == 7:
      #Ventas totales
      fecha = input('Escribe la fecha en el formato dd/mm/aaaa: ')
      venta_total(fecha)
      main()

    if src == 8:
      #Modificar ventas
      print('1 Modificar dia')
      print('2 Modificar mes')
      print('3 Modificar anio')
      print('4 Modificar total vendido')
      print('*******************************************')
      modif = int(input('Selecciona una opcion: '))
      if modif == 1:
        print('\n------------------------------------------------')
        lectura('ventas_totales.csv')
        print('------------------------------------------------\n')
        d = str(input('Escribe el dia a modificar: '))
        modifica_ventas(0,d,'ventas_totales.csv')
        main()

      if modif == 2:
        print('\n------------------------------------------------')
        lectura('ventas_totales.csv')
        print('------------------------------------------------\n')
        m = str(input('Escribe el mes a modificar: '))
        modifica_ventas(1,m,'ventas_totales.csv')
        main()

      if modif == 3:
        print('\n------------------------------------------------')
        lectura('ventas_totales.csv')
        print('------------------------------------------------\n')
        a = str(input('Escribe el anio a modificar: '))
        modifica_ventas(2,a,'ventas_totales.csv')
        main()

      if modif == 4:
        print('\n------------------------------------------------')
        lectura('ventas_totales.csv')
        print('------------------------------------------------\n')
        t = str(input('Escribe el total vendido a modificar: '))
        modifica_ventas(3,t,'ventas_totales.csv')
        main()

    if src == 9:
      #Eliminar ventas
      print('\n------------------------------------------------')
      lectura('ventas_totales.csv')
      print('------------------------------------------------\n')
      elimina_ventas_totales()
      main()

    if src == 10:
      #Salir
      quit()
    
    if src >= 11:
      print('\n***Opcion no valida***\n')
      main()


  main()
  
except KeyboardInterrupt:
    print('\n*** Saliste del programa ***')
except SystemExit:
    print('\n*** Saliste del programa ***')
except ValueError:
    print('\n*** Valor no valido ***\n')
    main()