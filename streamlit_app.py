# Created the main python file
import streamlit
import pandas

streamlit.title("My parents new healthy dinner")

streamlit.header("Breakfast Menu")

streamlit.text("🥣 Porridge")

streamlit.text("🥗 Smoothie")

streamlit.text("🐔  Boiled eggs")

streamlit.text("🥑 Avacado")


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)

# Adding multi-select

streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))






