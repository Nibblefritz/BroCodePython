def display_invoice(username, amount, due_date):
    print(f"Hello {username},")
    print(f"Your invoice amount is ${amount:.2f}.")
    print(f"Your invoice is due on {due_date}.")
    print("Thank you for your business!\n")
    print()
    
display_invoice("Alice", 150.75, "2023-10-31")
display_invoice("Bob", 200.00, "2023-11-15")
display_invoice("Charlie", 99.99, "2023-12-01")