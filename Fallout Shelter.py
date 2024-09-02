import psycopg2

try:
    connection = psycopg2.connect(
        host='localhost', 
        user='Yonaikel', 
        password='yils1101', 
        database='FalloutShelter'
    )
    print("conexion exitosa")
except Exception as ex:
    print(ex)


opc_menu1 = 0
opc_menu = 0
while opc_menu != 2:
    print("Menu")
    print("1. Refugio 001")
    print("2. Salir")
    opc_menu = int(input("¿Que refugio quieres ver?: "))
    if opc_menu == 1:
        print("Menu")
        print("1. Moradores")
        print("2. Salir")
        opc_menu1 = int(input("\nElegir opcion: "))
 

        if opc_menu1 == 1:
            print("Menu")
            print("1. Ver los moradores")
            print("2. Agregar morador")
            print("3. Editar morador")
            print("4. Actualizar morador")
            print("5. Salir")
            opc_menu2 = int(input("\nElegir opcion: "))

            if opc_menu2 == 1:
                cursor = connection.cursor()
                cursor.execute(f"SELECT * FROM moradores")
                moradores=cursor.fetchone()
                while moradores:
                    print(moradores[1], moradores[2])
                    moradores=cursor.fetchone()
                cursor.close()
                resp = input("¿ Quieres ver un morador mas detalladamente ?: ")
                if resp == "si":
                    morador_nombre = input("¿ Nombre del morador ?: ")
                    morador_apellido = input("¿ Apellido del morador ?: ")
                    cursor = connection.cursor()
                    cursor.execute(f"SELECT * FROM moradores WHERE nombre = '{morador_nombre}' AND apellido = '{morador_apellido}'")
                    moradores=cursor.fetchone()
                    cursor.execute(f"SELECT * FROM hijo WHERE padre = '{morador_nombre}'")
                    hijos=cursor.fetchone()
                    while moradores:
                        print(moradores[1], moradores[2], moradores[3], moradores[4], moradores[5], moradores[6], moradores[7], moradores[8])
                        moradores=cursor.fetchone()
                    while hijos:
                        print(hijos[1], moradores[2])
                        hijos= cursor.fetchone()
                    cursor.close()


            elif opc_menu2 == 2:
                nombre = input("¿Cual es el nombre del morador?: ")
                apellido = input("¿Cual es el apellido del morador?: ")
                sexo = input("¿Cual es el sexo del morador?: ")
                resp_mora = input("¿El morador nacio en el refugio?: ")
                if resp_mora == "si":
                    origen = "Nacido en el Refugio"
                    padre = input("¿Quien es el padre?: ")
                    madre = input("¿Quien es la madre?: ")
                elif resp_mora == "no":
                    origen = "desconocido"

                else:
                    print("Opcion no valida")

                pareja = input("¿Tiene pareja?: ")
                
                if pareja == "si":
                    nombre_pareja = input("¿Nombre de la pareja?: ")
                    apellido_pareja = input("¿Apellido de la pareja?: ")
                    cursor = connection.cursor()
                    cursor.execute("SELECT MiN(id_morador) FROM moradores")
                    id_mayor_mora = cursor.fetchone()
                    id_mayor_mora = id_mayor_mora[0]
                    if id_mayor_mora != 1: 
                        id_mayor_mora = 1
                    elif id_mayor_mora == 1:
                        cursor.execute("SELECT MAX(id_morador) FROM moradores")
                        id_mayor_mora = cursor.fetchone()
                        id_mayor_mora = id_mayor_mora[0]
                        id_mayor_mora = id_mayor_mora + 1
                    cursor.execute(f"INSERT INTO moradores VALUES ('{id_mayor_mora}', '{nombre}', '{apellido}', '{sexo}', '{origen}', '{padre}', '{madre}', '{nombre_pareja}', '{apellido_pareja}')")
                    connection.commit()
                    cant_hijos = int(input("¿Cuantos hijos tiene ?: "))
                    for i in range(0, cant_hijos):
                        nombre_hijo = input("¿Cual es el nombre?: ")
                        sexo_hijo = input("¿Cual es el sexo?")
                        if sexo == "masculino":
                            padre = nombre
                            madre = nombre_pareja
                        else:
                            madre = nombre
                            padre = nombre_pareja
                       
                        cursor.execute("SELECT MIN(id_hijo) FROM hijo")
                        id_mayor_hijo = cursor.fetchone()
                        id_mayor_hijo = id_mayor_hijo[0]
                        if id_mayor_hijo != 1: 
                            id_mayor_hijo = 1
                        elif id_mayor_hijo == 1:
                            cursor.execute("SELECT MAX(id_hijo) FROM hijo")
                            id_mayor_hijo = cursor.fetchone()
                            id_mayor_hijo = id_mayor_hijo[0]
                            id_mayor_hijo = id_mayor_hijo + 1
                        cursor.execute(f"INSERT INTO hijo VALUES ('{id_mayor_hijo}', '{nombre_hijo}', '{apellido}', '{sexo_hijo}', '{padre}', '{madre}')")
                        connection.commit()
                    cursor.close()

            elif opc_menu2 == 3:
                editar_nombre = input("¿Nombre del morador a editar?: ")
                editar_apellido = input("¿Apellido del morador a editar?: ")
                resp_edit_nomb = input("¿Quieres editar el nombre del morador?: ")
                if resp_edit_nomb == "si":
                    nuevo_nombre = input("¿Cual es el nuevo nombre del morador?: ")
                resp_edit_apellido = input("¿Quieres editar el apellido del morador?: ")
                if resp_edit_apellido == "si":
                    nuevo_apellido = input("¿Cual es el nuevo apellido del morador?: ")
                resp_edit_sex = input("¿Quieres editar el sexo del morador?: ")
                if resp_edit_sex == "si":
                    nuevo_sex = input("¿Cual es el nuevo sexo del morador?: ")
                resp_edit_origen = input("¿Quieres cambiar el origen del morador?: ")
                if resp_edit_origen == "si":
                    nuevo_origen = input("¿Cual es el nuevo origen del morador?: ")
                resp_edit_padre = input("¿Quieres cambiar el nombre padre de el morador?: ")
                if resp_edit_padre == "si":
                    nuevo_nombre_padre = input("¿Cual es el nuevo nombre del padre del morador?: ")
                resp_edit_madre = input("¿Quieres cambiar el nombre de la madre de el morador?: ")
                if resp_edit_madre == "si":
                    nuevo_nombre_madre = input("¿Cual es el nuevo nombre de la madre del morador?: ")
                resp_edit_pareja_nombre = input("¿Quieres cambiar el nombre de la pareja de el morador?: ")
                if resp_edit_pareja_nombre == "si":
                    nuevo_nombre_pareja = input("¿Cual es el nuevo nombre de la pareja del morador?: ")
                resp_edit_pareja_apellido =  input("¿Quieres cambiar el apellido de la pareja de el morador?: ")
                if resp_edit_pareja_apellido == "si":
                    nuevo_apellido_pareja = input("¿Cual es el nuevo apellido de la pareja de el morador?: ")
                cursor=connection.cursor()
                


    else:
        print("Esta opcion no esta disponible")