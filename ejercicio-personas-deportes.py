#Crear clase Personas
#- Nombre
#- Apellido
#- Edad
#- Estado civil
#- velocidad = 0
#- Velocidad Maxima
#- Caminar: Mostrar un mensaje que estan caminando. Velocidad + 0.1km
#- Hablar: metodo donde le pasan un parametro y retorna el texto o lo imprime
#- Casarse, divorciarse, o enviudar (cambia el estado civil)

class Personas: 
    def __init__(self, nombre, apellido, edad, estado_civil, velocidad_maxima):
        self.nombre = nombre 
        self.apellido = apellido
        self.edad = edad
        self.estado_civil = estado_civil
        self.velocidad = 0
        self.velocidad_maxima = velocidad_maxima

    def caminar(self):
        if self.velocidad < self.velocidad_maxima:
            self.velocidad += 0.1
        print(self.nombre + " " + self.apellido + " está caminando a " + str(round(self.velocidad, 1)) + " km/h.")

    def hablar(self, texto):
        print(self.nombre + " dice: " + texto)
    
    def casarse(self):
        self.estado_civil = 'casado/a'
        print(self.nombre + " " + self.apellido + " se ha casado.")
    
    def divorciarse(self):
        self.estado_civil = 'divorciado/a'
        print(self.nombre + " " + self.apellido + " se ha divorciado.")
    
    def enviudar(self):
        self.estado_civil = 'viudo/a'
        print(self.nombre + " " + self.apellido + " ha enviudado.")

persona = Personas("Julio","Gómez", 40, "soltero", 5)
persona.caminar()
persona.hablar("Hola, ¿cómo estás?")
persona.casarse()
persona.divorciarse()
persona.enviudar()

# Tres clases que heredan
# 1- Basketbolistas. Aparte tienen Numero de jugador, equipo y numero de camiseta
# Los basketbolistas pueden ser transferidos a otros equipos, y pueden cambiar de numero de camiseta
# En el main, van a crear varios jugadores, van a ir haciendo operaciones. Van a listar los jugadores que
# juegan en Ferro
# 2- Tenistas. Tienen aparte ranking ATP, marca de raqueta, un record de partidos ganados y perdidos y un rival
# Los rivales, son una lista de otros tenistas.
# 3- Velocistas. Tienen que tener club al que pertenecen, Mejor marca en 100 metros, en 200 m.
# pueden correr carreras, y si el tiempo supera la mejor marca, esa marca pasa a ser la mejor.

# Definición de clases aquí

class Deportistas:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Basketbolistas(Deportistas):
    def __init__(self, nombre, edad, numero_jugador, equipo, numero_camiseta):
        super().__init__(nombre, edad)
        self.numero_jugador = numero_jugador
        self.equipo = equipo
        self.numero_camiseta = numero_camiseta

    def transferir(self, nuevo_equipo):
        self.equipo = nuevo_equipo

    def cambiar_numero_camiseta(self, nuevo_numero):
        self.numero_camiseta = nuevo_numero

    def __str__(self):
        return f'{self.nombre}, Jugador #{self.numero_jugador}, Equipo: {self.equipo}, Camiseta: {self.numero_camiseta}'

def main():
    jugador1 = Basketbolistas("Juan Pérez", 25, 10, "Ferro", 23)
    print(jugador1)

if __name__ == "__main__":
    main()


class Tenistas(Deportistas):
    def __init__(self, nombre, edad, ranking_atp, marca_raqueta, partidos_ganados, partidos_perdidos, rivales):
        super().__init__(nombre, edad)
        self.ranking_atp = ranking_atp
        self.marca_raqueta = marca_raqueta
        self.partidos_ganados = partidos_ganados
        self.partidos_perdidos = partidos_perdidos
        self.rivales = rivales 

    def __str__(self):
        rivales_nombres = ', '.join([rival.nombre for rival in self.rivales]) if self.rivales else 'Ninguno'
        return (f'{self.nombre}, Ranking ATP: {self.ranking_atp}, Raqueta: {self.marca_raqueta}, '
                f'Partidos Ganados: {self.partidos_ganados}, Partidos Perdidos: {self.partidos_perdidos}, '
                f'Rivales: {rivales_nombres}')
    
class Velocistas(Deportistas):
    def __init__(self, nombre, edad, club, mejor_marca_100m, mejor_marca_200m):
        super().__init__(nombre, edad)
        self.club = club
        self.mejor_marca_100m = mejor_marca_100m
        self.mejor_marca_200m = mejor_marca_200m

    def correr_carrera(self, distancia, tiempo):
        if distancia == 100 and tiempo < self.mejor_marca_100m:
            self.mejor_marca_100m = tiempo
        elif distancia == 200 and tiempo < self.mejor_marca_200m:
            self.mejor_marca_200m = tiempo

    def __str__(self):
        return (f'{self.nombre}, Club: {self.club}, Mejor Marca 100m: {self.mejor_marca_100m}, '
                f'Mejor Marca 200m: {self.mejor_marca_200m}')


def main():
    jugador1 = Basketbolistas("Juan Pérez", 25, 10, "Ferro", 23)
    tenista1 = Tenistas("Maria Gómez", 28, 5, "Wilson", 300, 120, [])
    velocista1 = Velocistas("Luis Martínez", 22, "Club Atlético", 10.5, 21.8)

    print(jugador1)
    print(tenista1)
    print(velocista1)

    jugador1.transferir("Boca")
    jugador1.cambiar_numero_camiseta(12)
    print("Después de transferencia:")
    print(jugador1)

    velocista1.correr_carrera(100, 10.3)
    print("Después de la carrera:")
    print(velocista1)

if __name__ == "__main__":
    main()
        