class Person:
    """人的类"""
    def __init__(self,name):
        self.name = name
    def anzhuang_zidan(self,dan_jia_temp,zi_dan_temp):
        """把子弹安装到弹夹中"""

        dan_jia_temp.baocun_zidan(zi_dan_temp)

    def anzhuang_danjia(self,gun_temp,dan_jia_temp):
        """把弹夹安装到抢中"""

        gun_temp.baocun_danjia(dan_jia_temp)


    
class Gun:
    """枪类"""
    def __init__(self,name):
        self.name = name  #记录枪的类型
        self.danjia = None
    def baocun_danjia(self,dan_jia_temp):
        self.danjia = dan_jia_temp
    def __str__(self):
        return "枪的信息:%s"%(self.name)



class Danjia:
    """弹夹类"""
    def __init__(self,max_num):
        self.max_num = max_num
        self.zidan_list =[] #用来记录子弹的引用
    def baocun_zidan(self,zi_dan_temp):
        """将这颗子弹保存"""
        self.zidan_list.append(zi_dan_temp)

    def __str__(self):
        return "弹夹的信息:%d/%d"%(len(self.zidan_list),self.max_num)



class Zidan:
    """子弹类"""
    def __init__(self,shanghai):
        self.shanghai = shanghai #子弹的伤害


def main():

    laowang = Person("老王")

    ak47 = Gun("ak47")

    dan_jia = Danjia(20)
    for _ in range(15):
        zi_dan = Zidan("10")

        laowang.anzhuang_zidan(dan_jia,zi_dan)

    laowang.anzhuang_danjia(ak47,dan_jia)

    print(dan_jia)
    print(ak47)

if __name__ == "__main__":
    main()