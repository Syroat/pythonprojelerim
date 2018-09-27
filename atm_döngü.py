print("""
*********************************
    ATM UyGuLaMaSI
  c0der By xVenoM

  İşlemler:

  1- Bakiye Sorgula
  2- Para Yatır
  3- Para Çek

Çıkmak için 'q' ya basın ...

*********************************
""")

bakiye=1500
ad="Yusuf"
soyad="Demir"
şifre=12345
print("Devam etmek için şifrenizi girmelisiniz! ")
şifre12=int(input("Şifre :"))
if şifre12 == şifre:
    print("Başarıyla giriş yaptınız ....")
    while True:
        işlem=int(input("İşlem No : "))

        if işlem==1:
            print("Bakiyeniz : {}".format(bakiye))

        elif işlem==2:
            yatır=int(input("Yatıracağınız miktarı giriniz : "))
            bakiye += yatır
            print("Başarıyla para yatırdınız ...")

        elif işlem==3:
            çek=int(input("Çekmek istediğiniz miktarı giriniz : "))
            bakiye -= çek
            print("Başarıyla para çekiliyor ...")
            
        elif str(işlem)=="q":
            print("Programdan çıkılıyor ....")
            break

else:
    print("Hatalı şifre!")

        
