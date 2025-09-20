import random
import datetime

class FinanceChatbot:
    def __init__(self):
        self.expenses = []
        self.balance = 1000  # starting balance (example)

    def get_response(self, message):
        message = message.lower()

        if "add expense" in message:
            try:
                amount = int(message.split()[-1])
                self.expenses.append(amount)
                self.balance -= amount
                return f"✅ Added expense of ₹{amount}. Current balance: ₹{self.balance}"
            except:
                return "❌ Please specify expense amount like: add expense 200"

        elif "show expenses" in message:
            if not self.expenses:
                return "📂 No expenses recorded yet."
            return f"📊 Your expenses: {self.expenses}, Total = ₹{sum(self.expenses)}"

        elif "balance" in message:
            return f"💵 Your current balance is ₹{self.balance}"

        elif "advice" in message:
            tips = [
                "💡 Save at least 20% of your income every month.",
                "📉 Track daily expenses to reduce unwanted spending.",
                "📈 Invest in mutual funds or SIPs for long-term growth.",
                "💳 Avoid using credit cards for unnecessary purchases."
            ]
            return random.choice(tips)

        elif "date" in message:
            return f"📅 Today's date is {datetime.date.today()}"

        else:
            return "🤔 I can help with: add expense <amount>, show expenses, balance, advice, date."
