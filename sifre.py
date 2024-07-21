import random 

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

a = int (input('Istediginiz sifrenizin uzunlugunu sayi olarak yazin: '))

parola = ''

for i in range (a):

    parola += random.choice(karakterler)

print("Parolaniz: " , parola)
