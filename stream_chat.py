import streamlit as st
from spellchecker import SpellChecker
from chat import chatbot

def main():
    st.title("Chatbot")

    message = st.text_input("Enter your message:")
    if st.button("Ask"):
        bot_response = get_bot_response(message)
        st.text(bot_response)

def get_bot_response(message):
    spell = SpellChecker()
    words = message.split()
    corrected_words = [spell.correction(word) for word in words]
    corrected_message = ' '.join(corrected_words)
    bot_response = chatbot(corrected_message).capitalize()
    return bot_response

if __name__ == "__main__":
    main()
