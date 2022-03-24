"""
Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the array, return -1.

Examples:

    solution(["Jimmy", "Layla", "Bob"]) ➞ 2
    solution(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0
    solution(["Jimmy", "Layla", "James"]) ➞ -1

Notes:

    Assume all names start with a capital letter and are lowercase thereafter (i.e. don't worry about finding "BOB" or "bob").

    [execution time limit] 4 seconds (py3)

    [input] array.string names

    [output] integer

https://app.codesignal.com/solutions/mwnw5B6ecb4wDLwSP?accessToken=riSN79DwWmRmwFk5H-oSMFqzhcyL2ZqgZPNFLE9xwZ

"""

def solution(names):

    for name in range(len(names)):
        if names[name] == "Bob":
            return name
        
    return -1