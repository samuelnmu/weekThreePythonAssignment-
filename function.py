# def calculate_discount(price, discount_percent):
#     price = {
#         "soap": 20,
#         "salt": 10,
#         "sugar":100,
#         "flour": 200
#     }
#     discount_percent = 20
    
#     print(input("Enter Item"))
    
#     postDiscount = price * discount_percent / 100
    
#     print(f"price is {postDiscount}")
    

# calculate_discount()

def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount.

    Args:
        price: The original price of the item.
        discount_percent: The discount percentage.

    Returns:
        The final price after applying the discount, or the original price if the discount is less than 20%.
    """

    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
    else:
        final_price = price

    return final_price

if __name__ == "__main__":
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percentage)

    print("The final price after applying the discount is:", final_price)
    
    
    
    
    