#Python program to find the Mean,median,mode
n_num = [1, 2, 3, 4, 5]
n = len(n_num)
get_sum = sum(n_num)
mean = get_sum / n
print("Mean / Average is: " + str(mean))


n_num = [1, 2, 3, 4, 5] 
n = len(n_num) 
n_num.sort() 
  
if n % 2 == 0: 
    median1 = n_num[n//2] 
    median2 = n_num[n//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = n_num[n//2] 
print("Median is: " + str(median)) 


from collections import Counter  
n_num = [1, 2, 3, 4, 5, 5] 
n = len(n_num) 
  
data = Counter(n_num) 
get_mode = dict(data) 
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
  
if len(mode) == n: 
    get_mode = "No mode found"
else: 
    get_mode = "Mode is : " + ', '.join(map(str, mode)) 
      
print(get_mode) 


#Python program to swap cases of a given string
def swap_case_string(str1):
   result_str = ""   
   for item in str1:
       if item.isupper():
           result_str += item.lower()
       else:
           result_str += item.upper()           
   return result_str
print(swap_case_string("Python Exercises"))
print(swap_case_string("Java"))
print(swap_case_string("NumPy"))


# program to convert an integer to binary & octa decimal
dec = 344
print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")
