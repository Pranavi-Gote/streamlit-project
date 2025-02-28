import streamlit as  st
import sqlite3
from streamlit_option_menu import option_menu
#st.title("Welcome to my app")
#st.write(":red[I am a paragraph]")
#st.header("Heading")
#st.subheader("Sub Heading")
#st.markdown("<h1>hello</h1><h2>hello</h2>",unsafe_allow_html=True)
#st.markdown("<marquee style='color:red;'><h1>hello</h1><h2>hello</h2></marquee>",unsafe_allow_html=True)
#st.image('https://images.unsplash.com/photo-1734779205618-30ee0220f56f?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHwyfHx8ZW58MHx8fHx8',caption ='this is an image')
#st.button("Signin")
#st.checkbox("Java")
#gender = st.radio("Gender",options=['Male','Female'])
#st.error(gender)
#st.success("ok")
#st.info("Streamlit")
#st.warning("Alert")
#st.text_input("Enter Your Name")
#st.text_input("Enter Your Password")
st.title("Registration Form")
def connectdb():
    conn = sqlite3.connect("mydb.db")
    return conn

def createTable():
    with connectdb() as conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS student(name text, password text, roll int primary key, branch text)")
        conn.commit()

def addRecord(data):
    with connectdb() as conn:
        cur=conn.cursor()
        try:
            cur.execute("INSERT INTO student(name, password,roll,branch) VALUES(?,?,?,?)",data)
            conn.commit()
        except sqlite3.IntegrityError:
            st.error("Student already registered")

def display():
    with connectdb() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM student")
        result = cur.fetchall()
        return result

def Signup():
    name = st.text_input("Enter Your Name")
    password =st.text_input("Enter Your Password",type='password')
    repassword =st.text_input("Retype Your Password",type='password')
    roll =st.number_input("Enter Your Roll Number",format="%0.0f")
    branch = st.selectbox("Enter Branch",options=["CSE","AIML","IOT"])
    if st.button('SignIn'):
        if password != repassword:
            st.warning("Password Mismatch")
        else:
            addRecord((name,password,roll,branch))
            st.success("Student registered !!!!")


createTable()
with st.sidebar:
    st.sidebar.image("https://images.unsplash.com/photo-1724583698704-94b3f4771c58?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
    selected = option_menu("My App", ['Signup','Display All Record'],icons=['box-arrow-in-right','table'])

if selected == 'Signup':
    Signup()
else:
    data = display()
    st.table(data)
