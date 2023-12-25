import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

def bike_rent_season (day_df): 
    season_df = day_df.groupby(by="season").count_rent.sum().reset_index() 
    return season_df
def total_reg_df(day_df):
   reg_df =  day_df.groupby(by="dateday").agg({
      "registered": "sum"
    })
   reg_df = reg_df.reset_index()
   reg_df.rename(columns={
        "registered": "register_sum"
    }, inplace=True)
   return reg_df

day_df = pd.read_csv("all_data.csv")

reg_df = total_reg_df(day_df)

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("bike_rent.jfif")

st.header('Bike Sharing :bike:')

st.subheader('Daily Rent')

col1, col2= st.columns(2)

with col1:
    total_rent = day_df.count_rent.sum()
    st.metric("Total Rent", value=total_rent)
with col2:
    total_sum = reg_df.register_sum.sum()
    st.metric("Total Registered", value=total_sum)

st.subheader('Grafik Jumlah Penyewa Berdasarkan Musim')
# Mengatur warna pada grafik
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
# Membuat subplot dengan 1 baris dan 1 kolom, dengan ukuran (20, 10)
fig, ax = plt.subplots(figsize=(20, 10))
# Membuat barplot untuk y="season" dan x="count_rent", menggunakan data=day_df
sns.barplot(
        x="count_rent",
        y="season",
        data=day_df.sort_values(by="season", ascending=True),
        palette=colors,
        ax=ax
    )
# mengatur judul, label y dan x, serta tick params untuk subplot tersebut
plt.title('Grafik Jumlah Penyewa Sepeda Setiap Musim', fontsize=40)
plt.xlabel('Jumlah Penyewa Sepeda', fontsize=20)
plt.ylabel('Musim', fontsize=20)
plt.tick_params(axis='x', labelsize=35)
plt.tick_params(axis='y', labelsize=30)
# Menampilkan grafik
st.pyplot(fig)

st.subheader('Grafik Jumlah Penyewa Sepeda berdasarkan Cuaca')
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3"]
fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(
    x='weathersit',
    y='count_rent',
    data=day_df.sort_values(by="season", ascending=True),
    palette=colors,
    ax=ax)

plt.title('Grafik Jumlah Penyewa Sepeda berdasarkan Cuaca', fontsize=40)
plt.xlabel('Cuaca')
plt.ylabel('Jumlah Penyewa Sepeda')
st.pyplot(fig)

st.subheader('Grafik Perbedaan Jumlah Penyewa Berdasarkan Hari Kerja, Hari Libur, dan Hari Dalam Seminggu')
# fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(15, 10))

# Membuat grafik jumlah penyewa sepeda berdasarkan workingday (hari kerja)
fig, ax = plt.subplots(figsize=(15,10))
sns.barplot(
    x='workingday',
    y='count_rent',
    data=day_df,
    ax=ax,
    palette=['#e74c3c', '#2ecc71'])
ax.set_title('Grafik Jumlah Penyewa Sepeda berdasarkan Hari Kerja', fontsize=40)
ax.set_xlabel('Hari Kerja')
ax.set_ylabel('Jumlah Penyewa Sepeda')
st.pyplot(fig)

# Membuat grafik jumlah penyewa sepeda berdasarkan holiday (hari libur)
fig, ax = plt.subplots(figsize=(15,10))
sns.barplot(
    x='holiday',
    y='count_rent',
    data=day_df,
    ax=ax,
    palette=['#e74c3c', '#2ecc71'])
ax.set_title('Grafik Jumlah Penyewa Sepeda berdasarkan Hari Libur', fontsize=40)
ax.set_xlabel('Hari Libur')
ax.set_ylabel('Jumlah Penyewa Sepeda')
st.pyplot(fig)

# Membuat grafik jumlah penyewa sepeda berdasarkan berdasarkan weekday (hari dalam seminggu)
fig, ax = plt.subplots(figsize=(15,10))
sns.barplot(
    x='weekday',
    y='count_rent',
    data=day_df,
    ax=ax,
    palette='magma')
ax  .set_title('Grafik Jumlah Pengguna Sepeda berdasarkan Hari dalam Seminggu', fontsize=40)
ax.set_xlabel('Hari dalam Seminggu')
ax.set_ylabel('Jumlah Penyewa Sepeda')
st.pyplot(fig)
st.caption('Copyright (c) Submission Nadia 2023')