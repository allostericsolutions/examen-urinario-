import streamlit as st
import random

# Preguntas y respuestas sobre estructuras y medidas
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

def main():
    st.title("Examen de Estructuras y Medidas")

    if "preguntas" not in st.session_state:
        st.session_state.preguntas = random.sample(list(questions_and_answers.items()), len(questions_and_answers))
    if "respuestas" not in st.session_state:
        st.session_state.respuestas = {}
    if "calificacion_mostrada" not in st.session_state:
        st.session_state.calificacion_mostrada = False

    for i, (pregunta, datos) in enumerate(st.session_state.preguntas):
        st.write(f"**Pregunta {i + 1}:** {pregunta}")
        respuesta_usuario = st.radio("Selecciona una opción:", datos["options"], key=f"pregunta_{i}")
        st.session_state.respuestas[pregunta] = respuesta_usuario

    if len(st.session_state.respuestas) == len(questions_and_answers) and not st.session_state.calificacion_mostrada:
        if st.button("Mostrar Calificación"):
            aciertos = sum([st.session_state.respuestas[pregunta] == datos["answer"] for pregunta, datos in questions_and_answers.items()])
            mostrar_calificacion(aciertos, len(questions_and_answers))
            st.session_state.calificacion_mostrada = True

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

if __name__ == "__main__":
    main()
