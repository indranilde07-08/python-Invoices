import streamlit as st
import function

todos = function.get_todos()


def add_todo():
    todo = st.session_state["add"]+"\n"
    todos.append(todo)
    function.write_todos(todos)
    st.session_state["add"]= ""


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is increase your productivity")

for index,todo in enumerate(todos):
    st.checkbox(todo,key=f"todo_{index}")

st.text_input(label= "", placeholder="Add new todo....",on_change=add_todo,
              key="add")



