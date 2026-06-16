# Kütüphane Yönetim Sistemi

Bu proje, Python programlama dili ve SQLite veritabanı kullanılarak geliştirilmiş terminal tabanlı bir kütüphane yönetim sistemi uygulamasıdır.

Proje kapsamında kitap, üye ve ödünç alma işlemleri veritabanı üzerinde yönetilmektedir. Kullanıcı, terminal üzerinden menüler aracılığıyla kitap ve üye kayıtları oluşturabilir, mevcut kayıtları listeleyebilir, güncelleyebilir, silebilir ve kitap ödünç/iade işlemlerini gerçekleştirebilir.

## Projenin Amacı

Bu projenin amacı, bir kütüphanede ihtiyaç duyulan temel işlemleri basit, anlaşılır ve veritabanı destekli bir sistem ile gerçekleştirmektir.

Sistem aşağıdaki temel ihtiyaçlara çözüm sunar:

- Kitap kayıtlarının yönetilmesi
- Üye kayıtlarının yönetilmesi
- Kitap ödünç verme işlemlerinin takip edilmesi
- Kitap iade işlemlerinin kaydedilmesi
- Kitap stok durumunun güncel tutulması
- Verilerin SQLite veritabanında saklanması

## Kullanılan Teknolojiler

| Teknoloji | Açıklama |
| --- | --- |
| Python 3 | Uygulama geliştirme dili |
| SQLite | Veritabanı yönetimi |
| Git | Sürüm kontrol sistemi |
| GitHub | Proje deposu |
| CLI | Terminal tabanlı kullanıcı arayüzü |

## Sistem Özellikleri

### Kitap İşlemleri

- Kitap ekleme
- Kitap listeleme
- Kitap güncelleme
- Kitap silme

Kitaplar için kitap adı, yazar, yayın yılı ve stok bilgisi tutulmaktadır.

### Üye İşlemleri

- Üye ekleme
- Üye listeleme
- Üye güncelleme
- Üye silme

Üyeler için ad ve telefon bilgisi tutulmaktadır.

### Ödünç İşlemleri

- Kitap ödünç verme
- Kitap iade alma
- Ödünç kayıtlarını listeleme

Bir kitap ödünç verildiğinde kitabın stok değeri 1 azalır. Kitap iade edildiğinde stok değeri 1 artar.

## Veritabanı Tasarımı

Projede SQLite veritabanı kullanılmaktadır. Veritabanı tabloları `sql/create_tables.sql` dosyasında oluşturulmuştur.

### books Tablosu

| Alan | Tür | Açıklama |
| --- | --- | --- |
| id | INTEGER | Kitap ID değeri |
| title | TEXT | Kitap adı |
| author | TEXT | Yazar adı |
| year | INTEGER | Yayın yılı |
| stock | INTEGER | Stok adedi |

### members Tablosu

| Alan | Tür | Açıklama |
| --- | --- | --- |
| id | INTEGER | Üye ID değeri |
| name | TEXT | Üye adı |
| phone | TEXT | Telefon numarası |

### loans Tablosu

| Alan | Tür | Açıklama |
| --- | --- | --- |
| id | INTEGER | Ödünç kayıt ID değeri |
| book_id | INTEGER | Ödünç verilen kitabın ID değeri |
| member_id | INTEGER | Kitabı alan üyenin ID değeri |
| loan_date | TEXT | Ödünç alma tarihi |
| return_date | TEXT | İade tarihi |

`loans` tablosunda `book_id` alanı `books` tablosuna, `member_id` alanı ise `members` tablosuna bağlıdır.

## Proje Dosya Yapısı

LibraryManagementSystem/

- main.py
- database.py
- books.py
- members.py
- loans.py
- library.db
- sql/create_tables.sql
- tests/test_cases.txt
- .gitignore
- README.md

  ## Dosyaların Görevleri

- main.py: Ana menü ve alt menülerin çalıştırıldığı dosya.
- database.py: Veritabanı bağlantısı ve tablo oluşturma işlemlerinin yapıldığı dosya.
- books.py: Kitap ekleme, listeleme, güncelleme ve silme işlemlerinin bulunduğu dosya.
- members.py: Üye ekleme, listeleme, güncelleme ve silme işlemlerinin bulunduğu dosya.
- loans.py: Kitap ödünç verme, iade alma ve ödünç listeleme işlemlerinin bulunduğu dosya.
- sql/create_tables.sql: Veritabanı tablolarını ve örnek verileri oluşturan SQL dosyası.
- tests/test_cases.txt: Manuel test senaryolarının bulunduğu dosya.
- README.md: Proje açıklamaları ve kullanım talimatlarının bulunduğu dosya.

  ## Kurulum ve Çalıştırma

- Projeyi çalıştırmak için bilgisayarda Python 3 kurulu olmalıdır.

- GitHub üzerinden projeyi indirmek için -> 
   git clone https://github.com/Ela2001/LibraryManagementSystem.git

- Proje klasörüne girmek için -> 
   cd LibraryManagementSystem

- Programı çalıştırmak için -> 
   python main.py

## Kullanım

Program çalıştırıldığında kullanıcıyı ana menü karşılar:

===== KÜTÜPHANE YÖNETİM SİSTEMİ =====

1- Kitap İşlemleri  
2- Üye İşlemleri  
3- Ödünç İşlemleri  
4- Çıkış

Kullanıcı yapmak istediği işleme göre ilgili menü numarasını seçer.

## Örnek Kullanım

Kitap ekleme örneği:

1- Kitap İşlemleri  
1- Kitap Ekle  
Kitap adı: Sefiller  
Yazar: Victor Hugo  
Yayın yılı: 1862  
Stok adedi: 5

Üye ekleme örneği:

2- Üye İşlemleri  
1- Üye Ekle  
Üye adı: Ali Yılmaz  
Telefon: 05551234567

Kitap ödünç verme örneği:

3- Ödünç İşlemleri  
1- Kitap Ödünç Ver  
Ödünç verilecek kitap ID: 1  
Üye ID: 1

## Testler

Proje manuel olarak terminal üzerinden test edilmiştir. Test senaryoları `tests/test_cases.txt` dosyasında yer almaktadır.

Test edilen temel işlemler:

- Program başlatma
- Kitap ekleme
- Kitap listeleme
- Kitap güncelleme
- Kitap silme
- Üye ekleme
- Üye listeleme
- Üye güncelleme
- Üye silme
- Kitap ödünç verme
- Kitap iade alma
- Ödünç kayıtlarını listeleme
- Programdan çıkış

## Git ve GitHub Kullanımı

Proje Git ile sürüm kontrolüne alınmış ve GitHub deposuna yüklenmiştir. Geliştirme sürecinde anlamlı commit mesajları kullanılmıştır.

GitHub deposu:

https://github.com/Ela2001/LibraryManagementSystem

## Sonuç

Bu proje ile Python ve SQLite kullanılarak çalışan bir veritabanı uygulaması geliştirilmiştir. Uygulama, terminal üzerinden kullanıcı etkileşimi sağlayarak kitap, üye ve ödünç alma işlemlerinin yönetilmesini mümkün hale getirmektedir.

Proje eğitim amacıyla hazırlanmıştır.
