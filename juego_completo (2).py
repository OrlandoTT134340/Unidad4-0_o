import json
import random


class Jugador:
    def __init__(self, nombre, puntaje=0):
        self.nombre = nombre
        self.puntaje = puntaje


class Ranking:
    def __init__(self, archivo="ranking.json"):
        self.archivo = archivo
        self.registros = self.cargar()

    def cargar(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def guardar_puntaje(self, jugador):
        if jugador:
            self.registros.append({"nombre": jugador.nombre, "puntaje": jugador.puntaje})
            self.registros.sort(key=lambda x: x["puntaje"], reverse=True)
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(self.registros, f, indent=2, ensure_ascii=False)

    def mostrar(self):
        print("\n--- RANKING DE JUGADORES ---")
        if not self.registros:
            print("Aún no hay puntajes registrados.")
        for i, reg in enumerate(self.registros, start=1):
            print(f"{i}. {reg['nombre']}: {reg['puntaje']} pts")


class Pregunta:
    def __init__(self, texto, dificultad, respuesta_correcta):
        self.texto = texto
        self.dificultad = dificultad
        self.respuesta_correcta = respuesta_correcta

    def esta_correcto(self, respuesta):
        return str(respuesta).strip().lower() == str(self.respuesta_correcta).strip().lower()

    def calcular_puntaje(self, respuesta_o_flag):
        puntos = {"facil": 10, "media": 20, "dificil": 30}
        return puntos.get(self.dificultad.lower(), 10)


class PreguntaMultiple(Pregunta):
    def __init__(self, texto, dificultad, opciones, respuesta_correcta):
        super().__init__(texto, dificultad, respuesta_correcta)
        self.opciones = opciones


class PreguntaVF(Pregunta):
    def __init__(self, texto, dificultad, respuesta_correcta):
        super().__init__(texto, dificultad, respuesta_correcta)


def cargar_preguntas(ruta="preguntas.json"):
    lista_objetos = []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for item in datos:
                tipo = item.get("tipo", "").lower()
                texto = item.get("texto", "")
                dificultad = item.get("dificultad", "facil")
                respuesta = item.get("respuesta", "")

                if tipo in ("multiple", "opcion_multiple"):
                    opciones = item.get("opciones", [])
                    lista_objetos.append(PreguntaMultiple(texto, dificultad, opciones, respuesta))
                elif tipo in ("vf", "verdadero_falso"):
                    lista_objetos.append(PreguntaVF(texto, dificultad, respuesta))
    except Exception as e:
        print(f"Error al cargar preguntas: {e}")
    return lista_objetos


def hacer_prueba(preguntas):
    puntaje_obtenido = 0
    for i, p in enumerate(preguntas, start=1):
        print(f"\nPregunta {i} [{p.dificultad}]: {p.texto}")
        if isinstance(p, PreguntaMultiple):
            for idx, op in enumerate(p.opciones, start=1):
                print(f"  {idx}. {op}")
            resp = input("Escribe tu respuesta: ")
        else:
            resp = input("Escribe Verdadero o Falso: ")

        if p.esta_correcto(resp):
            pts = p.calcular_puntaje(0)
            puntaje_obtenido += pts
            print(f"¡Correcto! +{pts} puntos.")
        else:
            print(f"Incorrecto. La respuesta era: {p.respuesta_correcta}")
    return puntaje_obtenido


class Juego:
    def __init__(self):
        self.jugador = None
        self.preguntas = []
        self.ranking = Ranking()

    def registrar_jugador(self):
        nombre = input("Ingresa el nombre del jugador: ").strip()
        if nombre:
            self.jugador = Jugador(nombre)
            print(f"Jugador '{self.jugador.nombre}' registrado.")

    def cargar_preguntas(self):
        ruta = input("Ruta del archivo JSON (Enter para 'preguntas.json'): ").strip()
        if not ruta:
            ruta = "preguntas.json"
        self.preguntas = cargar_preguntas(ruta)
        print(f"Se cargaron {len(self.preguntas)} preguntas.")

    def jugar_ronda(self):
        if not self.jugador:
            print("Primero debes registrar un jugador.")
            return
        if not self.preguntas:
            print("Primero debes cargar las preguntas.")
            return
        seleccion = random.sample(self.preguntas, min(3, len(self.preguntas)))
        puntos = hacer_prueba(seleccion)
        self.jugador.puntaje += puntos
        print(f"\nPuntaje acumulado de {self.jugador.nombre}: {self.jugador.puntaje}")

    def ver_ranking(self):
        self.ranking.mostrar()

    def menu(self):
        while True:
            print("\n=== MENÚ PRINCIPAL ===")
            print("1. Registrar jugador")
            print("2. Cargar preguntas")
            print("3. Jugar ronda")
            print("4. Ver ranking")
            print("5. Salir")
            opcion = input("Elige una opción: ").strip()

            if opcion == "1":
                self.registrar_jugador()
            elif opcion == "2":
                self.cargar_preguntas()
            elif opcion == "3":
                self.jugar_ronda()
            elif opcion == "4":
                self.ver_ranking()
            elif opcion == "5":
                if self.jugador:
                    self.ranking.guardar_puntaje(self.jugador)
                    print("Puntaje guardado en el ranking.")
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida.")


if __name__ == "__main__":
    app = Juego()
    app.menu()
