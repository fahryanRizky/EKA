import asyncio
import time
from prompt.prompt_engineering import kirim_pesan_async

async def tanya_satu(prompt: str)->str:
    messages = [
        {"role": "user", "content": prompt}
    ]

    return await kirim_pesan_async(messages)

async def main():
    prompts= [
        "Apa itu Python? Jawab 1 kalimat.",
        "Apa itu JavaScript? Jawab 1 kalimat.",
        "Apa itu Rust? Jawab 1 kalimat.",
    ]

    print("==  SEQUENTIAL   ==")
    mulai = time.time()
    for p in prompts:
        hasil = await tanya_satu(p)
        print(f"- {hasil}")
    print(f"Waktu: {time.time() - mulai:.2f} detik")

    print("\n==  Paralel   ==")
    mulai = time.time()
    hasil_list = await asyncio.gather(*(tanya_satu(p)
    for p in prompts))

    for hasil in hasil_list:
        print(f"{hasil}")
    print(f"Waktu: {time.time() - mulai:.2f} detik")

if __name__ == "__main__":
    asyncio.run(main())