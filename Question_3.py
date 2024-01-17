def convert_to_cm_nested(heights_inches):
    heights_cm = []
    for height in heights_inches:
        height_cm = height * 2.54
        heights_cm.append(round(height_cm, 2))
    return heights_cm

# 1) Using List Comprehensions
def convert_to_cm_list_comprehension(heights_inches):
    return [round(height * 2.54, 2) for height in heights_inches]
# 2) Using Nested Loop
def main():
    heights_inches = []

    input_str = input("Enter heights in inches separated by commas: ")

    try:
        heights_inches = [float(height) for height in input_str.split(',')]
    except ValueError:
        print("Invalid input. Please enter valid numbers separated by commas.")
        return


    heights_cm_nested = convert_to_cm_nested(heights_inches)


    heights_cm_list_comp = convert_to_cm_list_comprehension(heights_inches)

    print("\nHeights in Inches:", heights_inches)
    print("Heights in Centimeters (Using Nested Loop):", heights_cm_nested)
    print("Heights in Centimeters (Using List Comprehension):", heights_cm_list_comp)

if __name__ == "__main__":
    main()
