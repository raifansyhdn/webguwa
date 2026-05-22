import streamlit as st

st.title("🎈 halo barudak")
import streamlit as st
import random

# Konfigurasi halaman
st.set_page_config(page_title="Game Tebak Angka", page_icon="🎮")

st.title("🎮 Game Tebak Angka")
st.write("Saya telah memilih angka antara **1 sampai 100**. Bisakah kamu menebaknya?")

# Inisialisasi Game (Hanya dijalankan sekali)
if 'target' not in st.session_state:
    st.session_state.target = random.randint(1, 100)
    st.session_state.percobaan = 0
    st.session_state.game_over = False

def reset_game():
    st.session_state.target = random.randint(1, 100)
    st.session_state.percobaan = 0
    st.session_state.game_over = False

# Input dari pengguna
tebakan = st.number_input("Masukkan tebakanmu:", min_value=1, max_value=100, step=1)

if st.button("Cek Angka"):
    st.session_state.percobaan += 1
    
    if tebakan < st.session_state.target:
        st.warning("Terlalu RENDAH! Coba lagi.")
    elif tebakan > st.session_state.target:
        st.warning("Terlalu TINGGI! Coba lagi.")
    else:
        st.success(f"🎉 TEPAT SEKALI! Angkanya adalah {st.session_state.target}.")
        st.write(f"Kamu berhasil menebak dalam {st.session_state.percobaan} percobaan.")
        st.session_state.game_over = True

# Tombol Reset
if st.session_state.game_over:
    if st.button("Main Lagi?"):
        reset_game()
        st.rerun()

# Sidebar untuk informasi
st.sidebar.header("Statistik")
st.sidebar.write(f"Jumlah percobaan: {st.session_state.percobaan}")
