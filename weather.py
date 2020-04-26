import requests
from bs4 import BeautifulSoup

# mengambil url dari kota semarang
page = requests.get('https://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?kab=Semarang&Prov=Jawa_Tengah&AreaID=501262')
soup = BeautifulSoup(page.content, 'html.parser')

print("="*50,"\n")
print("          Web Scraping data BMKG Terkini      \n")

# mendeklarasikan kota
datakota = soup.find('h4', attrs ={'class' : 'margin-bottom-30'}).get_text()
print("Provinsi  : ",datakota)

# mendeklarasikan range waktu cuaca
waktu = soup.find('h2', attrs ={'class' : 'kota'}).get_text()
print("Waktu     : ",waktu)

# mendeklarasikan range suhu
suhu = soup.find('h2', attrs ={'class' : 'heading-md'}).get_text()
print("Suhu      : ",suhu)

# mendeklarasikan keterangan
keterangan = soup.find('div', attrs = {'class' : 'service-block clearfix'})
keterangann = keterangan.find_next('p')
all=keterangann.text
print('Hasil     : ',all,"\n")
print("="*50,"\n")