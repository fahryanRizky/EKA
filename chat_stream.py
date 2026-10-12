from prompt.prompt_engineering import kirim_pesan_stream

if __name__ == "__main__":
    history = [
        {"role": "system", "content": "kamu asisten pribadiku, jawab dengan singkat"}
    ]

    while True:
        user_input = input("\nkamu: ")
        if user_input.lower() == "exit":
            break

        history.append({"role": "user", "content": user_input})

        hasil = ""
        for potongan in kirim_pesan_stream(history, temperature= 0.7):
            print(potongan, end="", flush= True)
            hasil += potongan
        print()

        history.append({"role": "assistant", "content": hasil})