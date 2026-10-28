# AI-Based Interview Proctoring System

An AI-powered system that monitors candidates during online interviews and flags suspicious activity in real time — combining a CNN-based facial expression classifier, OpenCV face detection, and MediaPipe head-pose estimation, served through a Flask backend with a live HTML/CSS/JavaScript dashboard.


##  Overview

Traditional facial expression recognition tells you *what* expression a face shows. This project goes further — it uses facial signals as one input among several (face presence, face count, head orientation) to flag potentially suspicious behavior during a live interview, such as:

- No face detected in frame
- Multiple faces detected
- Candidate looking away from the screen for extended periods

The goal is **AI-assisted proctoring**, not automated accusation — the system flags patterns for a human reviewer, it does not make a final judgment.

##  Objectives

- Build and train a CNN for facial expression classification using the FER-2013 dataset
- Implement real-time face detection using OpenCV
- Implement head-pose estimation using MediaPipe Face Mesh
- Combine these signals into a rule-based suspicion-scoring system
- Serve predictions in real time via a Flask backend
- Display live webcam feed and suspicion alerts on a responsive web dashboard

##  System Architecture


## 🚀 Current Progress

-  Environment setup (Python venv, TensorFlow, OpenCV, MediaPipe)
-  Dataset acquisition and exploratory data analysis (FER-2013)
-  Image preprocessing pipeline (resize, normalize, reshape)
-  Train/validation/test split
-  CNN model design and training
-  Model evaluation and improvement
-  OpenCV real-time face detection
- MediaPipe head-pose estimation
- Suspicion-scoring logic
- Flask backend integration
- Web dashboard (HTML/CSS/JS)
- Final testing and deployment

---

##  How to Run (Local Setup)

```bash
# 1. Clone the repository
git clone https://github.com/sanjanasharmaa09/interview-proctoring-ai.git
cd interview-proctoring-ai

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the preprocessing pipeline
python src/preprocessing.py

# 5. (Once available) Run the Flask app
python src/app.py
```

---

##  Results

*To be added once model training and evaluation are complete (accuracy, confusion matrix, and sample predictions will be included here).*

---

## Limitations

- The system flags **patterns**, not confirmed cheating — it is a decision-support tool, not a final verdict
- Performance depends on lighting conditions, camera quality, and webcam angle
- Trained on the FER-2013 dataset, which has known class imbalance (e.g., fewer "Disgust" samples)

---

##  Future Scope

- Multi-face tracking for group interview scenarios
- Object detection (phone/book) for stricter monitoring
- Cloud deployment for remote accessibility
- Analytics dashboard with historical suspicion logs

---

##  Author

**Sanjana Sharma**
Final-year BCA (AI & Data Science), Graphic Era Hill University, Bhimtal
🔗 [GitHub](https://github.com/sanjanasharmaa09) 
