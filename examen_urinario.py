import streamlit as st
import random

# Preguntas y respuestas
questions_and_answers = {
    "Length of the adult kidney": {
        "options": ["7-10 cm", "9-12 cm", "11-14 cm", "13-16 cm"],
        "answer": "9-12 cm"
    },
    "Width of the adult kidney": {
        "options": ["2-4 cm", "4-6 cm", "6-8 cm", "8-10 cm"],
        "answer": "4-6 cm"
    },
    "Length of the neonatal kidney": {
        "options": ["1.5-2.5 cm", "2-3 cm", "3.5-5.0 cm", "4-6 cm"],
        "answer": "3.5-5.0 cm"
    },
    "Width of the neonatal kidney": {
        "options": ["1-2 cm", "2-3 cm", "3-4 cm", "4-5 cm"],
        "answer": "2-3 cm"
    },
    "Length of the ureters": {
        "options": ["10-15 cm", "15-20 cm", "20-25 cm", "28-34 cm"],
        "answer": "28-34 cm"
    },
    "Diameter of the ureters": {
        "options": ["2 mm", "4 mm", "6 mm", "8 mm"],
        "answer": "6 mm"
    },
    "Thickness of the bladder wall": {
        "options": ["1-3 mm", "3-6 mm", "6-9 mm", "9-12 mm"],
        "answer": "3-6 mm"
    },
    "Length of the female urethra": {
        "options": ["2 cm", "4 cm", "6 cm", "8 cm"],
        "answer": "4 cm"
    },
    "Length of the male urethra": {
        "options": ["10 cm", "15 cm", "20 cm", "25 cm"],
        "answer": "20 cm"
    },
    "AP dimension of the adult kidney": {
        "options": ["1.5-2.5 cm", "2-3 cm", "2.5-4.0 cm", "3-4 cm"],
        "answer": "2.5-4.0 cm"
    },
    "AP dimension of the neonatal kidney": {
        "options": ["0.5-1.5 cm", "1-2 cm", "1.5-2.5 cm", "2-3 cm"],
        "answer": "1.5-2.5 cm"
    }
}

# --- Funciones para la lógica del examen ---

def mostrar_pregunta(pregunta, opciones, respuesta_correcta, indice):
    # Obtener la respuesta seleccionada del estado de la sesión, inicialmente es None
    respuesta_seleccionada = st.session_state.get(f"respuesta_{indice}", None)

    # Mostrar las opciones sin establecer un índice inicial
    indice_respuesta = st.radio(pregunta, range(len(opciones)), format_func=lambda i: opciones[i], key=f"pregunta_{indice}")

    # Guardar la respuesta seleccionada en el estado de la sesión
    st.session_state[f"respuesta_{indice}"] = indice_respuesta

    # Chequea si se ha seleccionado una respuesta
    if respuesta_seleccionada is not None:
        if opciones[indice_respuesta] == respuesta_correcta:
            st.success("¡Correcto!")
            return True
        else:
            st.error("Incorrecto.")
            return False

def mostrar_calificacion(aciertos, total_preguntas):
    porcentaje = (aciertos / total_preguntas) * 100
    st.write(f"<h3>Tu calificación final es: {aciertos}/{total_preguntas} ({porcentaje:.1f}%)</h3>", unsafe_allow_html=True)

    if porcentaje <= 50:
        st.write("¡Necesitas estudiar más! ¡Tú puedes!")
    elif porcentaje <= 70:
        st.write("Buen esfuerzo, ¡pero todavía puedes mejorar!")
    elif porcentaje <= 85:
        st.write("¡Bien hecho! Sigue practicando.")
    elif porcentaje <= 90:
        st.write("¡Muy bien! ¡Vas por buen camino!")
    else:
        st.write("¡Excelente trabajo! ¡Eres un experto en anatomía!")

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
