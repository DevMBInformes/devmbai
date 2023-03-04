from data.config_general import config_general


'''
parte 1- es cuando el obj_table funciona para los 
casos de configuración que solo tendran un valor por lo que no
se deben generar nuevos.
'''
#objeto prueba
data_base_proob = 'data1'

#probamos que funcione la creacion de la base de datos y la tabla.
o = config_general(data_base_proob)
o.create_table()

#generamos la creacion de valores por defectos.


#tenemos que poder generar valores propios

#tenemos que poder actualizar los valores de un id particular

'''
parte 2...
Aqui empezamos a trabajar con mucho valores tanto para enviar como para 
recibir... deben cumplirse todas las pruebas anteriores sumados a los nuevos cambios.


'''
