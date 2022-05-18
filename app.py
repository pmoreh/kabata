import streamlit as st
import sqlite3

conn= sqlite3.connect('data.db')
c = conn.cursor()

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')
def add_userdata(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()
def login_user(username,password):
    c.execute( 'SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data= c.fetchall()
    return data
def view_all_users():
    c.execute('SELECT * FROM userstable')
    data=c.fetchall()
    return data


# def create_table():
#     c.execute('userstable')

def main():
    '''building biometric fingerprint login'''

    st.title('Biometric FingerPrint Machine')

    menu =['Home','Login','Register']
    choice= st.sidebar.selectbox('Menu',menu)

    if choice=='Home':
        st.subheader('Homes')

    elif choice=='Login':
        st.subheader('Login Section')

        username=st.sidebar.text_input('User Name')
        password = st.sidebar.text_input('Password',type='password')

        if st.sidebar.checkbox('Login'):
            create_usertable()
            result= login_user(username,password)
            if result:
                st.success('You have successfully Logged in as {}!'.format(username))

                task=st.selectbox('Task',['Add Post','Analytics','Add Profile'])

                if task=='Add Post':
                    st.subheader('Add your post')
                elif task =='Analytics':
                    st.subheader('Analytics')
                elif task =='Add Profile':
                    st.subheader('User Profiles')
            else:
                st.warning('Register first ,you are not in the system')

    elif choice=='Register':
        st.subheader('Register User')
        new_user= st.text_input('Username')
        new_password= st.text_input('Password',type='password')
        fingeprint = st.button('register fingerprint')

        if st.button('Register'):
            create_usertable()
            add_userdata(new_user,new_password)
            st.success('You have successfully registered in TUK Biometric')
            st.info('Go To Login Menu  to Login')

            v = view_all_users()
            print(v)










if __name__== '__main__':
    main()