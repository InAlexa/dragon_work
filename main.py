mayor = 0
residuo = 0

# uno
num1 = int(input('Ingrese un número entero:'))
num2 = int(input('Ingrese otro número entero'))

if num1 > num2:
    mayor = num1
    print('El número mayor es', mayor)
elif num2 > num1:
    mayor = num2
    print('El número mayor es', mayor)

# dos
residuo = mayor % 2
if residuo == 0:
    print(f'El número {mayor} es par porque su residuo es 0')
else:
    print(f'El número {mayor} es impar porque su residuo es {residuo}')

# tres