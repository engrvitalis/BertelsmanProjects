def get_rainfall():
    """
    This program continuously prompts the user for name of city
    and quantity of rainfall in mm. When the user enters blank space, 
    the program is terminated and a dict is returned with city names 
    and total rainfall for each city.

    @param: None
    @return: dict
    """

    rainfall = dict()

    while True:
        city = input("Enter city name: ")
        if not city:
            break

        try:
            rain_qty = float(input("Enter rain quantity in mm: ").lower())
        except ValueError:
            print("Quantity of rain must be either int or float!")
            continue

        if city in rainfall:
            rainfall[city] += rain_qty
        else:
            rainfall[city] = rain_qty

    return rainfall



print(get_rainfall())