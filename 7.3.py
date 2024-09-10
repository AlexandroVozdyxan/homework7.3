def second_index(text, some_str):
    if text.count(some_str) > 1:
        return text.find(some_str, text.index(some_str) + 1)
    else:
        print("Error")
str = input("Enter a text: ")
find_letter = input("Enter a str what you want find: ")


assert second_index("smile smile", "le") == 9, 'Test0'
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')