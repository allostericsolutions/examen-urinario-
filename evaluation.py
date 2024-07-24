# Bloque para la sección "Evaluation" fuera del "Content"
elif st.session_state.pagina_actual == "Evaluation": 
    st.write("## Evaluation Mode")
    exec(open('Abdominal Sonography Overview/evaluation.py').read())
headers = {
    "authorization": st.secrets["my_proud"],
    "content-type": "application/json"
}
