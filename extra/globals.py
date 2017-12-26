import datetime
from django.http import HttpResponse



def separador_de_miles(numero,gs=False):
   numero=str(numero)
   vector=numero.split(".")
   s=vector[0]
   for i in range(len(vector[0]),0,-3):
      if i == 1 and s[0] == "-":
           s=s[:i]+s[i:]
      else:
        s=s[:i]+"."+s[i:]
   a=s[:len(s)-1]
   if gs:
       return a
   if len(vector) == 2 and vector[1] !="00":
       
       if len(vector[1]) > 2:
           dato=vector[1][0:2]
       else:
           dato=vector[1]
       a+= ","+dato
  
   return a
