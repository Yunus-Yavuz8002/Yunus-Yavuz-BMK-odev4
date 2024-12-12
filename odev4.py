# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 
def soyle(yazı,tekrar_sayısı):

    for i in range(tekrar_sayısı):
        print(yazı)
soyle("Merhaba",3)

# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.

# def hesap(x,y):
#     alan=x*y
#     cevre=2*(x+y)
#     return alan, cevre
# print(hesap(10,2))


# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
# import random
# def yazıtura():
#     sonuc=["yazı","tura"]
#     secim=random.choice(sonuc)
#     return secim
# print(yazıtura())

# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
# def asal_sayilar_hangileri(bas,son):
#      asal_sayilar=[]

#      for sayi in range(bas,son+1):
#          if sayi>1:
#              for x in range(2,int(sayi**0.5)+1):
#                  if sayi % x == 0:
#                      break
#              else:
#                      asal_sayilar.append(sayi)
#      return asal_sayilar
# bas=5
# son=50
# print(f"{bas} ve {son} arasındaki asal sayılar:{asal_sayilar_hangileri(bas,son)}")


# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.
# def tam_bolenler(sayi):
#     bolenler=[]

#     for x in range(1,int(sayi)+1):
#         if sayi%x==0:
#             bolenler.append(x)
        
        
    
#     return bolenler

# sayi=50
# print(f"{sayi} sayısının tam bölenleri:{tam_bolenler(sayi)}")
