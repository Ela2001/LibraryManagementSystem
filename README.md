# Kütüphane Yönetim Sistemi

Bu proje, Python ve SQLite kullanılarak geliştirilmiş terminal tabanlı bir Kütüphane Yönetim Sistemi uygulamasıdır.

## Kullanılan Teknolojiler

- Python 3
- SQLite
- Git
- GitHub
- Terminal / CLI

## Proje Amacı

Bu uygulamanın amacı, bir kütüphanedeki kitap, üye ve ödünç alma işlemlerini basit ve düzenli bir şekilde yönetmektir.

## Özellikler

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
- Ödünç listesini görüntüleme
- Kitap stok takibi

## Veritabanı Yapısı

Projede 3 temel tablo bulunmaktadır:

### books

| Alan | Tür |
| --- | --- |
| id | INTEGER |
| title | TEXT |
| author | TEXT |
| year | INTEGER |
| stock | INTEGER |

### members

| Alan | Tür |
| --- | --- |
| id | INTEGER |
| name | TEXT |
| phone | TEXT |

### loans

| Alan | Tür |
| --- | --- |
| id | INTEGER |
| book_id | INTEGER |
| member_id | INTEGER |
| loan_date | TEXT |
| return_date | TEXT |

## Kurulum ve Çalıştırma

Projeyi çalıştırmak için bilgisayarda Python 3 kurulu olmalıdır.

Terminalde proje klasörüne girilir:

```bash
cd LibraryManagementSystem