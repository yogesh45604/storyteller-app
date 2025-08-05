from fastapi import FastAPI
from models import StoryRequest, StoryResponse
from deepinfra_api import generate_story, generate_image
from utils import create_prompt, parse_story

# app = FastAPI()

# @app.post("/generate", response_model=StoryResponse)
# async def generate_story_endpoint(req: StoryRequest):
#     prompt = create_prompt(req.genre, req.characters, req.sections)
#     response =  generate_story(prompt)
#     raw = response["choices"][0]["message"]["content"]
#     summary, paragraphs = parse_story(raw)
#
#     # Optional: Generate images for each paragraph
#     # images = []
#     # for p in paragraphs:
#     #     img_url =  generate_image(p[:200])  # truncate prompt to 200 chars
#     #     images.append(img_url)
#     #
#     # return StoryResponse(summary=summary, paragraphs=paragraphs, images=images)
#     return StoryResponse(summary=summary, paragraphs=paragraphs, images=None)


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.concurrency import run_in_threadpool
from models import StoryRequest, StoryResponse
from deepinfra_api import generate_story, generate_image
from utils import create_prompt, parse_story
import os
# Create static directory at startup
os.makedirs("static", exist_ok=True)
app = FastAPI()

# Mount static image folder
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/generate", response_model=StoryResponse)
async def generate_story_endpoint(req: StoryRequest):
    prompt = create_prompt(req.genre, req.characters, req.sections)
    response = generate_story(prompt)  # assuming this is already sync
    raw = response["choices"][0]["message"]["content"]
    summary, paragraphs = parse_story(raw)

    # Generate images asynchronously using run_in_threadpool
    images = []
    for p in paragraphs:
        img_url = await run_in_threadpool(generate_image, p[:200])  # Truncate prompt if needed
        images.append(img_url)

    return StoryResponse(summary=summary, paragraphs=paragraphs, images=images)


import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000, log_level="debug")