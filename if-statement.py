is_available = False
is_discount = False
is_coming = True
if is_available and is_discount:
    print("Product is available and discount is 10%")
elif not (is_available) or not (is_discount):
    print("Product is either not available or no discount")
elif is_available or is_coming:
    print("Product is either available or coming soon")
else:
    print("Product is not available")
