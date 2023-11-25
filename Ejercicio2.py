'''
Escriba un programa en Python para construir el siguiente patrón.
*
* *
* * *
* * * *
* * * * *      5
* * * *
* * *
* *
*

'''

# [0,1,2,3,4,5> ==> 0,1,2,3,4

for fila in range(5):  #range(0,5,1)
       i = (fila+1)     # ==> 1,2,3,4,5
       print('#'*i)
 
# [5,4,3,2,1> ==> 5,4,3,2

for fila in range(5,1,-1): 
       i = (fila-1)     # ==> 4,3,2,1
       print('#'*i)




