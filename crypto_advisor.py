# crypto_advisor.py
# CryptoBuddy: Your friendly crypto advisor chatbot

crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 0.3  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 0.6  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 0.8  
    }  
}

def crypto_advisor(query):
    query = query.lower()

    if "trending up" in query or "long-term growth" in query:
        # Prioritize coins with rising price trend and high market cap
        candidates = [c for c, d in crypto_db.items() if d["price_trend"] == "rising" and d["market_cap"] == "high"]
        if candidates:
            return f"{candidates[0]} is trending up with a strong market cap! 🚀"
        else:
            # fallback to any rising trend
            candidates = [c for c, d in crypto_db.items() if d["price_trend"] == "rising"]
            if candidates:
                return f"{candidates[0]} is trending up! 🚀"
            else:
                return "No cryptocurrencies are trending up right now."

    elif "most sustainable" in query or "eco-friendly" in query:
        # Prioritize coins with low energy use and sustainability score > 0.7
        sustainable_coins = [c for c, d in crypto_db.items() if d["energy_use"] == "low" and d["sustainability_score"] > 0.7]
        if sustainable_coins:
            best = max(sustainable_coins, key=lambda c: crypto_db[c]["sustainability_score"])
            score = crypto_db[best]["sustainability_score"] * 10
            return f"{best} is the most sustainable with a score of {score}/10! 🌱"
        else:
            return "No highly sustainable cryptocurrencies found."

    elif "advice" in query or "buy" in query:
        # Combine profitability and sustainability filters
        good_coins = [c for c, d in crypto_db.items() if d["price_trend"] == "rising" and d["market_cap"] == "high" and d["sustainability_score"] > 0.7]
        if good_coins:
            return f"Consider {good_coins[0]} for growth and sustainability! 🚀🌱"
        else:
            return "Consider diversifying; no single coin meets all criteria perfectly."

    else:
        return "Sorry, I didn't understand that. Try asking about trending or sustainable cryptos!"

def main():
    print("CryptoBuddy: Hey there! Ask me about crypto trends or sustainability. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("CryptoBuddy: Catch you later! 🚀")
            break
        response = crypto_advisor(user_input)
        print("CryptoBuddy:", response)

if __name__ == "__main__":
    main()
