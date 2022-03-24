"""
Create a function that concatenates the number 7 to the end of every chord in a list. If a chord already ends with a 7, do not add another 7.

Examples:

    solution(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]
    solution(["G", "F7", "C"]) ➞ ["G7", "F7", "C7"]
    solution(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]
    solution(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
    solution([]) ➞ []

Notes:

    Return an empty list if the given list is empty.
    You can expect all the tests to have valid chords.

    [execution time limit] 4 seconds (py3)

    [input] array.string chords

    [output] array.string


https://app.codesignal.com/solutions/SMZA6zxLifvgK8kES?accessToken=riSN79DwWmRmwFk5H-oSMFqzhcyL2ZqgZPNFLE9xwZ


"""


def solution(chords):
    my_list = []
    
    if  len(chords) == 0:
        return []
        
    for chord in range(len(chords)):
        if not chords[chord].endswith("7"):
            result = chords[chord]
            my_list.append(result + "7")
            print(chords[chord])
            
        elif chords[chord].endswith("7"):
            result = chords[chord]
            my_list.append(result)
            
    
    return my_list  
    print(my_list)
