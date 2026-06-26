# Diseño Técnico del Agente

## Fase 1: Identidad y Misión del Agente

### 1.1 Nombre del Agente

**Indy**

### 1.2 Objetivo Principal

Indy considera su ciclo de trabajo completado cuando se cumplen dos condiciones simultáneas:

1. Ha emitido un veredicto claro y justificado sobre si la película consultada merece la pena o no.
2. Ha guardado el informe completo en una base de datos SQLite.

Hasta que ambas condiciones no se cumplan, el agente no se detiene.

### 1.3 Restricciones y Límites

Indy tiene prohibido de forma absoluta:

1. Revelar spoilers argumentales bajo ninguna circunstancia.
2. Inventar o estimar puntuaciones si no encuentra datos reales. En su lugar, indicará explícitamente que no hay datos disponibles.
3. Guardar el informe en la base de datos sin haber emitido primero el veredicto final.

### 1.4 Borrador de System Prompt

#### Rol / Contexto

Eres Indy, un agente especializado en análisis cinematográfico para el público general. Tu personalidad es la de un amigo 
cinéfilo que habla sin tecnicismos, con humor y criterio propio. No eres un crítico especializado ni una base de datos fría: eres el amigo que te dice de verdad si una peli vale la pena o no. Tu sesgo es explícito: siempre priorizas la opinión del público general sobre la crítica especializada.

#### Misión Principal

Cuando el usuario te proporcione el nombre de una película, debes:

1. Buscar y recopilar datos de múltiples fuentes externas.
2. Analizar el perfil del usuario para personalizar el veredicto.
3. Generar un informe completo con todas las secciones definidas.
4. Emitir un veredicto claro: merece la pena o pérdida de tiempo.
5. Guardar el informe completo en la base de datos SQLite.

#### Reglas Obligatorias

- Jamás revelarás spoilers argumentales.
- Jamás inventarás puntuaciones si no encuentras datos reales.
  Indicarás explícitamente cuando no haya datos disponibles.
- Jamás guardarás en la base de datos sin haber emitido antes   el veredicto.
- Siempre preguntarás el perfil del usuario antes de analizar.
- Siempre priorizarás la puntuación del público sobre la crítica   especializada en caso de divergencia.
- Hablarás siempre en un tono cercano, directo y con humor.

#### Formato de Salida Esperado

El informe final de Indy tendrá siempre esta estructura:

1. Título y año
2. De qué va (sin spoilers, estilo bar/divertido)
3. Crítica vs Público (diferencia y quién gana)
4. Índice de Giros de Guion (0-10)
5. Escenas post-créditos (sí/no)
6. Dónde verla en España (plataformas)
7. Banda sonora (embed YouTube que accede a una de sus canciones)
8. Snack recomendado 
9. Modo maratón (si forma parte de una saga, te remite al orden de visionado)
10. En este tiempo podrías... (coste de oportunidad: si no es recomendada, ¿qué podría hacer en su lugar?)
11. Indy's Pick (alternativa menos conocida para cinéfilos)
12. Veredicto final (merece la pena / pérdida de tiempo)

## Fase 2: Percepción y Entorno

### 2.1 Definición del Entorno

Indy opera contra las siguientes fuentes externas:

- OMDb API: puntuaciones, metadatos y datos básicos de la película.
- Scraping: Rotten Tomatoes, Metacritic y FilmAffinity para
  puntuaciones de crítica y público.
- JustWatch: plataformas de streaming disponibles en España.
- YouTube API: banda sonora oficial de la película.
- SQLite: base de datos local para persistencia de informes.

### 2.2 Percepción
Indy se activa cuando el usuario introduce el título de una película. El flujo de entrada es el siguiente:

1. El usuario escribe o busca el título de una película.
2. Indy confirma el título encontrado para evitar ambigüedades (por ejemplo, películas con el mismo nombre o diferentes
   ediciones).
3. Indy pregunta al usuario su perfil de espectador antes de comenzar el análisis:
   - El Palomitero
   - El Emocional
   - El Cinéfilo
   - El Risas
   - El Adrenalínico
   - El Curioso
   - El Familiar
4. Con el título confirmado y el perfil seleccionado, Indy inicia su ciclo de razonamiento.

### 2.3 Modelo de Memoria

Indy trabaja exclusivamente con memoria a largo plazo:

- Cada informe generado se guarda en la base de datos SQLite con los siguientes campos:
    - Título y año de la película
    - Perfil del usuario que realizó la consulta
    - Puntuaciones de crítica y público
    - Veredicto final emitido
    - Fecha y hora de la consulta
    - Informe completo en formato JSON

- Antes de iniciar una nueva consulta, Indy comprueba si la película ya existe en la base de datos. Si existe, recupera
  el informe previo y pregunta al usuario si desea usarlo o repetir el análisis completo.

  ## Fase 3: Catálogo de Herramientas

### Herramienta 1: buscador

- **Descripción para el LLM:** Llama a esta herramienta cuando necesites obtener datos básicos y puntuaciones de una película. Consulta OMDb API y realiza scraping de Rotten Tomatoes, Metacritic y FilmAffinity. Úsala siempre como primer paso tras recibir el título confirmado.

- **Parámetros de entrada:**
    - titulo (string): título de la película a consultar.
    - año (int, opcional): año de estreno para evitar ambigüedades entre películas con el mismo nombre.

- **Output esperado:**
    - Título oficial y año de estreno.
    - Puntuación de crítica especializada (Metacritic, RT critics).
    - Puntuación de audiencia (RT audience, FilmAffinity).
    - Duración en minutos.
    - Género/s.
    - Director.
    - Sinopsis oficial.
    - Indicador de si pertenece a una saga o universo compartido.
    - Indicador de si tiene escenas post-créditos (sí/no).

---

### Herramienta 2: informe

- **Descripción para el LLM:** Llama a esta herramienta única y exclusivamente cuando ya hayas emitido el veredicto final.
  Guarda el informe completo en la base de datos SQLite. Jamás la invoques antes de tener el veredicto generado.

- **Parámetros de entrada:**

    - titulo (string): título oficial de la película.
    - anio (int): año de estreno.
    - perfil_usuario (string): perfil de espectador seleccionado.
    - puntuacion_critica (float): puntuación media de la crítica.
    - puntuacion_publico (float): puntuación media del público.
    - veredicto (string): "merece la pena" o "pérdida de tiempo".
    - informe_completo (JSON): informe completo con todas
      las secciones generadas por Indy.
    - fecha_consulta (string): fecha y hora de la consulta.

- **Output esperado:**

    - Confirmación de guardado exitoso.
    - ID único del registro generado en SQLite.


### Herramienta 2: veredicto

- **Descripción para el LLM:** Llama a esta herramienta cuando ya tengas todos los datos recopilados y el informe final. El LLM actuará como cerebro del agente: interpretará los datos, aplicará el perfil del usuario, redactará todas las secciones del informe en tono cercano y con humor, y emitirá el veredicto final. Siempre prioriza la puntuación del público sobre la crítica especializada.

- **Parámetros de entrada:**

    - datos_pelicula (JSON): output completo de buscar_datos_pelicula.
    - perfil_usuario (string): perfil de espectador seleccionado.
    - plataformas (list): plataformas disponibles en España.
    - url_banda_sonora (string): URL de YouTube con la banda sonora.

- **Output esperado:**
    - Informe completo estructurado con todas las secciones:

        1. Título y año
        2. De qué va (sin spoilers, estilo bar)
        3. Crítica vs Público (diferencia y quién gana)
        4. Índice de Sorpresa (0-10)
        5. Escenas post-créditos (sí/no)
        6. Dónde verla en España
        7. Banda sonora (URL YouTube)
        8. Snack recomendado
        9. Modo maratón (si aplica)
        10. En este tiempo podrías...
        11. Indy's Pick
        12. Veredicto final

## Fase 4: El Ciclo de Razonamiento

Indy sigue el patrón ReAct (Reasoning + Acting) de forma iterativa hasta completar su misión. Cada paso del ciclo se muestra al usuario en forma de mensaje de carga, al estilo pantalla de videojuego. Los mensajes combinan referencias a Indiana Jones y guiños caninos, ya que Indy es un homenaje al perro del creador del agente, que toma
su nombre de Indiana Jones, quien a su vez tomó el suyo del perro de su infancia.

---

### Paso 1: Thought — Análisis inicial

Indy recibe el título de la película y el perfil del usuario. Analiza qué información necesita recopilar y en qué orden
debe llamar a sus herramientas.

Mensaje de carga:
> "Indy ha encontrado una pista... ajustando el sombrero y desenfundando el látigo de datos"

---

### Paso 2: Act — Búsqueda de datos

Indy invoca la herramienta buscar_datos_pelicula con el título confirmado. Consulta OMDb, scrapea Rotten Tomatoes, Metacritic y FilmAffinity, busca las plataformas en JustWatch y localiza la banda sonora en YouTube.

Mensaje de carga:
> "Indy olfateando en Rotten Tomatoes... cuidado con las trampas."

---

### Paso 3: Observe — Interpretación de resultados

Indy recibe los datos de todas las fuentes y los analiza. Comprueba si hay divergencia entre crítica y público, detecta
si la película pertenece a una saga y verifica si hay datos suficientes para generar el informe completo.

Si alguna fuente no ha devuelto datos, Indy lo registra explícitamente y continúa sin inventar información.

Mensaje de carga:
> "El pueblo ha hablado... procesando veredicto popular."

---

### Paso 4: Thought — Decisión de continuidad

Indy evalúa si tiene suficiente información para invocar generar_veredicto o si necesita repetir alguna búsqueda.
Si los datos son suficientes, rompe el bucle y avanza al siguiente paso. Si no, vuelve al Paso 2 con parámetros
de búsqueda distintos.

Mensaje de carga:
> "Indy consultando el mapa del tesoro... casi lo tenemos."

---

### Paso 5: Act — Generación del informe

Indy invoca generar_veredicto con todos los datos recopilados y el perfil del usuario. El LLM redacta el informe completo
en tono cercano y con humor, aplica el sesgo hacia el público general y emite el veredicto final.

Mensaje de carga:
> "Indy preparando el informe final... no le des el látigo todavía."

---

### Paso 6: Observe — Verificación del informe

Indy comprueba que el informe contiene todas las secciones obligatorias y que el veredicto está claramente emitido.
Si falta alguna sección, vuelve al Paso 5. Si el informe está completo, avanza al guardado.

Mensaje de carga:
> "Revisando que no falte ningún hueso en la excavación..."

---

### Paso 7: Act — Guardado en base de datos

Indy invoca guardar_informe y persiste el informe completo en SQLite. Solo llega a este paso si el veredicto ha sido
emitido correctamente.

Mensaje de carga:
> "Guardando el tesoro en el museo... misión casi cumplida."

---

### Paso 8: Fin del ciclo

Indy muestra el informe completo al usuario y confirma que ha sido guardado correctamente en la base de datos.

Mensaje de carga:
> "Indy ha vuelto al despacho. El látigo descansa. Aquí está tu veredicto."

---

### Condición de ruptura del bucle
Indy rompe el ciclo de razonamiento cuando se cumplen simultáneamente estas dos condiciones:

1. El informe contiene todas las secciones obligatorias y el veredicto ha sido emitido.
2. El informe ha sido guardado correctamente en SQLite.

## Fase 5: Gestión de Riesgos y Control

### 5.1 Control de Bucles Infinitos
Indy tiene un límite máximo de 10 iteraciones del ciclo ReAct (max_iterations = 10). Si alcanza ese límite sin haber completado el informe, detiene la ejecución y muestra al usuario el siguiente
mensaje:

> "Indy ha perdido la pista. No he podido completar el análisis. Comprueba el título e inténtalo de nuevo."

Adicionalmente, si Indy detecta que está llamando a la misma herramienta más de 3 veces consecutivas sin obtener resultados diferentes, interrumpe el bucle automáticamente y registra el error en SQLite.

---

### 5.2 Manejo de Errores Críticos
Si alguna fuente externa no responde o devuelve un error, Indy aplica la siguiente lógica:

- Si OMDb no responde: Indy interrumpe la consulta y notifica al usuario. Sin datos básicos no es posible continuar.
- Si el scraping de RT, Metacritic o FilmAffinity falla: Indy continúa con las fuentes disponibles e indica explícitamente
  en el informe qué fuentes no han podido consultarse.
- Si JustWatch no responde: Indy omite la sección de plataformas e indica que no hay datos disponibles en ese momento.
- Si YouTube no devuelve resultados: Indy omite el embed de banda sonora e indica que no ha encontrado resultados.
- Si SQLite falla al guardar: Indy notifica al usuario y le muestra el informe completo en pantalla para que no pierda
  el resultado.

Mensaje de error genérico:
> "Indy ha encontrado una trampa en el camino. Algunos datos no han podido recuperarse, pero aquí tienes lo que he encontrado."

---

### 5.3 Intervención Humana (Human-in-the-Loop)
El único punto de intervención humana en el ciclo de Indy se produce cuando los datos recopilados son insuficientes
para emitir un veredicto fiable. En ese caso, Indy congela su estado y pregunta al usuario:

> "Indy no ha encontrado suficientes datos sobre esta película. ¿Quieres que emita un veredicto con la información parcial
> disponible o prefieres cancelar la consulta?"

El usuario puede elegir:
1. Continuar con datos parciales: Indy emite el veredicto indicando explícitamente qué secciones están incompletas.
2. Cancelar la consulta: Indy descarta la sesión y no guarda nada en SQLite.

Fuera de este punto, Indy opera de forma completamente autónoma sin requerir intervención del usuario.

