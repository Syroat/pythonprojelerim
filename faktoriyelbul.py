print("""
$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$

    Faktöriyel bulma programı ..

      c0der by Syroat

$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$

""")
while True:
    sayı= int(input("Sayıyı giriniz:"))

    faktoriyel = 1
    
    for i in range(2,sayı+1):
        faktoriyel *= i
        print(faktoriyel)
