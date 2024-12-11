# Kural Tabanlı Sınıflandırma
 # Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri  gösteriiz.

import pandas as pd
pd.set_option("display.max_rows", None)
df = pd.read_csv('persona.csv')
df.head()
df.shape
df
# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?

df["SOURCE"].nunique()
df["SOURCE"].value_counts()

# Soru3: aç unique PRICE vardır?

df['PRICE'].nunique()

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

df['PRICE'].value_counts()

# SORU5: Hangi ülkeden kaçar tane satış olmuş?

#1
df["COUNTRY"].value_counts()

#2
df.groupby('COUNTRY')['PRICE'].count()
#3
df.pivot_table(values="PRICE",index="COUNTRY",aggfunc="count")

# Soru 7: SOURCE türlerine göre satış sayıları nedir?

df["SOURCE"].value_counts()

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?

df.groupby(by=['COUNTRY']).agg({"PRICE": "mean"})

# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?

df.groupby(by=['SOURCE']).agg({"PRICE": "mean"})

# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

df.groupby(by=["COUNTRY", 'SOURCE']).agg({"PRICE": "mean"})
