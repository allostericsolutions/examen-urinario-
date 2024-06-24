import streamlit as st
import random

# Datos de medidas y estructuras
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
def mostrar_calificacion(aciertos, total_preguntas):
    porcentaje = (aciertos / total_preguntas) * 100
    st.write(f"## Tu calificación final es: {aciertos}/{total_preguntas} ({porcentaje:.1f}%)")

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

def main():
    st.title("Examen de Anatomía")
    
    # Inicializar el estado de la sesión si no existe
    if "preguntas_respondidas" not in st.session_state:
        st.session_state.preguntas_respondidas = {}
        st.session_state.aciertos = 0
        st.session_state.mostrar_calificacion = False

    preguntas = list(questions_and_answers.items())
    random.shuffle(preguntas)
    
    # Mostrar preguntas
    for i, (pregunta, datos) in enumerate(preguntas):
        if i not in st.session_state.preguntas_respondidas:
            st.write(f"### {pregunta}")
            respuesta = st.radio(f"Selecciona la respuesta correcta para '{pregunta}':", datos["options"], key=f"pregunta_{i}")
            
            if st.button(f"Responder {i+1}", key=f"boton_{i}"):
                if respuesta == datos["answer"]:
                    st.session_state.aciertos += 1
                st.session_state.preguntas_respondidas[i] = respuesta

    # Mostrar el botón para mostrar la calificación final si se han respondido todas las preguntas
    if len(st.session_state.preguntas_respondidas) == len(preguntas):
        if not st.session_state.mostrar_calificacion:
            if st.button("Mostrar Calificación"):
                st.session_state.mostrar_calificacion = True
    
    # Mostrar la calificación final
    if st.session_state.mostrar_calificacion:
        mostrar_calificacion(st.session_state.aciertos, len(preguntas))

if __name__ == "__main__":
    main()
