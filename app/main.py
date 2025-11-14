from pizza_menu_order import PizzaOrder, Order_Calculation
from storage import save_order, load_orders

def main():
    while True:
        print("\n====Welcome to Python Pizza Bar====")
        print("1. Place a new order")
        print("2. Show previous order")
        print("3. Quit")

        choice = input("Your choice(1/2/3): ")
        if choice == "1":
            name = input("Enter your name: ").strip().capitalize()
            pizza = input("Pizza name (margarita/kebabpizza/hawaiian/pepperoni_feast/new_yorker): ").strip().lower()
            size = input("Size (small/medium/large): ").strip().lower()
            print("Available toppings: extra_cheese, red_onion, mushrooms, black_olives")
            toppings_input = input("Choose extra toppings (comma separated, or leave empty): ").strip().lower()
            if toppings_input =="":
                toppings = []
            else:
                toppings = [t.strip().lower() for t in toppings_input.split(",")]

            order = PizzaOrder(name,pizza,size,toppings)
            pizza_price = Order_Calculation()
            try:
                total = pizza_price.pizza_price(order)
            except ValueError as e:
                print(f"Error: {e}")
                continue

            print("\n--- Order Details ---")
            print(f"Customer: {order.customer_name}")
            print(f"Pizza: {order.pizza_name}")
            print(f"Size: {order.size}")
            if order.topping:
                print(f"Toppings: {', '.join(order.topping)}")
            else:
                print("Toppings: None")
            print(f"Total: {total} kr")
            save_order({
                "customer": name,
                "pizza": pizza,
                "size": size,
                "toppings": toppings,
                "total": total
            })
            print("Order saved!")

        elif choice == "2":
            orders = load_orders()

            if not orders:
                print("\nNo saved orders yet.")
            else:
                print("\n--- Saved Orders ---")
                for i, order in enumerate(orders, start=1):
                    print(f"Order {i}:")
                    print(f"  Customer: {order['customer']}")
                    print(f"  Pizza: {order['pizza']}")
                    print(f"  Size: {order['size']}")
                    print(f"  Total: {order['total']} kr")
                    print(f"  Time: {order['time']}")
                    print() 
        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
   