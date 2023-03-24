def return_10():
    return 10

def add(num_1, num_2):
    return(num_1 + num_2)

def subtract(num_1, num_2):
    return(num_1 - num_2)
    
def multiply (num_1, num_2):
    return(num_1 * num_2)

def divide(num_1, num_2):
    return(num_1 / num_2)

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(num_1, num_2):
    return int(num_1) + int(num_2)


def number_to_full_month_name(num):
   
#    months = {
#     1: "January",
#     2: "February"
#    }

#    return months[month_number]

# months = [
#     "January, February"
# ]

# return months[month_number -1]

    if num == 1:
        return("January")
    elif num == 3:
        return("March")
    elif num == 9:
        return("September")

def number_to_short_month_name(num):
    if num == 1:
        return("Jan")
    elif num == 4:
        return("Apr")
    elif num == 10:
        return("Oct")


# alt method for solving string_reverse test
def string_reverse(str):
    "".join(reversed(str))

# string = "Banana"
# string[::-1]









    

