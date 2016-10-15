import random

def game():
	i=0
	a=input("플레이어 : ")
	b="컴퓨터"
	a_point=0
	b_point=0
	print("가위바위보를 시작합니다.")
	while(i<10):
		c = input(a+"는 가위, 바위, 보중 하나를 입력하세요.(가위 : 1, 바위 : 2, 보 : 3)")
		c =int(c)
		d = random.randint(1, 3)
		d = int(d)
		if(c==d):
			print("비겼습니다.")
		elif(c==1):
			if(d==2):
				print(b,"가 승리하였습니다.")
				b_point=b_point+1
			elif(d==3):
				print(a,"가 승리하였습니다.")
				a_point=a_point+1
		elif(c==2):
			if(d==1):
				print(a,"가 승리하였습니다.")
				a_point=a_point+1
			elif(d==3):
				print(b,"가 승리하였습니다.")
				b_point=b_point+1
		elif(c==3):
			if(d==1):
				print(b,"가 승리하였습니다.")
				b_point=b_point+1
			elif(d==2):
				print(a,"가 승리하였습니다.")
				a_point=a_point+1
		else: print("no",a_point,b_point,c,d)
		i+=1
	if(a_point>b_point):
		print(a,"의 승점은 ",a_point,"이고, ",b,"의 승점은 ",b_point,"으로 승리자는 ",a,"입니다.")
	elif(a_point<b_point):
		print(a,"의 승점은 ",a_point,"이고, ",b,"의 승점은 ",b_point,"으로 승리자는 ",b,"입니다.")
	elif(a_point==b_point):
		print(a,"의 승점은 ",a_point,"이고, ",b,"의 승점은 ",b_point,"으로 무승부입니다.")

game()
