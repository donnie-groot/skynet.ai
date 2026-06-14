###### standard library imports ######
#import os 

###### 3rd party imports ######

###### local imports ######
from functions.get_file_content import get_file_content


def test() -> None:
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")

    # add the other test cases below here
    result1 =get_file_content("calculator", "main.py")
    print(result1)
    result2 = get_file_content("calculator", "pkg/calculator.py")
    print(result2)
    result3 =get_file_content("calculator", "/bin/cat")
    print(result3)
    result4 = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result4)
if __name__ == "__main__":
    test()