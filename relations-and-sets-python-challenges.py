# Edit these to configure your set and relation.
param1 = {1, 2, 3, 4, 5}
param2 = {(1, 2), (2, 3), (1, 3), (2, 2)}






def Is_reflexive(set1, set2):
# Checks if a relation is reflexive
    # Empty set to catch integers used in relation
    domain_integers = set()
    # Iterating through the tuples of the relations
    for tuple in set2:
        # If the tuple is reflexive we add it to the domain set.
        if tuple[0] == tuple[1]:
            domain_integers.add(tuple[0])
    
    # Defining the integers that were not reflexive in the above iteration.
    reflexive_test_integers = set1 - domain_integers
    # Iterate by each of these found values, through tuples in set2
    for integer in reflexive_test_integers:
        for tuple in set2:
            # Did we find any relations on these non-reflexive integers? If not we push on.
            if integer == tuple[0]:
                return f"Is R reflexive? No, '{integer}' in the domain has a relation but not to itself."

    # We can infer that if domain integers is a subset of our set1 after catching all other cases, we can say it is reflexive.
    if domain_integers.issubset(set1):
        return "Yes"
    



def Is_symmetric(set2):
    # Iterating to go through each tuple's elements
    for tuple in set2:
        # Defining a new tuple that is the inverse of the tuple we are using to iterate with.
        new_tuple = (tuple[1], tuple[0])
        # If the new tuple is in our set, then we know it is symmetric so we can continue.
        if new_tuple in set2:
            continue
        # If we don't find the tuple we're looking for, it's not symmetrical.
        else:
            return f"Is R symmetric? No, {tuple} not symmetrical"
    # Returning yes to print that it is symmetrical.
    return "Yes"




def Is_transitive(set2):
    # Iterating two tuples to find cases where the values connect to each other.
    for tuple1 in set2:
        for tuple2 in set2:
            if tuple1[1] == tuple2[0]:
                # If that's all good, we can get into our 3rd tuple. We check here that the value of tuple2 can map to the same endpoint as tuple3.
                for tuple3 in set2:
                    if tuple2[1] == tuple3[1]:
                        # If it does, we define a new simulated tuple to test over our relation. We want to go from Point A to Point C directly.
                        new_tuple = (tuple1[0], tuple3[1])
                        # If we don't find it, we can finally say it's not transitive.
                        if new_tuple not in set2:
                            return f"Is R transitive? No, you cannot get from {tuple1[0]} to {tuple3[0]} with a shortcut."
                    # Else continue used to reset the iterator to the next tuple3 case if it was found in there.
                    else:
                        continue
            # Else continue used to reset the iterator to the next tuple1 and tuple2 match case if it was not found in there.
            else:
                continue
    # Yes statement to show that it is true.
    return "Is R transitive? Yes"

# Catch all function to show the entire solution. Call this at the top!
def what_is_this_function(param1, param2):
    print(f"Set A = {param1}")
    print(f"Rel R = {param2}")
    print(Is_reflexive(param1, param2))
    print(Is_symmetric(param2))
    print(Is_transitive(param2))

# Executing the big function to display all the results.
what_is_this_function(param1, param2)