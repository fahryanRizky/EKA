from prompt.prompt_engineering import tanya

teks_list = [
    "makanannya enak banget",
    "pengiriman cepat, tapi barang rusak",
    "lumayanlah",
    "saya sangat suka dengan pelayanannya",
    "biasa aj sih",
]

if __name__ == "__main__":
    print("=== SKENARIO A: ZERO-SHOT ===")
    for teks in teks_list:
        prompt = f'Klasifikasikan sentimen teks berikut menjadi Positif/Negatif/Netral.\n\nTeks: "{teks}"'
        hasil = tanya(prompt, temperature=0.0)
        print(f"Teks: {teks} Sentimen: {hasil}")

    print("\n=== SKENARIO B: FEW-SHOT ===")
    for teks in teks_list:
        prompt = f"""Klasifikasikan sentimen teks berikut menjadi Positif/Negatif/Netral.

        Contoh:
        Teks: "Pelayanannya lambat" → Negatif
        Teks: "Biasa aja" → Netral
        Teks: "Produknya luar biasa!" → Positif
        Teks: "Sangat mengecewakan" → Negatif

        Sekarang klasifikasikan:
        Teks: "{teks}"
        """
        hasil = tanya(prompt, temperature=0.0)
        print(f"Teks: '{teks}' Sentimen: {hasil}")