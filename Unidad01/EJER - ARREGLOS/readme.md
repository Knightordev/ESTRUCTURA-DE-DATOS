El archivo "arreglos.py" funciona de la siguiente forma:
crea una lista vacia a la cual se le incertan el numero de veces una lista de 4 indices,
luego al indice [0][i] se le asigna el nombre del departamento, por otra parte,
se recorre esa lista en [i][0] y se le asigna un mes mediante una lista de meses.

luego se utilizan metodos para agregar, mostrar o eliminar una venta mensual, los cuales usan otro metodo que verifican que
el indice [mes][departamento] exista.
metodos:
add_sales() -> agrega una venta mensual, agrega directamente al arreglo bidimencional
look_sale() -> busca una venta mensual, nos imprime el mes, el departamento y la venta mensual
delete_sales() -> elimina la venta mensual -> asigana "sin venta" a los indices buscados
does_this_sale_exist(month_index, sales_index) -> verifica que existan los indices buscados y retorna False o True en dado caso de que no o si existan respectivamente
show_sales_table() -> muestra una tabla con los meses, los departamentos y las ventas mensuales


Se crea un arreglo bidimensional ventas[12][3]
Se utilizan dos arreglos de apoyo:  
meses[]: contiene los nombres de los 12 meses.  
departamentos[]: contiene los nombres de los 3 departamentos.  
insertarVenta(int mes, int depto, double monto)  
Inserta o actualiza una venta en la posición [mes][departamento].  

buscarVenta(int mes, int depto)
Busca si existe una venta registrada en [mes][departamento] y muestra el resultado.  

eliminarVenta(int mes, int depto)
Elimina una venta registrada en [mes][departamento] asignando 0.  

mostrarVentas()
Imprime en formato tabular todas las ventas registradas en el arreglo bidimensional.  
