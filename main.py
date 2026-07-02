###### standard library imports ######
import os 
import argparse
###### 3rd party imports ######
from dotenv import load_dotenv
from google import genai
from google.genai import types

###### local imports ######
from prompts import system_prompt
from call_function  import available_functions
from call_function import available_functions, call_function


def main():
    # setting up parser 
    parser = argparse.ArgumentParser(description="skynet")
    parser.add_argument("user_prompt", type=str, help="user_prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    
    # checking if verbose is true
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
    
    
    
    client = get_client()
    messages: list[types.Content] = [
    types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]

    for _ in range(20):
        try:
            result = generate_content(client, messages, args.verbose)
            if result:
                print(result)
                return
        except Exception as e:
            print(f"Error: {e}")
    print("Max iterations reached, no final response")


def get_client(): 
    # grabing api keyd
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # error handleing in case of no key
    if api_key is None:
        raise RuntimeError("no api key found please imput api key")
    return genai.Client(api_key=api_key)


def generate_content(client: genai.Client, messages: list[types.Content], verbose):
    # seting up client so we can make requests 
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt ),
        )
        
    # error handleing for meta data
    if response.usage_metadata is None:
        raise RuntimeError("usage_metadata is None, API request may have failed")
    
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    


    if response.candidates:
        messages.append(response.candidates[0].content)


    if not response.function_calls:
        return response.text
    else:
        function_responses = []
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, verbose)
            
            if not function_call_result.parts:
                raise Exception("function call result has no parts")
            
            function_response = function_call_result.parts[0].function_response
            if function_response is None:
                raise Exception("function response is None")
            
            if function_response.response is None:
                raise Exception("function response payload is None")
            
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

            function_responses.append(function_call_result.parts[0])
        messages.append(types.Content(role="tool", parts=function_responses))
        return None

if __name__ == "__main__":
    main()
