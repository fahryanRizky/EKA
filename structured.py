import json
from prompt.prompt_engineering import tanya
from config.json import ekstrak_json

deskripsi_list = [
    "Budi, 25 tahun, 3 tahun pengalaman sebagai data scientist. Skill: Python, SQL, TensorFlow. Melamar posisi AI Engineer.",
    "Sari, 22 tahun, fresh graduate. Skill: JavaScript, React. Melamar posisi Frontend Developer.",
    "Andi, 30 tahun, 7 tahun pengalaman. Skill: Python, Go, Kubernetes, Docker. Melamar posisi Backend Engineer.",
]

if __name__ == "__main__":
    print("== skenario A: tanpa structured output ==")
    for deskripsi in deskripsi_list:
        prompt = f"Ekstrak informasi dari deskripsi berikut: nama, usia, skill, pengalaman, posisi. Deskripsi: {deskripsi}"
        hasil = tanya(prompt, temperature=0.0)
        print(f"teks: {deskripsi}\nhasil -> {hasil}\n")

    print("\n== skenario B: dengan structured output (JSON) ==")
    for deskripsi in deskripsi_list:
        prompt = f'''Ekstrak informasi dari deskripsi berikut ke dalam JSON.

Format JSON:
{{
  "nama": "string",
  "usia": integer,
  "skill": ["string"],
  "pengalaman_tahun": integer,
  "posisi_dilamar": "string"
}}

Deskripsi: {deskripsi}

JSON:'''
        hasil = tanya(prompt, temperature=0.0)
        try:
            data = ekstrak_json(hasil)
            print("valid json:", data)
        except json.JSONDecodeError as e:
            print("bukan json:", e)
            print("Raw output:", hasil)