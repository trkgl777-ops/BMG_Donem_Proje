# Brookshear Makine Dili Yorumlayıcısı
# Kullanıcıdan 4 haneli hex kod alıp, komutu Türkçe açıklayan program

def main():
    print("Brookshear Makine Dili Yorumlayıcısı")
    print("=" * 40)
    print("Lütfen 4 haneli bir HEX kodu girin (Örnek: 14A3, 5012)")
    print("Çıkmak için 'q' tuşuna basabilirsiniz.")
    print("=" * 40)

    while True:
        hex_kodu = input("\nHEX Kodunu Girin: ").strip().upper()

        if hex_kodu == 'Q':
            print("Program sonlandırılıyor...")
            break

        # Giriş validasyonu
        if len(hex_kodu) != 4:
            print("HATA: Kod tam olarak 4 haneli olmalıdır!")
            continue

        # Geçerli hex karakterleri kontrolü
        valid_hex_chars = set("0123456789ABCDEF")
        if not all(c in valid_hex_chars for c in hex_kodu):
            print("HATA: Geçersiz HEX karakteri! Sadece 0-9 ve A-F kullanılabilir.")
            continue

        # Kodu parçalara ayır
        opcode_hex = hex_kodu[0]
        operand = hex_kodu[1:]

        # Opcode'u ondalık sayıya çevir
        try:
            opcode = int(opcode_hex, 16)
        except ValueError:
            print("HATA: Opcode çevrim hatası!")
            continue

        # Komutları decode et
        aciklama = decode_komut(opcode, operand)

        # Sonucu göster
        print("\n" + "=" * 40)
        print(f"Girilen Kod: {hex_kodu}")
        print(f"Açıklama: {aciklama}")
        print("=" * 40)


def decode_komut(opcode, operand):
    """
    Brookshear makinesi komutlarını decode eder
    """
    
    # Operand'ı parçala (register ve adres/veri için)
    if len(operand) == 3:
        reg_hex = operand[0]
        adres_hex = operand[1:]
        
        try:
            register = int(reg_hex, 16)
            adres = int(adres_hex, 16)
        except ValueError:
            return "HATA: Operand çevrim hatası!"
    else:
        return "HATA: Operand formatı hatalı!"

    # Opcode'a göre işlem seç
    if opcode == 0x1:  # 1 - Load from Memory
        return f"{adres_hex} adresindeki bellek hücresinin içeriğini, {register} numaralı kaydediciye yükle."
    
    elif opcode == 0x2:  # 2 - Load Immediate
        return f"{adres_hex} değerini (hex), {register} numaralı kaydediciye doğrudan yükle."
    
    elif opcode == 0x3:  # 3 - Store
        return f"{register} numaralı kaydedicideki değeri, {adres_hex} adresindeki bellek hücresine kaydet."
    
    elif opcode == 0x4:  # 4 - Move
        reg2_hex = operand[2]
        reg2 = int(reg2_hex, 16)
        return f"{register} numaralı kaydedicideki değeri, {reg2} numaralı kaydediciye kopyala."
    
    elif opcode == 0x5:  # 5 - Add Integer
        reg2_hex = operand[2]
        reg2 = int(reg2_hex, 16)
        return f"{register} ve {reg2} numaralı kaydedicilerdeki tam sayıları topla, sonucu {register}. kaydediciye kaydet."
    
    elif opcode == 0x6:  # 6 - Add Float
        reg2_hex = operand[2]
        reg2 = int(reg2_hex, 16)
        return f"{register} ve {reg2} numaralı kaydedicilerdeki ondalıklı sayıları topla, sonucu {register}. kaydediciye kaydet."
    
    elif opcode == 0x7:  # 7 - OR
        reg2_hex = operand[2]
        reg2 = int(reg2_hex, 16)
        return f"{register} ve {reg2} numaralı kaydedicilere mantıksal VEYA (OR) işlemi uygula, sonucu {register}. kaydediciye kaydet."
    
    elif opcode == 0x8:  # 8 - AND
        reg2_hex = operand[2]
        reg2 = int(reg2_hex, 16)
        return f"{register} ve {reg2} numaralı kaydedicilere mantıksal VE (AND) işlemi uygula, sonucu {register}. kaydediciye kaydet."
    
    elif opcode == 0x9:  # 9 - XOR
        reg2_hex = operand[2]
        reg2 = int(reg2_hex, 16)
        return f"{register} ve {reg2} numaralı kaydedicilere mantıksal ÖZEL VEYA (XOR) işlemi uygula, sonucu {register}. kaydediciye kaydet."
    
    elif opcode == 0xA:  # A - Rotate
        count = int(operand[2], 16)
        return f"{register} numaralı kaydedicideki değeri, {count} kez sağa döndür (rotate)."
    
    elif opcode == 0xB:  # B - Jump
        reg2_hex = operand[2]
        reg2 = int(reg2_hex, 16)
        return f"{register} ve {reg2} numaralı kaydediciler eşitse, program akışını {adres_hex} adresine atla."
    
    elif opcode == 0xC:  # C - Halt
        return "Programı durdur (HALT)."
    
    else:
        return f"Bilinmeyen opcode: {opcode} (HEX: {opcode:X})"


# Programı başlat
if __name__ == "__main__":
    main()