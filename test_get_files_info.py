###### standard library imports ######
#import os 

###### 3rd party imports ######
#import from thing i downloaded 

###### local imports ######
from functions.get_files_info import get_files_info


result1 = get_files_info("calculator", ".")
print("Result for current directory:")
print(result1)
result2 = get_files_info("calculator", "/bin")
print("Result for '/bin' directory:")
print(result2)
result3 = get_files_info("calculator", "../")
print("Result for '../' directory:")
print(result3)
result4 = get_files_info("calculator", "pkg")
print("Result for 'pkg' directory:")
print(result4)