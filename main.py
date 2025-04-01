#crear lkista para almacenar las ventas de la semana 
ventas=[]
#usar un ciclo para ingresar las ventas 
for i in range(7):  #7 dias de la sema
    venta=float(input(f"ingrese las ventas del dia {i+1}:"))
    ventas.append(venta)

    #procesar los datos 
    total_ventas=sum(ventas)
    
    print(total_ventas)

    #procesar los datos 
    total_ventas=sum(ventas)
    promedio_ventas=total_ventas/len(ventas)

    #condicion ára veririficar si se alcanzo la meta 
    meta=5000

    if total_ventas>=meta:
        mensaje="felicidades haz alcanzado la meta"
    else:
        mensaje ="no alcanzo la meta"
   
    #imprimir el resultado
    print("\n----reporte----")
    print(f"total de ventas:  ${total_ventas}")
    print(f"promedio $ {total_ventas}")
    print(mensaje)
