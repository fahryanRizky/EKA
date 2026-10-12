from prompt.prompt_engineering import kirim_pesan_history

if __name__ == "__main__":
    history = [
        {"role": "system", "content": "kamu asisten yang jawab singkat, jawab dalam satu kalimat"}
    ]

    while True:
        user_input = input("kamu: ")
        if user_input.lower() == "exit":
            break

        history.append({"role": "user", "content": user_input})

        hasil = kirim_pesan_history(history, temperature= 0.7)
        print(f"AI: {hasil}")

        history.append({"role": "assistant", "content": hasil})