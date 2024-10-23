import modulo_tareas as mt


def main():
    while True:
        mt.mostrar_menu()  
        num = input()
        if num.isdecimal():
            num = int(num)
            if not mt.proceso_seleccionado(num):  
                break
        else:
            print('Introduzca un número del 1 al 3')


if __name__ == "__main__":
    main()
