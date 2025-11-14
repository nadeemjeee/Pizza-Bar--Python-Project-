import json
import datetime

DB_FILE = "db.json"

def save_order(order_details):
    orders = load_orders()
    order_details["time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    orders.append(order_details)

    with open(DB_FILE, "w") as f:
        json.dump(orders,f)

def load_orders():
    try:
        with open (DB_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return[]
    except json.JSONDecodeError:
        return[]

