def encryption(metin,anahtar):
    alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    sifrelenmis_metin=""

    for harf in metin:
        if harf.lower() in alfabe:
            index = alfabe.index(harf.lower())
            sifrelenmis_index = ( index + anahtar ) % len(alfabe)

            if harf.isupper():
                sifrelenmis_metin += alfabe[sifrelenmis_index].upper()
            else:
                sifrelenmis_metin += alfabe[sifrelenmis_index]

        else:
            sifrelenmis_metin += harf

    return sifrelenmis_metin

def decoder(metin, anahtar):
    alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    cozulmus_metin=""

    for harf in metin:
        if harf.lower() in alfabe:
            index = alfabe.index(harf.lower())
            # Negatif indeks değerlerini alabilmek için len(alfabe) kadar ekleyerek tekrarlamak
            cozulmus_index = (index - anahtar) % len(alfabe)

            if harf.isupper():
                cozulmus_metin += alfabe[cozulmus_index].upper()
            else:
                cozulmus_metin += alfabe[cozulmus_index]
        else:
            cozulmus_metin += harf

    return cozulmus_metin



while True:
    try:
        secim = int(input("Yapmak istediğiniz işlemi seçin\n1 - Çevirme işlemi\n2 - Çözme işlemi\n3 - Çıkış\n:"))

        if secim == 1:
            metin = input("Çevirmek istediğiniz metni giriniz: ")
            anahtar = int(input("Kaç adım öteleneceğini giriniz: "))
            print(f"\n\nşifrelenmiş metin : {encryption(metin, anahtar)}\n\n")
        elif secim == 2:
            metin = input("Çözmek istediğiniz metni giriniz: ")
            anahtar = int(input("Kaç adım öteleneceğini giriniz: "))
            print(f"\n\nçözülmüş metin : {decoder(metin, anahtar)}\n\n")
        elif secim == 3:
            print("\nÇıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen 1, 2 veya 3 seçeneklerinden birini girin.")

    except ValueError:
        print("Geçersiz giriş! Sayı girmelisiniz.")
