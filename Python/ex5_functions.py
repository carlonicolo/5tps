# 29/09/2023
# liste

lst_number: list = [7,8,3,1,9,5]
lst_misc: list = [1,2,"3",4,5,6]

#print(lst_number)
#print(lst_misc)

#for i in lst_number:
  #print(i)
  #print(i*3)
  #print(lst_number[i]) #no

for i in range(len(lst_misc)):
  #print(i)
  print(i*3)
  #print(lst_number[i])

print(type(lst_misc))

print(type(lst_misc[3]))
print(type(lst_misc[2]))

equals = "="
n_equals = "=" * 10

print(n_equals)