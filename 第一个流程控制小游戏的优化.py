print('欢迎来到异世界，请先验证身份：')
while True:
    try:
        age = int(input('Please enter your age：'))
        break
    except ValueError:
        print('The format you entered is not int,Please re-enter')
while True:
        gender = input('Please enter your gender：').lower()
        if gender in ['male','man','women','female']:
            break
        else:
            print('Please select an input in [man，woman，male，female]')
'''
sex = input('Please enter your gender：')
if isinstance(sex, str):
    break
else:
    print('The format you entered is not string,Please re-enter')
'''
#print('请输入数字')
if age >= 18 and gender in ['male','man']:
    print('Welcome to new world!')
else:
    print('Sorry，You don\'t meet the conditions')