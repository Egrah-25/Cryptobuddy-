# 🤖 CryptoBuddy – Your First AI-Powered Financial Sidekick!

## 📌 Overview
CryptoBuddy is a simple **rule-based chatbot** built in Python that provides basic cryptocurrency investment advice.  
It considers **profitability** (price trends, market cap) and **sustainability** (energy use, eco-scores).  

This project was created as part of **Week 1 AI Assignment**.

---

## ⚙️ Features
- Suggests which cryptocurrencies are **trending up** 📈
- Identifies the **most sustainable coin** 🌱
- Gives advice for **long-term growth** 🚀
- Friendly, beginner-friendly interaction
- Includes a **risk disclaimer**

---

## 🛠️ Tools Used
- **Python**  
- **If-Else Logic** (rule-based AI)  
- Runs on **Google Colab / Jupyter Notebook / Any IDE**

---

## 📊 Sample Data
```python
crypto_db = {
    "Bitcoin": {"price_trend": "rising", "market_cap": "high", "energy_use": "high", "sustainability_score": 3/10},
    "Ethereum": {"price_trend": "stable", "market_cap": "high", "energy_use": "medium", "sustainability_score": 6/10},
    "Cardano": {"price_trend": "rising", "market_cap": "medium", "energy_use": "low", "sustainability_score": 8/10}
}
## Example interaction 

You: Which crypto is trending up?
CryptoBuddy: Bitcoin, Cardano 🚀

You: What’s the most sustainable coin?
CryptoBuddy: Cardano 🌱 with a strong sustainability score!

You: Which crypto should I buy for long-term growth?
CryptoBuddy: Cardano looks great for long-term growth! 🚀🌱
