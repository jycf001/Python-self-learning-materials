import re
print('欢迎来到异世界，请先验证身份：')
while True:
    try:
        age = int(input('Please enter your age：'))
        break
    except ValueError:
        print('The format you entered is not int,Please re-enter')
while True:
        gender = input('Please enter your gender：')
        if not re.match(r'^[a-zA-Z\u4e00-\u9fa5]+$', gender):
            print('The format you entered is not string,Please re-enter')
        else:
            break
#print('请输入数字')
if age >= 18 and gender in ['male','man']:
    print('Welcome to new world!')
else:
    print('Sorry，You don\'t meet the conditions')