# library
import streamlit as st

# write
st.title("Software perkalian")
st.write('ini adalah aplikasi perkalian')

# input bilangan pertama
number1 = st.number_input('masukkan bilangan pertama')
st.write(f'bilangan pertama adalah {number1}')

# input bilangan kedua
number2 = st.number_input('masukkan bilangan kedua')
st.write(f'bilangan kedua adalah {number2}')

# hasil kali 2
hasil = number1*number2

if st.button('kalkulasi'):
    st.write(f'Hasil kali antara {number1} dan {number2} adalah {hasil}')
else:
    st.write('Silahkan pencet tombol kalkulasi!')