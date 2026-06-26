"""
indy_agent_skeleton.py
======================
Esqueleto de clases para el agente Indy.
proyecto final bootcamp data science 2026 · the bridge

estructura orientada a objetos — cada clase encapsula su propia lógica.
IndyAgent orquesta todo sin saber cómo trabaja cada tool por dentro.
"""

import sqlite3
import requests
from abc import ABC, abstractmethod
from datetime import datetime


# ─────────────────────────────────────────────
# CLASE BASE: Tool
# todas las tools heredan de aquí
# ─────────────────────────────────────────────

class Tool(ABC):
    """clase base para todas las herramientas de Indy."""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def run(self, movie_title: str) -> dict:
        """lógica principal de cada tool. obligatorio implementar."""
        pass

    def validate_input(self, movie_title: str) -> bool:
        """comprueba que el input no está vacío."""
        return isinstance(movie_title, str) and len(movie_title.strip()) > 0

    def __repr__(self):
        return f"Tool(name={self.name})"


# ─────────────────────────────────────────────
# TOOL 1: MovieDataTool
# busca metadatos básicos de la película
# ─────────────────────────────────────────────

class MovieDataTool(Tool):
    """obtiene título, año, género, sinopsis y reparto desde OMDb."""

    def __init__(self, api_key: str):
        super().__init__(
            name="movie_data",
            description="busca metadatos básicos de la película en OMDb"
        )
        self.api_key = api_key
        self.base_url = "http://www.omdbapi.com/"

    def run(self, movie_title: str) -> dict:
        if not self.validate_input(movie_title):
            return {"error": "título inválido"}

        params = {
            "t": movie_title,
            "apikey": self.api_key,
            "plot": "full"
        }
        # aquí iría la llamada real a la API
        # response = requests.get(self.base_url, params=params)
        # return response.json()

        # placeholder para desarrollo
        return {
            "title": movie_title,
            "year": None,
            "genre": None,
            "plot": None,
            "director": None,
            "actors": None,
            "runtime": None,
            "source": "omdb"
        }


# ─────────────────────────────────────────────
# TOOL 2: ScoreFetcherTool
# obtiene puntuaciones y detecta divergencia críticos vs público
# ─────────────────────────────────────────────

class ScoreFetcherTool(Tool):
    """recopila puntuaciones de múltiples fuentes y detecta divergencia."""

    def __init__(self, api_key: str):
        super().__init__(
            name="score_fetcher",
            description="obtiene puntuaciones de imdb, rt, metacritic y calcula divergencia"
        )
        self.api_key = api_key

    def run(self, movie_title: str) -> dict:
        if not self.validate_input(movie_title):
            return {"error": "título inválido"}

        scores = self._fetch_scores(movie_title)
        divergence = self._detect_divergence(scores)

        return {
            "scores": scores,
            "divergence": divergence,
            "public_score": scores.get("imdb_audience"),
            "critic_score": scores.get("metacritic")
        }

    def _fetch_scores(self, movie_title: str) -> dict:
        """llama a OMDb para obtener ratings de múltiples fuentes."""
        # placeholder — OMDb devuelve RT, Metacritic e IMDb en una sola llamada
        return {
            "imdb_audience": None,   # 0-10
            "rotten_tomatoes": None, # 0-100
            "metacritic": None,      # 0-100
            "filmaffinity": None     # 0-10, requiere scraping
        }

    def _detect_divergence(self, scores: dict) -> dict:
        """calcula si hay gap significativo entre crítica y público."""
        # lógica: si la diferencia normalizada > umbral → divergencia detectada
        return {
            "detected": False,
            "gap": None,
            "favors": None  # "audience" o "critics"
        }


# ─────────────────────────────────────────────
# TOOL 3: StreamingCheckerTool
# plataformas donde ver la peli en España
# ─────────────────────────────────────────────

class StreamingCheckerTool(Tool):
    """comprueba disponibilidad en plataformas de streaming en España."""

    def __init__(self):
        super().__init__(
            name="streaming_checker",
            description="busca en qué plataformas está disponible la peli en España"
        )
        self.country = "ES"

    def run(self, movie_title: str) -> dict:
        if not self.validate_input(movie_title):
            return {"error": "título inválido"}

        # aquí iría la consulta a JustWatch API o scraping
        return {
            "available": [],        # ["Netflix", "HBO Max", etc.]
            "rent": [],             # plataformas donde alquilar
            "buy": [],              # plataformas donde comprar
            "country": self.country,
            "source": "justwatch"
        }


# ─────────────────────────────────────────────
# TOOL 4: VerdictBuilderTool
# genera el veredicto ajustado por perfil de espectador
# ─────────────────────────────────────────────

class VerdictBuilderTool(Tool):
    """genera el veredicto final ajustado a 7 perfiles de espectador."""

    PROFILES = [
        "El Palomitero",
        "El Emocional",
        "El Cinéfilo",
        "El Risas",
        "El Adrenalínico",
        "El Curioso",
        "El Familiar"
    ]

    def __init__(self, llm_client):
        super().__init__(
            name="verdict_builder",
            description="emite veredicto final con análisis por perfil de espectador"
        )
        self.llm_client = llm_client

    def run(self, movie_title: str, context: dict = None) -> dict:
        """context contiene scores, metadata y resto de datos recogidos."""
        if not self.validate_input(movie_title):
            return {"error": "título inválido"}

        profile_verdicts = self._build_profile_verdicts(context)
        final_verdict = self._build_final_verdict(context)
        snack = self._suggest_snack(context)
        twist_index = self._calculate_twist_index(context)

        return {
            "final_verdict": final_verdict,       # "sí merece la pena" / "pasa de ella"
            "profile_verdicts": profile_verdicts,  # dict con los 7 perfiles
            "twist_index": twist_index,            # 0-10
            "post_credits": None,                  # True/False/None
            "snack_pairing": snack,
            "time_cost": None                      # actividades alternativas
        }

    def _build_profile_verdicts(self, context: dict) -> dict:
        """devuelve veredicto personalizado para cada perfil."""
        return {profile: None for profile in self.PROFILES}

    def _build_final_verdict(self, context: dict) -> str:
        """veredicto global priorizando opinión del público."""
        return None

    def _suggest_snack(self, context: dict) -> str:
        """maridaje de snack según género de la película."""
        return None

    def _calculate_twist_index(self, context: dict) -> int:
        """índice de sorpresa/giro del 0 al 10."""
        return None


# ─────────────────────────────────────────────
# TOOL 5: CanineAlertTool 🐾
# easter egg — solo se activa si hay perro relevante
# ─────────────────────────────────────────────

class CanineAlertTool(Tool):
    """
    detecta si hay un perro con papel relevante en la película.
    easter egg: solo aparece en el informe si has_dog == True.
    consulta DoesTheDogDie API si detecta presencia canina.
    """

    DOESTHEDOG_URL = "https://www.doesthedogdie.com/media"

    def __init__(self, llm_client):
        super().__init__(
            name="canine_alert",
            description="alerta canina: ¿hay perro? ¿sobrevive? 🐾"
        )
        self.llm_client = llm_client

    def run(self, movie_title: str) -> dict:
        if not self.validate_input(movie_title):
            return {"error": "título inválido"}

        has_dog = self._detect_dog_presence(movie_title)

        if not has_dog:
            return {"has_dog": False}  # sin perro → no aparece en el informe

        survival = self._check_survival(movie_title)

        return {
            "has_dog": True,
            "dog_name": survival.get("dog_name"),
            "survives": survival.get("survives"),   # True / False / "unknown"
            "source": survival.get("source")
        }

    def _detect_dog_presence(self, movie_title: str) -> bool:
        """pregunta al LLM si hay perro relevante en la peli."""
        # aquí iría la llamada al LLM con un prompt específico
        return False  # placeholder

    def _check_survival(self, movie_title: str) -> dict:
        """consulta DoesTheDogDie. si no hay datos, devuelve 'unknown'."""
        # aquí iría la llamada a la API de DoesTheDogDie
        return {
            "dog_name": None,
            "survives": "unknown",
            "source": "doesthedogdie"
        }


# ─────────────────────────────────────────────
# TOOL 6: MarathonModeTool
# modo maratón para sagas y universos compartidos
# ─────────────────────────────────────────────

class MarathonModeTool(Tool):
    """detecta si la peli pertenece a una saga y sugiere orden de visionado."""

    def __init__(self, llm_client):
        super().__init__(
            name="marathon_mode",
            description="modo maratón: orden de visionado para sagas y universos"
        )
        self.llm_client = llm_client

    def run(self, movie_title: str) -> dict:
        if not self.validate_input(movie_title):
            return {"error": "título inválido"}

        return {
            "is_saga": False,
            "saga_name": None,
            "total_movies": None,
            "watch_order": [],      # lista ordenada
            "current_position": None
        }


# ─────────────────────────────────────────────
# TOOL 7: IndysPickTool
# recomienda una película alternativa menos conocida
# ─────────────────────────────────────────────

class IndysPickTool(Tool):
    """Indy's Pick: sugiere una alternativa oscura similar a la consultada."""

    def __init__(self, llm_client):
        super().__init__(
            name="indys_pick",
            description="recomienda una joya oculta del mismo palo que la consultada"
        )
        self.llm_client = llm_client

    def run(self, movie_title: str, context: dict = None) -> dict:
        if not self.validate_input(movie_title):
            return {"error": "título inválido"}

        return {
            "title": None,
            "year": None,
            "reason": None,     # por qué Indy la recomienda
            "where_to_watch": None
        }


# ─────────────────────────────────────────────
# Database
# gestiona SQLite — historial e informes
# ─────────────────────────────────────────────

class Database:
    """gestiona la conexión y operaciones con SQLite."""

    def __init__(self, db_path: str = "indy_reports.db"):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """abre conexión con la base de datos."""
        self.connection = sqlite3.connect(self.db_path)
        return self

    def disconnect(self):
        """cierra la conexión."""
        if self.connection:
            self.connection.close()
            self.connection = None

    def create_tables(self):
        """crea las tablas si no existen."""
        query = """
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_title TEXT NOT NULL,
            query_date TEXT NOT NULL,
            final_verdict TEXT,
            scores TEXT,          -- JSON serializado
            streaming TEXT,       -- JSON serializado
            full_report TEXT,     -- JSON serializado completo
            has_dog BOOLEAN DEFAULT FALSE
        );
        """
        self.connection.execute(query)
        self.connection.commit()

    def save_report(self, report: dict) -> int:
        """guarda el informe completo. devuelve el id generado."""
        import json
        query = """
        INSERT INTO reports (movie_title, query_date, final_verdict, scores, streaming, full_report, has_dog)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor = self.connection.execute(query, (
            report.get("title"),
            datetime.now().isoformat(),
            report.get("final_verdict"),
            json.dumps(report.get("scores", {})),
            json.dumps(report.get("streaming", {})),
            json.dumps(report),
            report.get("has_dog", False)
        ))
        self.connection.commit()
        return cursor.lastrowid

    def get_history(self, movie_title: str = None) -> list:
        """devuelve historial. si se pasa título, filtra por película."""
        if movie_title:
            query = "SELECT * FROM reports WHERE movie_title LIKE ? ORDER BY query_date DESC"
            cursor = self.connection.execute(query, (f"%{movie_title}%",))
        else:
            query = "SELECT * FROM reports ORDER BY query_date DESC"
            cursor = self.connection.execute(query)
        return cursor.fetchall()

    def already_queried(self, movie_title: str) -> bool:
        """comprueba si ya existe un informe de esa peli (caché)."""
        cursor = self.connection.execute(
            "SELECT id FROM reports WHERE movie_title = ?", (movie_title,)
        )
        return cursor.fetchone() is not None

    def __enter__(self):
        self.connect()
        self.create_tables()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()


# ─────────────────────────────────────────────
# ReportBuilder
# construye el informe final a partir de todos los datos
# ─────────────────────────────────────────────

class ReportBuilder:
    """ensambla el informe final a partir de los resultados de cada tool."""

    def build(self, movie_data: dict, scores: dict, streaming: dict,
              verdict: dict, canine: dict = None, marathon: dict = None,
              indys_pick: dict = None) -> dict:
        """combina todos los datos en un único informe estructurado."""

        report = {
            "title": movie_data.get("title"),
            "year": movie_data.get("year"),
            "genre": movie_data.get("genre"),
            "runtime": movie_data.get("runtime"),
            "scores": scores.get("scores"),
            "divergence": scores.get("divergence"),
            "streaming": streaming.get("available"),
            "final_verdict": verdict.get("final_verdict"),
            "profile_verdicts": verdict.get("profile_verdicts"),
            "twist_index": verdict.get("twist_index"),
            "post_credits": verdict.get("post_credits"),
            "snack_pairing": verdict.get("snack_pairing"),
            "time_cost": verdict.get("time_cost"),
            "has_dog": canine.get("has_dog") if canine else False,
            "canine_alert": canine if canine and canine.get("has_dog") else None,
            "marathon_mode": marathon if marathon and marathon.get("is_saga") else None,
            "indys_pick": indys_pick,
            "generated_at": datetime.now().isoformat()
        }

        return report

    def format_for_display(self, report: dict) -> str:
        """formatea el informe para mostrarlo en terminal o Streamlit."""
        # aquí iría el formateo final — depende de la interfaz elegida
        return str(report)


# ─────────────────────────────────────────────
# IndyAgent
# el cerebro — orquesta el loop ReAct
# ─────────────────────────────────────────────

class IndyAgent:
    """
    agente principal. orquesta todas las tools siguiendo el patrón ReAct:
    Reason → Act → Observe → Reason → ...
    no termina hasta que ha emitido veredicto Y guardado en SQLite.
    """

    def __init__(self, config: dict):
        """
        config debe contener:
        - omdb_api_key
        - llm_client (instancia del cliente LLM)
        - db_path (opcional, default: indy_reports.db)
        """
        self.config = config
        self.db = Database(config.get("db_path", "indy_reports.db"))
        self.report_builder = ReportBuilder()

        # registro de tools disponibles
        self.tools = {
            "movie_data": MovieDataTool(config["omdb_api_key"]),
            "score_fetcher": ScoreFetcherTool(config["omdb_api_key"]),
            "streaming_checker": StreamingCheckerTool(),
            "verdict_builder": VerdictBuilderTool(config["llm_client"]),
            "canine_alert": CanineAlertTool(config["llm_client"]),
            "marathon_mode": MarathonModeTool(config["llm_client"]),
            "indys_pick": IndysPickTool(config["llm_client"])
        }

        self.max_iterations = 10  # guardrail: evita bucles infinitos
        self.iteration_count = 0

    def run(self, movie_title: str) -> dict:
        """
        loop principal del agente.
        no para hasta: veredicto emitido + informe guardado en SQLite.
        """
        print(f"\n🐾 Indy arrancando análisis: '{movie_title}'\n")

        self.iteration_count = 0
        context = {"movie_title": movie_title}

        # comprueba caché — ¿ya analizamos esta peli?
        with self.db as db:
            if db.already_queried(movie_title):
                print("📦 encontrado en caché — recuperando informe anterior")
                return db.get_history(movie_title)[0]

        # loop ReAct
        while self.iteration_count < self.max_iterations:
            self.iteration_count += 1
            action = self._reason(context)

            if action == "done":
                break

            result = self._act(action, movie_title, context)
            context = self._observe(action, result, context)

        # construye y guarda el informe final
        report = self._build_and_save(movie_title, context)
        return report

    def _reason(self, context: dict) -> str:
        """
        decide qué tool ejecutar a continuación según el estado actual.
        devuelve el nombre de la tool o 'done' si el ciclo está completo.
        """
        if "movie_data" not in context:
            return "movie_data"
        if "scores" not in context:
            return "score_fetcher"
        if "streaming" not in context:
            return "streaming_checker"
        if "canine" not in context:
            return "canine_alert"
        if "marathon" not in context:
            return "marathon_mode"
        if "indys_pick" not in context:
            return "indys_pick"
        if "verdict" not in context:
            return "verdict_builder"
        return "done"

    def _act(self, action: str, movie_title: str, context: dict) -> dict:
        """ejecuta la tool indicada."""
        print(f"  → ejecutando: {action}")
        tool = self.tools.get(action)
        if not tool:
            return {"error": f"tool '{action}' no encontrada"}

        if action == "verdict_builder":
            return tool.run(movie_title, context)
        return tool.run(movie_title)

    def _observe(self, action: str, result: dict, context: dict) -> dict:
        """actualiza el contexto con el resultado de la tool."""
        key_map = {
            "movie_data": "movie_data",
            "score_fetcher": "scores",
            "streaming_checker": "streaming",
            "verdict_builder": "verdict",
            "canine_alert": "canine",
            "marathon_mode": "marathon",
            "indys_pick": "indys_pick"
        }
        key = key_map.get(action, action)
        context[key] = result
        return context

    def _build_and_save(self, movie_title: str, context: dict) -> dict:
        """construye el informe final y lo guarda en SQLite."""
        report = self.report_builder.build(
            movie_data=context.get("movie_data", {}),
            scores=context.get("scores", {}),
            streaming=context.get("streaming", {}),
            verdict=context.get("verdict", {}),
            canine=context.get("canine"),
            marathon=context.get("marathon"),
            indys_pick=context.get("indys_pick")
        )

        with self.db as db:
            report_id = db.save_report(report)
            print(f"\n✅ informe guardado en SQLite — id: {report_id}")

        return report


# ─────────────────────────────────────────────
# punto de entrada (para pruebas)
# ─────────────────────────────────────────────

if __name__ == "__main__":
    # configuración mínima para probar el esqueleto
    config = {
        "omdb_api_key": "TU_API_KEY_AQUI",
        "llm_client": None,   # aquí irá el cliente real (Groq, OpenAI, etc.)
        "db_path": "indy_reports.db"
    }

    agent = IndyAgent(config)
    report = agent.run("John Wick")
    print("\n📋 Informe generado:")
    print(report)
