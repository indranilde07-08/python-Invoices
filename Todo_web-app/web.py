import streamlit as st
import function


st.set_page_config(layout= "wide")
todos = function.get_todos("todos.txt")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    h1, h2, h3, p {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def add_todo():
    todo = st.session_state["add"]+"\n"
    todos.append(todo)
    function.write_todos(todos)
    st.session_state["add"]= ""


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is increase your <b>productivity</b>",
         unsafe_allow_html = True)

st.text_input(label= "", placeholder="Add new todo....",on_change=add_todo,
              key="add")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=f"todo_{index}")
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[f"todo_{index}"]
        st.rerun() #instant refresh






