# CryptoBuddy - Cryptocurrency Advisor Chatbot

**Your First AI-Powered Financial Sidekick!** 🌟

CryptoBuddy is a simple rule-based chatbot built in Python that analyzes cryptocurrency data and provides investment advice based on price trends and sustainability. It demonstrates basic AI decision-making using `if-else` logic on predefined data.

## Features
- Responds to queries about trending cryptocurrencies and sustainability.
- Prioritizes coins based on profitability (price trends, market cap).
- Highlights eco-friendly options with energy use and sustainability scores.
- Simple, beginner-friendly Python implementation.

## How to Use
1. Clone the repository.
2. Run `crypto_advisor.py` in your Python environment (Google Colab, Jupyter, or IDE).
3. Chat with CryptoBuddy by typing questions like:
   - "Which crypto is trending up?"
   - "What’s the most sustainable coin?"
   - "Which crypto should I buy for long-term growth?"

Type `exit` or `quit` to end the chat.

## Dataset Sample
```python
crypto_db = {
    "Bitcoin": {"price_trend": "rising", "market_cap": "high", "energy_use": "high", "sustainability_score": 0.3},
    "Ethereum": {"price_trend": "stable", "market_cap": "high", "energy_use": "medium", "sustainability_score": 0.6},
    "Cardano": {"price_trend": "rising", "market_cap": "medium", "energy_use": "low", "sustainability_score": 0.8},
}
