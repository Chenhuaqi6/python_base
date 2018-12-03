# 练习:
#   1. 写一个类Bicycle自行车类,有run方法,调用时
#   显示骑行的里程km
#     class Bicycle:
#         def run(self, km):
#             print("自行车骑行了", km, '公里')
#     再写一个EBicycle电动自行车类,在Bicycle的基础
#     上添加了电池电量volume属性,有两个方法:
#       fill_charge(vol)  用来充电 vol为电量
#       run(km)  方法,每骑行10km消耗电量1度,同时显
#       示当前电量,当电量耗尽时则调用Bicycle的run方法
#       (用脚蹬骑行)
    
#     class EBicycle:
#         ....
#     b = EBicycle(5)  新买的电动车内有5度电
#     b.run(10) 电动骑行了10km里,还剩4度电
#     b.run(100) 电动骑行了40km里,还剩0度电,用脚蹬
#             骑行了60km
#     b.fill_charge(10)  电动自行车充电10度
#     b.run(50)  电动骑行了50km里,还剩5度电

class Bicycle:
    def run(self,km):
        print("自行车骑行了", km ,"公里")

class EBicycle(Bicycle):
    def __init__(self,vol=0):
        self.volume = vol
    def fill_charge(self,vol):
        self.volume += vol
        print("电动车充电%d度" % self.volume)
    def run(self,km):
        e_km = min(km,self.volume * 10)
        if e_km > 0:
            self.volume -= e_km / 10
            print("电动骑行了%dkm,剩余电量%d度" % (e_km,self.volume))
        if km > e_km:
            super().run(km - e_km)
        


b = EBicycle(5)  #新买的电动车内有5度电
b.run(10) #电动骑行了10km里,还剩4度电
b.run(100) #电动骑行了40km里,还剩0度电,用脚蹬
        # 骑行了60km
b.fill_charge(10)  #电动自行车充电10度
b.run(50)  #电动骑行了50km里,还剩5度电

