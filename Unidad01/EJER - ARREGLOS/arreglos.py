month = 12
sales = 3
month_names = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
monthly_sales = []

for i in range(month+1):
    monthly_sales.append([0,0,0,0])
monthly_sales[0] = [" ", "Ropa", "Deportes", "Jugueteria"]
for i in range(1, month+1):
    monthly_sales[i][0] = month_names[i]
def show_sales_table():
    print("////Mostrar tabla////")
    for fila in monthly_sales:
        print("{:<12} {:<10} {:<10} {:<10}".format(*fila))

def add_sales():
    print("////añadiendo venta mensual////")
    month_index = int(input("Ingrese el mes 1-12 siendo 1-enero y 12-diciembre: "))
    sales_index = int(input(f"Ingrese a donde fue la venta \n 1 .- {monthly_sales[0][1]}, \n 2 .- {monthly_sales[0][2]}, \n 3 .- {monthly_sales[0][3]} \n indice: "))
    if(does_this_sale_exist(month_index, sales_index)):
        sales_to_set = int(input("Ingrese las ventas totales: "))
        monthly_sales[month_index][sales_index] = sales_to_set
        print("Añadido!")

def look_sale():
    print("////BUscar venta mensual////")
    month_index = int(input("Ingrese el mes 1-12 siendo 1-enero y 12-diciembre: "))
    sales_index = int(input(f"Ingrese a donde fue la venta \n 1 .- {monthly_sales[0][1]}, \n 2 .- {monthly_sales[0][2]}, \n 3 .- {monthly_sales[0][3]} \n indice: "))
    if(does_this_sale_exist(month_index, sales_index)):
        return f"venta del mes {monthly_sales[month_index][0]} de {monthly_sales[0][sales_index]} con ventas de {monthly_sales[month_index][sales_index]}" 

def delete_sales():
    print("////Eliminar venta mensual////")
    month_index = int(input("Ingrese el mes 1-12 siendo 1-enero y 12-diciembre: "))
    sales_index = int(input(f"Ingrese a donde fue la venta \n 1 .- {monthly_sales[0][1]}, \n 2 .- {monthly_sales[0][2]}, \n 3 .- {monthly_sales[0][3]} \n indice: "))
    if(does_this_sale_exist(month_index, sales_index)):
        monthly_sales[month_index][sales_index] = "sin venta"
        print("Eliminado!")

def does_this_sale_exist(month_index, sales_index):
        if(month_index < 1 or month_index > 12):
            return False
        else:
            if(sales_index < 1 or sales_index > 3):
                return False
            else:
                return True
add_sales()
show_sales_table()
print(look_sale())
show_sales_table()
delete_sales()
show_sales_table()