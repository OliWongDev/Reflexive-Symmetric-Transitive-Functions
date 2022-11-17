## PYTHON RELATIONS CHALLENGES (Reflexive, Transitive, Symmetrical)

## INTRO

As part of the discrete math exam revision, Coder Academy issued some optional Python challenges to consolidate our understanding of reflexive, symmetrical and transitive relations. The challenges were optional and had no offered solutions, so it was up to the students to a) attempt the challenges if they wanted to and b) figure it out on their own. 

With the logic of what each relation implies, I was able to create 3 functions that all meet the purpose criteria and return whether a relation is or is not reflexive/symmetrical/transitive.

## PURPOSE

I have decided to upload these functions to github to help other students or people who peruse by my github to understand how to work mathematical logic into a python function and assist with their studies, particularly if they are visual/doing learners like myself. Welcome!

## HOW TO USE

Down the bottom of the file, you will see a function called "what_is_this_function" which is a catch all for the parameters entered in. 

There are two parameters:

- "param1" allows you to define the domain of the set. This is to be a set of integers and is only relevant for the reflexive function to check if there are integers in the domain that have relations, but do not have their own reflexive relations. 

E.g if you enter in a set of {1, 2, 3, 4, 5} and the relations are {(1,1), (2, 4), (2, 2), (3, 3), (4, 10)}, the function is able to handle the '4' in the domain without calling true on '(4, 10)' 

- "param2" is the relations set which takes a set of tuples. Each codomain (first index in the tuple) must be from the domain ("param1") when entered manually. This conforms to mathematical logic where a relation's codomain is a subset of the domain. See here:

![Codomain image](/Codomain.png)

You can see that there are 4 dots (values) in the x section. That is the domain. 3 of them map to 3 relations in the codomain, and the y values of these particular parameters are shown outside this. 

For example, an acceptable "param2" would be:
```param1 = {1, 2, 3, 4}```
```param2 = {(1, 1), (2, 4), (3, 4), (4, 8)```

## REFLEXIVE FUNCTION

A relation is reflexive if all values used from the domain, are related to themselves in the relation. E.g (1, 1) uses itself, (2, 2) uses itself etc.

Please note that just because a value is in the domain, does not mean that the function is or is not reflexive. 

```param1 = {1, 2, 3, 4, 5}```
```param2 = {(1, 1), (2, 2), (3, 2), (3, 3), (4, 5)```

- The issue here is that 4 is used in the relation (4, 5), but it has no relation to itself (4, 4).
- The other thing to note is that '5' is in the domain, but because it is not accessed in the relation it is ignored to determine if it is reflexive or not.

### Python (Reflexive)

For the first part of the function I initialized an empty set "domain_integers" that would gather all integers that have a relation to themselves on the relation. This was done by iterating through the tuple indexs to see what matched. I used a set so that I could just add the first index of the tuple and not have duplicates. "domain_integers" therefore forms the set list of reflexive values e.g {1, 2, 3}

For the second part of the function I deducted these domain integers from the original set, to see what values are in the domain, but were not reflexive. As we talked about prior, this does not mean that a reflexive relation doesn't exist. But if they so dare to have a relation in "param2" this whole thing is busted. So I iterated through the relation again to find if there relations for these non-reflexive values. If it finds a relation, the function ends as the relation is not reflexive (return false)

For the third part, I check whether the domain integers are part of a subset to the original set. If they are, that means that all values contained are accounted for in the function and the function can be deemed reflexive (True)

## SYMMETRIC FUNCTION

A symmetric function occurs when all relations in the set have an inverse relation also in the set. E.g if there is '(4, 9)' there had better be a '(9, 4)' in that relation for it to be symmetric. 

A note is that we can basically ignore the domain for this one provided it's valid mathematically, we are only concerned about referring to the relations inside "param2".

```param2 = {(1, 2), (4, 5), (5, 4), (2, 1), (1, 5), (4, 4)}```

This relation is not symmetrical because '(1, 5)' does not have a cpusin '(5, 1)' inside the relation. As we also know, a set is unique so '(4, 4) does not need to be repeated twice for this to be symmetrical.

### Python (Symmetric)

The function only takes the relation "param2" as a parameter. We need to iterate through "param2" to split them up into tuples e.g "(1, 2)". 

From each tuple, we need to create an inverse tuple that will be checked to see if it is in the original set. I called this "new_tuple" and defined it as the tuple we used with the indexes switched. 

If the new tuple exists, we continue looping the function. We only need one to fail for it to not be symmetrical so a continue is appropriate here. We're also not returning any values from a successful symmetric relation.

If there isn't an inverse to one of our tuples, the return statement is brought out to end the function and declare the relation not symmetrical.

However, if we get to the end all okay our return message is "Yes" indicating that the relation is symmetric.

## TRANSITIVE FUNCTION

A relation is transitive if there is a shortcut from one relation value to another. Let's use an example.

I take a plane route from Paris ('1') to Berlin ('2'). This means the relation is (1, 2). 

I then take a plane from Berlin ('2') to London ('3'). This means the relation is (2, 3).

For a transitive relation to exist, we want to know if I can take a shortcut from Paris ('1') to London ('3'). If this plane route does exist, a transitive relation exists. If it doesn't we gotta layover for a bit to get there (not transitive).

If this does not work ONCE through all relations in our set, the relation is not transitive.

NOTES:
- A shortcut exists with (1, 2) --> (2, 1) on (1, 1). If we already are at 1, we can stay at 1. Why take an extra flight?

### Python (Transitive)

For the transitive function I first iterated through to get tuples again. I then iterated through to get another field of the same tuples to check tuple1 and tuple2 over.

If the second value of tuple1 '(1, 2)' was equivalent to the first in tuple2 '(2, 4)', it's possible we have a failure about to happen so we want to catch that. Anything else we do not need so we permit the loop to continue. 

Once we have gotten past this condition, we want to get another field of tuples to iterate over with the previous tuple1 and tuple2 case to see if it's truly busting our relation. For this next part, we need to know that if our tuple2 second value '(2, 4)' is equal to the tuple3 second value '(1, 4)'. If that is on, we can begin to analyse if we can get from tuple1 to tuple3. If it didn't meet that condition we keep looping through (continue).

For the next part I needed to make a new tuple that would encapsulate the first tuple1 value and the second tuple3 value ('1, 4'). This is a simulated test case to see if we can find the relation we need in the set. I defined this as 'new_tuple'. If new_tuple was not in the relations set, we could be assured that the relation overall is not transitive. We then get a return message indicating that the particular tuple relation that is not transitive.

Finally, the function returns a "yes" if the function goes through without finding the exception. This is to indicate in the parent function below that the relation is transitive.

## REVIEW

I really enjoyed this challenge and I think I needed the practice on loops/continues/tuples/nesting. Thankful.

This has got me keen to jump back on Hackerrank and give some of those pesky problems a go.

Any issues with the functions or if you know a different way they could be improved, let me know :)


