import streamlit as magic

magic.set_page_config(
    page_title="мое приложение",
    page_icon=":rocket:"
)

magic.write("Мoй первый сайт")

magic.header("это header")

magic.subheader("это subheader")

text = magic.text_input("Напиши что-то")

magic.write(text)

calculator = text = magic.text_input("Калькулятор")

if calculator:
    magic.write(eval(calculator))
     
slider = magic.slider( "Выбери число")

magic.write(slider)

data = magic.date_input("Выбери дату")

digit = magic.number_input("Выбери цифру",
0,
2149770912
)

click = magic.button("Нажми на меня")
if click:

    magic.balloons()

magic.write(click)

click_img = magic.button(
    "Нажми и я покажу картинку"
)

if click_img:
    magic.image("80.jpg",
    caption="Самые крутые люди  в мире",
    width=500
    )

magic.video(
    "https://www.youtube.com/watch?v=m1KBXAFqYRc&ab_channel=JustMoments",
    format="video/mp4"
)

with magic.form(key="my_from"):
    name = magic.text_input("Имя")
    password = magic.text_input("Пароль")
    submit = magic.form_submit_button(
       "Нажми меня"
    )

    if submit:
        magic.success("Ура!")

picture = magic.camera_input("Take a picture")

if picture:
    magic.image(picture)