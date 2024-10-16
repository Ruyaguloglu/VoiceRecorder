# import required(gerekli)  libraries
import sounddevice as sd
from scipy.io.wavfile import write
import os

# frekans ayarı( örnek sıklığı sayısı )
freq = 44100

# Kayıt süresi
duration = int(input("Kaç saniye kayıt yapmak istiyorsunuz:"))
print("kayıt başlıyor..")

#Kaydediciyi verilen değerlerle başlat süre ve örnek sıklığı sayısı
recording = sd.rec(int(duration * freq),
                    samplerate= freq, channels=2)

#Belirtilen saniye boyunca ses kaydedin
sd.wait()
print("Kayıt tamamlandı!")

# Kaydı .wav dosyası olarak kaydetme
file_name = "kayit.wav"
write( file_name, freq, recording)

print(f"Kayıt başarıyla '{file_name}' dosyasına kaydedildi.")

if os.name== 'nt':
    os.system(f"start {file_name}")















#BU NumPy dizisini bir sese dönüştürecek
# verilen örnekleme frekansına sahip dosya
#write("recording0.wav", freq,recording)

#NumPy dizisini bir ses dosyasına dönüştürün
#wv.write("recording1.wav",recording,freq,sampwidth=2)
