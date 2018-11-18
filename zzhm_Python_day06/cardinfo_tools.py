# 定义全局变量，用于存放名片信息。
# 定义为列表数据，初值为:[]
cards = []

def show_menu():
    print("欢迎使用名片管理系统V1.0".center(40, "*"))
    print("1.新建名片\n2.显示所有名片信息\n3.查询名片\n\n0.退出系统")
    print("*" * 50)

def new_card():
    print("插入新名片".center(40, '-'))
    name_s = input("请输入姓名：")
    phone_s = input("请输入电话：")
    qq_s = input("请输入QQ号码：")
    mail_s = input("请输入邮箱：")

    cards.append({"name" : name_s, "phone" : phone_s,
                  "qq" : qq_s, "mail" : mail_s})
    print("成功插入了\"%s\"的信息！" % name_s)

def show_all():
    if len(cards) == 0:
        print("目前没有名片信息".center(40, "-"))
        return

    print("显示所有名片信息".center(40, '-'))
    print("姓名\t\t电话\t\tQQ\t\t邮箱\n", "-" * 50)
    for onecard in cards:
        print("%-10s\t%10s\t%10s\t%10s" % (onecard["name"], onecard["phone"],
                                        onecard["qq"], onecard["mail"]))

def search_card():
    print("查询名片信息")
    find_name = input("请输入要查询的姓名:")
    for onecard in cards:
        if onecard["name"] == find_name:
            print("找到了对应的信息")
            deal_card(onecard)
            break
    else:
        print("未找到要查询的信息！")


def deal_card(find_card):
    search_action= input("请输入要执行的操作 [1]修改[2]删除[其他]返回主菜单:")
    if search_action == "1":
        print("修改信息")
        name_input = input("请输入新的姓名:")
        if len(name_input) == 0:
            find_card["name"] = find_card["name"]
        else:
            find_card["name"] = name_input

        find_card["phone"] = input_msg(find_card["phone"], "请输入电话[按下回车不修改]:")
        find_card["qq"] = input_msg(find_card["qq"], "请输入QQ[按下回车不修改]:")
        find_card["mail"] = input_msg(find_card["mail"], "请输入邮箱[按下回车不修改]:")
    elif search_action == "2":
        cards.remove(find_card)

def input_msg(srcinfo, tip_msg):
    dest_s = input(tip_msg)
    if len(dest_s) > 0:
        return dest_s
    return srcinfo

