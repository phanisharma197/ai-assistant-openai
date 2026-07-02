from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()



#recevie and write messages from Gen AI model
def ask_text(prompt, previous_response_id):
    args = {
        "model" : "gpt-5.5",
        "input" : prompt
    }

    if previous_response_id is not None:
        args["previous_response_id"] = previous_response_id


    args["stream"] = True

    stream = client.responses.create(**args)
    
    return stream



