import subprocess
import time
import os
import sys

# Step 1: Launch Flask API
flask_process = subprocess.Popen([sys.executable, "app.py"])
print("✅ Flask API launched...")

# Step 2: Wait briefly to ensure Flask is ready
time.sleep(2)

# Step 3: Launch Streamlit UI
try:
    subprocess.run(["streamlit", "run", "streamlit_ui.py"])
finally:
    # Optional: Kill Flask server after Streamlit is closed
    print("🛑 Closing Flask server...")
    flask_process.terminate()
