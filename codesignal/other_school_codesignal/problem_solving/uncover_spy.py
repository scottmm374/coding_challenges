"""
In a city-state of n people, there is a rumor going around that one of the n people is a spy for the neighboring city-state.

The spy, if it exists:

    Does not trust anyone else.
    Is trusted by everyone else (he's good at his job).
    Works alone; there are no other spies in the city-state.

You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact that person a trusts person b.

If the spy exists and can be found, return their identifier. Otherwise, return -1.

Example 1:

Input: n = 2, trust = [[1, 2]]
Output: 2
Explanation: Person 1 trusts Person 2, but Person 2 does not trust Person 1, so Person 2 is the spy.

Example 2:

Input: n = 3, trust = [[1, 3], [2, 3]]
Output: 3
Explanation: Person 1 trusts Person 3, and Person 2 trusts Person 3, but Person 3 does not trust either Person 1 or Person 2. Thus, Person 3 is the spy.

Example 3:

Input: n = 3, trust = [[1, 3], [2, 3], [3, 1]]
Output: -1
Explanation: Person 1 trusts Person 3, Person 2 trusts Person 3, and Person 3 trusts Person 1. Since everyone trusts at least one other person, there is no spy.

Example 4:

Input: n = 3, trust = [[1, 2], [2, 3]]
Output: -1
Explanation: Person 1 trusts Person 2, and Person 2 trusts Person 3. However, in this situation, we don't have any one person who is trusted by everyone else. So we can't determine who the spy is in this case.

Example 5:

Input: n = 4, trust = [[1, 3],[1, 4],[2, 3],[2, 4],[4, 3]]
Output: 3
Explanation: Person 1 trusts Person 3 and Person 4, Person 2 trusts Person 3 and Person 4, Person 4 trusts Person 3. Everyone trusts Person 3 but Person 3 does not trust anyone, so they are the spy.

    [execution time limit] 4 seconds (py3)

    [input] integer n

    The number of people in the city-state

    [input] array.array.integer trust

    Array of pairs indicating who each person in trusts.

    [output] integer

    The identifier of the spy.


"""

def solution(n, trust):
    # spy must show up in all trust[0][1] but never: trust[0][0]
    
    find_the_spy = {}
    trusted_people = set()
    
    for person in range(len(trust)):
        
        trusted_people.add(trust[person][0])
        
        if trust[person][1] not in find_the_spy:
            find_the_spy[trust[person][1]] = 1
            
        else:
            find_the_spy[trust[person][1]] += 1     
            
    for key, value in find_the_spy.items():
        
        if value == (n-1) and key not in trusted_people:
            
            return key
        
    return -1   
        