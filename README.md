# Smart-Employee-Sentiment-Wellness-Analysis
Analyze employee feedback using NLP to classify wellness levels and uncover actionable HR insights.
# 🧠 Smart Employee Sentiment & Wellness Analysis

Analyze employee feedback using NLP to classify employee wellness and uncover actionable HR insights.

---

## 📌 Project Objective

This project leverages **Natural Language Processing (NLP)** to assess employee sentiment from multiple sources:

* Employee survey responses
* Exit interviews

Employees are classified into three categories:

1. 🔴 **At Risk** – Negative sentiment + high attrition risk
2. 🟡 **Stable** – Mixed/neutral sentiment
3. 🟢 **Thriving** – Positive sentiment + low attrition risk

---

## 🔧 Key Tasks

### 1. Text Preprocessing

* Collect employee feedback data
* Clean and preprocess text (remove PII, tokenize, lemmatize)
* Handle emojis and abbreviations

### 2. Sentiment Analysis

* Use VADER or TextBlob for quick scoring
* Fine-tune a model like BERT for HR-specific language
* Generate sentiment scores (positive/neutral/negative)

### 3. Wellness Classification

* Combine sentiment scores with attrition risk scores (from Module 3)
* Define clear thresholds for "At Risk", "Stable", and "Thriving"

### 4. Topic Modeling 

* Use LDA or NMF to find key themes (e.g., burnout, poor leadership)
* Visualize with word clouds and bar charts

### 5. Integration

* Merge this module's output with Module 3
* Create a combined risk-sentiment report/dashboard input

---

## 📁 Project Structure

```
Smart-Employee-Sentiment-Wellness-Analysis/
├── data/                      # Raw and cleaned datasets
├── notebooks/                # Jupyter notebooks for each stage
├── models/                   # Saved ML models (e.g., BERT, vectorizers)
├── outputs/                  # Final reports, labeled data, visuals
├── src/                      # Python scripts for pipeline automation
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 Outputs

* `wellness_labels.csv` with sentiment + risk category
* `sentiment_report.pdf` with key insights and top quotes
* Topic modeling visualizations (e.g., word clouds)

---

## 🛠 Tech Stack

* **Libraries**: NLTK, SpaCy, TextBlob, VADER, HuggingFace Transformers
* **Models**: Logistic Regression, BERT (fine-tuned)
* **Visualization**: Matplotlib, Plotly, Wordcloud

---

## ✅ Status

* 📍 Requirements Defined
* 🔄 Data Collection In Progress
* 📊 Notebook Templates: ✅
* 🧠 Model Training: TBD

---

## 👤 Author

Pragna J | [GitHub Profile](https://github.com/JPragna)

> Part of the Smart Attrition & Wellness Intelligence Suite – Module 4
