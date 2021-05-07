#!/usr/bin/env python
# coding: utf-8

# In[31]:


def TemizVeri(ilk_str, ikinci_str, ucuncu_str):
    Birlesmis_deger = ""
    for a in range(len(ilk_str)):
        if not ilk_str[a].isdigit():
            
            Birlesmis_deger += ilk_str[a]
            
    Birlesmis_deger += "-"

    for a in range(len(ikinci_str)):
        if not ikinci_str[a].isdigit():
            Birlesmis_deger += ikinci_str[a]
            
    Birlesmis_deger += "-"

    for a in range(len(ucuncu_str)):
        if not ucuncu_str[a].isdigit():
             
                Birlesmis_deger += ucuncu_str[a]

    return Birlesmis_deger

print(TemizVeri("Ah5me4t", "M9eHm4eT", "Ha3K5a1n"))

