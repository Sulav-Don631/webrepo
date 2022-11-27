username=input('Name: '.upper())
password=input('Password: '.upper())
if int(len(password))==4:
	print('Your password is incorrect'.upper())
	print('Your not the user')
else:
	print(f'Name : {username}'.upper())
	print(f'passwprd : {passwprd}'.lower())

