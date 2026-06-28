from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

print("API Key loaded:", os.getenv("OPENAI_API_KEY") is not None)

client = OpenAI()

response = client.responses.create(
    model="gpt-5.5",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type" : "input_text",
                    "text" : "anlayze below imaze and give me a detailed description of it",

                },
                {
                    "type" : "input_image",
                    "image_url" : "https://media.formula1.com/image/upload/t_16by9Centre/c_lfill,w_3392/q_auto/v1740000001/fom-website/2025/F1%20movie/f1_movie_poster16x9%20(1).webp"
                }
            ]
        }
    ]
)

print(response.output_text)