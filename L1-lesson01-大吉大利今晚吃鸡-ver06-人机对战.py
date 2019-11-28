#人机对战
#在运行界面,先执行creatsoil(),再执行gamewithcomputer()
'''
 -*- coding: utf-8 -*-
@Time    : 2019-11-20 19:43
@Author  : Parker
@File    : L1-lesson01-大吉大利今晚吃鸡-ver05.py.py
@Software: PyCharm
@Motto   ：Always Be Coding...
'''
import random
import time
# 定义士兵类
class soildier:
    __mine = 3  # 每个士兵都有三个地雷
    # 埋入地下的地雷
    digmine = 0

    # 初始化方法
    def __init__(self, name, mine=__mine):
        self.name = name
        # 剩余的地雷
        self.mine = mine
        self.gun = None
        self.grenade = None
        self.bloodv = None
        self.medicine = None
        self.othersoildier = None
        # 初始化的时候就把地雷埋好
        # self.dighole()
        self.tip()

    # 对象初始化的提示语句
    def tip(self):
        tipwordlist = [(self.name), ("正"), ("在"), ("进"), ('入'), ('游'), ("戏"), ("模"), ("拟"), ("器"), ("."), ("."), (".")]
        for i in range(len(tipwordlist)):
            #           time.sleep(0.2)
            print("%s" % tipwordlist[i], end=" ")
        print()

    # 开枪方法
    def onfire(self):
        print("{}开枪操作".format(self.name))
        if self.gun is None:
            print("连枪都没有,怎么打?")
            return
        if self.bloodv.bloodvolume <= 0:
            print("你都挂了,还开什么枪???")
            return

        print("{}冲鸭,为了胜利!".format(self.name))
        self.gun.shoot(self.name)
        # 另一个士兵受到攻击
        self.othersoildier.__behit()

    # 使用手雷炸敌人
    def bomb_other_soildier(self):
        #(修改了此处代码)
        self.grenade.bombtarget(self.name)
        
        print("{}使用手雷操作".format(self.name))
        if self.bloodv.bloodvolume <= 0:
            print("你都挂了,还炸什么炸???")
            return
        if self.grenade.grenadecount <= 0:
            print("{},你现在没有手雷了".format(self.name))
            return
        print("{}要扔手雷了".format(self.name))
        self.grenade.fewergrenades(self.name)

        self.othersoildier.__bombed()

    # 敌人被炸的方法(私有方法)
    def __bombed(self):
        print(".", end='')
        print(".", end='')
        print(".", end='')
        print("{}被炸了".format(self.name))
        if self.bloodv.bloodvolume <= 0:
            print("我都挂了!还炸!")
            return
        self.bloodv.reduceblood(self.name, self.othersoildier.grenade.grenadehurt)

    # 不小心的自爆
    def selfdetonate(self):
        print("{}扔炸弹操作".format(self.name))
        print(".", end='')
        print(".", end='')
        print(".", end='')
        if self.bloodv.bloodvolume <= 0:
            print("没血了,不可能扔出去炸弹呀,哈哈")
            return
        print("oh,no!炸弹反弹了,把{}自己炸了~~~".format(self.name))
        self.grenade.grenadecount -= 1
        self.bloodv.reduceblood(self.name, self.grenade.grenadehurt)

    # 踩到地雷,就受到35点伤害
    def minebomb(self):
        print("{}踩到地雷了".format(self.name))
        if self.bloodv.bloodvolume <= 0:
            print("oh no {}不小心踩到地雷没血了...{}胜利".format(self.name,self.othersoildier.name))
            return
        if soildier.digmine == 0:
            print("地上已经没有地雷了")
            return
        soildier.digmine -= 1
        print("oh,no!{}踩到了地雷~~~".format(self.name))
        self.bloodv.reduceblood(self.name, 20)

    def __behit(self):
        if self.bloodv.bloodvolume == 0:
            print("{}没有血了,游戏结束".format(self.name))
            return
        self.bloodv.reduceblood(self.name)

    def usemedicine(self):
        print("{}使用药品操作".format(self.name))
        if self.medicine.medicinecount == 0:
            print("oh,不!{}现在已经没有药包了!\t".format(self.name))
            return
        if self.bloodv.bloodvolume >= 100:
            print("{}血是满的,直接刚吧\t".format(self.name))
            return
        if self.bloodv.bloodvolume <= 0:
            print("{},你已经挂了,加血也没用~~~\t".format(self.name))
            return
        self.medicine.decreasemedicine(self.name)
        self.bloodv.addblood(self.medicine.medicalvolume, self.name)

    def changing_cartridge_clip(self):
        print("{}换弹夹操作".format(self.name))
        if self.bloodv.bloodvolume <= 0:
            print("已经挂了,认命吧!\t")
            return
        self.gun.addbullet(self.name)

    # 挖坑埋地雷
    def dighole(self):
        print("{}挖地雷操作".format(self.name))
        if self.mine <= 0:
            print("{}已经没有地雷了~\t".format(self.name))
            return
        if self.bloodv.bloodvolume <= 0:
            print("{}已经挂了,{}胜利了\t".format(self.name, self.othersoildier.name))
            return
        soildier.digmine += 1
        self.mine -= 1
        minetip = [(self.name), ("正"), ("在"), ("埋"), ('地'), ('雷'), ("."), ("."), (".")]
        for i in range(len(minetip)):
            # time.sleep(0.3)
            print("%s" % minetip[i], end=" ")
        print("现在战场有{}枚地雷\t".format(soildier.digmine))


# 定义枪类
class gun:
    def __init__(self, guntype, bulletcount):
        self.guntype = guntype
        self.bulletcount = bulletcount

    def shoot(self, name):
        if self.bulletcount == 0:
            print("{}的{}没有子弹了,请及时添加子弹\t".format(name, self.guntype))
            return
        self.bulletcount -= 1
        print("{}的{}现在还有{}颗子弹\t".format(name, self.guntype, self.bulletcount))

    def addbullet(self, name):
        if self.bulletcount >= 30:
            print("{}不用加子弹,现在的子弹是满的!\t".format(self.guntype))
            return
        if 21 <= self.bulletcount <= 29:
            print("{}还有足够的子弹,不用加!\t".format(self.guntype))
            return
        self.bulletcount += 10
        print("{}的{}现在有{}发子弹\t".format(name, self.guntype, self.bulletcount))


# 定义药品类
class medicine:
    def __init__(self, medicinetype, medicinecount, medicalvolume):
        self.medicinetype = medicinetype
        self.medicinecount = medicinecount
        self.medicalvolume = medicalvolume

    def decreasemedicine(self, name):
        self.medicinecount -= 1
        print("{}现在还剩下{}个{}\t".format(name, self.medicinecount, self.medicinetype))


# 定义炸弹类
class grenade:
    def __init__(self, grenadename, grenadehurt, grenadecount):
        self.grenadename = grenadename
        self.grenadehurt = grenadehurt
        self.grenadecount = grenadecount

    def bombtarget(self, name):
        print("让一让,{}要扔炸弹啦".format(name))

    def fewergrenades(self, bombperson):
        self.grenadecount -= 1
        print("yes!{}将{}扔出去了,现在还剩{}个!\t".format(bombperson, self.grenadename, self.grenadecount))


# 定义血类
class blood:
    def __init__(self, bloodvolume):
        self.bloodvolume = bloodvolume

    def addblood(self, medicalvolume, name):
        self.bloodvolume += medicalvolume
        print("{}加完血了,现在有{}点血\t".format(name, self.bloodvolume))

    def reduceblood(self, bombedperson, hurt=10):
        if self.bloodvolume <=0:
            print("血量已经见底,请不要做无畏的抵抗了,游戏结束")
            return
        self.bloodvolume -= hurt
        print("{}现在还剩下{}点血\t".format(bombedperson, self.bloodvolume))


# first run
def creatsoil():
    global xmj, oxmj
    xmj = soildier("小码君")
    scar_xmj = gun("scar", 30)
    grenade_xmj = grenade("大手雷", 15, 4)
    blood_xmj = blood(100)
    medicine_xmj = medicine("大药包", 3, 20)

    oxmj = soildier("小码酱")
    m416_oxmj = gun("M416", 30)
    grenade_oxmj = grenade("mini手雷", 15, 4)
    blood_oxmj = blood(100)
    medicine_oxmj = medicine("药包", 3, 20)

    xmj.gun = scar_xmj
    xmj.grenade = grenade_xmj
    xmj.bloodv = blood_xmj
    xmj.medicine = medicine_xmj
    xmj.othersoildier = oxmj

    oxmj.gun = m416_oxmj
    oxmj.grenade = grenade_oxmj
    oxmj.bloodv = blood_oxmj
    oxmj.medicine = medicine_oxmj
    oxmj.othersoildier = xmj

def gamewithcomputer():
    wim_oxmj = win_xmj = 0
    lista = ["xmj.onfire()",
            "xmj.bomb_other_soildier()",
            "xmj.selfdetonate()",
            "xmj.minebomb()",
            "xmj.usemedicine()",
            "xmj.dighole()",
            ]

    listb = ["oxmj.onfire()",
            "oxmj.bomb_other_soildier()",
            "oxmj.usemedicine()",
            "oxmj.minebomb()",
            "oxmj.selfdetonate()",
            "oxmj.dighole()",
            ]

    for i in range(0, 5):
        creatsoil()
        for j in range(0, 50):
            a = random.randint(0, len(lista) - 1)
            print("------------电脑回合------------")
            eval(lista[a])
            
            zl = int(input("小码酱回合,请选择战斗指令 1.开枪,2.扔手雷,3.使用药包,4.自雷,5.踩到地雷,6.挖坑埋地雷\n"))
            b = zl-1
            eval(listb[b])
            if xmj.bloodv.bloodvolume <= 0:
                wim_oxmj +=1
                break

            if oxmj.bloodv.bloodvolume <= 0:
                win_xmj +=1
                break
    print("小码君胜利了{}次,小码酱胜利了{}次".format(win_xmj,wim_oxmj))
gamewithcomputer()
