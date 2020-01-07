import os
import time 
from time import strftime

#a,b,c,d,e,g,h,j,m,n,p,r,t,u,w,x,y,z
a = time.strftime("%a") # Mon - (Day)
b = time.strftime("%b") # Jan - (Month)
c = time.strftime("%c") # Mon Jan  6 10:33:06 2020 - (Day Month Date Time Year)
d = time.strftime("%d") # 06
e = time.strftime("%e") # 6

g = time.strftime("%g") # 20
h = time.strftime("%h") # Jan

j = time.strftime("%j") # 006

m = time.strftime("%m") # 01
n = time.strftime("%n") # \n - (types \n)

p = time.strftime("%p") # AM

r = time.strftime("%r") # 10:33:06 AM

t = time.strftime("%t") # \t - (types \t)
u = time.strftime("%u") # 1

w = time.strftime("%w") # 1
x = time.strftime("%x") # 01/06/20
y = time.strftime("%y") # 20
z  = time.strftime("%z") # +0530 (GMT)

#A,B,C,D,F,G,H,I,M,R,S,T,U,V,W,X,Y,Z
A = time.strftime("%A") # Monday
B = time.strftime("%B") # January
C = time.strftime("%C") # 20
D = time.strftime("%D") # 01/06/20

F = time.strftime("%F") # 2020-01-06
G = time.strftime("%G") # 2020
H = time.strftime("%H") # 10
I = time.strftime("%I") # 10

M = time.strftime("%M") # 33

R = time.strftime("%R") # 10:33
S = time.strftime("%S") # 06
T = time.strftime("%T") # 10:33:06
U = time.strftime("%U") # 01
V = time.strftime("%V") # 02
W = time.strftime("%W") # 01
X = time.strftime("%X") # 10:33:06
Y = time.strftime("%Y") # 2020
Z = time.strftime("%Z") # India Standard Time

print (a,b,c,d,e,g,h,j,m,n,p,r,t,u,w,x,y,z)
print(A,B,C,D,F,G,H,I,M,R,S,T,U,V,W,X,Y,Z)
print("-------------------------------------------------------")
print("Today's date:- " + d + '/' + m + '/' + Y)
print("The time is :- " + r)
print("Today the day/month is:- " + A+' / ' + B)
