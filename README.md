# 🔎 FastAPI Machine Learning API for Diabetes Risk Prediction

## 📋 Project Overview
- This project is a **Machine Learning API** built with **FastAPI** and **Uvicorn**.  
- It provides an endpoint to **predict health-related data** using an **SVM (Support Vector Machine) model** trained on Kaggle.  
- The API can be deployed **locally** or on **Virtual Machine** etc. 

## ✨ Features
✅ **FastAPI framework** for fast and efficient API development  
✅ **Pre-trained SVM model** for predictions  
✅ **Swagger UI (`/docs`)** for interactive API documentation  
✅ **Secure and scalable setup**  

---

## 🛠 Installation & Deployment

### **Setup**
To run this API on your **local machine**, follow these steps:

#### **Step 1: Clone the Repository**
```bash
git clone https://github.com/0alp/FastAPI-ML-Predictor.git
cd ML-PREDICT
```
#### **Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```
#### **Step 3: Run FastAPI Server**
```bash
uvicorn main:app --host 0.0.0.0 --port 7584 --reload
```
---
## ⚠️ Disclaimer (Liability Notice)
- This project provides a **machine learning API for diabetes predictions**. However, the predictions **are not guaranteed to be 100% accurate** and should **not** be used for **medical decisions or real-world critical applications**.
  
- The author of this project do not take any responsibility for incorrect predictions, system failures, or any damages resulting from the use of this software.

