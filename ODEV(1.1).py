#!/usr/bin/env python
# coding: utf-8

# In[ ]:


baslangic = 'E'
while baslangic == 'E':
    numara = input("Numara giriniz ")
    if int(numara) %2 == 0 :
        print("Numara bir çift sayı")
        baslangic = input("Devam edecek misiniz ? (E/H)" )
    else:
        print("Numara tek sayı ")
        baslangic = input("Devam edecek misiniz ? (E/H) ")

