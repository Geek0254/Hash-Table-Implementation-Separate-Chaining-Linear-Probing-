import random

def hash_function(key, table_size):
    return key % table_size

def insert_key(hash_table, key):
    index = hash_function(key, len(hash_table))
    if hash_table[index] is None:
        hash_table[index] = [key]
    else:
        hash_table[index].append(key)

def create_hash_table(size):
    return [None] * size

def generate_random_numbers(size):
    return [random.randint(1, 100) for _ in range(size)]

def main():
    print("------ Dynamic Hash Table Creation ------")
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
        insert_key(hash_table, key)

    print("\n------ Hash Table with Separate Chaining ------")
    for index in range(table_size):
        value = hash_table[index]
        if value is not None:
            print("Index: {} - Value: {}".format(index, value))
        else:
            print("Index: {} - Value: None".format(index))

if __name__ == "__main__":
    main()
