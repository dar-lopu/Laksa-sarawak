import streamlit as st
import random

st.set_page_config(page_title="Text Rearrange Challenge", page_icon="🧩")

st.title("🧩 Mari kita susun ayat")
st.write("Susun ayat dan dapatkan kunci untuk memori andaa! 🎥")

# --- Puzzle setup ---
correct_word = "KunyahLirik"
scrambled_word = "".join(random.sample(correct_word, len(correct_word)))

# Store the scrambled word in session state so it doesn't reshuffle on every input
if "scrambled_word" not in st.session_state:
    st.session_state.scrambled_word = scrambled_word
if "correct_word" not in st.session_state:
    st.session_state.correct_word = correct_word

st.subheader(f"Scrambled word: {st.session_state.scrambled_word}")

user_input = st.text_input("Your answer:")

if user_input:
   if user_input.strip().lower() == st.session_state.correct_word.lower():
       st.success("✅ Naisss, Dipersembahkan video memori yang dinantikan!")
       st.video("https://youtube.com/watch?v=4QPm75uvQP8?si=RtDFnlGhq0cjgGky")
   else:
       st.error("❌ SALAH WKWKWKWKWK!")  # <-- Replace with your own video or local file
   




