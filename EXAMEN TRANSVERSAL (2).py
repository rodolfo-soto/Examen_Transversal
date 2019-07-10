from os import system

#ACÁ ARRIBA MOSTRAR LA PROGRAMACION HARD
#opcion 1

def fn_comprar(comprador_nombre, comprador_rut,vistadeptos):
    system("cls")
    print("SISTEMA DE COMPRA DEPARTAMENTO")
    print("")
    print("LOS PRECIOS PARA LOS DEPARTAMENTOS SON LOS SIGUIENTES PARA EL PRIMER Y SEGUNDO PISO")
    print("Tipo A, 3800 UF")
    print("Tipo B, 3000 UF")
    print("Tipo C, 2800 UF")
    print("Tipo D, 3500 UF")
    print("")
    print("SELECCIONE DEPARTAMENTO QUE DESEA COMPRAR")
    print("")
    print("***IMPORTANTE***")
    print("**LOS PISOS QUE ESTAN OCUPADOS CON UNA 'X'** ")
    print("PISO|     TIPO   ")
    print("    | [A] [B] [C] [D]")
    contadorPiso = 10
    contadorDepto = 0
    indiceDepto = 0
    validador = True
    por_piso = 100
    tipo_a = 3800
    tipo_b = 3000
    tipo_c = 2800
    tipo_d = 3500
#probar
    cantidadTipoA = 0
    cantidadTipoB = 0
    cantidadTipoC = 0
    cantidadTipoD = 0
    totalTipoA = 0
    totalTipoB = 0
    totalTipoC = 0
    totalTipoD = 0
    recargoTotalTipoA = 0
    recargoTotalTipoB = 0
    recargoTotalTipoC = 0
    recargoTotalTipoD = 0

    while  contadorPiso < 11 and contadorPiso >0:
        print(str(contadorPiso) + "   | ", end = '')
        while contadorDepto < 4:
            print("[" + str(vistadeptos[indiceDepto]) + "] ", end = '')                        
            contadorDepto= contadorDepto + 1
            indiceDepto = indiceDepto + 1
        contadorPiso = contadorPiso - 1
        contadorDepto = 0
        print('')
    print('')
    print("ENTER PARA CONTINUAR")
    input()
    while validador == True:
        print("Ingrese el piso que va a comprar") 
        piso = int(input()) 
        if piso >10:
            print("PISO INVALIDO")
            continue

        print("Ingrese el tipo de departamento")
        letra = input().upper()

        piso = piso
        if letra == "A":
            cantidadTipoA = cantidadTipoA +1 
            totalTipoA = totalTipoA + tipo_a
            if piso <= 2:
                recargoTotalTipoA = recargoTotalTipoA 
                valor = tipo_a
                print("El VALOR ES DE: ", valor,"UF")
                print("")
            else:
                recargoTotalTipoA = recargoTotalTipoA + (piso*por_piso)-200
                valor = tipo_a + por_piso* piso - 200
                print("EL VALOR ES DE: ", valor,"UF")

        elif letra == "B":
            cantidadTipoB = cantidadTipoB +1
            totalTipoB = totalTipoB + tipo_b
            
            if piso <= 2:
                recargoTotalTipoB = recargoTotalTipoB
                valor = tipo_b
                print("El VALOR ES DE: ",valor,"UF")
                print("")
            else:
                recargoTotalTipoB = recargoTotalTipoB + (piso*por_piso)-200
                valor = tipo_b + por_piso*piso - 200
                print("EL VALOR ES DE: ",valor,"UF")

        elif letra == "C":
            cantidadTipoC = cantidadTipoC +1
            totalTipoC = totalTipoC + tipo_c
            if piso <= 2:
                valor = tipo_c
                recargoTotalTipoC = recargoTotalTipoC
                print("El VALOR ES DE: ",valor,"UF")
                print("")
            else:
                recargoTotalTipoC = recargoTotalTipoC + (piso*por_piso)-200
                valor = tipo_c + por_piso*piso - 200
                print("EL VALOR ES DE: ",valor,"UF")

        elif letra == "D":
            cantidadTipoD = cantidadTipoD +1
            totalTipoD = totalTipoD + tipo_d
            if piso <= 2:
                valor = tipo_d
                recargoTotalTipoD = recargoTotalTipoD
                print("El VALOR ES DE: ",valor,"UF")
                print("")
            else:
                recargoTotalTipoD = recargoTotalTipoD + (piso*por_piso)-200

                valor = tipo_d + por_piso*piso - 200
                print("EL VALOR ES DE: ",valor,"UF")

        if letra == "A":
            letra = 0
        elif letra == "B":
            letra = 1
        elif letra == "C":
            letra = 2
        elif letra == "D":
            letra = 3
        else:
            print("LETRA NO VALIDA")
            continue

        print("PISO|     TIPO   ")
        print("    | [A] [B] [C] [D]")

        #Contadores
        contadorPiso = 10
        contadorDepto = 0
        indiceDepto = 0
        ocupado = False

        while  contadorPiso < 11 and contadorPiso >0:
            print(str(contadorPiso) + "   | ", end = '')
            while contadorDepto < 4: 
                if contadorDepto == int(letra) and contadorPiso == int(piso):
                    if str(vistadeptos[indiceDepto]) == 'X':
                        ocupado = True 
                    else:
                        vistadeptos[indiceDepto] = 'X'
                print("[" + str(vistadeptos[indiceDepto]) + "] ", end = '')                        
                contadorDepto= contadorDepto + 1
                indiceDepto = indiceDepto + 1
            contadorPiso = contadorPiso - 1
            contadorDepto = 0
            print('')

        if ocupado == True:
            print("PISO OCUPADO")

        else:
            contador = 0
            validador = False
            print("INGRESE NUEVO COMPRADOR")
            print("")
            print("***IMPORTANTE***")
            print("**EL RUT DEBE SER INGRESADO SIN PUNTOS, GUION NI DIGITO VERIFICADOR**")
            print("")
            print("RUT DEL COMPRADOR: ")
            rut = int(input())

            while contador < len(comprador_rut):
                if rut == comprador_rut[contador]:
                    validador = True
                    break
                contador = contador + 1

            if validador == True:
                print("ESE RUT YA ESTA ALMACENADO")
                exit

            else:
                print("NOMBRE Y APELLIDO DEL COMPRADOR: ")
                nombre = input()
                
                print("")
                print("DATOS ALMACENADOS CORRECTAMENTE")


                comprador_nombre.append(nombre)
                comprador_rut.append(rut)
                piso_edificio.append(piso)
                letra_edificio.append(letra)
                valor_pago.append(valor)
                gananciasTotales.append('Tipo A	3800 UF ' + str(cantidadTipoA) + '	' + str(totalTipoA) + '	' + str(recargoTotalTipoA))
                gananciasTotales.append('Tipo B	3000 UF	' + str(cantidadTipoB) + '	' + str(totalTipoB) + '	' + str(recargoTotalTipoB))
                gananciasTotales.append('Tipo C	2800 UF	' + str(cantidadTipoC) + '	' + str(totalTipoC) + '	' + str(recargoTotalTipoC))
                gananciasTotales.append('Tipo D	3500 UF	' + str(cantidadTipoD) + '	' + str(totalTipoD) + '	' + str(recargoTotalTipoD))
                
    input()


#opcion 2

def fn_ptolibre(vistadeptos): 

    system("cls")
    print("***IMPORTANTE***")
    print("**LOS PISOS QUE ESTAN OCUPADOS CON UNA 'X'** ")
    print("PISO|     TIPO   ")
    print("    | [A] [B] [C] [D]")
    contadorPiso = 10
    contadorDepto = 0
    indiceDepto = 0
    while  contadorPiso < 11 and contadorPiso > 0:
        print(str(contadorPiso) + "   | ", end = '')
        while contadorDepto < 4:
            print("[" + str(vistadeptos[indiceDepto]) + "] ", end = '')                         
            contadorDepto= contadorDepto + 1
            indiceDepto = indiceDepto + 1
        contadorPiso = contadorPiso - 1
        contadorDepto = 0
        print('')
        
    print("SI DESEA VOLVER A LAS OPCIONES PRESIONE ENTER")
    input()
    False

#opcion 3

def fn_lista_comprador(comprador_rut,comprador_nombre,piso_edificio,letra_edificio):
    contador = 0
    system("cls")
    print("LISTA DE COMPRADORES")
    print("____________________")
    print("")

    if len(comprador_rut) == 0:
        print("AUN NO EXISTEN COMPRADORES")
    else:
        while contador < len(comprador_rut):
            comprador_rut.sort()
            print(comprador_rut[contador],comprador_nombre[contador],letra_edificio[contador],+int(piso_edificio[contador]))
            contador = contador + 1
    input()

#opcion 4

def fn_buscar(comprador_nombre,comprador_rut):
    contador = 0
    validador = False
    system("cls")
    print("SERVICIO DE BUSQUEDA COMPRADOR")
    print("")
    print("INGRESE EL RUT DEL COMPRADOR SIN PUNTOS, GUION NI DIGITO VERIFICADOR")
    rut = int(input())

    while contador < len(comprador_rut):
        if rut == comprador_rut[contador]:
            print("")
            print(comprador_nombre[contador] + "-" + str(comprador_rut[contador]))
            print("__________________________________")
            print("PRESIONE ENTER PARA VOLVER AL MENU")
            input()
            validador = True
            break
        contador = contador +1
    if validador == False:
        print("NO SE REGISTRA COMPRADOR POR ESE RUT")
        input()
    
input()

# OPCION 5


def fn_reasignar(comprador_rut,comprador_nombre,letra_edificio,piso_edificio):
    system("cls")
    contador = 0
    validador = False
    print("INGRESE EL RUT AL QUE DESEA REASIGNAR LA COMPRA")
    rut = int(input())
    while  contador < len(comprador_rut):
        if rut == comprador_rut[contador]:
            print("INGRESE NUEVO NOMBRE Y APELLIDO")
            nomb_apell = input()

            print("INGRESE NUEVO RUT")
            rut = int(input())

            comprador_nombre[contador] = nomb_apell
            comprador_rut[contador] = rut
            print("COMPRA REASIGNADA")
            validador = True
            break
        contador = contador + 1
    if validador == False:
        print("RUT INGRESADO NO EXISTE")
    input()

#OPCION 6


def fn_ganancias_totales(gananciasTotales):
    system("cls")
     
    print('Tipo de Departamento	Cantidad	Total	Recargo por Piso')
    print(gananciasTotales[0])
    print(gananciasTotales[1])
    print(gananciasTotales[2])
    print(gananciasTotales[3])
    input()




#ACÁ ABAJO MONTAR PROGRAMA PRINCIPAL
validador = True
comprador_nombre = []
comprador_rut = []
piso_edificio = []
letra_edificio = []
valor_pago = []
gananciasTotales = []


#array que un no se como usar
vistadeptos = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#todas en UF
while validador == True:
    system("cls")
    print("BIENVENIDOS AL SISTEMA")
    print("")
    print("INMOBILIARIA MURITO")
    print("ELIJA UNA OPCION: ")
    print("[1] Comprar departamento")
    print("[2] Mostrar departamentos disponibles")
    print("[3] Ver listado de compradores")
    print("[4] Buscar comprador")
    print("[5] Reasignar compra")
    print("[6] Mostrar ganancias totales")
    print("[7] SALIR")
    opcion = input()

    if opcion == "1":
        fn_comprar(comprador_nombre, comprador_rut,vistadeptos)
    elif opcion == "2":
        fn_ptolibre(vistadeptos)
    elif opcion == "3":
        fn_lista_comprador(comprador_rut,comprador_nombre,piso_edificio,letra_edificio)
    elif opcion == "4":
        fn_buscar(comprador_nombre,comprador_rut)
    elif opcion == "5":
        fn_reasignar(comprador_rut,comprador_nombre,letra_edificio,piso_edificio)
    elif opcion == "6":
        fn_ganancias_totales(gananciasTotales)
    elif opcion == "7":
        print("GRACIAS POR USAR EL SOFTWARE")
        validador = False
    else:
        print("MENU INVALIDO")
        validador= True
print("HASTA LUEGO")
input()
