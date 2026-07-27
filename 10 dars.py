# 1-QATOR: Veb-sayt yaratish uchun Streamlit va AI kutubxonasini chaqiramiz
import streamlit as st
from sklearn.tree import DecisionTreeClassifier

# Sarlavha va ko'rinish
st.title("🏫 Maktab AI-Shifokor Tizimi")
st.write("O'quvchi alomatlarini kiriting va AI tashxisini oling.")

# ==========================================
# 1-BOSQICH: AI MODELINI O'RGATAMIZ
# ==========================================
X_alomatlar = [[36.6, 0], [36.5, 0], [38.5, 1], [39.0, 1], [37.2, 1], [36.8, 0]]
Y_tashxis = [0, 0, 1, 1, 1, 0]

ai_shifokor = DecisionTreeClassifier()
ai_shifokor.fit(X_alomatlar, Y_tashxis)

# ==========================================
# 2-BOSQICH: TELEFONDA KO'RINADIGAN SHAKLLAR
# ==========================================
# Harorat kiritish maydoni (Telefonga juda qulay)
harorat = st.number_input("Tana haroratini kiriting (°C):", min_value=35.0, max_value=42.0, value=36.6, step=0.1)

# Yo'tal bor-yo'qligi tanlovi
yotal_input = st.radio("Yo'tal bormi?", ["Yo'q", "Ha"])
yotal = 1 if yotal_input == "Ha" else 0

# TASHXIS TUGMASI
if st.button("🔍 AI TASHXIS QILSIN"):
    natija = ai_shifokor.predict([[harorat, yotal]])
    
    if natija[0] == 1:
        st.error("🚨 Bu o'quvchida kasallik alomatlari bor! Uyga javob berish tavsiya etiladi.")
    else:
        st.success("✅ O'quvchi sog'lom! Darsda qolsa bo'ladi.")