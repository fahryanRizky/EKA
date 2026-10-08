from prompt.prompt_engineering import tanya

list_soal = [
    "Sebuah toko punya 45 apel. 1/3 apel busuk dan dibuang. Sisanya dijual dengan harga Rp2.000 per apel. Berapa total uang yang didapat?",
    "Jika 3 pekerja membangun tembok dalam 6 hari, berapa hari yang dibutuhkan 9 pekerja untuk membangun tembok yang sama?",
    "Andi lebih tinggi dari Budi. Budi lebih tinggi dari Cici. Siapa yang paling pendek?"
]

if __name__ == "__main__":
    print("=== SKENARIO A: Tanpa COT ===")
    for soal in list_soal:
        prompt = f"Jawab soal berikut. Jawab singkat dengan angka/hasil akhir saja.\n\nSoal: {soal}\nJawaban:"
        hasil = tanya(prompt, temperature=0.0)
        print(f"Teks: {soal} jawaban: {hasil}")

    print("\n=== SKENARIO B: Dengan COT ===")
    for soal in list_soal:
        prompt = f"Jawab soal berikut. Pikirkan langkah demi langkah sebelum memberikan jawaban akhir.\n\nSoal: {soal}\nJawaban:"
        hasil = tanya(prompt, temperature=0.0)
        print(f"Teks: '{soal}' jawaban: {hasil}")