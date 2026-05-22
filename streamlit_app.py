import streamlit as st

st.title("🎈 halo barudak")
import streamlit as st
import random

# Konfigurasi Halaman
st.set_page_config(page_title="Batu Gunting Kertas", page_icon="✊")

st.title("✊✌️🖐️ Batu Gunting Kertas")
st.write("Lawan komputer dan kumpulkan skor tertinggi!")

# Inisialisasi skor jika belum ada
if 'skor_pemain' not in st.session_state:
    st.session_state.skor_pemain = 0
if 'skor_komputer' not in st.session_state:
    st.session_state.skor_komputer = 0

# Fungsi Logika Game
def tentukan_pemenang(pemain, komputer):
    if pemain == komputer:
        return "Seri!"
    elif (pemain == "Batu" and komputer == "Gunting") or \
         (pemain == "Gunting" and komputer == "Kertas") or \
         (pemain == "Kertas" and komputer == "Batu"):
        st.session_state.skor_pemain += 1
        return "Kamu Menang! 🎉"
    else:
        st.session_state.skor_komputer += 1
        return "Kamu Kalah! 🤖"

# Layout Kolom untuk Tombol
col1, col2, col3 = st.columns(3)
pilihan = ["Batu", "Gunting", "Kertas"]
pilihan_pemain = None

with col1:
    if st.button("✊ Batu", use_container_width=True):
        pilihan_pemain = "Batu"
with col2:
    if st.button("✌️ Gunting", use_container_width=True):
        pilihan_pemain = "Gunting"
with col3:
    if st.button("🖐️ Kertas", use_container_width=True):
        pilihan_pemain = "Kertas"

# Eksekusi Pertandingan
if pilihan_pemain:
    pilihan_komputer = random.choice(pilihan)
    hasil = tentukan_pemenang(pilihan_pemain, pilihan_komputer)
    
    st.divider()
    
    # Menampilkan Hasil
    c1, c2 = st.columns(2)
    c1.metric("Pilihan Kamu", pilihan_pemain)
    c2.metric("Pilihan Komputer", pilihan_komputer)
    
    st.subheader(f"Hasil: {hasil}")
    st.divider()

# Menampilkan Skor di Sidebar
st.sidebar.title("Papan Skor")
st.sidebar.write(f"👤 Pemain: **{st.session_state.skor_pemain}**")
st.sidebar.write(f"🤖 Komputer: **{st.session_state.skor_komputer}**")

if st.sidebar.button("Reset Skor"):
    st.session_state.skor_pemain = 0
    st.session_state.skor_komputer = 0
    st.rerun()
