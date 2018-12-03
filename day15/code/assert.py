def get_score():
    s = int(input("请输入学生成绩: "))
    assert 0<= s <=100, "成绩超出范围"
    # if bool(0<=s <=100) == False:
    #     raise AssertionError("成绩超出范围")
    return s


try:
    score = get_score()
    print("学生成绩",score)
except AssertionError as err:
    print("错误类型",err)