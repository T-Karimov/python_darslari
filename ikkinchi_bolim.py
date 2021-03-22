# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 13:47:03 2021

@author: TEMUR
"""

# for funksiyasini o'rganish
#mehmonlar = ["ALI","Vali","Sardor","Sobir","Hasan"]
#for mehmon in mehmonlar:
 #   print(mehmon)
    #print("Hurmatli",{mehmon},"sizni 22.03.2021 da bo'lib o'tadigan naxor\
  #oshiga taklif etamiz")
    #print("Hurmat bilan Karimovlar oilasi")

#sonlar =list(range(1,10))
#for son in sonlar:
    #print(f"{son} ning kvadrati {son**2} teng")
#sonlar =list(range(10))
#sonlar_kubi = []
#for son in sonlar:
 #   sonlar_kubi.append(son**3)
#print(sonlar)
#sonlar_kubi= input("birinchi sonni kiriting\n>>>")
#print(sonlar_kubi)    
#ismlar=["Ali","Vali","Rustam","Sardor"]
#for ism in ismlar:
  #  print("Hurmatli",{ism},"sizni 12.04,2020 da naxor oshga taklif etamiz")
 #   print("Hurmat bilan Karimov lar oilasi")
#sonlar=list(range(1,16))
#for son in sonlar:
    #print(f"{son} ni kubi {son**3} ga teng")
    
#sonlar=list(range(11))
#sonlar_kubi=[]
#for son in sonlar:
#    sonlar_kubi.append(son**3)
#print(sonlar)
#print(sonlar_kubi)
#dostlar=[]
#print("4 ta yaqin dostizni kiriting")
#for dost in range(5):
 #   dostlar.append(input(f"{dost+1}-do'stingizni nomini kiriting \n>>>"))
#print(dostlar)
#ismlar=["Sanjar","Vali","Abror","Ogabek","Odilbek"]
#for ism in ismlar:
 #   print({ism},"bugun do'g'ilgan gunim gal jo'ro")
#print(f"kod {len(ismlar)} takrorlandi")


#kublar=list(range(1,101,2))
#for kub in kublar:
 #   print(kub**3)
#kinolar=[]
#print("5 ta sevimli kinoyizni kiriting")  
#for kino in range(6):
 #   kinolar.append(input(f"{kino+1}-kinoyizni nomini kiriting\n>>> "))
#print(kinolar)    

#avtolar = ["audi","bmw","volvo","kia","hundai"]
#for avto in avtolar:
#    if avto == 'bmw':
#        print(avto.upper())
#    else:
#        print(avto.title())
    
#ten = len ("helloworld")
#hundered=ten*ten
#one=len("t")    
#for s in range(hundered):
#    print(s+one)

#mahsulotlar= ["olma","anjir","banan","limon","shaftoli","olxo'ri","o'rik","do'lana","sabzi","qovun"]
#savat=[]
#bir=input("Savatga 1-mahsulotni qo'shing: ")
#ikki=input("Savatga ikkinchi mahsulotni qo'shing: ")
#uch=input("Savatga 3-mahsulotni qo'shing: ")
#tort=input("Savatga 5-mahsulotni qo'shing:")
#besh=input("Savatga beshinchi mahsulontni qo'shing: ")
#if bir.lower() in mahsulotlar:
#    print(f"Do'konimizda {bir.title()} bor")
#else:
#     print(f"Do'konimizda {bir.title()} yo'q")
#if ikki.lower() in mahsulotlar:
#    print(f"Do'konimizda {ikki.title()} bor")
#else:
#    print(f"Afsuski do'konimizda {ikki.title()} yo'q")
#if uch.lower() in mahsulotlar:
#    print(f"Do'konimizda {uch.title()} bor")
#else:
#    print(f"Afsuski do'konimizda {uch.title()} yo'q")
#if tort.lower() in mahsulotlar:
#    print(f"Do'konimizda {tort.title()} bor")
#else:
#    print(f"Afsuski do'konimizda {tort.title()} yo'q")
#if besh.lower() in mahsulotlar:
#    print(f"Do'konimizda {besh.title()} bor")
#else:
#    print(f"Afsuski do'konimizda {besh.title()} yo'q")
    
#mahsulotlar= ["olma","anjir","banan","limon","shaftoli","olxo'ri","o'rik","do'lana","sabzi","qovun"]
#bor_mahsulot = []
#yoq_mahsulot = []
#bir=input("Savatga 1-mahsulotni qo'shing: ")
#ikki=input("Savatga ikkinchi mahsulotni qo'shing: ")
#uch=input("Savatga 3-mahsulotni qo'shing: ")
#tort=input("Savatga 5-mahsulotni qo'shing:")
#besh=input("Savatga beshinchi mahsulontni qo'shing: ")
#if bir.lower() in mahsulotlar:
#    bor_mahsulot.append(bir.title())
#else:
#    yoq_mahsulot.append(bir.title())
#if ikki.lower() in mahsulotlar:
#    bor_mahsulot.append(ikki.title())
#else:
#    yoq_mahsulot.append(ikki.title())
#if uch.lower in mahsulotlar:
#    bor_mahsulot.append(uch.title())
#else:
#    yoq_mahsulot.append(uch.title())
#if tort.lower() in mahsulotlar:
#    bor_mahsulot.append(tort.title())
#else:
 #   yoq_mahsulot.append(tort.title())
#if besh.lower in mahsulotlar:
#    bor_mahsulot.append(besh.title())
#else:
#    yoq_mahsulot.append(besh.title())    
#print(f"Do'konimizda {bor_mahsulot} bor")
#print(f"Afsuski dokonimizda {yoq_mahsulot} yo'q")    
    
#foydalanuvchilar=["anvar","temur","vali","sardor","navruzbay"]
#login=input("Loginni kiriting ")   
#if login.lower() in foydalanuvchilar:
#    print(f"Afsuski {login} band, yangi login kiriting!")
#else:
#    print("Xush kelibsiz")
son=int(input("Istalgan sonni kiriting  "))    
if son%2:    
    
    print(f"{son} sonni 2 ga qoldiqsiz bo'linadi")
if son%4:
    print(f"{son} sonni 4 ga qoldiqsiz bo'linadi")
if son%6:
    print(f"{son} sonni 6 ga qoldiqsiz bo'linadi")
if son%8:
    print(f"{son} sonni 9ga qoldiqsiz bo'linadi")
if son%10:
    print(f"{son} sonni 10 ga qoldiqsiz bo'linadi")
    
    
    
    
    
    
    
    
    
    
    
    
    
    



















