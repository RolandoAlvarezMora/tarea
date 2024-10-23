
def ingresar_puntuacion_y_comentario():
    while True:
        point = obtener_puntuacion()
        if point:
            comment = obtener_comentario()
            guardar_datos(point, comment)
            break


def obtener_puntuacion():
    print('Por favor, introduzca una puntuación en una escala de 1 a 5')
    point = input()
    
    if point.isdecimal():
        point = int(point)
        if 1 <= point <= 5:
            return point
        else:
            print('Por favor, introduzca un valor entre el 1 y 5')
            return None
    else:
        print('Por favor, introduzca la puntuación en números')
        return None


def obtener_comentario():
    print('Por favor, introduzca un comentario')
    return input()


def guardar_datos(point, comment):
    post = f'puntuación: {point} comentario: {comment}'
    with open("data.txt", 'a') as file_pc:
        file_pc.write(f'{post}\n')
    print("Datos guardados exitosamente.")


def comprobar_resultados():
    print('Resultados hasta la fecha:')
    try:
        with open("data.txt", "r") as read_file:
            contenido = read_file.read()
            if contenido:
                print(contenido)
            else:
                print("No hay resultados disponibles.")
    except FileNotFoundError:
        print("El archivo no existe aún. No hay resultados disponibles.")


def finalizar():
    print('Finalizando')


def mostrar_menu():
    print('Seleccione el proceso que desea aplicar:')
    print('1: Ingresar puntuación y comentario')
    print('2: Comprobar los resultados obtenidos hasta ahora')
    print('3: Finalizar')


def proceso_seleccionado(num):
    if num == 1:
        ingresar_puntuacion_y_comentario()
    elif num == 2:
        comprobar_resultados()
    elif num == 3:
        finalizar()
        return False  
    else:
        print('Introduzca un número del 1 al 3')
    return True  
