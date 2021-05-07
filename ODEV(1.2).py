#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print(" 5 adet rakam giriniz")
sayici = 0
while sayici < 5 :
    rakam = int(input(" Rakamı giriniz : "))
    sayici = sayici + 1
    if rakam > 1 :
       for a in range(2,rakam):
           if (rakam % a) == 0:
               print("Verilem rakam asal sayı değil ")
               break
       else:
           print("Verilen rakam asal sayıdır")
    else:
       print("Verilen rakam asal sayı değil ")

