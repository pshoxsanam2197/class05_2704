# 21-m
class Yozuvchi:
    def __init__(self,ism):
        self.ism = ism

    def yozish(self):
        print("Yozmoqda")

class Shoir(Yozuvchi):
    def yozish(self):
        print("She'r yozmoqda")

ota = Yozuvchi("Yozuvshi")
ota.yozish()

bola = Shoir("Shoir")
bola.yozish()

# 22-m
class Internet:
    def __init__(self,tezlik):
        self.tezlik = tezlik

    def ulanish(self):
        print("Ulandi")

class Wifi(Internet):
    def ulanish(self):
        print("Wifi ulandi")

ota = Internet("Internet")
ota.ulanish()

bola = Wifi("Wifi")
bola.ulanish()
