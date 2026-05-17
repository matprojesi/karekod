import streamlit as st
import math

# --- ŞİFRELEME FONKSİYONLARI ---
def siralama_ve_kare_sifrele(metin):
    turk_alfabesi = "abcçdefgğhıijklmnoöprsştuüvyz"
    sifreli_kelimeler = []
    
    # Cümleyi önce boşluklardan kelimelere ayırıyoruz
    kelimeler = metin.lower().split()
    
    for kelime in kelimeler:
        harf_parcalari = []
        for harf in kelime:
            if harf in turk_alfabesi:
                sira = turk_alfabesi.index(harf) + 1
                harf_parcalari.append(str(sira ** 2))
        
        # Kelimenin içindeki harfleri tire (-) ile birleştiriyoruz
        sifreli_kelimeler.append("-".join(harf_parcalari))
    
    # Kelimeleri de aralarında belirgin bir eğik çizgi ( / ) olacak şekilde birleştiriyoruz
    return " / ".join(sifreli_kelimeler)

def sifre_coz(sifreli_dize):
    turk_alfabesi = "abcçdefgğhıijklmnoöprsştuüvyz"
    cozulmus_kelimeler = []
    
    # Önce şifreyi eğik çizgiye göre kelimelere bölüyoruz
    sifreli_kelimeler = sifreli_dize.split("/")
    
    for sifreli_kelime in sifreli_kelimeler:
        cozulen_kelime = []
        # Sonra her bir kelimedeki harfleri tireye göre ayırıyoruz
        harf_parcalari = sifreli_kelime.split("-")
        
        for parca in harf_parcalari:
            parca = parca.strip() # Etraftaki gereksiz boşlukları temizle
            if not parca:
                continue
            try:
                sayi = int(parca)
                kok = math.isqrt(sayi) # Sayının karekökünü al
                
                # Hem tam kare mi diye bakıyoruz hem de alfabede var mı (1-29 arası)
                if kok * kok == sayi and 1 <= kok <= 29:
                    cozulen_kelime.append(turk_alfabesi[kok-1])
                else:
                    return "Hata: Harf karşılığı bulunamadı veya tam kare değil."
            except ValueError:
                return "Hata: Geçersiz bir karakter girdiniz."
        
        # Çözülen harfleri birleştirip kelimeyi oluşturuyoruz (BÜYÜK HARFLE)
        cozulmus_kelimeler.append("".join(cozulen_kelime).upper())
        
    # Çözülen kelimeleri arasına boşluk koyarak cümleyi tamamlıyoruz
    return " ".join(cozulmus_kelimeler)

# --- WEB ARAYÜZÜ (TASARIM) ---
st.title("🔐 Kare Şifreleme Uygulaması")
st.markdown("Cümlelerinizi girin, sistem harflerin karelerini alarak şifrelesin! *(Örn: Merhaba Dünya)*")

islem = st.radio("İşlem Seçin:", ["Şifrele", "Şifre Çöz"])
metin_girisi = st.text_input("Buraya yazın:")

if st.button("Sonucu Göster"):
    if not metin_girisi:
        st.warning("Lütfen işlem yapmak için bir metin girin!")
    elif islem == "Şifrele":
        st.success(f"Şifrelenmiş Metin: {siralama_ve_kare_sifrele(metin_girisi)}")
    else:
        st.info(f"Çözülmüş Metin: {sifre_coz(metin_girisi)}")
