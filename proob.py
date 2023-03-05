import os

from data.config_general import config_general
from data.config_text_gpt import config_text_gpt 
os.system("clear")
'''
parte 1- es cuando el obj_table funciona para los 
casos de configuración que solo tendran un valor por lo que no
se deben generar nuevos.
'''
#objeto prueba
data_base_proob = 'data1'

print(f'comienza el trabajo con {data_base_proob}\n')


print('vamos a trabajar y comprobar config_general, heredada de obj_table\n\n')

print('''
      Esta clase lo que debe realizar es lo siguiente:
      1) Si la tabla no existe crearla
      2) Si la tabla no existia poder generar valores por defecto.
      3) Poder modificar valores y reimprimirlos
      4) Volver a setear los valores por defecto.
      5) Recuperar los valores que quedaron guardados en la base de datos.
      ''')

#probamos que funcione la creacion de la base de datos y la tabla.
o = config_general(data_base_proob)

print("1) si la tabla no existe crearla")
result = o.create_table()
print(f'el resultado de create_table es: {str(result)}')
os.system('sleep 1')

#generamos la creacion de valores por defectos.
print("\n2) Si la tabla no existia generar los valores por defecto")
result = o.record_default_values()
print(f'el resultado de record_default_values es: {str(result)}')
os.system('sleep 1')

#tenemos que poder generar valores propios
print("\n3)Poder modifcar los valores")
print('''
        vamos a generar valores propios...seteamos primero: el cambio de idioma a "en", 
        que sería ingles, con o.set_lang("en")''')
o.set_lang("en")
print('procedemos a guardar los valores a realizar el update_values_by_id...')
result = o.update_values_by_id()
print(f'resultado de o.update_values_by_id {result}')
result = o.get_values_config()
print(f'Recuperamos los valores con get_values_config(): {result}')
os.system('sleep 1')
#vamos a restaurar los valores par ver que corra bien.
print("\n4) Restaurar los valores por defecto")
print("vamos a hacer un record_default_values...")
result = o.record_default_values()
print(f'los resultado quedaron: {result}')
o.get_values_config()
os.system('sleep 1')
print('''\n5) Vamos a recuperar los valores de la base de datos y 
accedemos a través de la clase...''')
print(f'''
        id : {o.id}
        verbose : {o.verbose}
        vvv : {o.vvv}
        lang : {o.lang}
        log : {o.log}
      ''')

input('''\nTerminada la comprobación de la funcionalidad config_general, 
presione una tecla para continuar con las comprobaciones''')
os.system("clear")
print('''
      Vamos a continuar con las comprobaciones en la clase, config_text_gpt.
      Lo que esta clase debe poder realizar es lo siguiente:
      1) Si la tabla no existe, creala
      2) Crear un registro con valores por defecto, en campo cualquier campo, pero que haya un control para que no se pueda realizar dos veces con el mismo nombre.
      3) Traer el listado de configuraciones disponibles
      4) Crear un registro con valores personalizados
      5) Traer un registro disponible y poder verlo acceder a él através de la clase.
      6) modificar los valores de un registro.
      ''')

print("\n1) Si la tabla no existe crearla")
o = config_text_gpt(data_base_proob)
result = o.create_table()
print(f"El resultado es... {result}")
os.system("sleep 1")
print("\n2)vamos a generar los valores por defecto")
result = o.record_default_values()
print(f"El resultado fue {result}")
os.system("sleep 1")
print("\n3) Vamos a traer el listado de los valores actuales en la base de datos")
result = o.get_list()
print(f"El listado es este: {result}")

