
---

# Personel ve Öğrenci Sınıfları

Bu Python programı, `Personel` ve `Ogrenci` adında iki sınıf tanımlar. `Personel` sınıfı, bir kişinin temel bilgilerini içerirken, `Ogrenci` sınıfı `Personel` sınıfından miras alır ve bir öğrencinin ek bilgilerini ekler.

## Nasıl Kullanılır

1. `personel_ogrenci.py` dosyasını çalıştırın.
2. `Ogrenci` nesnesi oluştururken, ad, soyad, yaş, kimlik numarası ve isteğe bağlı olarak öğrenci numarası sağlayın.
3. `bilgileri_goster()` yöntemini kullanarak öğrenci bilgilerini görüntüleyin.

## Örnek Kullanım

```python
from personel_ogrenci import Ogrenci

# Öğrenci nesnesi oluştur
tunay = Ogrenci("Tunay", "İnce", 20, "1223456789", "222007560")

# Öğrenci bilgilerini görüntüle
tunay.bilgileri_goster()
```

## Sınıflar ve Metodlar

- `Personel`: Ad, soyad, yaş, kimlik numarası bilgilerini içerir.
- `Ogrenci`: `Personel` sınıfından miras alır. Ayrıca öğrenci numarası bilgisini de içerir.

## Geliştirme

Bu program, temel bir sınıf miras alma örneğidir. Geliştirmek için şunları düşünebilirsiniz:

- `Personel` sınıfına yeni özellikler ekleyin (örneğin, cinsiyet, e-posta adresi).
- `Ogrenci` sınıfını genişleterek yeni yöntemler ekleyin (örneğin, ders listesi).
- Sınıflar arasında daha karmaşık bir ilişki kurun (örneğin, öğretmen sınıfı).

## Lisans

Bu program MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyin.

---
