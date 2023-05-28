# If area = ["Mirpur", "Farmgate", "Dhanmondi"]
    # total_purchase_price > = 600
        # shipping free
    # 300 <= total_purchase_price < 600
        # shipping cost 80
    # otherwise
        # shipping cost 150

# If area = ["Mohakhali", "Gulshan"]:
    # total_purchase_price > = 800
        # shipping free
    # 500 <= total_purchase_price < 800
        # shipping cost 100
    # otherwise
        # shipping cost 200

# For rest of the area, shipping currently not available

user_area = 'Mirpur'
total_purchase_price = 400

if user_area in ["Mirpur", "Farmgate", "Dhanmondi"]:
    if total_purchase_price >= 600:
        print("Shipping is free.")
    elif total_purchase_price >= 300 and total_purchase_price < 600:
        print("Shipping price is 80.")
    else:
        print("Shipping is 150.")

# elif user_area in ["Mohakhali", "Gulshan"]:

else:
    print("Shipping currently not available.")
