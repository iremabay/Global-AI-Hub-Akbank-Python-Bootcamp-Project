import csv
from datetime import datetime
import os

#coded by İrem Abay and Ali Gultan
#irem.abay@outlook.com & aligultanx@gmail.com

print("\n")
print("                                    HOŞGELDİNİZ\n")
print(''' _____ _                 ____          _              _____           _                 
 |  __ (_)               / __ \        | |            / ____|         | |                
 | |__) | __________ _  | |  | |_ __ __| | ___ _ __  | (___  _   _ ___| |_ ___ _ __ ___  
 |  ___/ |_  /_  / _` | | |  | | '__/ _` |/ _ \ '__|  \___ \| | | / __| __/ _ \ '_ ` _ \ 
 | |   | |/ / / / (_| | | |__| | | | (_| |  __/ |     ____) | |_| \__ \ ||  __/ | | | | |
 |_|   |_/___/___\__,_|  \____/|_|  \__,_|\___|_|    |_____/ \__, |___/\__\___|_| |_| |_|
                                                              __/ |                      
                                                             |___/                       ''')

#Pizza classları oluşturuyoruz.

class Pizza():
    def __init__(self,aciklama,fiyat): #Ust sınıf olusturduk bunlardan sonraki pizza sınıfları super init fonksiyonuyla bu pizzalarin aciklama ve fiyatlarini alacak
        self.aciklama=aciklama
        self.fiyat=fiyat

    def aciklama_al(self):
        return self.aciklama
    def fiyatbilgisi_al(self):
        return self.fiyat


class Klasik_Pizza(Pizza): # parantezin içine pizza yazmamızın sebebi class özelliklerini ana sınıftan alması(Pizza sınıfı)
    def __init__(self):
        aciklama=f"Klasik Pizza"
        fiyat=44.99
        super().__init__(aciklama,fiyat)

class Margherita_Pizza(Pizza):
    def __init__(self):
        aciklama=f"Margherita Pizza(domates, mozarella, fesleğen)"
        fiyat=49.99
        super().__init__(aciklama, fiyat)

class Turk_Pizza(Pizza):
    def __init__(self):
        aciklama=f"Türk Pizza (Domates,mozarella,döner)"
        fiyat=54.99
        super().__init__(aciklama, fiyat)

class Dominos_Pizza(Pizza):
    def __init__(self):
        aciklama=f"Dominos Pizza (Domates,fesleğen,sucuk,salam,sosis,mantar,zeytin,mısır,mozarella)"
        fiyat=59.99
        super().__init__(aciklama, fiyat)


# pizza boyutlarını pizza sınıflarıyla çarpan bir sınıf oluşturuyoruz mesela büyük  boy seçersen  fiyatını 1.50 la çarpmak için
class Decarator(Pizza):
    def __init__(self,pizza,boyutuyla_carpma):
        self.pizza=pizza
        self.boyutuyla_carpma=boyutuyla_carpma
        self.fiyat=self.pizza.fiyatbilgisi_al()*self.boyutuyla_carpma

        # aciklamalari ve fiyatlarini alıp returnle yeni değerlerini döndürdük
        def aciklama_al(self):
            return self.pizza.aciklama_al()

        def fiyatbilgisi_al(self):
            return self.fiyat

# kücük,orta,büyük boy pizza sınıfları oluşturuyoruz

class Kucuk_Boy(Decarator):
    def __init__(self,pizza):
        super().__init__(pizza,0.7)
        self.aciklama="Kucuk Boy"
    def aciklama_al(self):
        return self.aciklama

class Orta_Boy(Decarator):
    def __init__(self,pizza):
        super().__init__(pizza,1.0)
        self.aciklama="Orta Boy"
    def aciklama_al(self):
        return self.aciklama

class Buyuk_Boy(Decarator):
    def __init__(self,pizza):
        super().__init__(pizza,1.5)
        self.aciklama="Büyük Boy"
    def aciklama_al(self):
        return self.aciklama

#Sos seçmek için ilk önce classlar oluşturuyoruz.
class Sos_Decarator(Pizza):
    def __init__(self,pizza):
        self.pizza=pizza
    def aciklama_al(self):
        return self.pizza.aciklama_al()
    def fiyatbilgisi_al(self):
        return self.pizza.fiyatbilgisi_al()

class Zeytin_Sos(Sos_Decarator):
    def __init__(self,pizza):
        super().__init__(pizza)
        self.fiyat = 2.50
        self.aciklama ="Zeytin sos"

    def aciklama_al(self):
        return self.aciklama

    def fiyatbilgisi_al(self):
        return self.fiyat

class Mantar_Sos(Sos_Decarator):
    def __init__(self,pizza):
        super().__init__(pizza)
        self.fiyat = 5.00
        self.aciklama ="Mantar Sos"

    def aciklama_al(self):
        return self.aciklama

    def fiyatbilgisi_al(self):
        return self.fiyat


class KeciPeyniri_Sos(Sos_Decarator):
    def __init__(self,pizza):
        super().__init__(pizza)
        self.fiyat = 3.00
        self.aciklama ="Keçi peyniri sos"

    def aciklama_al(self):
        return self.aciklama

    def fiyatbilgisi_al(self):
        return self.fiyat


class Et_Sos(Sos_Decarator):
    def __init__(self,pizza):
        super().__init__(pizza)
        self.fiyat = 7.5
        self.aciklama ="Et sos"

    def aciklama_al(self):
        return self.aciklama

    def fiyatbilgisi_al(self):
        return self.fiyat


class Sogan_Sos(Sos_Decarator):
    def __init__(self,pizza):
        super().__init__(pizza)
        self.fiyat = 3.5
        self.aciklama ="Sogan sos"

    def aciklama_al(self):
        return self.aciklama

    def fiyatbilgisi_al(self):
        return self.fiyat


class Misir_Sos(Sos_Decarator):
    def __init__(self,pizza):
        super().__init__(pizza)
        self.fiyat = 4.5
        self.aciklama ="Mısır sos"

    def aciklama_al(self):
        return self.aciklama

    def fiyatbilgisi_al(self):
        return self.fiyat


#veritabanina isim,tc kimlik no,kredi karti no,aciklama,kart cvvsi ve tutarini yazdircaz

def veritabanina_siparis_ekle(isim,tc_no,kredi_karti_no,kredi_karti_cvv,siparis_aciklamasi,toplam_tutar):

    now=datetime.now()
    siparis_zamani=now.strftime("%Y-%m-%d %H:%M:%S")

#siparis olusturuyoruz

    import os
    import csv

    yeni_siparis = [isim, tc_no, kredi_karti_no,kredi_karti_cvv,siparis_aciklamasi, toplam_tutar]
    dosya_adi = "Orders_Database.csv"

    if os.path.isfile(dosya_adi):
        with open(dosya_adi, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(yeni_siparis)
    else:
        basliklar = ["İsim ", "TC Kimlik ", "Kredi Karti Numarasi ","CVV ", "Siparis Aciklamasi ", "Siparis Zamani ",
                     "Toplam Tutar"]
        with open(dosya_adi, mode="w", newline="") as file:  #dosya yoksa oluşturup içine sipariş bilgilerini yazicak
            writer = csv.writer(file)                        #csv dosyasına satır satır bilgileri ekleyecek
            writer.writerow(basliklar)
            writer.writerow(yeni_siparis)



def main():

    # Menünün yazılı olduğu txt dosyasını açıp ekrana yazdırıyoruz.
    with open("Menu.txt", "r",encoding="utf-8") as menu:
        print(menu.read())

#pizza seçimi alıyoruz
    pizza_sec=input("Lütfen 1-4 aralığındaki pizzalardan seçiniz:\n1.Klasik\n2.Margherita\n3.Türk\n4.Dominos\n: ")
    while pizza_sec not in ["1","2","3","4"]:
        pizza_sec=input("Lütfen geçerli bir numara giriniz!(1-4): ")

    if pizza_sec == "1":
        pizza=Klasik_Pizza()
    elif pizza_sec == "2":
        pizza=Margherita_Pizza()
    elif pizza_sec == "3":
        pizza=Turk_Pizza()
    else:
        pizza=Dominos_Pizza()
#pizza boyutu seçimini alıyoruz
    boyut_secimi=input("Lütfen pizzanin boyutunu seçiniz:\n5.Küçük Boy\n6.Orta Boy\n7.Büyük Boy\n: ")
    while boyut_secimi not in ["5","6","7"]:
        boyut_secimi=input("Lütfen geçerli bir boyut seçiniz (5-7): ")

    if boyut_secimi=="5":
        boyut =Kucuk_Boy(pizza)
    elif boyut_secimi=="6":
        boyut =Orta_Boy(pizza)
    elif boyut_secimi=="7":
        boyut=Buyuk_Boy(pizza)

#pizza sosu seçimini alıyoruz.
    sos_secimi=input("Lütfen sos seçiniz:\n11.Zeytin Sosu\n12.Mantar Sosu\n13.Keçi Peyniri Sosu\n14.Et Sosu\n15.Soğan Sosu\n16.Mısır Sosu\n: ")
    while sos_secimi not in ["11","12","13","14","15","16"]:
        sos_secimi=input("Lütfen geçerli bir sos seçiniz(11-16): ")

    if sos_secimi=="11":
        sos=Zeytin_Sos(pizza)
    elif sos_secimi=="12":
        sos=Mantar_Sos(pizza)
    elif sos_secimi =="13":
        sos=KeciPeyniri_Sos(pizza)
    elif sos_secimi =="14":
        sos=Et_Sos(pizza)
    elif sos_secimi =="15":
        sos=Sogan_Sos(pizza)
    else:
        sos=Misir_Sos(pizza)


#Kullanicidan bilgilerini aliyoruz.
    isim=input("İsminiz: ")
    tc_no=input("Tc Kimlik numaraniz: ")
    kredi_karti_no=input("Kredi Karti numaraniz: ")
    kredi_karti_cvv=input("Kredi Karti cvv numaraniz: ")

    siparis_aciklamasi = f"{boyut.aciklama_al()} {pizza.aciklama_al()} with {sos.aciklama_al()}"

    toplam_tutar=boyut.fiyatbilgisi_al() + sos.fiyatbilgisi_al()


# siparisi veritabanina kaydediyoruz.
    veritabanina_siparis_ekle(isim,tc_no,kredi_karti_no,kredi_karti_cvv,siparis_aciklamasi,toplam_tutar)

#fiş oluşturma
    toplam_tutar = round(toplam_tutar,2) # Fiyatın virgülden sonraki kısmının sadece ilk 2 basamağını göstermesi için round fonksiyonunu kullandık.
    print("Sipariş Detayları:\n")
    print(f"Ad: {isim}")
    print(f"TC Kimlik Numarası: {tc_no}")
    print(f"Kredi Kartı Numarası: {kredi_karti_no}")
    print(f"Sipariş Açıklaması: {siparis_aciklamasi}")
    print(f"Toplam Fiyat: {toplam_tutar} TL")
    print(f"Sipariş Zamanı: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("\nSiparişiniz alınmıştır.\nBizi tercih ettiğiniz için teşekkür ederiz.")

main()
