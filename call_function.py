###### standard library imports ######
#import os 

###### 3rd party imports ######
from google.genai import types

###### local imports ######
from functions.get_files_info import schema_get_files_info



available_functions = types.Tool(
    function_declarations=[schema_get_files_info],
)