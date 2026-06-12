###### standard library imports ######
import os 
###### 3rd party imports ######
from dotenv import load_dotenv
from google import genai

###### local imports ######
# from module import something

# grabing api key
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# error handleing in case of no key

if api_key == None:
    raise RuntimeError("no api key found please imput api key")

# seting up client so we can make requests 
client = genai.Client(api_key=api_key)

# getting our output
response = client.models.generate_content(model="gemini-2.5-flash", contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")


if response.usage_metadata is None:
    raise RuntimeError("usage_metadata is None, API request may have failed")

print("Prompt tokens:", response.usage_metadata.prompt_token_count)
print("Response tokens:", response.usage_metadata.candidates_token_count)
print(response.text)



def main():
    # grabing api key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # error handleing in case of no key

    if api_key == None:
        raise RuntimeError("no api key found please imput api key")

    # seting up client so we can make requests 
    client = genai.Client(api_key=api_key)

    # getting our output
    response = client.models.generate_content(model="gemini-2.5-flash", contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")


    if response.usage_metadata is None:
        raise RuntimeError("usage_metadata is None, API request may have failed")

    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print(response.text)


if __name__ == "__main__":
    main()
