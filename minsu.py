제작
******************
"""
2016003736 이민수
"""



게임 코드
==================================
import random

def game():


플레이어 이름입력, 포인트초기화
-----------------------------------------
i=0
a=input("player : ")
b="computer"
a_point=0
b_point=0

print("start.")

10번 반복문 시작
------------------
while(i<10):

c는 플레이어에게서 받는 가위/바위/보
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
c = input(a,"please input gawi or bawi or bo(gawi : 1, bawi : 2, bo : 3)")
c =int(c)

d는 컴퓨터가 내는 가위/바위/보
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
d = random.randint(1, 3)
d = int(d)

게임 승리 판단부분
======================================
if(c==d):
print("draw.")

elif(c==1):

if(d==2):
print(b,"is win.")
b_point=b_point+1

elif(d==3):
print(a,"is win.")
a_point=a_point+1


elif(c==2):

if(d==1):
print(a,"is win.")
a_point=a_point+1

elif(d==3):
print(b,"is win.")
b_point=b_point+1


elif(c==3):

if(d==1):
print(b,"is win.")
b_point=b_point+1

elif(d==2):
print(a,"is win.")
a_point=a_point+1

else: print("no",a_point,b_point,c,d)

i+=1


각각의 점수 출력, 이긴사람/비긴사람 출력
===================================================
if(a_point>b_point):
print(a," win point ",a_point,", ",b," win point ",b_point," , winner is ",a)

elif(a_point<b_point):
print(a," win point ",a_point,", ",b," win point ",b_point," , winner is ",b)

elif(a_point==b_point):
print(a," win point ",a_point,", ",b," win point ",b_point," , result is draw")

실행
===============
game()
