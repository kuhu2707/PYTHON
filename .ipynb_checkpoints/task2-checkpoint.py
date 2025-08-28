#TASK 2 - USE NUMPY TO CREATE AN ARRAY OF NUMBERS AND STRINGS AND PERFROM BASIC OPERATIONS (SUM , MEAN , MEDIAN , MAX , MIN, SPLIT , APPEND , INSERT , CONCATENATE , SORT)
import numpy as np

num_array = np.array([10,50,56,34,23,11,16,27])
str_array = np.array(['car','truck','rikshaw','cycle','bus'])

#------------------FOR NUM_ARRAY-------------------
sum_num = print(np.sum(num_array))    #227

mean_num = print(np.mean(num_array))  #28.375

median_num = print(np.median(num_array))  #25.0

max_num = print(np.max(num_array))   #56

min_num = print(np.min(num_array))   #10

sort_num = print(np.sort(num_array)) #[10,11,16,23,27,34,50,56]

split_num =np.split(num_array,2)
print(split_num)    # [array([10,50,56,34]) , array([23,11,16,27])]

append_num = np.append(num_array,[7])
print(append_num)   #[10 50 56 34 23 11 16 27  7]

insert_num = np.insert(num_array,2,90)
print(insert_num)   #[10 50 90 56 34 23 11 16 27]

num2_array = np.array([23,12,45,67,34,78])
conact_num = np.concatenate((num_array,num2_array))
print(conact_num)     #[10 50 56 34 23 11 16 27 23 12 45 67 34 78]


#---------------------FOR STRING_ARRAY-----------------
str_sort = print(np.sort(str_array))   #['bus' 'car' 'cycle' 'rikshaw' 'truck']

str_append = print(np.append(str_array , ['apple','mango']))    #['car' 'truck' 'rikshaw' 'cycle' 'bus' 'apple' 'mango']

str_insert = print(np.insert(str_array,3,'kuhu'))     #['car' 'truck' 'rikshaw' 'kuhu' 'cycle' 'bus']

str2_array= (['indore','ujjain','dewas','maxi'])
conact_str = np.concatenate((str_array,str2_array))
print(conact_str)   #['car' 'truck' 'rikshaw' 'cycle' 'bus' 'indore' 'ujjain' 'dewas' 'maxi']