from Aspirante import *
from Empresa import *
def menu_principal():
    while True:
        print("==== Menú Principal ====")
        print("1. Aspirante")
        print("2. Empresa")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_aspirante()
        elif opcion == "2":
            menu_empresa()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


def menu_aspirante():
    while True:
        print("==== Menú Aspirante ====")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_aspirante()
        elif opcion == "2":
            iniciar_sesion_aspirante()
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


def registrar_aspirante():
    print("==== Registro de Aspirante ====")
    aspirante = Aspirante.componerAspirante

    print("¡Registro exitoso! Ahora puedes iniciar sesión como aspirante.")


def iniciar_sesion_aspirante():
    print("==== Inicio de Sesión para Aspirante ====")
    correo = input("Ingrese su correo electrónico: ")
    contraseña = input("Ingrese su contraseña: ")
    for aspirante in Aspirante.aspirantelista:
        if aspirante.correo == correo and aspirante.contraseña == contraseña:
            aspirante_encontrado = aspirante
            break

    if aspirante_encontrado:
        print("Inicio de sesión exitoso.")
        menu_opciones_aspirante(aspirante_encontrado)
    else:
        print("Correo o contraseña incorrectos. Por favor, intente nuevamente.")


def menu_opciones_aspirante(aspirante):
    while True:
        print(f"==== Menú de Opciones para Aspirante: {aspirante.nombre} ====")
        print("1. Agregar Experiencia")
        print("2. Agregar Educación")
        print("3. Buscar Ofertas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_experiencia(aspirante)
        elif opcion == "2":
            agregar_educacion(aspirante)
        elif opcion == "3":
            buscar_ofertas(aspirante)
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


def agregar_experiencia(aspirante):
    print("==== Agregar Experiencia ====")
    empresa = input("Ingrese el nombre de la empresa: ")
    descripcion = input("Ingrese una descripción de la experiencia: ")
    fecha_inicio = input("Ingrese la fecha de inicio (formato: DD/MM/AAAA): ")
    fecha_fin = input("Ingrese la fecha de finalización (formato: DD/MM/AAAA): ")
    cargo = input("Ingrese el cargo: ")
    funciones = input("Ingrese las funciones desempeñadas: ")

    experiencia = Experiencia(empresa, descripcion, fecha_inicio, fecha_fin, cargo, funciones)

    aspirante.agregar_experiencia(experiencia)

    print("Experiencia agregada correctamente.")


def agregar_educacion(aspirante):
    print("==== Agregar Educación ====")
    institucion = input("Ingrese el nombre de la institución educativa: ")
    fecha_inicio = input("Ingrese la fecha de inicio (formato: DD/MM/AAAA): ")
    fecha_fin = input("Ingrese la fecha de finalización (formato: DD/MM/AAAA): ")
    tipo_educacion = input("Ingrese el tipo de educación: ")
    certificados = input("Ingrese los certificados obtenidos: ")

    # Crear un objeto de la clase Educacion con los datos proporcionados
    educacion = Educacion(institucion, fecha_inicio, fecha_fin, tipo_educacion, certificados)

    # Agregar la educación al aspirante
    aspirante.agregar_educacion(educacion)

    print("Educación agregada correctamente.")


def buscar_ofertas(aspirante):
    print("==== Búsqueda de Ofertas ====")

    nombre_oferta = input("Ingrese el nombre de la oferta que desea buscar: ")

    # Obtener la lista de todas las ofertas disponibles
    lista_ofertas = Empresa.listaofertas()  # Reemplaza con tu lógica para obtener las ofertas disponibles

    # Realizar la búsqueda por nombre de oferta
    ofertas_encontradas = []
    for oferta in lista_ofertas:
        if nombre_oferta.lower() in Empresa.listaofertas.lower():
            ofertas_encontradas.append(oferta)

    # Mostrar los resultados de la búsqueda
    if len(ofertas_encontradas) > 0:
        print(f"Se encontraron {len(ofertas_encontradas)} oferta(s) con el nombre '{nombre_oferta}':")
        for oferta in ofertas_encontradas:
            print(f"- Nombre: {oferta.nombre}")
            print(f"  Tipo de contrato: {oferta.tipo_contrato}")
            print(f"  Cargo: {oferta.cargo}")
            print(f"  Número de vacantes: {oferta.numero_vacantes}")
            print()
    else:
        print(f"No se encontraron ofertas con el nombre '{nombre_oferta}'.")


def menu_empresa():
    while True:
        print("==== Menú Empresa ====")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_empresa()
        elif opcion == "2":
            iniciar_sesion_empresa()
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


def registrar_empresa():
    print("==== Registro de Aspirante ====")
    empresa = Empresa.componerEmpresa

    print("¡Registro exitoso! Ahora puedes iniciar sesión como aspirante.")


def iniciar_sesion_empresa():
    print("==== Inicio de Sesión para Empresa ====")
    correo = input("Ingrese su correo electrónico: ")
    contraseña = input("Ingrese su contraseña: ")
    for empresa in Empresa.componerEmpresa:
        if empresa.correo == correo and empresa.contraseña == contraseña:
            empresa_encontrado = empresa
            break

    if empresa_encontrado:
        print("Inicio de sesión exitoso.")
        menu_opciones_empresa(empresa_encontrado)
    else:
        print("Correo o contraseña incorrectos. Por favor, intente nuevamente.")
    

def menu_opciones_empresa(empresa):
    while True:
        print("==== Menú Empresa ====")
        print("1. Agregar Oferta")
        print("2. Ver Aspirantes Postulados")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == "1":
            agregar_oferta(empresa)
        elif opcion == "2":
            ver_aspirantes_postulados(empresa)
        elif opcion == "3":
            print("Saliendo del menú de la empresa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione un número válido.")


def agregar_oferta(empresa):
    print("==== Agregar Oferta ====")
    empresa = Empresa.componerEmpresa

    print("Oferta agregada con éxito.")


def ver_aspirantes_postulados(empresa):
    pass
menu_principal()