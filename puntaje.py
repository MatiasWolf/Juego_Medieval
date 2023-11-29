
def guardar_puntaje(puntaje):
    with open('puntaje.csv','w') as archivo:
        archivo.write(str(puntaje))

def cargar_puntaje():
    try:
        with open('puntaje.csv','r') as archivo:
            return int(archivo.read())
    except FileNotFoundError:
        return 0

