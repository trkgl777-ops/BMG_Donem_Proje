# BMG_Donem_Proje
Bmg Dönem Projesi :Bookshear Makine Dili Yorumlayıcısı
Kullanıcıdan 4 haneli bir hex kodu alınıyor ve kulalnıcının girdiği hex kodunu eğer geçerli br kod ise işlevi hakkında açıklama yapılıyor,gecersiz bir kod girildiyse kodun gecersiz oldugu belirtiliyor
# Brookshear Makine Dili Yorumlayıcısı (Decoder)

Bu proje, **Brookshear Makinesi**'nin makine dili komutlarını onaltılık (hexadecimal) formatta analiz ederek, Türkçe açıklamalarını kullanıcıya sunan bir Python programıdır. Program, kullanıcıdan 4 haneli bir onaltılık kod alır, bu kodu opcode ve operand kısımlarına ayırır ve ilgili makine komutunun ne işlem yaptığını anlaşılır bir şekilde ekrana yazdırır.

---

## Proje Amacı

Makine dili ve temel bilgisayar mimarisi kavramlarını somutlaştırmak, Brookshear mimarisinin komut kümesini tanımak ve makine kodlarının yorumlanma sürecini pratikte göstermektir.

---

## Özellikler

- Kullanıcıdan 4 haneli hexadecimal kod girişi alır.
- Girdi uzunluğunu ve geçerliliğini kontrol eder.
- Opcode’a göre komutu belirler ve operandları yorumlar.
- Tüm Brookshear komutlarını (1’den C’ye kadar) destekler.
- Türkçe, açıklayıcı çıktılar üretir.

---

##  Desteklenen Komutlar (Appendix C)

Program, aşağıdaki Brookshear makine komutlarını desteklemektedir:

1. **LOAD from Memory**
2. **LOAD using Immediate Addressing**
3. **STORE**
4. **MOVE**
5. **ADD (Integer)**
6. **ADD (Floating Point)**
7. **OR**
8. **AND**
9. **XOR**
10. **ROTATE**
11. **JUMP**
12. **HALT**

Her komut için opcode 1 haneli hexadecimal, operandlar ise kalan 3 hanelik kısımda yer alır.

---

## Kullanım

1. Programı çalıştırın.
2. 4 haneli bir hexadecimal kod girin (örnek: `14A3` veya `5012`).
3. Program, kodu analiz ederek Türkçe açıklamasını ekrana yazdırır.

### Örnek Çalışma:

```
Lütfen 4 haneli hexadecimal bir komut kodu giriniz: 14A3

Çözümleme:
- Opcode: 1
- Register: 4
- Adres: A3

Açıklama: A3 adresindeki bellek hücresinin içeriğini, 4 numaralı kaydediciye (Register) yükle.
```

---

##  Teknik Detaylar

- **Dil:** Python 3
- **Girdi Kontrolü:** 
  - Uzunluk kontrolü (4 haneli olmalı)
  - Geçerli hexadecimal karakter kontrolü (0-9, A-F)
- **Kod Çözümleme:** 
  - İlk hane → opcode
  - İkinci hane → kaydedici (register) numarası
  - Son iki hane → adres veya değer
- **Yapı:** if/elif veya match/case yapıları kullanılarak opcode’lar eşleştirilir.

---

##  Proje Yapısı

```
brookshear_decoder.py  # Ana Python dosyası
README.md              # Bu dosya
```

---

##  Test Senaryoları

- `14A3` → LOAD from Memory
- `5012` → ADD (Integer)
- `C000` → HALT
- `G123` → Hatalı giriş (geçersiz karakter)
- `12345` → Hatalı giriş (uzunluk hatası)

---

##  Referans

Bu proje, **J. Glenn Brookshear**'ın "Computer Science: An Overview" kitabının **Appendix C: A Simple Machine Language** bölümüne dayanmaktadır.

---

##  Geliştirici Notu

Bu proje, makine dili ve bilgisayar mimarisi temellerini anlamak amacıyla eğitsel bir araç olarak geliştirilmiştir. Her türlü geri bildirim ve katkıya açıktır.

---

**Not:** Bu README dosyası, projenin amacını, kullanımını ve teknik özelliklerini açıklamak için hazırlanmıştır. Görsel içermeyen, düz metin formatında yazılmıştır.
