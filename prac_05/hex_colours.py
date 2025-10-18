colour_name_to_code = {"amber": "#ffbf00", "aqua": "#00ffff", "army Green": "#4b5320", "aureolin": "#fdee00",
                "baby blue": "#89cff0", "blond": "#faf0be", "brass": "#b5a642", "heliotrope": "#df73ff",
                "inchworm": "#b2ec5d","jade": "#00a86b"}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    try:
        print(f"{colour_name.title()} is {colour_name_to_code[colour_name]}")
    except KeyError:
        print("Invalid colour name.")
    colour_name = input("Enter a colour name: ").lower()