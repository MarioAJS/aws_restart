'''
Reto Python: Busqueda de numeros primos
Mario Jimenez Saucedo
Metodo: Criba de Sundaram
Fundamento del metodo:
a) Ningun numero primo impar se puede expresar como el producto de dos factores impares
b) Todo numero primo impar se puede expresar como la diferencia de dos numeros al cuadrado,
esta representacion es unica.
Referencias:
https://www.baeldung.com/cs/prime-number-algorithms
https://artofproblemsolving.com/wiki/index.php/Sieve_of_Sundaram 
'''

from math import sqrt, floor

def numeros_primos(n):
   # lista vacia donde se obtendran los numeros primos menores a n
   P=[]
   k = floor((n - 1)/2)
   # lista de tamanio k+1 con valores booleanos = TRUE
   A = [True]*(k+1)

   # utilizar la criba para filtrar los numeros de la forma i+j+2ij donde 1<=i<=j
   for num in range(1,int(sqrt(k))+1):
      i = num
      j = i
      while ((i+j+(2*i*j)) <= k):
         A[(i+j+(2*i*j))] = False
         j += 1

   idx=0
   for a in A:
      if a == True:
         P.append((2*idx)+1)
      idx+=1

   #Agregar a la lista el 2 ya que este es el unico numero primo que es par y el metodo utilizado
   # devuelve los numeros primos impares.   
   P.insert(1,2)
   return P
   
try:
   textfile = "report.txt"
   n = int(input('Ingrese un numero natural "n" para determinar los numeros primos menores a n: '))
   assert n > 0
   primos = numeros_primos(n)

   with open(textfile, "w+") as outfile:
      outfile.write('\n'.join(str(i) for i in primos))

   print(f"Los numeros primos menores a {n} son:")
   print(primos)
   print(f"El resultado ha sido guardado en {textfile}")

except AssertionError:
   print("El numero ingresado no es un numero natural")
except ValueError:
   print("El numero ingresado no es un numero natural")