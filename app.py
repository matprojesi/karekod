import streamlit as st
import math

# Sayfa Ayarları
st.set_page_config(page_title="Kare Şifreleme", page_icon="🔐")

# --- ALGORİTMA FONKSİYONLARI ---
def siralama_ve_kare_sifrele(metin):
    turk_alfabesi = "abcçdefgğhıijklmnoöprsştuüvyz"
    parcalar = []
    for harf in metin.lower():
        if harf in turk_alfabesi:
            sira = turk_alfabesi.index(harf) + 1
            parcalar.append(str(sira ** 2))
    return "".join(parcalar)

def sifre_coz(sifreli_dize):
    turk_alfabesi = "abcçdefgğhıijklmnoöprsştuüvyz"
    cozulen = []
    i = 0
    while i < len(sifreli_dize):
        bulundu = False
        for basamak in [3, 2, 1]:
            parca = sifreli_dize[i : i + basamak]
            if parca:
                sayi = int(parca)
                kok = math.sqrt(sayi)
                if math.isclose(kok, round(kok)) and 1 <= round(kok) <= 29:
                    cozulen.append(turk_alfabesi[round(kok) - 1])
                    i += basamak
                    bulundu = True
                    break
        if not bulundu: return "Hata: Şifre geçersiz!"
    return "".join(cozulen).upper()

# --- WEB TASARIMI ---
st.title("🛡️ TÜBİTAK 4006: Kare Şifreleme")
st.info("Türk alfabesindeki harflerin sıra numaralarının karesini alarak mesajları gizliyoruz.")

tab1, tab2 = st.tabs(["Mesaj Şifrele", "Şifre Çöz"])

with tab1:
    mesaj = st.text_input("Şifrelenecek Metin:")
    if st.button("Şifreyi Oluştur"):
        sonuc = siralama_ve_kare_sifrele(mesaj)
        st.success(f"Şifreli Kod: {sonuc}")

with tab2:
    kod = st.text_input("Çözülecek Sayı Dizisi:")
    if st.button("Şifreyi Çöz"):
        sonuc = sifre_coz(kod)
        st.warning(f"Orijinal Mesaj: {sonuc}")

st.markdown("---")
st.caption("Bu proje matematik ve yazılımı birleştirmek amacıyla geliştirilmiştir.")
