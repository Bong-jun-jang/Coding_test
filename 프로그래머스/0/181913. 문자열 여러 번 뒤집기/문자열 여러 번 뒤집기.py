def solution(my_string, queries):
    
    for i in queries:
        start, end = i[0], i[1]+1
        org = my_string[start:end]
        res = org[::-1]
        my_string = my_string[:start] + res + my_string[end:]
    
    return my_string