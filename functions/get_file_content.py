###### standard library imports ######
import os 

###### 3rd party imports ######
from google.genai import types

###### local imports ######
from config import MAX_CHAR

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            
        if not os.path.isfile(target_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_dir, "r") as f:
            content = f.read(MAX_CHAR)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHAR} characters]'
            return content
    except Exception as e:
        return f"Error: {e}"
    


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the contents of a file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)