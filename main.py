###### standard library imports ######
import os 
import argparse
###### 3rd party imports ######
from dotenv import load_dotenv
from google import genai
from google.genai import types

###### local imports ######
# from module import something



def main():
    # setting up parser 
    parser = argparse.ArgumentParser(description="skynet")
    parser.add_argument("user_prompt", type=str, help="user_prompt")
    args = parser.parse_args()
    
    client = get_client()
    messages: list[types.Content] = [
    types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]

    generate_content(client, messages)


def get_client(): 
    # grabing api key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # error handleing in case of no key
    if api_key is None:
        raise RuntimeError("no api key found please imput api key")
    return genai.Client(api_key=api_key)


def generate_content(client: genai.Client, messages: list[types.Content]):
    # seting up client so we can make requests 
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=messages)
    # error handleing for meta data
    if response.usage_metadata is None:
        raise RuntimeError("usage_metadata is None, API request may have failed")
    
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print(response.text)



if __name__ == "__main__":
    main()
