

from together import Together
from dotenv import load_dotenv
import os

# ✅ Load environment variables from .env
load_dotenv()

# ✅ Get key from env
api_key = os.getenv("TOGETHER_API_KEY")

# ✅ Set up client
client = Together(api_key=api_key)

# Read input
input_path = r"C:\Users\praveen agarwal\automated-book-creation-pipeline\output\chapter1_spun.txt"
output_path = r"C:\Users\praveen agarwal\automated-book-creation-pipeline\output\chapter1.txt"

with open(input_path, "r", encoding="utf-8") as f:
    original_text = f.read()

# Prompt
prompt = f"""
You are an AI writer. Rewrite the following book chapter creatively.
Keep the meaning, but change sentence structure, tone, and storytelling style.
Don't remove details. Output rewritten version only.

Original:
\"\"\"{original_text}\"\"\"
"""

# Generate using a free Together model (e.g. Mixtral)
response = client.chat.completions.create(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",  # Free, high quality
    messages=[
        {"role": "system", "content": "You are a professional story editor."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.8,
    max_tokens=3000
)

rewritten_text = response.choices[0].message.content

# Save output
with open(output_path, "w", encoding="utf-8") as f:
    f.write(rewritten_text)

print(f"✅ Spun chapter saved to {output_path}")
