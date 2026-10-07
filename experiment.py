import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROK_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

MODEL = "openai/gpt-oss-20b"

def tanya(prompt: str, temperature: float = 0.7, top_p: float = 0.95 )-> str:
    response = client.chat.completions.create(
        model= MODEL,
        messages=[
            {"role": "user","content": prompt}
        ],
        temperature = temperature,
        top_p = top_p,
    )
    return response.choices[0].message.content

def hitung_token(teks: str) -> int:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": teks}],
        max_tokens=1,
    )
    return response.usage.prompt_tokens

if __name__ == "__main__":
    prompt = ("sebutkan 3 nama startup ai untuk petani indonesia, singkat saja.")
    print(prompt)

    print("==temperature 0.00==")
    for i in range(3):
        print(f"{tanya(prompt, temperature=0.0)}")
        print()

    print("==temperature 1.5==")
    for i in range(3):
        print(f"{tanya(prompt, temperature=1.5)}")
        print()

    print("==top_p 0.1")
    for i in range(3):
        print(f"{tanya(prompt, temperature=0.7, top_p=0.1)}")
        print()

    print("==top_p 1.0")
    for i in range(3):
        print(f"{tanya(prompt, temperature=0.7, top_p=1.0)}")
        print()

    print("==hitung token==")
    teks_a = "Halo"
    teks_b = "Halo, apa kabar kamu hari ini? Semoga sehat selalu."
    
    token_a = hitung_token(teks_a)
    token_b = hitung_token(teks_b)
    
    print(f"Teks A: '{teks_a}'")
    print(f"  Karakter: {len(teks_a)}, Token: {token_a}")
    print(f"Teks B: '{teks_b}'")
    print(f"  Karakter: {len(teks_b)}, Token: {token_b}")
    print(f"Selisih karakter: {len(teks_b) - len(teks_a)}")
    print(f"Selisih token: {token_b - token_a}")
    print(f"Rasio karakter/token (dari selisih): {(len(teks_b) - len(teks_a)) / (token_b - token_a):.2f}")
