# We will use args and kwargs to create a shipping label

def create_shipping_label(*args, **kwargs): # first pass positional arguments, then keyword arguments
    # Start with positional arguments
    for arg in args:
        print(arg, end=" ")
    print()
    if 'building' in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('building')}")
    elif 'po_box' in kwargs:
        print(f"{kwargs.get('street')}\n{kwargs.get('po_box')}")
    else:
        print(kwargs.get('street'))
    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

create_shipping_label("Dr.", "Jeffrey", "Bobby",
                      street="123 Main St", 
                      building="Suite 100",
                      city="Metropolis", 
                      state="CA", 
                      zip="12345")

print()

create_shipping_label("Sr.", "Bobby", "Jeffrey",
                      street="321 Street Main", 
                      city="Gotham", 
                      state="NY", 
                      zip="54321")

print()
create_shipping_label("Sra.", "Mamacita", "Sofia",
                      street="80085 Via La Calle", 
                      po_box="PO Box #123",
                      city="Ciudad", 
                      state="NV", 
                      zip="13579")