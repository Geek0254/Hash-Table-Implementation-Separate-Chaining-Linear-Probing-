import random
import time

def hash_function(key, table_size):
    return key % table_size

def insert_key_separate_chaining(hash_table, key):
    index = hash_function(key, len(hash_table))
    if hash_table[index] is None:
        hash_table[index] = [key]
    else:
        hash_table[index].append(key)

def insert_key_linear_probing(hash_table, key):
    index = hash_function(key, len(hash_table))
    while hash_table[index] is not None:
        index = (index + 1) % len(hash_table)
    hash_table[index] = key

def create_hash_table(size):
    return [None] * size

def generate_random_numbers(size):
    return [random.randint(1, 100) for _ in range(size)]

def display_hash_table(hash_table):
    for index, value in enumerate(hash_table):
        if value is not None:
            print("Index: {} - Value: {}".format(index, value))
        else:
            print("Index: {} - Value: None".format(index))

def separate_chaining():
    print("\n------ Separate Chaining ------")
    table_size = int(input("Enter the size of the hash table (number of slots): "))
    hash_table = create_hash_table(table_size)

    print("\nChoose an option for inputting values:")
    print("1. Randomly generate numbers")
    print("2. Manually input numbers")
    option = int(input("Enter the option (1 or 2): "))

    if option == 1:
        numbers = generate_random_numbers(table_size)
        print("\nGenerated Numbers:", numbers)
    elif option == 2:
        print("Enter {} numbers:".format(table_size))
        numbers = [int(input()) for _ in range(table_size)]
    else:
        print("Invalid option selected.")
        return

    for key in numbers:
        insert_key_separate_chaining(hash_table, key)

    print("\n------ Hash Table with Separate Chaining ------")
    display_hash_table(hash_table)

def linear_probing():
    print("\n------ Linear Probing ------")
    table_size = int(input("Enter the size of the hash table (number of slots): "))
    hash_table = create_hash_table(table_size)

    print("\nChoose an option for inputting values:")
    print("1. Randomly generate numbers")
    print("2. Manually input numbers")
    option = int(input("Enter the option (1 or 2): "))

    if option == 1:
        numbers = generate_random_numbers(table_size)
        print("\nGenerated Numbers:", numbers)
    elif option == 2:
        print("Enter {} numbers:".format(table_size))
        numbers = [int(input()) for _ in range(table_size)]
    else:
        print("Invalid option selected.")
        return

    for key in numbers:
        insert_key_linear_probing(hash_table, key)

    print("\n------ Hash Table with Linear Probing ------")
    display_hash_table(hash_table)

def both():
    print("\n------ Separate Chaining ------")
    table_size = int(input("Enter the size of the hash table (number of slots): "))
    hash_table = create_hash_table(table_size)

    print("\nChoose an option for inputting values:")
    print("1. Randomly generate numbers")
    print("2. Manually input numbers")
    option = int(input("Enter the option (1 or 2): "))

    if option == 1:
        numbers = generate_random_numbers(table_size)
        print("\nGenerated Numbers:", numbers)
    elif option == 2:
        print("Enter {} numbers:".format(table_size))
        numbers = [int(input()) for _ in range(table_size)]
    else:
        print("Invalid option selected.")
        return

    for key in numbers:
        insert_key_separate_chaining(hash_table, key)

    print("\n------ Hash Table with Separate Chaining ------")
    display_hash_table(hash_table)

    print("\nImplementing Linear Probing...")
    time.sleep(3)

    hash_table = create_hash_table(table_size)

    for key in numbers:
        insert_key_linear_probing(hash_table, key)

    print("\n------ Hash Table with Linear Probing ------")
    display_hash_table(hash_table)

def main():
    while True:
        print("\n------ Hash Table Implementation Options ------")
        print("1. Separate Chaining")
        print("2. Linear Probing")
        print("3. Both (Separate Chaining then Linear Probing)")
        print("4. Quit")

        option = int(input("Enter the option (1, 2, 3, or 4): "))

        if option == 1:
            separate_chaining()
        elif option == 2:
            linear_probing()
        elif option == 3:
            both()
        elif option == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid option selected. Please try again.")

if __name__ == "__main__":
    main()
