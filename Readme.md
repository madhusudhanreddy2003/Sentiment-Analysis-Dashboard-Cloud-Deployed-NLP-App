## 🧠 Sentiment Analysis Dashboard – Cloud-Deployed NLP App

---

### Real-time Sentiment Analysis using HuggingFace Transformers, Flask & Google Cloud Run

This project is a fully containerized, production-ready sentiment analysis web application built with Flask, powered by a HuggingFace Transformer model, and deployed on **Google Cloud Run using Docker + Cloud Build.**
<br>
It performs real-time sentiment classification (Positive / Negative) and is optimized to run in a CPU-only cloud environment with lightweight models and fast inference.

---

## APP URL
[https://sentiment-app-672537538984.asia-south1.run.app](https://sentiment-app-672537538984.asia-south1.run.app/)

---

## 🌟 Key Features
#### 🔍 Real-Time Sentiment Analysis
- Uses a light-weight HuggingFace transformer model
- Predicts Positive / Negative sentiment
- Provides confidence scoring

#### 🌐 Cloud-Native Deployment
- Fully deployed on Google Cloud Run
- Auto-scaling, serverless, highly available
- Cold-start optimized

#### 🐳 Dockerized Application
- Dockerfile optimized for small image size
- CPU-compatible Torch + Transformers

#### 🎨 Modern UI Dashboard
- Clean, responsive interface
- Gradient background
- User-friendly interaction

---

## 🏗️ Tech Stack

| Component            | Technology                            |
| -------------------- | ------------------------------------- |
| **Frontend**         | HTML5, CSS3 (Gradient UI), Bootstrap  |
| **Backend**          | Python Flask                          |
| **ML Model**         | HuggingFace Transformers (distilbert) |
| **Containerization** | Docker                                |
| **Cloud Deployment** | Google Cloud Run                      |
| **Build System**     | Google Cloud Build                    |
| **Runtime**          | Gunicorn                              |

---

## 📁 Project Structure
```bash
sentiment-dashboard/
│── app.py
│── templates/
│   ├── index.html
│   ├── result.html
│── requirements.txt
│── Dockerfile
│── README.md

```
---

## ⚙️ How It Works

1️⃣ User enters a sentence<br>
2️⃣ Flask backend forwards text to the HuggingFace model<br>
3️⃣ Model returns:
   - Sentiment label
   - Confidence score<br>
4️⃣ Result page displays:
   - Input text
   - Classification label
   - Confidence meter

---
## 🚀 Deployment Pipeline (Google Cloud Run)
**Step 1: Build Docker Image**
```bash
gcloud builds submit --tag gcr.io/<project-id>/sentiment-app
```

**Step 2: Deploy to Cloud Run**
```bash
gcloud run deploy sentiment-app `
   --image gcr.io/sentiment-dashboard-project/sentiment-app `
   --platform managed `
   --region asia-south1 `
   --allow-unauthenticated `
   --set-env-vars HF_API_KEY= "real_api_key_here"

```

**Step 3: Access Public URL**<br>
Cloud Run automatically generates a secure HTTPS URL<br>
*Example*:
```bash
https://sentiment-app-xxxxxx.asia-south1.run.app

```

## 📦 Dockerfile Overview

Your image is optimized to:
- Reduce size
- Install CPU-only PyTorch
- Cache HuggingFace model
- Use Gunicorn in production

---

## 🧪 Model Used

Model: distilbert/distilbert-base-uncased-finetuned-sst-2-english<br>
Optimized for:
- Binary sentiment classification
- Low latency
- CPU-only inference

---

## 📸 Screenshots

🔵 **Dashboard UI**

![Dashboard UI](Screenshots/Dash%20Board%20UI.png)

---

🟣 **Results Page**

![Results Page](Screenshots/Results%20UI.png)

---

☁️ **Google Cloud Run Dashboard**

![Google Cloud Run Dashboard](Screenshots/Google%20Cloud%20Run%20Dashboard.png)

---

## ⭐ Contributions

Contributions, suggestions, and feature requests are welcome!

---

### 👨‍💻 Author
Kethari Madhu Sudhan Reddy<br>
Python Developer • Data Analyst • AIML Engineer<br>
maddoxer143@gmail.com

---

### 📜 License

This project is an Open Source — use it freely!