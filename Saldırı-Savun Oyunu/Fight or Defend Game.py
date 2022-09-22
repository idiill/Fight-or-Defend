import time,sys,random

def hatali_eksik():
    print("Eksik veya hatalı tuşlama!!")
    
def nokta_ekle():
    print(".")
    time.sleep(.3) 
    print("..")
    time.sleep(.3)
    print("...")
    time.sleep(.3)
    
class Oyuncu():
    def __init__(self,isim,can=10,power=100,puan=0):
        self.isim=isim
        self.can=can
        self.power=power
        self.puan=puan
        
        
    def bilgileri_goster(self):
        print(f"İsim: {self.isim}\nCan: {self.can}\nPower: {self.power}\nPuan: {self.puan}\n") 
        
    def saldir(self,dusman):
        
        sonuc=self.saldir_savun_sayi()
        if sonuc==1:
            print("Saldırı Başladı...")
            nokta_ekle()
            print("Saldırı başarılı")
            self.power-=8
            self.power+=10
            dusman.can-=1
            self.bilgileri_goster()
            dusman.bilgileri_goster()
        else:
            print("Saldırı Başladı...")
            nokta_ekle()
            print("Saldırı başarısız")
            self.power-=8
            self.can-=1
            dusman.puan+=10
            self.bilgileri_goster()
            dusman.bilgileri_goster()
       
        
        
    def savun(self,dusman):
        
        sonuc=self.saldir_savun_sayi()
        if sonuc==1:
            print("Savunma Başladı...")
            nokta_ekle()
            print("Savunma başarılı")
            dusman.power-=8
            self.puan+=10
            dusman.can-=1
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            
        else:
            print("Savunma Başladı...")
            nokta_ekle()
            print("Savunma başarısız")
            dusman.power-=8
            self.can-=1
            dusman.puan+=10
            self.bilgileri_goster()
            dusman.bilgileri_goster()

    
    
    def saldir_savun_sayi(self):
        return random.randint(1,2)


    def exit(self):
        print("Oyun kapatılıyor")
        nokta_ekle()
        sys.exit()             
        
        
oyuncu_birinci=input("Birinci oyuncunun ismi: ")      
oyuncu_ikinci=input("İkinci oyuncunun ismi: ")       
oyuncu1=Oyuncu(oyuncu_birinci)
oyuncu2=Oyuncu(oyuncu_ikinci)             
               
print("Oyun başlatılıyor")
nokta_ekle()
while True:
    print("***Hamleler***\n1-Saldır\n2-Savun\n3-Çık\n") 
    secim=input("Seçiminiz: ")
    
    if secim=="1":
        oyuncu1.saldir(oyuncu2)
    elif secim=="2":
        oyuncu1.savun(oyuncu2)
    elif secim=="3":
       oyuncu1.exit()
    else:
        hatali_eksik()
    
    if oyuncu1.puan==100 or oyuncu2.can==0 or oyuncu2.power<=0:
        print("Oyunun kazananı",oyuncu1.isim)
        break
    if oyuncu2.puan==100 or oyuncu1.can==0 or oyuncu1.power<=0:
        print("Oyunun kazananı",oyuncu2.isim)
        break
     
                              