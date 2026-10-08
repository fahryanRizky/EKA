from config import client, MODEL

def tanya(prompt: str, system: str= None, temperature: float = 0.0) -> str:
    messages = []
    if system:
        messages.append({
            "role": "system",
            "content": system
            })
        
    messages.append({
            "role": "user", 
            "content": prompt
        })
        
    response = client.chat.completions.create(
        model= MODEL,
        messages = messages
    )

    return response.choices[0].message.content