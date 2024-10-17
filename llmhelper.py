
from openai import AzureOpenAI
import os


def call_llm_completion(system_prompt, user_prompt):
    new_email = ''
    client = AzureOpenAI(
    api_key=os.getenv('AZURE_OPENAI_API_KEY'),
    api_version=os.getenv('AZURE_OPENAI_VERSION'),
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')
    )

    completion = client.chat.completions.create(
        model=os.getenv('AZURE_DEPLOYMENTNAME'),  
        messages=[
            {
                "role": "system","content": system_prompt,
                "role": "user","content": user_prompt
            },
        ],
    )
    return completion.choices[0].message.content


def call_llm_vision(image_base64,mimetype,user_prompt):
    client = AzureOpenAI(
    api_key=os.getenv('AZURE_OPENAI_API_KEY'),
    api_version=os.getenv('AZURE_OPENAI_VERSION'),
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')
    )

    response = client.chat.completions.create(
        model=os.getenv('AZURE_DEPLOYMENTNAME'),  
        messages=[
            { "role": "system", "content": "You are a helpful assistant." },
            { "role": "user", "content": [  
                { 
                    "type": "text", 
                    "text": user_prompt
                },
                { 
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:{mimetype};base64,{image_base64}" 
                    }
                }
            ] } 
        ],
        max_tokens=2000 
    )
    return response.choices[0].message.content