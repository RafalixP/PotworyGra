#1
# def hidden_feature_1(a, b, *args):
#     print(a, b, args)

# hidden_feature_1("aa", "bb", 1,2)

#3 function inside the function
def adder(value):
    def inner_function(base):
        return base + value
    return inner_function

    
adder_5 = adder(5)