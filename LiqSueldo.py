#Ingresar los datos del sueldo mensual, codigo de estado civil (1soltero-2casado con hijos-3casado sin h) y el nombnre del empleado.
# Se debe descontar el 3% de obra social y el 11% de aportes jubilatorios y se debe incrementar $500 si es casado, $ 900 con hijos.

# ENTRADAS: n(nombre) - c(codigo estado civil) - s(sueldo)
# PROCESO: os(descuento o.social) - j(desc jubilacion) - cas(casado?) - h(casado con hijos?)
# SALIDAS: sn(sueldo neto)

n=0
c=0
s=0
os=0
j=0
cas=0
h=0
sn=0
l=0
print("Bienvenido, sistema liquidacion de sueldos")
l=int(input("Nueva liquidacion? Marque 1"))
while l==1:
    c=int(input("Codigo de estado civil: marque 1 soltero - 2 casado con hijos - 3 casado sin hijos"))
    while c<=3 and c>0:
        if c==1:
            n=input("Ingrese nombre y apellido del empleado")
            s=float(input("Ingrese importe del sueldo bruto"))
            os=s*3/100
            j=s*11/100
            sn=s-os-j
            print("Empleado:",n)
            print("Sueldo Neto: $",sn)
            n=0
            s=0
            os=0
            j=0
            s=0
            sn=0
            c=0
            l=int(input("Nueva liquidacion? Marque 1"))
        elif c==2:
            n=input("Ingrese nombre y apellido del empleado")
            s=float(input("Ingrese importe del sueldo bruto"))
            os=s*3/100
            j=s*11/100
            sn=s-os-j+500+900
            print("Empleado:",n)
            print("Sueldo Neto: $",sn)
            n=0
            s=0
            os=0
            j=0
            s=0
            sn=0
            c=0
            l=int(input("Nueva liquidacion? Marque 1"))
        elif c==3:
            n=input("Ingrese nombre y apellido del empleado")
            s=float(input("Ingrese importe del sueldo bruto"))
            os=s*3/100
            j=s*11/100
            sn=s-os-j+500
            print("Empleado:",n)
            print("Sueldo Neto: $",sn)
            n=0
            s=0
            os=0
            j=0
            s=0
            sn=0
            c=0
            l=int(input("Nueva liquidacion? Marque 1"))
        else:
            print("error, vuelva a comenzar")
else:
    print("Hasta luego")

