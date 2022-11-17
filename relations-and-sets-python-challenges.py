
def Is_reflexive(set1, set2):
# Checks if a relation is reflexive
    domain_integers = set()
    for tuple in set2:
        if tuple[0] == tuple[1]:
            domain_integers.add(tuple[0])
    
    reflexive_test_integers = set1 - domain_integers
    print(reflexive_test_integers)
    for integer in reflexive_test_integers:
        for tuple in set2:
            if integer == tuple[0]:
                print(tuple[0])
                return f"Is R reflexive? No, {integer} not in R"

    if domain_integers.issubset(set1):
        return "Yes"
    #
    
    # return True

param1 = {1, 2, 3, 4, 5}
param2 = {(1, 2), (2, 3), (1, 3), (2, 2)}

def Is_symmetric(set2):
    for tuple in set2:
        new_tuple = (tuple[1], tuple[0])
        if new_tuple in set2:
            continue
        else:
            return f"Is R symmetric? No, {tuple} not symmetrical"
    return "Yes"




def Is_transitive(set1, set2):
    for tuple1 in set2:
        for tuple2 in set2:
            if tuple1[1] == tuple2[0]:
                for tuple3 in set2:
                    if tuple2[1] == tuple3[1]:
                        new_tuple = (tuple1[0], tuple3[1])
                        if new_tuple not in set2:
                            return f"Is R transitive? No, you cannot get from {tuple1[0]} to {tuple3[0]} with a shortcut."
                    else:
                        continue
            else:
                continue
    return "Yes"

def what_is_this_function(param1, param2):
    print(f"Set A = {param1}")
    print(f"Rel R = {param2}")
    print(Is_reflexive(param1, param2))
    print(Is_symmetric(param2))
    print(Is_transitive(param2))