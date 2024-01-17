def fullname(first_name, last_name):
    return first_name + " " + last_name
def string_alternative(full_name):
    return full_name[::2]
def main():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    full_name = fullname(first_name, last_name)
    print("Full Name:", full_name)
    alternate_chars = string_alternative(full_name)
    print("Every Other Character in Full Name:", alternate_chars)
    
main()
