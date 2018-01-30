h = input('请输入身高：')
w = input('请输入体重：')
height = float(h)
weight = float(w)
bmi = weight/(height*height)
if bmi < 18.5:
    print('低于18.5：过轻')
elif bmi >= 18.5 and bmi < 25:
    print('18.5-25：正常')
elif bmi >= 25 and bmi < 28:
    print('25-28：过重')
elif bmi >= 28 and bmi < 32:
    print('28-32：肥胖')
elif bmi >= 32:
    print('高于32：严重肥胖')

print('bmi=',bmi)
    
    
