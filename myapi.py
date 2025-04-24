# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class Message(BaseModel):
#     message: str

# @app.post("/chat")
# def index(msg: Message):
#     userinput = msg.message.lower()

#     if "hello" in userinput:
#         reply = "Hey there! How can I be of help today?"
#     elif "what is fastapi" in userinput:
#         reply = "FastAPI is a modern, high-performance Python web framework for building APIs. It's known for its speed, ease of use, and automatic documentation generation."
#     elif "goodbye" in userinput:
#         reply = "See you tomorrow!"
#     else:
#         reply = "Sorry, I didn't quite get that. Could you rephrase?"

#     return {"reply": reply}


#GET  > Retrieve data
#PUT    > replace/ updates existing resources
#POST    > Updates/ send  resources to server
#DELETE   > Delete resources








# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import openai
# import os

# # Set your OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")

# app = FastAPI()

# class ChatRequest(BaseModel):
#     message: str

# @app.post("/chat")
# async def chat(request: ChatRequest):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",  # or "gpt-4"
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": request.message}
#             ]
#         )
#         reply = response.choices[0].message["content"]
#         return {"reply": reply}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))





from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": request.message}
            ]
        )
        reply = response['choices'][0]['message']['content']
        return {"reply": reply}
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
