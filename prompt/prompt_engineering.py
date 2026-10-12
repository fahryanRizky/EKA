from config import client, MODEL, async_client

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

def kirim_pesan_history(messages: list, temperature: float= 0.7)->str:
    response = client.chat.completions.create(
        model= MODEL,
        messages= messages,
        temperature= temperature
    )

    return response.choices[0].message.content

def kirim_pesan_stream(message: list, temperature: float= 0.7):
    stream = client.chat.completions.create(
        model= MODEL,
        messages= message,
        temperature= temperature,
        stream= True
    )

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta

async def kirim_pesan_async(message: list, temperature: float= 0.7)-> str:
    response = await async_client.chat.completions.create(
        model= MODEL,
        messages= message,
        temperature= temperature,
    )

    return response.choices[0].message.content