
from together import Together
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

api_key = os.getenv("TOGETHER_API_KEY")

client = Together(api_key=api_key)

# ✅ File paths
input_path = r"C:\Users\praveen agarwal\automated-book-creation-pipeline\output\chapter1_spun.txt"
output_path = r"C:\Users\praveen agarwal\automated-book-creation-pipeline\output\chapter1_review.txt"

# ✅ Read AI-Written Chapter
with open(input_path, "r", encoding="utf-8") as f:
    spun_text = f.read()

# ✅ Prompt for Review Agent
prompt = f"""
You are an expert reviewer for creative book writing.
Your job is to:
1. Read the rewritten chapter.
2. Give constructive feedback (3–5 bullet points).
3. Provide a review score between 1–10.
Be specific in your review — focus on writing style, clarity, creativity, coherence.

Chapter to review:
\"\"\"{spun_text}\"\"\"
"""

# ✅ Send to Together LLM (Mixtral works well)
response = client.chat.completions.create(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    messages=[
        {"role": "system", "content": "You are a professional story reviewer."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=1500
)

# ✅ Save result
review = response.choices[0].message.content
with open(output_path, "w", encoding="utf-8") as f:
    f.write(review)

print(f"✅ Review complete. Saved to {output_path}")
