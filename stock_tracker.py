import csv
import webbrowser
from datetime import datetime

def stock_tracker():
    print("📈 Advanced Stock Portfolio Tracker")

    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 2800,
        "AMZN": 3400,
        "MSFT": 300
    }

    portfolio = {}
    total_investment = 0
    total_current_value = 0

    while True:
        print("\nAvailable stocks:", list(stock_prices.keys()))
        stock = input("Enter stock name (or 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("❌ Stock not available!")
            continue

        try:
            qty = int(input("Enter quantity: "))
            buy_price = float(input("Enter buy price: "))
        except:
            print("❌ Invalid input!")
            continue

        portfolio[stock] = (qty, buy_price)

    rows = ""

    for stock, (qty, buy_price) in portfolio.items():
        current_price = stock_prices[stock]
        invested = qty * buy_price
        current_value = qty * current_price
        profit = current_value - invested

        total_investment += invested
        total_current_value += current_value

        color = "green" if profit >= 0 else "red"

        rows += f"""
        <tr>
            <td>{stock}</td>
            <td>{qty}</td>
            <td>${buy_price}</td>
            <td>${current_price}</td>
            <td>${invested}</td>
            <td>${current_value}</td>
            <td style='color:{color}; font-weight:bold;'>${profit}</td>
        </tr>
        """

    total_profit = total_current_value - total_investment
    total_color = "green" if total_profit >= 0 else "red"

    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_content = f"""
    <html>
    <head>
        <title>Stock Portfolio Report</title>
        <style>
            body {{
                font-family: Arial;
                background-color: #f4f6f8;
                padding: 20px;
            }}
            h1 {{
                text-align: center;
                color: #2c3e50;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                background: white;
                box-shadow: 0px 0px 10px gray;
            }}
            th, td {{
                padding: 12px;
                border-bottom: 1px solid #ddd;
                text-align: center;
            }}
            th {{
                background-color: #3498db;
                color: white;
            }}
            tr:hover {{
                background-color: #f1f1f1;
            }}
            .summary {{
                margin-top: 20px;
                padding: 15px;
                background: white;
                box-shadow: 0px 0px 10px gray;
            }}
        </style>
    </head>
    <body>

    <h1>📊 Stock Portfolio Report</h1>
    <p><b>Generated on:</b> {time_now}</p>

    <table>
        <tr>
            <th>Stock</th>
            <th>Quantity</th>
            <th>Buy Price</th>
            <th>Current Price</th>
            <th>Invested</th>
            <th>Current Value</th>
            <th>Profit/Loss</th>
        </tr>
        {rows}
    </table>

    <div class="summary">
        <h3>Total Invested: ${total_investment}</h3>
        <h3>Current Value: ${total_current_value}</h3>
        <h3 style="color:{total_color};">Total Profit/Loss: ${total_profit}</h3>
    </div>

    </body>
    </html>
    """

    file_name = "portfolio_report.html"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(html_content)

    print("\n✅ Report generated successfully!")
    webbrowser.open(file_name)


stock_tracker()