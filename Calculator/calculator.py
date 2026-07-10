def kalkulyator():
    print("--- Python Kalkulyator ---")
    
    # Foydalanuvchidan sonlarni kiritishni so'raymiz
    try:
        son1 = float(input("Birinchi sonni kiriting: "))
        amal = input("Amalni kiriting (+, -, *, /): ")
        son2 = float(input("Ikkinchi sonni kiriting: "))
    except ValueError:
        print("Xatolik: Iltimos, faqat son kiriting!")
        return

    # Amallarni tekshiramiz va hisoblaymiz
    if amal == '+':
        natija = son1 + son2
    elif amal == '-':
        natija = son1 - son2
    elif amal == '*':
        natija = son1 * son2
    elif amal == '/':
        # Nolga bo'lish xavfini tekshiramiz
        if son2 == 0:
            print("Xatolik: Sonni nolga bo'lish mumkin emas!")
            return
        natija = son1 / son2
    else:
        print("Xatolik: Noto'g'ri amal kiritildi!")
        return

    # Natijani ekranga chiqaramiz
    print(f"Natija: {son1} {amal} {son2} = {natija}")

# Dasturni ishga tushirish
if __name__ == "__main__":
    kalkulyator()