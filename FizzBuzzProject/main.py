# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

### You can delete this un-needed function
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    max = int(input("Enter the maximum number for FizzBuzz: "))
    rule_nums = input("Enter the rules that you want to implement, each separated by a space: ")

    rules = rule_nums.split()

    ### Could you seperate out the main FizzBuzz logic into a seperate function
    for x in range (1, max+1):
        out_string = ""
        if x % 3 == 0 and "3" in rules:
            out_string += "Fizz"
        if x % 5 == 0 and "5" in rules:
            out_string += "Buzz"
        if x % 7 == 0 and "7" in rules:
            out_string += "Bang"
        if x % 11 == 0 and "11" in rules:
            out_string = "Bong"

        if x % 13 == 0 and "13" in rules:
            index = out_string.find('B')
            if index == -1:
                out_string += "Fezz"
            else:
                out_string = out_string[:index] + "Fezz" + out_string[index:]

        ### In this bit of code you are converting a string into an array of strings and then turning that array back into a string
        ### You also rely on the fact that the words that will be printed are 4 letters long what if that was no longer the case?
        ### Could you instead see if you can use an array of strings right from the start and only convert it back to a string at the end when printing the result?
        ### Please let me know if you have any questiosn about what I've said :)
        if x % 17 == 0 and "17" in rules:
            names = []
            if len(out_string) > 4:
                while len(out_string) != 0:
                    names.append(out_string[-4:])
                    out_string = out_string[-4:]

                names.reverse()
                for name in names:
                    out_string += name

        if out_string == "":
            out_string += str(x)

        print(out_string)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
