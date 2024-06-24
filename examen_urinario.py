import streamlit as st
import random

# Questions and answers about structures and measurements
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
    st.title("Structures and Measurements Quiz")

    # Mostrar el logo usando markdown y HTML
    st.markdown(
        '<img src="https://raw.githubusercontent.com/allostericsolutions/examen-urinario-/main/Allosteric_Solutions.png" width="100">',
        unsafe_allow_html=True
    )

    if "questions" not in st.session_state:
        st.session_state.questions = random.sample(list(questions_and_answers.items()), len(questions_and_answers))
    if "answers" not in st.session_state:
        st.session_state.answers = {}
        for i in range(len(questions_and_answers)):
            st.session_state.answers[f"question_{i}"] = -1
    if "grade_shown" not in st.session_state:
        st.session_state.grade_shown = False

    for i, (question, data) in enumerate(st.session_state.questions):
        st.write(f"**Question {i + 1}:** {question}")
        user_answer = st.radio("Select an option:", data["options"], key=f"question_{i}")
        st.session_state.answers[f"question_{i}"] = user_answer

    if len(st.session_state.answers) == len(questions_and_answers) and not st.session_state.grade_shown:
        if st.button("Show Grade"):
            correct_answers = sum([st.session_state.answers[f"question_{i}"] == data["answer"] for i, (question, data) in enumerate(questions_and_answers.items())])
            show_grade(correct_answers, len(questions_and_answers))
            st.session_state.grade_shown = True

    # Enlace a tu página web
    st.markdown('<a href="https://www.allostericsolutions.com/" target="_blank">Visit our website</a>', unsafe_allow_html=True)

def show_grade(correct_answers, total_questions):
    percentage = (correct_answers / total_questions) * 100
    st.write(f"<h3>Your final grade is: {correct_answers}/{total_questions} ({percentage:.1f}%)</h3>", unsafe_allow_html=True)

    if percentage <= 50:
        st.write("You need a lot of work, keep going!")
    elif percentage <= 70:
        st.write("The effort has been good, but there is still more to do.")
    elif percentage <= 85:
        st.write("Good, but you can do more.")
    elif percentage <= 90:
        st.write("Very good!")
    else:
        st.write("Excellent!")

if __name__ == "__main__":
    main()
