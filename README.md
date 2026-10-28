
---

## 🚀 Current Progress

- [x] Environment setup (Python venv, TensorFlow, OpenCV, MediaPipe)
- [x] Dataset acquisition and exploratory data analysis (FER-2013)
- [x] Image preprocessing pipeline (resize, normalize, reshape)
- [x] Train/validation/test split
- [ ] CNN model design and training
- [ ] Model evaluation and improvement
- [ ] OpenCV real-time face detection
- [ ] MediaPipe head-pose estimation
- [ ] Suspicion-scoring logic
- [ ] Flask backend integration
- [ ] Web dashboard (HTML/CSS/JS)
- [ ] Final testing and deployment

---

## ⚙️ How to Run (Local Setup)

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

## 📊 Results

*To be added once model training and evaluation are complete (accuracy, confusion matrix, and sample predictions will be included here).*

---

## 🔒 Limitations

- The system flags **patterns**, not confirmed cheating — it is a decision-support tool, not a final verdict
- Performance depends on lighting conditions, camera quality, and webcam angle
- Trained on the FER-2013 dataset, which has known class imbalance (e.g., fewer "Disgust" samples)

---

## 🔮 Future Scope

- Multi-face tracking for group interview scenarios
- Object detection (phone/book) for stricter monitoring
- Cloud deployment for remote accessibility
- Analytics dashboard with historical suspicion logs

---

## 👩‍💻 Author

**Sanjana Sharma**
Final-year BCA (AI & Data Science), Graphic Era Hill University, Bhimtal
🔗 [GitHub](https://github.com/sanjanasharmaa09) | [LinkedIn](https://linkedin.com/in/sanjanasharma25)
