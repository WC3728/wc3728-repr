import random


class Goods(object):
    def __init__(self, name, price, balance):
        self.name = name
        self.price = price
        self.balance = balance


# 商品仓库类
class Storage(object):
    def __init__(self):
        self.good_list = []
        names = ['Mac电脑','PythonBook','草莓键盘','iPhone']
        prices = [20000,30,80,7000]
        balances = [100,50,40,200]
        for i in range(len(names)):
            goods = Goods(names[i] ,prices[i] ,balances [i])
            self.good_list.append(goods)


# 购物车类
class GoodsCar(object):
    def __init__(self, buy_list=None):
        if buy_list == None:
            buy_list = []
        self.buy_list = buy_list
    def __str__(self):
        return "%s" % (self.buy_list)


# 用户类
class User(object):
    def __init__(self, name, Id, password, goods_car, is_login=False):
        self.name = name
        self.Id = Id
        self.password = password
        self.goods_car = goods_car
        self.is_login = is_login


# APP类
class APP(object):
    def __init__(self):
        self.user_dict = {}
    def get_uid(self):
        while True:
            uid = str(random.randint(10000,99999))
            if uid not in self.user_dict:
                return uid

    # 用户注册
    def register(self):
        uid = self.get_uid()
    #购物车对象
        goodscar = GoodsCar()
        name = input("请输入姓名:")
        password = input("请输入密码:")
        #根据信息创建一个用户
        user = User(name , uid ,password , goodscar ,False)
        self.user_dict[uid] = user
        print(self.user_dict[uid].__dict__)
    # 用户登录
    def login(self):
        uid = input("请输入您的id:")
        #print(self.user_dict)
        if uid not in self.user_dict:
            print("请先进行注册！！")
            return None
        user = self.user_dict[uid]
        if user.is_login:
            print("已是登陆状态！！")
            return user
        while True:
            password = input("请输入密码:")
            if password == user.password:
                user.is_login = True
                print("登陆成功！！！")
                return user
            else:
                print("请输入正确密码！！")
    # 购买商品
    def shopping(self):
        user = self.login()
        if user  == None :
            return
        uid = user.Id
        #登录成功了
        print('''
            0.Mac电脑
            1.PythonBook
            2.草莓键盘
            3.iPhone
        ''')
        #输入购买商品的序号
        index = int(input("请选择商品序号:"))
        #获取仓库中对应商品
        storage = Storage()
        goods = storage.good_list[index]
        #请用户输入购买商品的数量
        num = int(input("请输入购买商品的数量:"))
        while num > goods.balance:
            num = int(input("商品剩余量为:%d 请重新输入购买商品的数量:" %(goods.balance)))
        else:
            bug_goods = None
            for bg in user.goods_car.buy_list:
                if bg.name == goods.name:
                    bug_goods = bg
                    break
            if bug_goods:
                bug_goods.balance += num
            else:
                user_goods = Goods(goods.name , goods.price ,num )
                user.goods_car.buy_list.append(user_goods)
            #仓库中剩余量发生变化
            goods.balance -= num
            for gd in user.goods_car.buy_list:
                print(gd.name ,gd.price ,gd.balance)
    # 删除购物车中商品
    def deletegoods(self):
        user = self.login()
        if user == None :
            print("请先登录")
            return
        good_name = input("请输入商品名字:")
        goods = None
        flag = False
        for bg in user.goods_car.buy_list:
            if bg.name == good_name:
                goods = bg
                flag = True
            if not flag :
                print("没有该商品")
                return
            storage = Storage()
            #在仓库中获得该商品
            index = 0
        for i in range(len(storage.good_list)):
            if storage.good_list[i].name == good_name:
                index = i
        #根据位置索引获得商品
        storage_goods = storage.good_list[index]
        #有该商品
        num = int(input("请输入要减少商品的数量:"))
        if num >= goods.balance:
            user.goods_car.buy_list.remove(goods)
            #仓库中加上
            storage_goods.balance += goods.balance
        else:
            goods.balance -= num
            storage_goods.balance += num
        for gd in user.goods_car.buy_list:
            print(gd.name, gd.price, gd.balance,gd.price*gd.balance)
    # 结算
    def settlegoods(self):
        user = self.login()
        if user == None:
            print("请先登录")
            return
        total = 0
        for goods in user.goods_car.buy_list:
            total += (goods.price*goods.balance)
        print("商品总计{}元".format(total))
        user.goods_car.buy_list.clear()
        print(self.user_dict)

    # 退出登录
    def signout(self):
        user = self.login()
        if user!= None:
            user.is_login = False
            print("退出成功")


if __name__ == "__main__":
    app = APP()
    while True:
        print("        商城购物系统")
        print("        1.用户注册")
        print("        2.登录")
        print("        3.购买商品")
        print("        4.删除购物车中的商品")
        print("        5.结算")
        print("        6.退出登录")

        operand = int(input('您要进行的操作是:'))
        if operand == 1:
            print('>' * 10 + '用户注册' + '<' * 10)
            # 注册用户操作,将注册信息放入列表字典
            app.register()
        elif operand == 2:
            print('>' * 10 + '登录' + '<' * 10)
            app.login()
        elif operand == 3:
            print('>' * 10 + '购买商品' + '<' * 10)
            app.shopping()
            pass
        elif operand == 4:
            print('>' * 10 + '删除购物车商品' + '<' * 10)
            app.deletegoods()
            pass
        elif operand == 5:
            print('>' * 10 + '结算' + '<' * 10)
            app.settlegoods()
            pass
        elif operand == 6:
            print('>' * 10 + '退出登陆' + '<' * 10)
            app.signout()
        else:
            print('输入指令错误,退出系统！！！')
            exit()