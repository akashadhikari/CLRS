def insertionSort(alist):
   for index in range(1,len(my_array)):

     currentvalue = my_array[index]
     position = index

     while position>0 and my_array[position-1]>currentvalue:
         my_array[position]=my_array[position-1]
         position = position-1

     my_array[position]=currentvalue

my_array = [5,2,4,6,1,3]
insertionSort(my_array)
print(my_array)
