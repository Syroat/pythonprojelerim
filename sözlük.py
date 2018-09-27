print("""*****************************************
 
  Python Sözlük Programı

      c0der by Syroat

Yapabilecekleriniz:

Sözlüğünüzü dilediğiniz gibi genişletip
sözlükte ne var ne yok bakabilirsiniz.

Sözlüğe birşey eklemek için '1'
Sözlüktekilere bakmak için  '2'

Çıkmak için 'q'
*****************************************
""")

sözlük = {"bir":1,"iki":2,"üç":3}

while True:
    işlem=input("İşlem Seçiniz: ")

    if işlem == "q":
        print("Programdan çıkılıyor ...")
        break
    elif int(işlem) == 1:
        a=input("Yazıyla hangi sayıya karşılık geliyor?(oniki) : ")
        b=int(input("Sayıyla karşılığı ney ? : "))
        print("Ekleniyor .....")
        sözlük[a] = b
        print("Başarıyla eklendi!")

    elif int(işlem) == 2:
        print("""
                Sözlükteki anahtarlara bakmak için '1'
                Sözlükteki değerlere bakmak için   '2'
                Herşeye bakmak için '3'
              """)
        işlem2=int(input("İşlem seçin:"))
        if işlem2 == 1:
            print(sözlük.keys())

        elif işlem2 ==2:
            print(sözlük.values())

        elif işlem2 ==3:
            print(sözlük)

        else:
            print("Hatalı işlem!")
            print("Başa döndürülüyorsunuz ....")
            

        
        
        
        
