from openai import OpenAI
from ..config import setting

client = OpenAI(
  api_key=setting.OPENAI_API_KEY,  # Replace with your OpenAI API key
  base_url="https://oai.helicone.ai/v1",  # Set the API endpoint
  default_headers= {  # Optionally set default headers or set per request (see below)
    "Helicone-Auth": f"Bearer {setting.HELICONE_API_KEY}",
  }
)


def get_response(user: str, system: str, chat_history: list[dict], model:str="gpt-4o-mini") -> str:
    
    response = client.chat.completions.create(
        model=model,
        messages=
        [{"role": "system", "content": system}]+
        chat_history +
        [{"role": "user", "content": user}] 
    )
    return response.choices[0].message.content

def get_parsed_response(user: str, system: str, response_format, model:str="gpt-4o-mini", json_dump:bool=True) -> dict:
    
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