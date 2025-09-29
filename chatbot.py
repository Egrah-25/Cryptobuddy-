# chatbot.py

# --- Step 1: Predefined crypto dataset ---
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

# --- Step 2: Greeting function ---
def greet():
    print("🤖 Hi, I’m CryptoBuddy – your AI-powered financial sidekick!")
    print("Ask me about trending cryptos, sustainability, or long-term growth advice. 🚀🌱")
    print("Type 'exit' to quit.\n")

# --- Step 3: Chatbot logic ---
def chatbot():
    greet()
    while True:
        user_query = input("You: ").lower()

        if user_query == "exit":
            print("CryptoBuddy: Goodbye! Remember, crypto is risky—always do your own research! ✨")
            break

        # Rule 1: Most sustainable coin
        elif "sustainable" in user_query:
            recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            print(f"CryptoBuddy: {recommend} 🌱 is the most eco-friendly option with a strong sustainability score!")

        # Rule 2: Which crypto is trending up?
        elif "trending" in user_query or "rising" in user_query:
            rising_coins = [c for c in crypto_db if crypto_db[c]["price_trend"] == "rising"]
            print(f"CryptoBuddy: These coins are trending up: {', '.join(rising_coins)} 🚀")

        # Rule 3: Best for long-term growth
        elif "long-term" in user_query or "growth" in user_query:
            candidates = [
                c for c in crypto_db 
                if crypto_db[c]["price_trend"] == "rising" 
                and crypto_db[c]["sustainability_score"] >= 7/10
            ]
            if candidates:
                print(f"CryptoBuddy: {candidates[0]} looks great for long-term growth! 🚀🌱")
            else:
                print("CryptoBuddy: None perfectly match long-term criteria right now. Keep researching!")

        else:
            print("CryptoBuddy: Hmm 🤔 I didn’t get that. Try asking about sustainability, trending coins, or long-term growth.")

# --- Step 4: Run chatbot ---
if __name__ == "__main__":
    chatbot()
