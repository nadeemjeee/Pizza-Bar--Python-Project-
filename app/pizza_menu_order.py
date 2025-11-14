
pizza_prices = {
    "margarita": 80,
    "kebabpizza": 95,
    "hawaiian" : 85,
    "pepperoni_feast": 105,
    "new_yorker" : 110

}
size_extra = {
    "small" : 0,
    "medium": 10,
    "large" : 25
}
extra_topping = {
    "extra_cheese" : 10,
    "red_onion" : 5,
    "mushrooms": 10,
    "black_olives" : 10
}
class PizzaOrder:
    def __init__(self,customer_name,pizza_name,size,topping):
        self.customer_name = customer_name
        self.pizza_name = pizza_name
        self.size = size
        self.topping = topping
        
    def to_dict(self):
        return{
            "customer_name" : self.customer_name,
            "pizza_name" : self.pizza_name,
            "size" : self.size,
            "topping": self.topping
        }
class Order_Calculation:
    def pizza_price(self,order):
        if order.pizza_name not in pizza_prices:
            raise ValueError("Invalid Pizza Name")
        if order.size not in size_extra:
            raise ValueError("Wrong size")
        base_price = pizza_prices[order.pizza_name]+size_extra[order.size]

        extras = 0
        for t in order.topping:
            if t not in extra_topping:
                raise ValueError("Not in topping list: " + t)
            extras +=extra_topping[t]
        return base_price + extras






