def all_true_in_tuple(data):
    return all(data)


tuple1 = (True, True, True)
tuple2 = (True, False, True)

print(all_true_in_tuple(tuple1))  
print(all_true_in_tuple(tuple2))  
