def invalid_name(list, element_name):
    global name_dic
    for dic in list:
        try:
            if dic["user_name"] == element_name:
                return True
        except:
            if dic["product_name"] == element_name:
                name_dic = dic
                return True
    return False
def add_user():
    if admin_privileges == True:
        user_name = input("Enter the user name (b: return to the menu)")
        if user_name == "b":
            return admin_menu()
    else:
        user_name = input("Enter the user name")
    while invalid_name(users, user_name):
        user_name = input("User name already exist. Enter another username ")
    password = input("Enter the password ")
    global logged_user
    logged_user = len(users)
    users.append({
        "user_id": len(users),
        "user_name": user_name,
        "password": password,
        "products": []
    })
    print("User " + user_name + " succesfuly added")
    if admin_privileges:
        admin_menu()
    else:
        user_menu()
def remove_user():
    print("This is the users list: ")
    print_elements_names(users)
    user_name = input("Enter the username that you want to remove   (b)To return to the menu")
    if user_name == "b":
        return admin_menu()
    remove_id = None
    for user in users:
        if user["user_name"] == user_name:
            remove_id = user["user_id"]
            print(user)
            break
    if remove_id is None:
        print("User not found")
    else:
        answer = input("Do you really want yo delete this user Y/n")
        if answer == "Y":
            del users[remove_id]
            admin_menu()
        elif answer == "n":
            return remove_user()
        else:
            print("Invalid input")
            return remove_user()
def add_product():
    product_name = input("Add a product name:    (b)To return to the menu")
    if product_name == "b":
        return admin_menu()
    if invalid_name(products, product_name):
        answer = input("Product name already exists. "
                       "Do you want to increase the quantity? (i), or choose another name?(c)").lower()
        if answer == "c":
            return admin_menu()
        elif answer == "i":
            quantity_to_add = int(input("How many units to add?: "))
            name_dic["product_quantity"] += quantity_to_add
            return admin_menu()
        else:
            print("Invalid input")
            return add_product()
    product_price = int(input("What is the product price? "))
    product_quantity = int(input("What is the quantity? "))
    products.append({
        "product_id": len(products),
        "product_name": product_name,
        "product_price": product_price,
        "product_quantity": product_quantity
    })
    print("Product " + product_name + " succesfuly added")
    admin_menu()
def print_elements_names(list):
    for dic in list:
        try:
            print("\t" + dic["user_name"])
        except:
            print("\t" + dic["product_name"])
def remove_product():
    print("This is the products list")
    print_elements_names(products)
    product_name = input("Enter the product that you want to remove   (b)To return to the menu")
    if product_name == "b":
        return admin_menu()
    remove_id = None
    for product in products:
        if product["product_name"] == product_name:
            remove_id = product["product_id"]
            print(product)
            break
    if remove_id is None:
        print("Product not found")
    else:
        answer = input("Do you really want yo delete this product Y/n").lower()
        if answer == "y":
            del products[remove_id]
            return admin_menu()
        elif answer == "n":
            return remove_user()
        else:
            print("Invalid input")
            return remove_user()
def check_lists(lists):
    i = 1
    for dic in lists:
        print("(" + str(i) + ")", dic)
        i += 1
def check_users():
    check_lists(users)
    admin_menu()
def check_products():
    check_lists(products)
    admin_menu()
def shopping():
    i = 0
    print("Products list:")
    for product in products:
        print("("+str(i)+")", product["product_name"], "\t", str(product["product_price"]) + "$",
              "\t", str(product["product_quantity"])+"u")
        i += 1
    product_number = int(input("Enter the product number that you want to buy \n (-1)To return to the menu"))
    if product_number == -1:
        return user_menu()
    if product_number in range(0, len(products)):
        users[logged_user]["products"].append(products[product_number])
        products[product_number]["product_quantity"] -= 1
    else:
        print("The number choosed does not exist in the products list")
        shopping()
    user_menu()
def check_cart():
    try:
        sum = 0
        i = 0
        for product in users[logged_user]["products"]:
            print("(" + str(i) + ")", product["product_name"], "\t", str(product["product_price"])+ "$")
            sum += product["product_price"]
            i += 1
        print("\n\t The sum is: ", str(sum) + "$")
    except:
        print("This user does not have products")
        user_menu()
    if admin_privileges:
        admin_menu()
    else:
        user_menu()
def remove_from_cart():
    try:
        i = 0
        for product in users[logged_user]["products"]:
            print("(" + str(i) + ")", product["product_name"], "\t", str(product["product_price"]) + "$")
            i += 1
    except:
        print("This user does not have products")
        return user_menu()
    answer = int(input("Type the number of product to remove"))
    if answer in range(0, len(users[logged_user]["products"])):
        res = input("Are you sure that you want to remove this item? Y/N").lower()
        if res == "y":
            users[logged_user]["products"][answer]["product_quantity"] +=1
            del users[logged_user]["products"][answer]
            if admin_privileges:
                admin_menu()
            else:
                user_menu()
        elif res == "n":
            return remove_from_cart()
        else:
            return remove_from_cart()
    else:
        print("Invalid input")
        return remove_from_cart()
def finish ():
    print("Thanks for choosing us")
    quit()
def admin_menu():
    task_number = input("(1)Add user \n" + "(2)Remove user \n" + "(3)Add product \n" + "(4)Remove product \n" +
                        "(5)Check users\n" + "(6)Check products \n" + "(7)Quit \nPlease choose an operation \n")
    while int(task_number) not in range(1, 8):
        task_number = input("Incorrect operation enter another number ")
    return {
        "1": add_user,
        "2": remove_user,
        "3": add_product,
        "4": remove_product,
        "5": check_users,
        "6": check_products,
        "7": quit

    }[task_number]()
def user_menu():
    answer = input("\t(1)Shopping.\n\t(2)Check your cart\n\t"
                   "(3)Remove a product from the cart\n\t(4)Finish\nPlease choose an operation\n")
    return {
        "1": shopping,
        "2": check_cart,
        "3": remove_from_cart,
        "4": finish,
    }[answer]()
products = [
    {
        "product_id": 0,
        "product_name": "Adidas Shoes                       ",
        "product_price": 100,
        "product_quantity": 50

    },
    {
        "product_id": 1,
        "product_name": "Nike T-shirt                       ",
        "product_price": 30,
        "product_quantity": 150
    },
    {
        "product_id": 2,
        "product_name": "Hat                                 ",
        "product_price": 25,
        "product_quantity": 30
    },
    {
        "product_id": 3,
        "product_name": "Jeans pants                         ",
        "product_price": 60,
        "product_quantity": 55
    },
    {
        "product_id": 4,
        "product_name": "Adidas Shoes                         ",
        "product_price": 10,
        "product_quantity": 150
    },
]
users = [
    {
        "user_id": 0,
        "user_name": "admin",
        "password": "admin1234",

    },
    {
        "user_id": 1,
        "user_name": "Jimmy",
        "password": "Jimmy1234",
        "products": [products[1]]
    },
    {
        "user_id": 2,
        "user_name": "Maria",
        "password": "Maria1234",
        "products": [products[1]]
    },
]
name_dic = None
tries = 5
logged_user = None
admin_privileges = False
answer = input("(1)Register.\n (2)Sign in.\n Please choose an option ")
while int(answer) in range(1, 3):
    if answer == "1":
        add_user()
    elif answer == "2":
        while tries > 0:
            user_name = input("Introduzca el nombre de usuario ")
            user_password = input("Introduce tu contraseña ")
            for user in users:
                if user_name == user["user_name"] and user_password == user["password"]:
                    print("Hola " + user_name)
                    logged_user = user["user_id"]
                    tries = -1
                    break
            if tries != -1:
                print("Datos incorrectos\n" + str(tries) + " Intentos restantes")
                tries -= 1
    if user_name == "admin":
        admin_privileges = True
        admin_menu()
    else:
        user_menu()

