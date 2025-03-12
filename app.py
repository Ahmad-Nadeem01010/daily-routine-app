import streamlit as st
import random
import json
import os

# File to store past routines
ROUTINE_FILE = "routine_history.json"

# Load past routines
def load_past_routines():
    if os.path.exists(ROUTINE_FILE):
        with open(ROUTINE_FILE, "r") as file:
            return json.load(file)
    return []

# Save generated routines
def save_routine(routine):
    past_routines = load_past_routines()
    past_routines.append(routine)
    with open(ROUTINE_FILE, "w") as file:
        json.dump(past_routines, file, indent=4)

# Adjust routine based on feedback
def adapt_routine(routine, feedback, comments):
    if feedback == "Needs Improvement":
        routine.append("🔄 Adjust your routine: Try swapping an activity for something new tomorrow!")
    elif feedback == "Average":
        routine.append("✅ Keep refining: Make one small change to improve your day.")
    else:
        routine.append("🎯 Great job! Keep up the momentum!")

    if comments:
        routine.append(f"📝 User Feedback: {comments}")

    return routine

# Generate a dynamic routine
def generate_routine(wake_time, sleep_time, physical_activity, mental_activity, creative_passion):
    morning_routines = [
        "🧘‍♂️ 10-15 minutes of meditation or deep breathing exercises.",
        "☀️ Step outside for fresh air and sunlight.",
        "🏋️‍♂️ A short, energizing workout to start the day.",
        "📝 Write down three things you're grateful for."
    ]
    
    afternoon_routines = [
        "🌞 Take a walk outside to refresh your mind.",
        "📚 Read or learn something new.",
        "🎶 Listen to uplifting music or a podcast.",
        "👥 Engage in meaningful conversations."
    ]
    
    evening_routines = [
        "🛑 Wind down with a gratitude journal.",
        "🛁 Take a relaxing bath before bed.",
        "📖 Read a book to relax your mind.",
        "🧩 Do a creative or puzzle activity before sleep."
    ]
    
    routine = [
        f"🌅 {wake_time}: Wake up and hydrate with a glass of water.",
        random.choice(morning_routines),
        f"📖 Engage in {mental_activity} to stimulate your brain.",
        f"🏃‍♂️ {physical_activity} to stay active.",
        "🍎 Have a healthy breakfast with brain-boosting foods.",
        f"🎨 Spend time on {creative_passion} to enhance creativity.",
        random.choice(afternoon_routines),
        random.choice(evening_routines),
        f"🌙 {sleep_time}: Sleep early for brain recovery."
    ]

    return routine

# Streamlit UI
st.title("🧠 Daily Routine Generator")

# User inputs
wake_time = st.text_input("Enter your wake-up time (e.g., 6:30 AM):")
sleep_time = st.text_input("Enter your sleep time (e.g., 10:30 PM):")
physical_activity = st.text_input("Enter your preferred physical activity: (e.g., yoga, walking):")
mental_activity = st.text_input("Enter your preferred mental activity (e.g., puzzles, reading):")
creative_passion = st.text_input("Enter your creative passion (e.g., writing, painting):")

if st.button("Generate Routine"):
    if wake_time and sleep_time and physical_activity and mental_activity and creative_passion:
        routine = generate_routine(wake_time, sleep_time, physical_activity, mental_activity, creative_passion)
        st.subheader("Your Personalized Daily Routine:")
        for item in routine:
            st.write(item)

        # Feedback section
        st.subheader("How was your routine?")
        feedback = st.radio("Rate your experience:", ["Good", "Average", "Needs Improvement"])
        comments = st.text_area("Any suggestions for improvement?")
        
        if st.button("Submit Feedback"):
            routine = adapt_routine(routine, feedback, comments)
            save_routine(routine)
            st.success("Thank you for your feedback! Your routine has been updated.")
    else:
        st.error("Please fill in all fields before generating a routine.")

