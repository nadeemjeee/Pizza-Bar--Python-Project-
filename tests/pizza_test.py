from app.pizza_menu_order import PizzaOrder, Order_Calculation
import pytest

def test_basic_pizza_no_toppings():
    # margarita (80) + medium (10) = 90
    order = PizzaOrder("Nadeem", "margarita", "medium", [])
    calc = Order_Calculation()
    assert calc.pizza_price(order) == 90

def test_pizza_with_toppings():
    # pepperoni_feast (105) + large (25) + extra_ost (10) + champinjoner (10) = 150
    order = PizzaOrder("Moosa", "pepperoni_feast", "large", ["extra_cheese", "mushrooms"])
    calc = Order_Calculation()
    assert calc.pizza_price(order) == 150

def test_invalid_pizza_raises():
    order = PizzaOrder("Dawood", "not_a_pizza", "small", [])
    calc = Order_Calculation()
    with pytest.raises(ValueError):
        calc.pizza_price(order)
