import streamlit as st
import json

# APP STARTS HERE
st.set_page_config(layout="wide")
st.title("Assistant TD")

# Loading the exercises from the json
with open('exercises.json') as f:
    chapters_content = json.load(f)

def chapter_page():
    with st.container(border=True):
        st.markdown("Choisis le chapitre que tu souhaites travailler :")
        for chapter_number, chapter_content in chapters_content.items():
            chapter_name = chapter_content["chapter_name"]
            st.button(
                chapter_name,
                on_click=go_to_exercise_page,
                args=(chapter_number,)
            )

def exercise_page():
    chapter_number = st.session_state["chapter_number"]
    exercises = chapters_content[chapter_number]["exercises"]

    if exercises == {}:
        st.markdown("Pas d'exercice disponible pour ce chapitre pour l'instant.")
    for exercise_number, exercise_content in exercises.items():
        with st.container(border=True):
            st.markdown(f"**Exercice {exercise_number}**")
            # st.markdown(f"{exercise_content['instructions']}")
            for hint_number, hint_content in exercise_content["hints"].items():
                if st.button(f"Indice {hint_number}", key=f"{exercise_number}_{hint_number}"):
                    st.markdown(hint_content)
    st.button(
        "Retourner au choix des chapitres",
        on_click=go_back_to_chapter_page
    )

def go_to_exercise_page(chapter_number):
    st.session_state["page"] += 1
    st.session_state["chapter_number"] = chapter_number

def go_back_to_chapter_page():
    st.session_state["page"] -= 1

# Mechanism that enables to change pages
if "page" not in st.session_state:
    st.session_state["page"] = 0

if st.session_state.page == 0:
    chapter_page()
else:
    exercise_page()
