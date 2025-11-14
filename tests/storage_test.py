import json
import datetime
import app.storage as storage
from app.pizza_menu_order import PizzaOrder, Order_Calculation

def test_save_and_load_orders(tmp_path, monkeypatch):
    # Redirect DB_FILE to a temp file
    db = tmp_path / "db.json"
    monkeypatch.setattr(storage, "DB_FILE", str(db))

    # Save one order
    sample = {
        "customer": "Nadeem",
        "pizza": "margarita",
        "size": "small",
        "toppings": [],
        "total": 80
    }
    storage.save_order(sample)

    # Load and verify
    orders = storage.load_orders()
    assert len(orders) == 1
    assert orders[0]["customer"] == "Nadeem"
    assert orders[0]["pizza"] == "margarita"
    assert "time" in orders[0]  
