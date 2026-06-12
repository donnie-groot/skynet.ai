###### standard library imports ######
import os 
import argparse
###### 3rd party imports ######
from dotenv import load_dotenv
from google import genai

###### local imports ######
# from module import something


def main():
    # setting up parser 
    parser = argparse.ArgumentParser(description="skynet")
    parser.add_argument("user_prompt", type=str, help="user_prompt")
    args = parser.parse_args()
    # grabing api key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # error handleing in case of no key

    if api_key == None:
        raise RuntimeError("no api key found please imput api key")

    # seting up client so we can make requests 
    client = genai.Client(api_key=api_key)

    # getting our output
    response = client.models.generate_content(model="gemini-2.5-flash", contents=args.user_prompt)


    if response.usage_metadata is None:
        raise RuntimeError("usage_metadata is None, API request may have failed")


    parser = argparse.ArgumentParser(description="skynet")
    parser.add_argument("user_promt", type=str, help="user prompt")
    args = parser.parse_args

    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print(response.text)


if __name__ == "__main__":
    main()
