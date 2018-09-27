print("""
**************************
    Kullanıcı Giriş
        Programı

    İşlemler :
    
1- Giriş Yap
2- Üye Ol

Çıkmak için 'q'ya basın.
**************************
""")

sys_kullanıcıad="yusuf"
sys_şifre= "1234"
kad = "boş"
şif = "boş"

while True:
    işlem=input("İşlem no:")

    if işlem=="q":
        print("Programdan Çıkılıyor ....")
        break
    
    elif int(işlem)==1:
        kullanıcıad=input("Kullanıcı adınız:")
        şifre= input("Şifreniz:")
        
        if (kullanıcıad==sys_kullanıcıad and şifre==sys_şifre) or (kullanıcıad==kad and şifre==şif):
            print("Sisteme hoşgeldiniz ...")
            break

        elif (kullanıcıad==sys_kullanıcıad and şifre!=sys_şifre) or (kullanıcıad==kad and şifre!=şif):
            print("Hatalı Şifre ...")

        else:
            print("Kullanıcı adınız ve parolanız hatalı ...")

    elif int(işlem)==2:
        kad=input("Kullanıcı ad:")
        şif=input("Şifre:")
        şif1=input("Şifrenizi onaylayın :")
        
        if şif==şif1:
            print("Başarıyla üye oldunuz ...")

        else:
            print("Şifreler birbirleriyle uyuşmuyor...")

    else:
        print("Hatalı İşlem ...")






        
