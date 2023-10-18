class  airplane:
    def __init__(self,samolyot_name,samalyot_bak,texnik_xolat,uchish_tezligi,kishi_sigimi) -> None:
        super().__init__()
        self.name=samolyot_name
        self.bak=samalyot_bak
        self.texnik=texnik_xolat
        self.uchish=uchish_tezligi
        self.sigim=kishi_sigimi 
    def malumot(self):
        return f'''name->{self.name}
bak-{self.bak} litr
texnik-{self.texnik} xolatda
tezligi-{self.uchish} km soat
''' 
s1=airplane('Uzbekiston',4500,'Alo',300,250)
class Aeraport:
    def __init__(self,nomi:str,och_yil:str) -> None:
        self.nomi=nomi
        self.yil=och_yil
        self.dbilet=[]
        self.vbilet=[]
    def salom(self) -> str:
        return f'{self.nomi}'    
class bilet:
    def __init__(self,voqti,davlati,narxi) -> None:
        self.vaqti=voqti
        self.davlat=davlati
        self.narxi=narxi
    def __str__(self) -> str:
        return f'''vaqti-{self.vaqti}
davlat-{self.davlat}
price-{self.narxi}$'''
    def __str__(self) -> str:
                return f'''vaqti-{self.vaqti}
davlat-{self.davlat}
price-{self.narxi}'''

class karta:
    def __init__(self,raqami:int,amal_qilishi:int,pinkod:int,name:str,balance:int) -> None: 
        self.nomi=name
        self.__kod=pinkod
        self.raqam=raqami
        self.muddati=amal_qilishi
        self.__balance=balance

    def Add_money(self,sum):
        self.__balance+=sum
        print(f"{sum} kartaga qo'shildi")
    def get_Money(self,yech):
        if self.__balance>yech:
            self.__balance-=yech
            print(f'{yech} UZS yechildi')
        else:
            print("xisobingizda yetarli pul mavjud emas!!")    
    def Parolni_ozgartir(self,new):
        self.__kod=new  
        print("parol O'zgardi")  
    def Pul_Otkazmalar(self,karta_raqami:int,nomi:str,kart:int):
        self.__balance-=kart
        print(f"{nomi} kartasiga {kart} UZS otkazildi")
    def xisob(self):
        print(f'{self.__balance} UZS')   
    def Paynet(self,number,money):
        if self.__balance>money:
            self.__balance-=money
            print(f'{number} ga {money} UZS otkazildi')     
        else:
            print("xisobingizda yetarli pul mavjud emas!!")    
    
    def __str__(self) -> str:
        return f'''nomi {self.nomi}
        parol {self.__kod}
        karta raqam {self.raqam}
        balance {self.__balance}'''
    
class user(karta):
        def __init__(self, raqami: int, amal_qilishi: int, pinkod: int, name: str, balance: int,nbalance:int) -> None:
            super().__init__(raqami, amal_qilishi, pinkod, name, balance)
            self.nbalance=nbalance
m1=Aeraport(input("Enter your name: "),input("ochilgan yili: "))

for i in range(int(input("nechta davlat kiritasiz: "))):

    i=bilet(input("soat toliq kiriting: "),input("davlat: "),int(input("price: ")))

    m1.dbilet.append(i)   

for i in range(int(input("nechta viloyat kiritasiz: "))):
    i=bilet(input("soat toliq kiriting: "),input("viloyat: "),int(input("price: ")))   

    m1.vbilet.append(i)

use=user(int(input('Karta raqamini kiriting: ')),int(input("Amal qilish muddati: ")),int(input("Parolni kiriting: ")),input('karta nomini kiriting: '),int(input("kbalanceyni kiriting: ")),int(input("naxt_balance narx kiriting: ")))    

print(f"Assalomu Aleykum bizni {m1.nomi} INTERNATION AEROPORTGA Xush kelibsiz!!!")

print("Bizda")   
while(True):
    print(f"""1.samalyot xaqida malumot
2.bilet va boshqa malumotlar,
3.bilet_olish,4.Exit""")
    k=int(input("Enter your choice: "))
    if k==1:
        print(s1.malumot())
    elif k==2:
         print("bizda ikki xil tur mavjud 1.Davlat,2.Viloyat")
         k=int(input("Enter your choice: "))
         if k==1:
            for i in m1.dbilet:
                 print(f'{str(i)} $') 
         elif k==2:
                    for i in m1.vbilet:
                        print(f'{str(i)} UZS')            
    elif k==3:
        print("bizda ikki xil tur mavjud 1.Davlat,2.Viloyat")
        k=int(input("Enter your choice: "))
        if k==1:
            for i in m1.dbilet:
                 a=input("Davlatni kiriting: ")
                 if a in str(i):
                      print("1.karta,2.naxt")  
                      o=int(input("kiriting: "))
                      if o==1:
                          k=int(input("Karta raqamini kiriting: "))
                          if k==use.__kod:
                              use.get_Money(int(input("summani kiriting: ")))
                          else:
                              print("parol xato")   
                              break
                      elif o==2:  
                        d=int(input("Summani kiriting: "))
                        if d>use.__balance:
                            d-=use.__balance
                        else:
                            print("yetarli mablag mavjud emas!!!")  
                 else:
                     print("Afsuskiy Bu reys uchib ketib bolibdi")            
        elif k==2:
            for i in m1.vbilet:
                 a=input("Viloyatni kiriting: ")
                 if a in str(i):
                      print("1.karta,2.naxt")
                      o=int(input("kiriting: "))
                      if o==1:
                          k=int(input("Karta raqamini kiriting: "))
                          if k==use.__kod:
                              use.get_Money(int(input("summani kiriting: ")))
                          else:
                              print("parol xato")   
                              break        
                          while True:
                            print(f"""1.Xisobni Toldirish,
2.Pul yechish,
3.Parolni O'zgartirish,
4.Paynet,
5.Xisobni ko'rish,
6.Pul Otkazmalar,
7.Exit""")
                            a=int(input("Enter your number: "))
                            if a==1:
                                use.Add_money(int(input("kerakli summani kiriting: ")))
                            elif a==2:
                                use.get_Money(int(input("summani kiriting: ")))
                            elif a==3:
                                use.Parolni_ozgartir(int(input("new parol kiriting: ")))
                            elif a==4:
                                use.Paynet(input("Telefon raqamingizni kiriting: "),int(input("summani kiriting: ")))
                            elif a==5:
                                use.xisob()   
                            elif a==6:
                                use.Pul_Otkazmalar(int(input('karta raqamini kiriting: ')),input("nomini kiriting: "),int(input("summani kiriting: ")))    
                            elif a==7:
                                print('Chek Chiqarilsinmi')
                                b=input(">> ")
                                if b=='Xa' or b=='xa':
                                    print('chek chiqarildi')
                                    break
                                else:
                                    break                 
                      elif o==2:
                        d=int(input("Summani kiriting: "))
                        if d>use.balance:
                            d-=use.balance
                        else:
                            print("yetarli mablag mavjud emas!!!")  
    else:
        print('yolingiz bexatar bolsin')         
        break       
