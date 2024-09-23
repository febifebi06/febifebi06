import requests
import pandas as pd 
# Ganti dengan API key kamu
api_key = "f6757d675b552fdf32c2c549f08e1116"
# Daftar kota yang ingin diambil datanya
cities = ["Jakarta", "Tokyo", "New York"]
# Fungsi untuk mengambil data cuaca
def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={"Jakarta", "Tokyo", "New York"}&appid={"f6757d675b552fdf32c2c549f08e1116"}&units=metric"
    response = requests.get(url)
    data = response.json()
return data

# Menyimpan data ke dalam list
data_list = []import pandas as pd
import numpy as np

# Membaca data dari file CSV
df = pd.read_csv("weather_data.csv")

# Menghitung rata-rata suhu
average_temp = df['main.temp'].mean()
print("Rata-rata suhu:", average_temp)

# Menentukan kota dengan suhu tertinggi dan terendah
highest_temp_city = df.loc[df['main.temp'].idxmax(), 'name']
lowest_temp_city = df.loc[df['main.temp'].idxmin(), 'name']
print("Kota dengan suhu tertinggi:", highest_temp_city)
print("Kota dengan suhu terendah:", lowest_temp_city)

# Analisis lebih lanjut (misalnya: menghitung frekuensi cuaca)
# ...
for city in cities:
    data = get_weather_data(city)
    data_list.append(data)
# Membuat DataFrame Pandas
df = pd.DataFrame(data_list)

# Menyimpan ke file CSV
df.to_csv("weather_data.csv", index=False)  



