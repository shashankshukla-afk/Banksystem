CHATBOT_KNOWLEDGE_BASE = {
    # --- General & Chat Flow ---
    "hello": [
        "Hi! Welcome to your Python study helper.",
        "Hello there! How can I assist you with your fundamentals?"
    ],
    "how are you": [
        "I'm a program, so I'm doing great! Ready to talk Python?",
        "I'm functioning perfectly and ready to help you study."
    ],
    "what is your name": [
        "I am the Python Fundamentals Chatbot, here to test your basics.",
        "I don't have a name, but I know a lot about Python basics!"
    ],
    "bye": [
        "Goodbye! Have a great day and keep coding.",
        "See you later! Come back anytime you need a quick review."
    ],
    
    # --- Variables and Data Types ---
    "what is a variable": [
        "A variable is a reserved memory location to store values, like a labeled box.",
        "In Python, variables don't require explicit declaration before use."
    ],
    "what are data types": [
        "Data types define the type of data a variable holds, like int, float, str, or bool.",
        "Python is dynamically typed, meaning you don't declare the type explicitly."
    ],
    "what is an integer": [
        "An integer (`int`) is a whole number, positive or negative, without a decimal point.",
        "Integers are fundamental numerical data types in Python."
    ],
    "what is a string": [
        "A string (`str`) is a sequence of characters, enclosed in single or double quotes.",
        "Strings are immutable, meaning they cannot be changed after creation."
    ],
    
    # --- Input/Output (I/O) ---
    "how to get user input": [
        "You use the `input()` function to get text input from the user.",
        "The `input()` function always returns the data as a string."
    ],
    "how to print output": [
        "You use the `print()` function to display information to the console.",
        "`print()` can output strings, numbers, or the contents of variables."
    ],
    
    # --- Operators ---
    "what is an operator": [
        "An operator is a symbol that tells the interpreter to perform a specific mathematical or logical manipulation.",
        "Examples include `+`, `-`, `*` (arithmetic) and `==`, `>` (comparison)."
    ],
    "comparison operators": [
        "Comparison operators like `==`, `>`, `<`, `!=` are used to compare two values.",
        "They always return a boolean value: `True` or `False`."
    ],
    "logical operators": [
        "Logical operators are `and`, `or`, and `not`. They combine conditional statements.",
        "`and` requires both conditions to be true; `or` requires at least one to be true."
    ],
    
    # --- Conditional Statements ---
    "what is if else": [
        "The `if/else` structure executes a block of code based on whether a condition is True or False.",
        "It controls the flow of execution in your program."
    ],
    "what is elif": [
        "`elif` stands for 'else if'. It allows you to check multiple conditions sequentially.",
        "It's used when you have more than two possible outcomes."
    ],
    
    # --- Loops ---
    "what is a loop": [
        "A loop allows you to repeat a block of code. The main types are 'for' and 'while'.",
        "Loops are key for iterating over collections like lists."
    ],
    "for loop vs while loop": [
        "`for` loops are for iterating over a sequence (known number of times). `while` loops repeat as long as a condition is true (unknown number of times).",
        "Use a `for` loop when you know how many times you need to repeat, and `while` otherwise."
    ],
    "how to stop a loop": [
        "You can use the `break` statement to exit a loop immediately.",
        "You can use the `continue` statement to skip the current iteration and move to the next."
    ],
    
    # --- Python Collections (Lists, Dictionaries, etc.) ---
    "what is a list": [
        "A list is an ordered, mutable (changeable) collection of items, enclosed in square brackets `[]`.",
        "Lists are one of the most versatile collection types in Python."
    ],
    "how to add to a list": [
        "You can use the `.append()` method to add an item to the end of a list.",
        "Use the `.insert()` method to add an item at a specific index."
    ],
    "what is a dictionary": [
        "A dictionary is an unordered, mutable collection of **key:value** pairs, enclosed in curly braces `{}`.",
        "Keys must be unique and immutable (like strings or numbers)."
    ],
    "how to access dictionary": [
        "You access a dictionary value by referencing its key inside square brackets, e.g., `my_dict['key']`.",
        "You can use the `.get()` method to safely retrieve a value without raising an error if the key isn't found."
    ],
    "what is a tuple": [
        "A tuple is an ordered, **immutable** (unchangeable) collection of items, often defined with parentheses `()`.",
        "Tuples are generally used for collections of items that shouldn't change."
    ],
    
    # --- Functions ---
    "what is a function": [
        "A function is a block of reusable code that performs a specific, single task.",
        "Functions help break code into modular, manageable pieces."
    ],
    "how to define a function": [
        "You define a function using the `def` keyword, followed by the function name and parentheses.",
        "Functions can optionally take arguments and return a value using the `return` statement."
    ],
    "what is a return statement": [
        "The `return` statement is used to exit a function and send a value back to the code that called it.",
        "If a function doesn't explicitly return a value, it returns `None`."
    ],
    
    # --- File I/O (Basic) ---
    "what is file io": [
        "File I/O (Input/Output) refers to reading data from a file or writing data to a file.",
        "It allows your program to interact with external storage."
    ],
    "how to open a file": [
        "You use the built-in `open()` function, specifying the file path and the mode ('r' for read, 'w' for write, 'a' for append).",
        "It's best practice to use the `with open(...) as file:` structure to ensure the file is closed automatically."
    ],
    
    # --- Basic Error Handling ---
    "explain try except": [
        "The `try/except` block is used for basic error handling. Code that might fail goes in `try`.",
        "If an error occurs in `try`, the program jumps to the `except` block instead of crashing."
    ],
    "what is a value error": [
        "A `ValueError` is raised when a function receives an argument of the correct type but an inappropriate value.",
        "A common example is trying to convert a non-numeric string like 'hello' into an integer with `int('hello')`."
    ]
}