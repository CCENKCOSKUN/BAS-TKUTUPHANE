#!/usr/bin/env python
# coding: utf-8

# In[ ]:


kullanıcılar = {}
adminşifre = '123456'
isteklistesi = []
silinenkitapbilgileri = []

class kitap:
    def __init__(self, kitapadı, kitapyazar, kitapözet):
        self.kitapadı = kitapadı
        self.kitapyazar = kitapyazar
        self.kitapözet = kitapözet

class kitaplar:
    def __init__(self):
        self.kitaplistesi = []
    
    def kitapekle(self, kitap):
        self.kitaplistesi.append(kitap)
    
    def kitapsil(self, kitapadı):
        kitap = self.kitapbul(kitapadı)
        if kitap:
            self.kitaplistesi.remove(kitap)
            silinenkitapbilgileri.append(kitap)
            print("{} silindi".format(kitap.kitapadı))
        else:
            print("{} listede bulunamadı.".format(kitapadı))
    
    def kitapsırala(self):
        if self.kitaplistesi:
            print("Kütüphanedeki kitaplar sırasıyla:")
            for kitap in sorted(self.kitaplistesi, key=lambda k: k.kitapadı):
                print(kitap.kitapadı)
        else:
            print("Kütüphanede hiç kitap yok.")
    
    def kitapbul(self, kitapadı):
        for kitap in self.kitaplistesi:
            if kitap.kitapadı == kitapadı:
                return kitap
        return None

class admin:
    def __init__(self, kütüphane):
        self.kütüphane = kütüphane
    
    def kitapekle(self):
        kitapad = input("Kitap adını girin: ")
        kitapyazar = input("Kitabın yazarını girin: ")
        kitapözet = input("Kitabın kısa bir özetini girin: ")
        yenikitap = kitap(kitapad, kitapyazar, kitapözet)
        self.kütüphane.kitapekle(yenikitap)
    
    def kitapsil(self):
        kitapad = input("Silinecek kitabın adını girin: ")
        self.kütüphane.kitapsil(kitapad)

class kullanıcı:
    def __init__(self, kütüphane):
        self.kütüphane = kütüphane
    
    def kitapözetgor(self):
        kitapadı = input("Özetini görmek istediğiniz kitabın adını giriniz: ")
        kitap = self.kütüphane.kitapbul(kitapadı)
        if kitap:
            print("Özet: {}".format(kitap.kitapözet))
        else:
            print("{} kitabı bulunamadı.".format(kitapadı))
    
    def kitapteslimal(self):
        kitapadı = input("Teslim almak istediğiniz kitabın adını giriniz: ")
        self.kütüphane.kitapsil(kitapadı)
    
    def kitapteslimet(self):
        kitapadı = input("Teslim edeceğiniz kitabın adını giriniz: ")
        kitap = None
        for k in silinenkitapbilgileri:
            if k.kitapadı == kitapadı:
                kitap = k
                break
        if kitap:
            self.kütüphane.kitapekle(kitap)
            silinenkitapbilgileri.remove(kitap)
            print(f"{kitapadı} kitabı teslim edildi.")
        else:
            print(f"{kitapadı} kitabı bulunamadı.")
    
    def isteklistesineekle(self):
        istek = input("İstek listesine eklemek istediğiniz kitabın adını giriniz: ")
        if istek in isteklistesi:
            print("İstek listesinde {} mevcut".format(istek))
        else:
            print("İstek listesine eklendi")
            isteklistesi.append(istek)

def adminmenü(kütüphane):
    admins = admin(kütüphane)
    while True:
        print("Hangi işlemi yapmak istersiniz?")
        sorgu = input("1-Kitap ekleme\n2-Kitap silme\n3-İstek listesini incele\n4-Kitap listele\nq-Çıkış\n")
        if sorgu == '1':
            admins.kitapekle()  # Burada doğru çağrılıyor
        elif sorgu == '2':
            admins.kitapsil()
        elif sorgu == '3':
            print("İstek listesi şu şekildedir:")
            print(isteklistesi)
        elif sorgu == '4':
            admins.kütüphane.kitapsırala()
        elif sorgu == 'q':
            print("Çıkış yapılıyor....")
            break
        else:
            print("Geçersiz seçenek. Lütfen 1, 2, 3, 4 veya q'yu kullanın.")

def anamenü():
    print("****** Merhaba. Kütüphanemize hoşgeldiniz :) ******\n")
    kütüphane = kitaplar()
    while True:
        seçim = input("1-Admin Girişi\n2-Kullanıcı girişi\nq-Çıkış\n").lower()
        if seçim == '1':
            admingiris(kütüphane)
        elif seçim == '2':
            kullanıcıgiriş(kütüphane)
        elif seçim == 'q':
            print("Çıkış yapılıyor..")
            break
        else:
            print("Geçersiz seçenek. Lütfen 1, 2 veya q'yu kullanın.")

def admingiris(kütüphane):
    adminşif = input("Lütfen admin şifresini giriniz:\n")
    if adminşif == adminşifre:
        print("Şifre doğru. Giriş yapılıyor...\n")
        adminmenü(kütüphane)
    else:
        print("Admin şifre hatalı.")               

def kullanıcıgiriş(kütüphane):
    sorgu = input("Üyeliğiniz var mıydı? evet/hayır: ")
    if sorgu == 'evet':
        x = input("Kullanıcı adınızı giriniz: ")
        if x in kullanıcılar:
            s = input("Şifrenizi giriniz: ")
            if kullanıcılar.get(x) == s:
                print("Başarıyla giriş yapıldı.")
                kullanıcımenü(kütüphane)
            else:
                print("Hatalı şifre.")
        else:
            print("Kullanıcı bulunamadı.")
    elif sorgu == 'hayır':
        print("Lütfen üyelik oluşturunuz.\n")
        kullanıcıadı = input("Kullanıcı adı giriniz: ")
        kullanıcışifre = input("Şifre belirleyiniz: ")
        kullanıcılar[kullanıcıadı] = kullanıcışifre
        print("Başarılı şekilde kayıt oldunuz.")
    else:
        print("Geçersiz seçenek. Lütfen evet veya hayır kullanın.")

def kullanıcımenü(kütüphane):
    users = kullanıcı(kütüphane)
    while True:
        print("1-Kitap özet görme\n2-Kitap seçip teslim almak\n3-Alınan kitabı teslim etmek\n")
        print("4-Mevcut kitapları a-z sıralama\n5-İstek listesine ekleme yapmak\nq-Çıkış\n")
        h = input("Hangi işlemi yapmak istersiniz?")
        if h == '1':
            users.kitapözetgor()
        elif h == '2':
            users.kitapteslimal()
        elif h == '3':
            users.kitapteslimet()
        elif h == '4':
            users.kütüphane.kitapsırala()
        elif h == '5':
            users.isteklistesineekle()
        elif h == 'q':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçerli bir seçenek seçiniz...")

anamenü()

