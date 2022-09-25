
from tkinter import ttk
from tkinter import *

import sqlite3





class Product:
    # connection dir property
    db_name = 'databaseyenny.db'

    def __init__(self, window):

        # Inicializar las ventanas
        self.wind = window
        self.wind.title('DATA BASE YENNY ')


#------------------proveedor----------------------------------
        # Crear el contenido  
        frame = LabelFrame(self.wind, text = 'Registrar un nuevo proveedor')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 10)

        # ID proveedor
        Label(frame, text = 'ID proveedor: ').grid(row = 1, column = 0)
        self.ID_proveedor = Entry(frame)
        self.ID_proveedor.focus()# para que el cursor se posicione en donde queramos en este caso en la cajita del nombre 
        self.ID_proveedor.grid(row = 1, column = 1)

         # Nombre proveedor  
        Label(frame, text = 'Nombre del proveedor: ').grid(row = 2, column = 0)
        self.nameprovedor = Entry(frame)
        self.nameprovedor.grid(row = 2, column = 1)

        #direccion proveedor 
        Label(frame, text = 'Direccion del Proveedor: ').grid(row = 3, column = 0)
        self.direccion = Entry(frame)
        self.direccion.grid(row = 3, column = 1)

         # Button agregar provedor 
        ttk.Button(frame, text = 'Guardar Proveedor',command = self.add_proveedor ).grid(row = 5, columnspan = 2) # w y e es para llenar el ancho de la caja de este a oeste

        #mensaje 
        self.message = Label(text = '', fg= 'pink')
        self.message.grid (row = 3, column = 0, columnspan = 2, sticky= W +E)

        #Tabla proveedores
        self.tree = ttk.Treeview(height=15,columns=('#0','#1'))
        self.tree.grid(row = 5,column = 0, columnspan=2)
        self.tree.heading('#0', text = 'ID proveedor',anchor = CENTER)
        self.tree.heading('#1',text = 'Nombre del proveedor', anchor = CENTER )
        self.tree.heading('#2',text = 'Direccion del proveedor ', anchor = CENTER )

        self.get_proveedores()



         #boton borrar 
        ttk.Button(text='BORRAR', command = self.borrar_proveedor ).grid(row = 16,column = 0,sticky=W+E )






        ttk.Button(text='ACTUALIZAR').grid(row = 16,column = 1,sticky=W+E )



#---------------------Crear el contenido del producto---------------------------------------- 
        
        frame = LabelFrame(self.wind, text = 'Registrar un nuevo producto')
        frame.grid(row = 0, column = 7, columnspan = 3, pady = 20)

         # Nombre producto 
        Label(frame, text = 'Nombre del producto: ').grid(row = 1, column = 0)
        self.nombreproducto = Entry(frame)
        self.nombreproducto.grid(row = 1, column = 1)

        #Id producto 
        Label(frame, text = 'ID Producto: ').grid(row = 2, column = 0)
        self.ID_producto = Entry(frame)
        self.ID_producto.grid(row = 2, column = 1)

        #Id proveedor
        Label(frame, text = 'ID Proveedor: ').grid(row = 3, column = 0)
        self.id_proveedor1 = Entry(frame)
        self.id_proveedor1.grid(row = 3, column = 1)

        #Descripcion 
        Label(frame, text = 'Descripcion: ').grid(row = 4, column = 0)
        self.descripcion = Entry(frame)
        self.descripcion.grid(row = 4, column = 1)

         # Button agregar producto 
        ttk.Button(frame, text = 'Guardar Producto',command=self.add_producto).grid(row = 5, columnspan = 2, sticky = W + E) # w y e es para llenar el ancho de la caja de este a oeste


        
        #Tabla producto 
        self.tree = ttk.Treeview(height=15,columns=('#0','#1','#2',))
        self.tree.grid(row = 5,column = 7, columnspan=5)
        self.tree.heading('#0', text = 'ID producto',anchor = CENTER)
        self.tree.heading('#1',text = 'ID proveedor', anchor = CENTER )
        self.tree.heading('#2',text = 'Nombre producto', anchor = CENTER )
        self.tree.heading('#3',text = 'Descripcion', anchor = CENTER )

        self.get_productos()

        ttk.Button(text='BORRAR', command = self.borrar_producto ).grid(row = 16,column = 10,sticky=W+E )






        ttk.Button(text='ACTUALIZAR').grid(row = 16,column = 11,sticky=W+E )


#----------------------------------------%%-----------------------------------------------
        
        
#---------------------------TRAER LA LISTA DE PRODUCTO-------------
    def run_query1(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_productos(self):
        records1 = self.tree.get_children()
        for element1 in records1:
            self.tree.delete(element1)

        query1 =  'SELECT * FROM PRODUCTO ORDER BY id_producto DESC'
        db_rows1 = self.run_query1(query1)

        for row1 in db_rows1:
           # print(row)    
           self.tree.insert('', 0, text = row1[0], values = (row1[1],row1[2],row1[3]))

      

#-----------TRAER LA LISTA DE PROVEEDORES----------
 # Function to Execute Database Querys
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute( query, parameters)
            conn.commit()
        return result

         # Get Proveedores from Database
    def get_proveedores(self):
    #limpiar la tabla  
        records =self.tree.get_children()
        for element in records:
            self.tree.delete(element)

# obteniendo los datos de la tabla proveedor 
        query = 'SELECT * FROM PROVEEDOR ORDER BY id_proveedor DESC'
        db_rows = self.run_query(query)

    #rellenar los datos    
        for row in db_rows:
            #print(row) #para ver la lista en pantalla el comando 

          self.tree.insert('', 0, text = row[0], values =( row[1], row[2]))




 # User Input Validation validar si no estan vacios 
    def validation(self):    
       return len(self.ID_proveedor.get()) != 0 and len(self.nameprovedor.get()) != 0 and len(self.direccion.get()) != 0 


    def validation(self):    
       return len(self.ID_producto.get()) != 0 and len(self.id_proveedor1.get()) != 0 and len(self.nombreproducto.get()) != 0 and len(self.descripcion.get()) != 0    


#------------Agregar un nuevo producto o proveedor------------------------------------------
    def add_proveedor(self):

        if self.validation():

            query = 'INSERT INTO PROVEEDOR VALUES(?,?,?) '
            parameters = (self.ID_proveedor.get(),self.nameprovedor.get(),self.direccion.get())
            self.run_query(query,parameters)
            self.message['text'] = 'El producto {} se agrego exitosamente!'.format(self.nameprovedor.get())
            self.ID_proveedor.delete(0,END)
            self.nameprovedor.delete(0,END)
            self.direccion.delete(0,END)

            

            #print("data saved")
        else:
            
            self.message['text'] = ('Todos los campos deben estar COMPLETOS ')
       

#-------------------------------Agregar un nuevo producto--------------------------------------------------------------------
    def add_producto(self):

        if self.validation():

            query1 = 'INSERT INTO PRODUCTO VALUES(?,?,?,?) '
            parameters = (self.ID_producto.get(),self.id_proveedor1.get(),self.nombreproducto.get(),self.descripcion.get())
            self.run_query1(query1,parameters)
            self.message['text'] = 'El producto {} se agrego exitosamente!!!!!!!!!'.format(self.nameprovedor.get())
            self.ID_proveedor.delete(0,END)
            self.nameprovedor.delete(0,END)
            self.direccion.delete(0,END)

            

            #print("data saved")
        else:
            
            self.message['text'] = ('Todos los campos deben estar COMPLETOS!!! ')
        self.get_productos()
        
    
 #--------------------------------------------   
    def borrar_proveedor(self):
        self.message['text'] = ''
        try:
           self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return
        self.message['text'] = ''
        PROVEEDOR = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM PROVEEDOR WHERE name = ?'
        self.run_query(query, (PROVEEDOR, ))
        self.message['text'] = 'Record {} deleted Successfully'.format(PROVEEDOR)
        self.get_proveedores()

#-----------------------------------------------------------------------------
    def borrar_producto(self):
        self.message['text'] = ''
        try:
           self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return
        self.message['text'] = ''
        producto = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM PRODUCTO WHERE name = ?'
        self.run_query(query, (producto, ))
        self.message['text'] = 'Record {} deleted Successfully'.format(producto)
        self.get_productos()

    


    


        
        


    
    
    
    
    
if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()





