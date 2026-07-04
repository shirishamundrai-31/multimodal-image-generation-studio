import os
import requests
from urllib.parse import quote

def generate_image(prompt):
    try:
        os.makedirs("generated_images", exist_ok=True)

        safe_prompt = quote(prompt)

        image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?width=1024&height=1024&seed=42"

        response = requests.get(image_url)

        if response.status_code == 200:

            filename = "generated_images/generated_image.png"

            with open(filename, "wb") as f:
                f.write(response.content)

            return filename

        return None

    except Exception as e:
        print(e)
        return None