# 名片管理系统，主流程控制文件

# 导入功能函数模块文件
import cardinfo_tools

# 主循环，显示系统功能，接收用户功能选择信息
# 根据功能选项，调用对应的功能函数

while True:
    # 1> 显示菜单信息
    cardinfo_tools.show_menu()
    # 2> 接收用户输入(输入'0'，退出系统)
    action_s = input("请输入功能选项：")
    if action_s in ["1", "2", "3"]:
        # 若选择功能"1",调用cardinfo_tools模块中的new_card()，完成1条名片信息的插入
        if action_s == "1":
            cardinfo_tools.new_card()
        # 若选择功能"2",调用cardinfo_tools模块中的show_all()，显示所有名片信息
        elif action_s == "2":
            cardinfo_tools.show_all()
        # 若选择功能"3",调用cardinfo_tools模块中的search_card()，查询名片信息
        else:
            cardinfo_tools.search_card()
    # 如果输入"0"，退出系统
    elif action_s== "0":
        print("欢迎下次使用！")
        break
    else:
        print("输入的信息有误，请重新输入!")