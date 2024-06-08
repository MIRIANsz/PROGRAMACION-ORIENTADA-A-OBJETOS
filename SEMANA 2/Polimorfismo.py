class Ave:
    def volar(self):
        print("El ave está volando.")

class Pinguino(Ave):
    def volar(self):
        print("El pingüino no puede volar.")

def hacer_volar(ave):
    ave.volar()

# Crear instancias de Ave y Pinguino
mi_ave = Ave()
mi_pinguino = Pinguino()

hacer_volar(mi_ave)
hacer_volar(mi_pinguino)

