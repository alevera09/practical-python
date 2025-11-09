bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
sears_height   = 442             # Height (meters)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day += 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)


"""
¿Qué línea es el error?
    line 8


       
¿Cuál es el error?
    NameError, el error es que days no esta definido


Corregir el error
    Lo corregi sumando day asi mismo ya que creo que esa era la intencion

Ejecute el programa correctamente
"""