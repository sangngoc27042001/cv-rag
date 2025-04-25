from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_response(user: str, system: str, chat_history: list[dict], model:str="gpt-4o-mini") -> str:
    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        messages=
        [{"role": "system", "content": system}]+
        chat_history +
        [{"role": "user", "content": user}] 
    )
    return response.choices[0].message.content

def get_parsed_response(user: str, system: str, response_format, model:str="gpt-4o-mini", json_dump:bool=True) -> dict:
    
    client = OpenAI()
    response = client.beta.chat.completions.parse(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ],
        response_format=response_format
    )
    if json_dump:
        return response.choices[0].message.parsed.model_dump()
    return response.choices[0].message.parsed