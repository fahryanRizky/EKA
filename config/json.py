import json

def ekstrak_json(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        # Buang ```json di awal dan ``` di akhir
        parts = text.split("```")
        if len(parts) >= 2:
            text = parts[1]
            if text.startswith("json"):
                text = text[4:]
            text = text.strip()
    return json.loads(text)