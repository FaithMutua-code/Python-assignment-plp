# Task 1: Sum integers from user input
print("Task 1: Sum integers from a list")
numbers = input("Enter integers separated by spaces: ").split()
int_list = [int(num) for num in numbers]
total = sum(int_list)
print("Sum of all integers:", total)
print("-" * 40)

# Task 2: Tuple of favorite books and print each
print("Task 2: Favorite books")
books = ("1984", "To Kill a Mockingbird", "Pride and Prejudice", "The Hobbit", "Harry Potter")
for book in books:
    print(book)
print("-" * 40)

# Task 3: Dictionary with person info from user input
print("Task 3: Person info dictionary")
person = {}
person['name'] = input("Enter your name: ")
person['age'] = input("Enter your age: ")
person['favorite_color'] = input("Enter your favorite color: ")
print("Person info:", person)
print("-" * 40)

# Task 4: Sets and common elements
print("Task 4: Find common elements in two sets")
set1 = set(map(int, input("Enter integers for set 1 separated by spaces: ").split()))
set2 = set(map(int, input("Enter integers for set 2 separated by spaces: ").split()))
common = set1.intersection(set2)
print("Common elements:", common)
print("-" * 40)

# Task 5: List comprehension for odd length words
print("Task 5: Words with odd length")
words = ["apple", "banana", "pear", "grape", "kiwi", "melon"]
odd_length_words = [word for word in words if len(word) % 2 == 1]
print("Words with odd length:", odd_length_words)
