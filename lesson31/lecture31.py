import streamlit as st


# st.title("this is my first strimleat aplication")
# st.write("hello, streamlit")

# st.title("this is title")
# st.header("this is header")
# st.subheader("this is subheader")

# st.text("just a text")
# st.caption("small gray note")
# st.divider()


# st.markdown("**this is a bold text** and this is not")
# st.markdown("*this is italic text* and this is not")
# st.markdown("### this is third level header")
# st.markdown("## this is second level header")
# st.markdown("# this is first level header")
# st.markdown("""
# - first element
# - second element
# """)

# st.markdown("[google link](https://www.google.com)")

# st.code("print('hello')", language="python")

# st.write("**bold** text")
# st.write(23)
# st.write([1, 2, 3])
# st.write({"name": "saba"})
# st.write("number:", 7)


# name = st.text_input("enter your name")

# if name:
#     st.write(f"hello **{name}**")

# feedback = st.text_area("coment", height=150)

# if feedback:
#     st.write(f"symbols: {len(feedback)}")


# age = st.number_input(
#     "age",
#     min_value=0,
#     max_value=120,
#     value=22,
#     step=1
# )


# temp = st.slider("temp", 0, 100, 50)

# temp = st.slider("temp", min_value=0, max_value=200, value=100)

# price = st.slider("price", 0, 1000, (100, 500))
# st.write(price)
# st.write(f"min: {price[0]}, max: {price[1]}")


# city = st.selectbox("city", ["tbilisi", "batumi", "kutaisi"])
# st.write(f"you live in: {city}")

# color = st.radio("color", ["red", "yellow", "blue"])
# st.write(f"your color is: {color}")

# langs = st.multiselect("languages", ["python", "c", "c++", "java"])
# st.write(f"your language is: {langs}")


# agree = st.checkbox("i agree wit this terms")
# st.write(agree)

# import datetime

# birthday = st.date_input(
#     "birth day: ",
#     value=datetime.date(2003, 7, 15),
#     min_value=datetime.date(1950, 1, 1),
#     max_value=datetime.date.today()
# )

# st.write(birthday)

# button = st.button("click me")

# if button:
#     st.write("you clicked the button")
#     st.balloons()

# button = st.button("click this")
# if button:
#     st.success("good boy")

# button2 = st.button("do not click this")
# if button2:
#     st.error("fuck you")

# if st.button("dont click me again"):
#     st.warning("i warnd you")

# if st.button("click to get information"):
#     st.info("you are ugly")

# st.warning("this is a bad thing")


# num1 = st.number_input("first number", value=0)
# num2 = st.number_input("second number", value=0)
# result = None
# operations = ["add(+)", "substract(-)", "multiply(x)", "divide(÷)"]
# operation = st.selectbox("operation", operations)

# if st.button("calculate"):
#     if operation == operations[0]:
#         result = num1 + num2
#     elif operation == operations[1]:
#         result = num1 - num2
#     elif operation == operations[2]:
#         result = num1 * num2
#     elif operation == operations[3]:
#         if num2 == 0:
#             st.error("you can't divide by zero")
#         else:
#             result = num1/num2

# if result is not None:
#     st.success(f"result is: {result}")


# col1, col2 = st.columns(2)

# with col1:
#     st.header("left one")
#     st.write("coment number 1")
# with col2:
#     st.header("right one")
#     st.write("coment number 2")

# col1, col2, col3 = st.columns([1, 2, 1])

# with col1:
#     st.header("left one")
#     st.write("coment number 1")
# with col2:
#     st.header("middle one")
#     st.write("coment number 2")

# with col3:
#     st.header("right one")
#     st.write("coment number 3")


with st.expander("details"):
    st.write("this text apears and dissapears")
