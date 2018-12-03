

from student_info import *





def main_():
    infos = []
    while True:
        from menu import mymenu
        mymenu()
        want = input("请输入您想要的操作: ")

        if want == "1":
            try:
                input_student(infos)
            except ValueError as err:
                print("发生错误，错误类型",err)
                print("请重新选择操作")
        if not want:
            print("请重新输入: ")
            
        if want == "2":
           
            output_student(infos)
        if want == "3":
           
            rm(infos)
        if want == "4":
            
            change(infos)
        if want == "5":
            highg_d(infos)
        if want == "6":
            
            lowd_g(infos)
        if want == "7":
           
            h_d(infos)
        if want == "8":
           
            d_h(infos)
        if want == "9":
        
            read_file()
        if want == "10":
            save_infos(infos)
        if want == "q":
            print("感谢使用")
            break
main_()