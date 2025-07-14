import streamlit as st
import os

# Input path for reviewed chapter
input_path = r"C:\Users\praveen agarwal\automated-book-creation-pipeline\output\chapter1_review.txt"

# Output path for human-edited version
output_path = r"C:\Users\praveen agarwal\automated-book-creation-pipeline\output\chapter1_human_edited.txt"

st.title("📘 Human Feedback Editor")

# Load the reviewed chapter
if os.path.exists(input_path):
    with open(input_path, "r", encoding="utf-8") as f:
        reviewed_text = f.read()
else:
    st.error("❌ Reviewed chapter not found!")
    st.stop()

# Show original reviewed text
st.subheader("✍️ AI-Reviewed Chapter")
st.text_area("Original (Read Only)", reviewed_text, height=300, disabled=True)

# Editable box for human feedback
st.subheader("🧠 Your Edits")
human_input = st.text_area("Edit the content here", reviewed_text, height=300)

# Rating (Optional)
st.subheader("⭐ Rate the AI Output (1–5)")
rating = st.slider("Your rating", 1, 5, 3)

# Save edited version
if st.button("💾 Save My Edited Version"):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(human_input)

    # Log rating
    with open("../output/ratings_log.txt", "a", encoding="utf-8") as log:
        log.write(f"chapter1_review.txt -> Edited | Rating: {rating}\n")

    st.success("✅ Your edited version was saved successfully!")
