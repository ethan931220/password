# password = 'a123456'
time = 3
password = input('請輸入密碼')
while time>0:
    if password == 'a123456':
	    print('登入成功')
	    break
	else:
		time = time-1
		print('還剩',time'次')
print('登入失敗')




