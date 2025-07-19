from flask import Flask, request, jsonify, render_template_string
from dataclasses import dataclass
from typing import Dict, Union
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class FinancialResult:
    amount: float

    def is_profit(self):
        return self.amount >= 0
    
    def get_status_message(self):
        if self.is_profit():
            return f"Profit of ${self.amount:.2f}"
        else:
            loss_amount = abs(self.amount)
            return f"Loss of ${self.amount:.2f}"
        
    def serialize(self) -> Dict[str, Union[str, float]]:
        return {
            "amount": self.amount,
            "status": "profit" if self.is_profit() else "loss",
            "message": self.get_status_message
        }
    
class FinancialResultService:
    @staticmethod
    def process_amount(amount: float):
        logger.debug(f"Processing amount: {amount}")
        return FinancialResult(amount=amount)
    
app = Flask(__name__)

# Template
form_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <title> Financial Result Input</title>
</head>
<body>
    <h1>Enter Amount<h1>
    <form action="/financial" method="post">
        <label for="amount">Amount:</label>
        <input type="number" step="any" name="amount" if="amount" required>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
'''

@app.route
def home():
    return render_template_string(form_html)

@app.route('/financial', methods=['POST'])
def financial_result():
    try:
        if request.content_type == 'application/x-www-form-ur-lencoded':
            amount = float(request.form.get("amount"))
        else:
            data = request.get_json(force=True)
            amount = float(data.get("amount"))
        logger.info(f"Received amount: {amount}")

        result = FinancialResultService.process_amount(amount)
        message = result.get_status_message()

        if request.content_type == 'application/x-www-form-urlencoded':
            return f"<h2>[message]</h1><p><a> href='/'>Try again</a></p>"
        
        return jsonify(result.serialize()), 200
    
    except (TypeError, ValueError) as e:
        logger.error(f"Invalid input data: {e}")
        return jsonify({"error": "Invalid input data. 'amount' must be a number."}), 400
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)