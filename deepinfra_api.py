# import httpx
#
# from dotenv import load_dotenv
# import os
#
# load_dotenv()  # Loads variables from .env into environment
#
# HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
#
# async def generate_story(prompt: str) -> str:
#     # url = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
#     # url = "https://api-inference.huggingface.co/models/bigscience/mt0-large"
#     url ="https://router.huggingface.co/v1/chat/completions"
#     payload = {"inputs": prompt}
#     headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
#
#     async with httpx.AsyncClient() as client:
#         resp = await client.post(url, json=payload, headers=headers)
#         resp.raise_for_status()
#         data = resp.json()
#         return data[0]["generated_text"] if isinstance(data, list) and "generated_text" in data[0] else str(data)
#
# async def generate_image(prompt: str) -> str:
#     url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
#     payload = {"inputs": prompt}
#     async with httpx.AsyncClient() as client:
#         resp = await client.post(url, json=payload)
#         resp.raise_for_status()
#         # Hugging Face returns image bytes; you need to save and serve or use a placeholder
#         # For demo, return a placeholder image
#         return "https://via.placeholder.com/300x200.png?text=Image"

import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into environment

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

def generate_story(prompt: str) -> dict:
    url = "https://router.huggingface.co/v1/chat/completions"
    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "zai-org/GLM-4.5:novita"
    }
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    resp = requests.post(url, json=payload, headers=headers)
    resp.raise_for_status()
    return resp.json()

# def generate_image(prompt: str) -> str:
#     url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
#     payload = {"inputs": prompt}
#     headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
#     resp = requests.post(url, json=payload, headers=headers)
#     resp.raise_for_status()
#     # For demo, return a placeholder image
#     return "https://via.placeholder.com/300x200.png?text=Image"
import uuid
import os
from huggingface_hub import InferenceClient
import uuid

def generate_image(prompt: str) -> str:
    client = InferenceClient(
        provider="replicate",
        api_key=os.environ["HUGGINGFACE_API_KEY"],
    )
    image = client.text_to_image(
        prompt,
        model="Qwen/Qwen-Image",
    )
    os.makedirs("static", exist_ok=True)
    filename = f"{uuid.uuid4()}.png"
    filepath = os.path.join("static", filename)
    image.save(filepath)
    return f"/static/{filename}"
