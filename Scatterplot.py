#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import library yang diperlukan
import pandas as pd
import matplotlib.pyplot as plt

# Membaca database
data = pd.read_csv("C:/sandy/522466531_bukalapak.csv")

# Membuat line chart
plt.scatter(data['jumlah_sold'], data['jumlah_rating'])

# Menambahkan judul ke plot
plt.title("Jumlah Rating dan Jumlah Sold")

# Menetapkan label sumbu X dan Y
plt.xlabel('Jumlah Sold')
plt.ylabel('Jumlah Rating')

# Menampilkan plot
plt.show()


# In[ ]:




