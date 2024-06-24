import streamlit as st
import random

# Preguntas y respuestas
questions_and_answers = {
    # ... (el diccionario de preguntas y respuestas es el mismo) ...
}

# --- Funciones para la lógica del examen ---

def mostrar_pregunta(pregunta, opciones, respuesta_correcta, indice):
    # Obtener la respuesta seleccionada del estado de la sesión, o None si no hay respuesta previa
    respuesta_seleccionada = st.session_state.get(f"respuesta_{indice}", None)

    # Mostrar las opciones usando un índice
    indice_respuesta = st.radio(pregunta, range(len(opciones)), format_func=lambda i: opciones[i], key=f"pregunta_{indice}", index=respuesta_seleccionada)
    
    # Guardar la respuesta seleccionada en el estado de la sesión
    st.session_state[f"respuesta_{indice}"] = indice_respuesta

    if opciones[indice_respuesta] == respuesta_correcta:
        st.success("¡Correcto!")
        return True
    else:
        st.error("Incorrecto.")
        return False

def mostrar_calificacion(aciertos, total_preguntas):
    # ... (la función mostrar_calificacion() es la misma) ...

# --- Interfaz de usuario de Streamlit ---

st.title("Examen de Anatomía")

# Inicializar el estado de la sesión si no existe
if "preguntas_respondidas" not in st.session_state:
    st.session_state.preguntas_respondidas = []
if "aciertos" not in st.session_state:
    st.session_state.aciertos = 0

preguntas = list(questions_and_answers.items())
random.shuffle(preguntas)

# Mostrar las preguntas solo una vez
if not st.session_state.preguntas_respondidas:
    for i, (pregunta, datos) in enumerate(preguntas):
        st.write("---")
        if mostrar_pregunta(pregunta, datos["options"], datos["answer"], i):
            st.session_state.aciertos += 1
        st.session_state.preguntas_respondidas.append(pregunta)

# Mostrar la calificación solo después de responder todas las preguntas
if len(st.session_state.preguntas_respondidas) == len(questions_and_answers):
    if st.button("Mostrar Calificación"):
        mostrar_calificacion(st.session_state.aciertos, len(questions_and_answers))
