my_cats = []
cats_with_hats = ""

for cat in range(1, 101):
    my_cats.append([cat, False])

for pass_number in range(1,101):
    for cat in my_cats:
        if (cat[0] % pass_number) == 0:
            cat[1] = not cat[1]

for cat in my_cats:
    if cat[1]:
        print(f"Cat {cat[0]} is wearing a hat.")

            
