# dict的key必须是不可变对象
d = {'michael':95,'bob':75,'Tracy':85}
print(d['michael'])
print(d.get('michel'))
d.pop('bob')
print(d)