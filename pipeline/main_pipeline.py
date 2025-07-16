
# pipeline/main_pipeline.py

import os

# Agent Paths
scraped_path = r"C:\Users\praveen agarwal\automated-book-creation-pipeline\output\chapter1.txt"
spun_path = r"C:\Users\praveen agarwal\automated-book-creation-pipeline\output\chapter1_spun.txt"
review_path = r"C:\Users\praveen agarwal\automated-book-creation-pipeline\output\chapter1_review.txt"
human_edited_path = r"C:\Users\praveen agarwal\automated-book-creation-pipeline\output\chapter1_human_edited.txt"
ratings_log_path = r"C:\Users\praveen agarwal\automated-book-creation-pipeline\output\ratings_log.txt"

# 1️⃣ Scraper Agent (assumed already ran manually via scraper.py)
print(f"✅ Scraper Agent Output Exists: {scraped_path}")

# 2️⃣ Writer Agent
from ai_writer.ai_writer import generate_spun_text
if not os.path.exists(spun_path):
    generate_spun_text(scraped_path, spun_path)
    print(f"✅ Writer Agent saved output to {spun_path}")
else:
    print(f"🟡 Writer output already exists at {spun_path}")

# 3️⃣ Reviewer Agent
from ai_reviewer.ai_reviewer import review_chapter
if not os.path.exists(review_path):
    review_chapter(spun_path, review_path)
    print(f"✅ Reviewer Agent saved output to {review_path}")
else:
    print(f"🟡 Review already exists at {review_path}")

# 4️⃣ Human Feedback
if os.path.exists(human_edited_path):
    print(f"✅ Human Feedback exists: {human_edited_path}")
else:
    print(f"🟡 Waiting for human to edit via human_feedback_app.py and save at: {human_edited_path}")

# 5️⃣ Feedback Logging
if os.path.exists(ratings_log_path):
    print(f"✅ Ratings log found at: {ratings_log_path}")
else:
    print(f"🟡 No rating submitted yet. Submit via human_feedback_app.py GUI")

print("✅ Phase 6 pipeline run complete.")
