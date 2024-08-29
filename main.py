from fastapi import FastAPI
from pydantic import BaseModel
import string

# Define the data model for the request body
class QueryRequest(BaseModel):
    query: str

app = FastAPI()

@app.get("/")
async def read_root():
    return{"Message":"Welcome to my chatbot"}
@app.post("/api/v1/query")
async def get_response(request: QueryRequest):
    # Extract the query from the request body
    user_query = request.query

    # Remove punctuation from the query
    user_query = ''.join(char for char in user_query if char not in string.punctuation)
    
    reponse_dict = {
        'hi': 'Hello! How can I help you today?',
        'who are you': 'I am ChatGPT, an AI language model created by OpenAI.',
        'what is your name': 'I am called ChatGPT.',
        'how are you': 'I am just a program, but I am functioning perfectly. How can I assist you?',
        'what can you do': 'I can answer questions, help with tasks, and provide information on a wide range of topics.',
        'tell me a joke': 'Why don’t scientists trust atoms? Because they make up everything!',
        'what is the weather like': 'I don’t have real-time data access, but you can check a weather website or app for current conditions.',
        'what is the capital of France': 'The capital of France is Paris.',
        'how old are you': 'I don’t have an age, but I was created by OpenAI.',
        'what is the meaning of life': 'The meaning of life is a philosophical question that varies by individual and belief system. Some say 42!'
    }

    print("User query: " + user_query)

    # Define a response based on the query
    if user_query.lower() in reponse_dict.keys():
        return {"response": f"{reponse_dict[user_query.lower()]}"}
    else:
        return {"response": "I don't understand your query."}

if __name__ == "_main_":
    import multiprocessing
    import subprocess
    import uvicorn
    
    workers = multiprocessing.cpu_count() * 2 + 1
    
    # uvicorn_cmd = [
    #     "uvicorn",
    #     "main:app",
    #     "--host=localhost",
    #     # "--port=8080",
    #     # f"--workers={workers}",
    #     "--reload"
    # ]
    
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True, workers=workers)
    #subprocess.run(uvicorn_cmd)