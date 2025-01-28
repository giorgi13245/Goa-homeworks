#1
def string_to_number(s):
    return int(s)


#2
def boolean_to_string(b):
    return str(b)


#3
def make_upper_case(s):
    s=s.upper()
    return s



#4
def bool_to_word(boolean):
    if boolean==True:
        return "Yes"
    else:
        return "No"


#5
def make_negative( number ):
    if number<0:
        return number
    else:
        return number*-1






#6
def square_sum(numbers):
    result=0
    for i in numbers:
        result+= i**2
        
    return result






