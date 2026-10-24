import streamlit as st

st.title("🛒 Kassometer")
st.write("Berechne deine Einkaufskosten!")

objekt = st.text_input("Was hast du gekauft?")
menge = st.number_input("Wie viele?", min_value=1, step=1)
preis = st.number_input("Preis pro Stück in Euro", min_value=0.0)

if st.button("Gesamtpreis berechnen"):
    endpreis = menge * preis
    st.success(f"Dein Einkauf kostet {endpreis:.2f} €.")
