import tkinter as tk
from tkinter import font, ttk, messagebox
import random

class Equipo:
    def __init__(self, nombre, entrenador):
        self.nombre = nombre
        self.entrenador = entrenador
        self.jugadores = []
        self.victorias = 0

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

class Jugador:
    def __init__(self, nombre, edad, posicion):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion

class Estadio:
    def __init__(self, nombre, ciudad, capacidad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad = capacidad

class MundialGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mundial de Fútbol")
        self.geometry("1024x600")
        self.config(bg="#f0f0f0")
        
        self.teams = self.generar_equipos()
        self.estadios = self.generar_estadios()
        self.grupos = self.dividir_en_grupos()
        self.resultados = self.generar_resultados()
        
        self.configurar_gui()
        self.mostrar_pantalla_principal()

    def configurar_gui(self):
        # Configuración de la barra superior
        self.barra_superior = tk.Frame(self, bg="#333333", height=50)
        self.barra_superior.pack(side=tk.TOP, fill='x')

        self.label_titulo = tk.Label(self.barra_superior, text="Mundial de Fútbol", bg="#333333", fg="#ffffff", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        # Configuración del menú lateral
        self.menu_lateral = tk.Frame(self, bg="#333333", width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='y')

        # Botones del menú lateral
        botones_info = [
            ("Estadios", self.mostrar_estadios),
            ("Equipos", self.mostrar_equipos),
            ("Grupos", self.mostrar_grupos),
            ("Partidos", self.mostrar_partidos),
            ("Octavos", self.mostrar_octavos),
            ("Cuartos de Final", self.mostrar_cuartos_final),
            ("Semifinal", self.mostrar_semifinal),
            ("Final", self.mostrar_final)
        ]

        for text, command in botones_info:
            button = tk.Button(self.menu_lateral, text=text, command=command, bg="#444444", fg="#ffffff", font=("Arial", 12), relief='flat', padx=10, pady=5)
            button.pack(fill='x', pady=5)
            button.config(cursor="hand2")

        # Configuración del cuerpo principal
        self.cuerpo_principal = tk.Frame(self, bg="#ffffff")
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

        # Frame para el contenido
        self.frame_equipos = tk.Frame(self.cuerpo_principal, bg="#ffffff")
        self.frame_equipos.pack(fill='both', expand=True)

    def mostrar_pantalla_principal(self):
        self.limpiar_frame_equipos()

        label_bienvenida = tk.Label(self.frame_equipos, text="¡Bienvenidos al Mundial de Fútbol!", bg="#ffffff", fg="#333333", font=("Arial", 24))
        label_bienvenida.pack(pady=20)

    def generar_equipos(self):
        equipos = []
        nombres_equipos = [
            ("Brasil", "Tite"), ("Argentina", "Lionel Scaloni"), ("Francia", "Didier Deschamps"),
            ("Alemania", "Hansi Flick"), ("España", "Luis Enrique"), ("Inglaterra", "Gareth Southgate"),
            ("Italia", "Roberto Mancini"), ("Bélgica", "Roberto Martínez"), ("Portugal", "Fernando Santos"),
            ("Países Bajos", "Frank de Boer"), ("Croacia", "Zlatko Dalic"), ("Uruguay", "Diego Alonso"),
            ("México", "Gerardo Martino"), ("Colombia", "Reinaldo Rueda"), ("Suiza", "Murat Yakin"),
            ("Estados Unidos", "Gregg Berhalter")
            ]
            
        jugadores_por_equipo = {
            "Brasil": [("Alisson", "Portero"), ("Thiago Silva", "Defensa"), ("Marquinhos", "Defensa"),
                    ("Casemiro", "Centrocampista"), ("Neymar", "Delantero"), ("Vinícius Jr.", "Delantero"),
                    ("Richarlison", "Delantero"), ("Fabinho", "Centrocampista"), ("Eder Militão", "Defensa"),
                    ("Alex Sandro", "Defensa"), ("Fred", "Centrocampista")],
            "Argentina": [("Emiliano Martínez", "Portero"), ("Nicolás Otamendi", "Defensa"), ("Leandro Paredes", "Centrocampista"),
                        ("Lionel Messi", "Delantero"), ("Lautaro Martínez", "Delantero"), ("Ángel Di María", "Delantero"),
                        ("Rodrigo De Paul", "Centrocampista"), ("Giovani Lo Celso", "Centrocampista"), ("Lisandro Martínez", "Defensa"),
                        ("Nahuel Molina", "Defensa"), ("Marcos Acuña", "Defensa")],
            "Francia": [("Hugo Lloris", "Portero"), ("Raphaël Varane", "Defensa"), ("Presnel Kimpembe", "Defensa"),
                        ("N'Golo Kanté", "Centrocampista"), ("Paul Pogba", "Centrocampista"), ("Kylian Mbappé", "Delantero"),
                        ("Antoine Griezmann", "Delantero"), ("Olivier Giroud", "Delantero"), ("Lucas Hernández", "Defensa"),
                        ("Benjamin Pavard", "Defensa"), ("Adrien Rabiot", "Centrocampista")],
            "Alemania": [("Manuel Neuer", "Portero"), ("Mats Hummels", "Defensa"), ("Antonio Rüdiger", "Defensa"),
                        ("Joshua Kimmich", "Centrocampista"), ("Leon Goretzka", "Centrocampista"), ("Toni Kroos", "Centrocampista"),
                        ("Thomas Müller", "Delantero"), ("Serge Gnabry", "Delantero"), ("Kai Havertz", "Delantero"),
                        ("Niklas Süle", "Defensa"), ("Ilkay Gündogan", "Centrocampista")],
            "España": [("Unai Simón", "Portero"), ("Sergio Ramos", "Defensa"), ("Aymeric Laporte", "Defensa"),
                    ("Sergio Busquets", "Centrocampista"), ("Dani Olmo", "Delantero"), ("Álvaro Morata", "Delantero"),
                    ("Gerard Moreno", "Delantero"), ("Thiago", "Centrocampista"), ("Koke", "Centrocampista"),
                    ("Jordi Alba", "Defensa"), ("Eric García", "Defensa")],
            "Inglaterra": [("Jordan Pickford", "Portero"), ("Harry Maguire", "Defensa"), ("John Stones", "Defensa"),
                            ("Declan Rice", "Centrocampista"), ("Harry Kane", "Delantero"), ("Raheem Sterling", "Delantero"),
                            ("Jadon Sancho", "Delantero"), ("Phil Foden", "Centrocampista"), ("Mason Mount", "Centrocampista"),
                            ("Kyle Walker", "Defensa"), ("Ben Chilwell", "Defensa")],
            "Italia": [("Gianluigi Donnarumma", "Portero"), ("Leonardo Bonucci", "Defensa"), ("Giorgio Chiellini", "Defensa"),
                        ("Marco Verratti", "Centrocampista"), ("Lorenzo Insigne", "Delantero"), ("Ciro Immobile", "Delantero"),
                        ("Federico Chiesa", "Delantero"), ("Nicolo Barella", "Centrocampista"), ("Jorginho", "Centrocampista"),
                        ("Giovanni Di Lorenzo", "Defensa"), ("Leonardo Spinazzola", "Defensa")],
            "Bélgica": [("Thibaut Courtois", "Portero"), ("Toby Alderweireld", "Defensa"), ("Jan Vertonghen", "Defensa"),
                        ("Kevin De Bruyne", "Centrocampista"), ("Romelu Lukaku", "Delantero"), ("Eden Hazard", "Delantero"),
                        ("Dries Mertens", "Delantero"), ("Youri Tielemans", "Centrocampista"), ("Axel Witsel", "Centrocampista"),
                        ("Thomas Meunier", "Defensa"), ("Thorgan Hazard", "Defensa")],
            "Portugal": [("Rui Patrício", "Portero"), ("Rúben Dias", "Defensa"), ("Pepe", "Defensa"),
                        ("João Moutinho", "Centrocampista"), ("Cristiano Ronaldo", "Delantero"), ("Diogo Jota", "Delantero"),
                        ("Bernardo Silva", "Delantero"), ("William Carvalho", "Centrocampista"), ("João Félix", "Centrocampista"),
                        ("Raphael Guerreiro", "Defensa"), ("Nélson Semedo", "Defensa")],
            "Países Bajos": [("Maarten Stekelenburg", "Portero"), ("Matthijs de Ligt", "Defensa"), ("Stefan de Vrij", "Defensa"),
                            ("Frenkie de Jong", "Centrocampista"), ("Memphis Depay", "Delantero"), ("Georginio Wijnaldum", "Delantero"),
                            ("Donyell Malen", "Delantero"), ("Denzel Dumfries", "Defensa"), ("Davy Klaassen", "Centrocampista"),
                            ("Daley Blind", "Defensa"), ("Patrick van Aanholt", "Defensa")],
            "Croacia": [("Dominik Livaković", "Portero"), ("Domagoj Vida", "Defensa"), ("Dejan Lovren", "Defensa"),
                        ("Luka Modrić", "Centrocampista"), ("Ivan Perišić", "Delantero"), ("Andrej Kramarić", "Delantero"),
                        ("Mateo Kovačić", "Centrocampista"), ("Ante Rebić", "Delantero"), ("Josko Gvardiol", "Defensa"),
                        ("Sime Vrsaljko", "Defensa"), ("Josip Juranović", "Defensa")],
            "Uruguay": [("Fernando Muslera", "Portero"), ("Diego Godín", "Defensa"), ("José María Giménez", "Defensa"),
                        ("Nahitan Nández", "Centrocampista"), ("Luis Suárez", "Delantero"), ("Edinson Cavani", "Delantero"),
                        ("Matías Vecino", "Centrocampista"), ("Lucas Torreira", "Centrocampista"), ("Federico Valverde", "Centrocampista"),
                        ("Giovanni González", "Defensa"), ("Martín Cáceres", "Defensa")],
            "México": [("Guillermo Ochoa", "Portero"), ("Héctor Moreno", "Defensa"), ("Néstor Araujo", "Defensa"),
                        ("Héctor Herrera", "Centrocampista"), ("Raúl Jiménez", "Delantero"), ("Jesús Corona", "Delantero"),
                        ("Andrés Guardado", "Centrocampista"), ("Diego Lainez", "Centrocampista"), ("Carlos Rodríguez", "Centrocampista"),
                        ("Gerardo Arteaga", "Defensa"), ("Edson Álvarez", "Defensa")],
            "Colombia": [("David Ospina", "Portero"), ("Davinson Sánchez", "Defensa"), ("Yerry Mina", "Defensa"),
                        ("Juan Cuadrado", "Centrocampista"), ("Radamel Falcao", "Delantero"), ("Luis Díaz", "Delantero"),
                        ("James Rodríguez", "Centrocampista"), ("Matheus Uribe", "Centrocampista"), ("Wilmar Barrios", "Centrocampista"),
                        ("Stefan Medina", "Defensa"), ("William Tesillo", "Defensa")],
            "Suiza": [("Yann Sommer", "Portero"), ("Manuel Akanji", "Defensa"), ("Nico Elvedi", "Defensa"),
                        ("Granit Xhaka", "Centrocampista"), ("Haris Seferović", "Delantero"), ("Xherdan Shaqiri", "Delantero"),
                        ("Breel Embolo", "Delantero"), ("Denis Zakaria", "Centrocampista"), ("Remo Freuler", "Centrocampista"),
                        ("Kevin Mbabu", "Defensa"), ("Ricardo Rodríguez", "Defensa")],
            "Estados Unidos": [("Zack Steffen", "Portero"), ("John Brooks", "Defensa"), ("Matt Miazga", "Defensa"),
                                ("Christian Pulisic", "Centrocampista"), ("Weston McKennie", "Centrocampista"), ("Tim Weah", "Delantero"),
                                ("Josh Sargent", "Delantero"), ("Sergiño Dest", "Defensa"), ("Tyler Adams", "Centrocampista"),
                                ("Antonee Robinson", "Defensa"), ("Gio Reyna", "Delantero")]
        }

        
        for nombre, entrenador in nombres_equipos:
            equipo = Equipo(nombre, entrenador)
            if nombre in jugadores_por_equipo:
                for jugador in jugadores_por_equipo[nombre]:
                    nuevo_jugador = Jugador(jugador[0], 25, jugador[1])
                    equipo.agregar_jugador(nuevo_jugador)
            equipos.append(equipo)
        return equipos

    def generar_estadios(self):
        estadios = [
            Estadio("Estadio Azteca", "Ciudad de México", 87000),
            Estadio("Maracaná", "Río de Janeiro", 78000),
            Estadio("Wembley", "Londres", 90000),
            Estadio("Camp Nou", "Barcelona", 99354),
            Estadio("San Siro", "Milán", 80018),
            Estadio("Allianz Arena", "Múnich", 75000)
        ]
        return estadios

    def dividir_en_grupos(self):
        grupos = {}
        nombres_grupos = ["Grupo A", "Grupo B", "Grupo C", "Grupo D"]
        equipos_por_grupo = len(self.teams) // len(nombres_grupos)

        for i, nombre_grupo in enumerate(nombres_grupos):
            grupos[nombre_grupo] = self.teams[i*equipos_por_grupo:(i+1)*equipos_por_grupo]

        return grupos

    def mostrar_equipos(self):
        self.limpiar_frame_equipos()

        for grupo, equipos in self.grupos.items():
            frame_grupo = tk.Frame(self.frame_equipos, bg="#ffffff")
            frame_grupo.pack(fill='both', expand=True, pady=10)
            
            for equipo in equipos:
                frame_equipo = tk.Frame(frame_grupo, bg="#ffffff")
                frame_equipo.pack(fill='both', expand=True, pady=5)

                label_nombre = tk.Label(frame_equipo, text=f"{equipo.nombre} - Entrenador: {equipo.entrenador}", bg="#ffffff", fg="#333333", font=("Arial", 12))
                label_nombre.pack(side=tk.LEFT)

                button_alineacion = tk.Button(frame_equipo, text="Ver Alineación", bg="#444444", fg="#ffffff", font=("Arial", 10), relief='flat', padx=10, pady=5, command=lambda e=equipo: self.mostrar_alineacion(e))
                button_alineacion.pack(side=tk.RIGHT)
                button_alineacion.config(cursor="hand2")

    def mostrar_alineacion(self, equipo):
        self.limpiar_frame_equipos()

        label_titulo = tk.Label(self.frame_equipos, text=f"Alineación de {equipo.nombre}", bg="#ffffff", fg="#333333", font=("Arial", 16, "bold"))
        label_titulo.pack(pady=10)

        for jugador in equipo.jugadores:
            label_jugador = tk.Label(self.frame_equipos, text=f"{jugador.nombre} - Posición: {jugador.posicion}", bg="#ffffff", fg="#333333", font=("Arial", 12))
            label_jugador.pack()

    def mostrar_estadios(self):
        self.limpiar_frame_equipos()

        scrollbar = tk.Scrollbar(self.frame_equipos)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        tree = ttk.Treeview(self.frame_equipos, yscrollcommand=scrollbar.set)
        tree["columns"] = ("Estadio", "Ciudad", "Capacidad")
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Estadio", anchor=tk.W, width=150)
        tree.column("Ciudad", anchor=tk.W, width=150)
        tree.column("Capacidad", anchor=tk.W, width=150)
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("Estadio", text="Estadio", anchor=tk.W)
        tree.heading("Ciudad", text="Ciudad", anchor=tk.W)
        tree.heading("Capacidad", text="Capacidad", anchor=tk.W)

        for estadio in self.estadios:
            tree.insert("", "end", values=(estadio.nombre, estadio.ciudad, estadio.capacidad))

        tree.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=tree.yview)

    def mostrar_grupos(self):
        self.limpiar_frame_equipos()

        for grupo, equipos in self.grupos.items():
            frame_grupo = tk.Frame(self.frame_equipos, bg="#ffffff")
            frame_grupo.pack(fill='both', expand=True, pady=10)

            label_grupo = tk.Label(frame_grupo, text=grupo, bg="#ffffff", fg="#333333", font=("Arial", 14, "bold"))
            label_grupo.pack()

            for equipo in equipos:
                frame_equipo = tk.Frame(frame_grupo, bg="#ffffff")
                frame_equipo.pack(fill='both', expand=True, pady=5)

                label_nombre = tk.Label(frame_equipo, text=f"{equipo.nombre} - {equipo.victorias} Pts", bg="#ffffff", fg="#333333", font=("Arial", 12))
                label_nombre.pack(side=tk.LEFT)

                button_alineacion = tk.Button(frame_equipo, text="Ver Alineación", bg="#444444", fg="#ffffff", font=("Arial", 10), relief='flat', padx=10, pady=5, command=lambda e=equipo: self.mostrar_alineacion(e))
                button_alineacion.pack(side=tk.RIGHT)
                button_alineacion.config(cursor="hand2")

    def generar_resultados(self):
        resultados = {}
        for grupo, equipos in self.grupos.items():
            resultados[grupo] = {}
            for i in range(len(equipos)):
                for j in range(i + 1, len(equipos)):
                    equipo1 = equipos[i]
                    equipo2 = equipos[j]
                    resultado = (random.randint(0, 5), random.randint(0, 5))
                    resultados[grupo][(equipo1.nombre, equipo2.nombre)] = resultado
                    if resultado[0] > resultado[1]:
                        equipo1.victorias += 3
                    elif resultado[0] < resultado[1]:
                        equipo2.victorias += 3
                    else:
                        equipo1.victorias += 1
                        equipo2.victorias += 1
        return resultados

    def mostrar_partidos(self):
        self.limpiar_frame_equipos()

        for grupo, partidos in self.resultados.items():
            frame_grupo = tk.Frame(self.frame_equipos, bg="#ffffff")
            frame_grupo.pack(fill='both', expand=True, pady=10)

            label_grupo = tk.Label(frame_grupo, text=grupo, bg="#ffffff", fg="#333333", font=("Arial", 14, "bold"))
            label_grupo.pack()

            for equipos, resultado in partidos.items():
                partido = f"{equipos[0]} vs {equipos[1]}"
                resultado_texto = f"{resultado[0]} - {resultado[1]}"
                label_partido = tk.Label(frame_grupo, text=f"{partido}: {resultado_texto}", bg="#ffffff", fg="#333333", font=("Arial", 12))
                label_partido.pack(anchor="w")

    def mostrar_octavos(self):
        self.limpiar_frame_equipos()

        octavos_equipos = {}
        for grupo, equipos in self.grupos.items():
            clasificados = sorted(equipos, key=lambda x: (-x.victorias, random.random()))[:2]
            octavos_equipos[grupo] = clasificados

        octavos_combinaciones = [
            (octavos_equipos["Grupo A"][0], octavos_equipos["Grupo B"][1]),
            (octavos_equipos["Grupo A"][1], octavos_equipos["Grupo B"][0]),
            (octavos_equipos["Grupo C"][0], octavos_equipos["Grupo D"][1]),
            (octavos_equipos["Grupo C"][1], octavos_equipos["Grupo D"][0]),
            (octavos_equipos["Grupo B"][0], octavos_equipos["Grupo A"][1]),
            (octavos_equipos["Grupo B"][1], octavos_equipos["Grupo A"][0]),
            (octavos_equipos["Grupo D"][0], octavos_equipos["Grupo C"][1]),
            (octavos_equipos["Grupo D"][1], octavos_equipos["Grupo C"][0])
        ]

        self.octavos_resultados = {}
        for i, (equipo1, equipo2) in enumerate(octavos_combinaciones, start=1):
            resultado = (random.randint(0, 5), random.randint(0, 5))
            self.octavos_resultados[f"Partido {i}"] = (equipo1, equipo2, resultado)

        label_titulo = tk.Label(self.frame_equipos, text="Resultados de Octavos de Final", bg="#ffffff", fg="#333333", font=("Arial", 16, "bold"))
        label_titulo.pack(pady=10)

        for partido, (equipo1, equipo2, resultado) in self.octavos_resultados.items():
            label_partido = tk.Label(self.frame_equipos, text=f"{equipo1.nombre} vs {equipo2.nombre}: {resultado[0]} - {resultado[1]}", bg="#ffffff", fg="#333333", font=("Arial", 12))
            label_partido.pack()

    def mostrar_cuartos_final(self):
        self.limpiar_frame_equipos()

        cuartos_equipos = [self.octavos_resultados[f"Partido {i}"][random.randint(0, 1)] for i in range(1, 9)]

        cuartos_combinaciones = [
            (cuartos_equipos[0], cuartos_equipos[1]),
            (cuartos_equipos[2], cuartos_equipos[3]),
            (cuartos_equipos[4], cuartos_equipos[5]),
            (cuartos_equipos[6], cuartos_equipos[7])
        ]

        self.cuartos_resultados = {}
        for i, (equipo1, equipo2) in enumerate(cuartos_combinaciones, start=1):
            resultado = (random.randint(0, 5), random.randint(0, 5))
            self.cuartos_resultados[f"Partido {i}"] = (equipo1, equipo2, resultado)

        label_titulo = tk.Label(self.frame_equipos, text="Resultados de Cuartos de Final", bg="#ffffff", fg="#333333", font=("Arial", 16, "bold"))
        label_titulo.pack(pady=10)

        for partido, (equipo1, equipo2, resultado) in self.cuartos_resultados.items():
            label_partido = tk.Label(self.frame_equipos, text=f"{equipo1.nombre} vs {equipo2.nombre}: {resultado[0]} - {resultado[1]}", bg="#ffffff", fg="#333333", font=("Arial", 12))
            label_partido.pack()

    # Funciones para mostrar semifinales y final
    def mostrar_semifinal(self):
        self.limpiar_frame_equipos()

        semifinal_equipos = [self.cuartos_resultados[f"Partido {i}"][random.randint(0, 1)] for i in range(1, 5)]

        semifinal_combinaciones = [
            (semifinal_equipos[0], semifinal_equipos[1]),
            (semifinal_equipos[2], semifinal_equipos[3])
        ]

        self.semifinal_resultados = {}
        for i, (equipo1, equipo2) in enumerate(semifinal_combinaciones, start=1):
            resultado = (random.randint(0, 5), random.randint(0, 5))
            self.semifinal_resultados[f"Partido {i}"] = (equipo1, equipo2, resultado)

        label_titulo = tk.Label(self.frame_equipos, text="Resultados de Semifinales", bg="#ffffff", fg="#333333", font=("Arial", 16, "bold"))
        label_titulo.pack(pady=10)

        for partido, (equipo1, equipo2, resultado) in self.semifinal_resultados.items():
            label_partido = tk.Label(self.frame_equipos, text=f"{equipo1.nombre} vs {equipo2.nombre}: {resultado[0]} - {resultado[1]}", bg="#ffffff", fg="#333333", font=("Arial", 12))
            label_partido.pack()

    def mostrar_final(self):
        self.limpiar_frame_equipos()

        equipos_final = [self.semifinal_resultados[f"Partido {i}"][random.randint(0, 1)] for i in range(1, 3)]
        resultado_final = (random.randint(0, 5), random.randint(0, 5))

        label_titulo = tk.Label(self.frame_equipos, text="Resultado de la Final", bg="#ffffff", fg="#333333", font=("Arial", 16, "bold"))
        label_titulo.pack(pady=10)

        label_partido = tk.Label(self.frame_equipos, text=f"{equipos_final[0].nombre} vs {equipos_final[1].nombre}: {resultado_final[0]} - {resultado_final[1]}", bg="#ffffff", fg="#333333", font=("Arial", 12))
        label_partido.pack()

    def limpiar_frame_equipos(self):
        for widget in self.frame_equipos.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MundialGUI()
    app.mainloop()
