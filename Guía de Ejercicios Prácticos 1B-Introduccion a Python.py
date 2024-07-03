nombredeusuario = input("Introduzca su nombre de usuario por favor: ")
Saludo_1 = "Hola " + nombredeusuario
print(Saludo_1)
numero1 = int(input("Introduzca primer número: "))
numero2 = int(input("Introduzca segundo número: "))
resultado1 = (numero1)+(numero2)
print("la suma de los numeros es " + str(resultado1))
nombre = input("Introduzca su nombre: ")
apellido = input("Introduzca su apellido: ")
edad = int(input("Introduzca su edad: "))
datospersonales = "Usted es " + nombre + " " + apellido + " y tiene " + str(edad) + " años de edad"
print(datospersonales)
datosdealumno1 = input("Ingrese nombre de alumno: ")
datosdealumno2 = int(input("Ingrese Número de Comisión: "))
datosdealumno3 = input("Ingrese asignatura: ")
datosdealumno4 = input("Ingrese nombre de profesor/a: ")
datosdealumno5 = input("Ingrese si estuvo presente en la clase respondiendo con SI o NO: ")
datosdealumnofinal = "Usted es " + datosdealumno1 + " de la comisión N° " + str(datosdealumno2) + ", quien cursa la asignatura " + datosdealumno3 + " enseñada por " + datosdealumno4 + ", siendo que el alumno " + datosdealumno5 + " estuvo presente en la clase"
print(datosdealumnofinal)
cuadrado = int(input("Especifique el valor del lado de un cuadrado: "))
areadelcuadrado = cuadrado**2
print(areadelcuadrado,"es el valor del area del cuadrado basandonos en el dato especificado")
lado_1_rectangulo = int(input("Especifique valor de base de un rectangulo: "))
lado_2_rectangulo = int(input("Especifique valor de altura del rectangulo: "))
Resultado_Rectangulo = lado_1_rectangulo*lado_2_rectangulo
print(Resultado_Rectangulo,"es el valor de la superficie del rectangulo en base a los valores especificados")
triangulobase = int(input("Ingrese Base de Triangulo: "))
trianguloaltura = int(input("Ingrese Altura de Triangulo: "))
print("Basandonos en los datos que se plantearon, la superficie del triangulo tiene un valor de")
triangulosuperficie = triangulobase*trianguloaltura*0.5
print(triangulosuperficie)
Producto = input("Ahora ingrese el nombre de un producto: ")
Precio = int(input("Ahora ingrese el precio de dicho producto: "))
tasadeiva = float(0.21)
iva = Precio * tasadeiva
preciototal = Precio + iva
print("Basandonos en el precio de su producto, sumandole la tasa de IVA, daria como resultado que")
resumenproducto = Producto + " = " + str(preciototal)
print(resumenproducto)
print("A continuación se sacará el promedio aproximado de sus notas")
Nota1 = int(input("Ingrese su primer nota redondeando el valor: "))
Nota2 = int(input("Ingrese su segunda nota redondeando el valor: "))
Nota3 = int(input("Ingrese su tercer nota redondeando el valor: "))
PromedioNotas = (Nota1 + Nota2 + Nota3)/3
DevolucionPromedio = "Su promedio es de " + str(PromedioNotas)
print(DevolucionPromedio)
Nombre = input("Una vez más indique su nombre por favor: ")
Edad = int(input("¿Y su edad?: "))
Edad_10 = (Edad + 10)
Edad_10D = "Dentro de 10 años usted tendrá " + str(Edad_10) + " Años, pero eso es solo un número ;), Disfrute la vida"
print(Edad_10D)