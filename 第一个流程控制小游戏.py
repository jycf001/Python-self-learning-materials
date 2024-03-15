print('欢迎来到异世界，请先验证身份：')
age = int(input('Please enter your age：'))
sex = str(input('Please enter your gender：'))
#print('请输入数字')
if age >= 18 and sex in ['male','man']:
    print('Welcome to new world!')
else:
    print('Sorry，You don\'t meet the conditions')