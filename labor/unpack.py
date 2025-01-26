first=("myname" , 12 , 12.88 , 's' , True)
a , b , c , d , e = first
print(a, "\n" ,b, "\n" , c ,"\n", d)
a,b, *c=first
print(a , "\n" , b , "\n" , c)
a , b , *c , d = first
print(a , "\n" , b , "\n" , c , "\n" , d)