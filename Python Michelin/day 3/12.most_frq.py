def most_frq_value(numbers):
    frq_dict= {
        no:numbers.count(no) for no in numbers if no % 2 ==0
     
     }
    return frq_dict
print(most_frq_value([101,202,303,202,404, 404,606]))