#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
os.system('color a')
setting = int(input("Apakah library Numpy, IPython, Matplotlib sudah anda instal? 1: Ya, 2: Tidak>>"))
if setting == 1:
    os.system('pip install numpy')
    os.system('pip install matplotlib')
    os.system('pip instal ipython')
else:
    print("Baik kita lanjutkan!")
os.system('python code/codemetnum2.py')
k=input("Tekan ENTER untuk exit")

