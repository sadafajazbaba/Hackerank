if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    curr_max = -120
    second_max = -125
    
    for val in arr:
        if val > curr_max:
            second_max = curr_max
            curr_max = val
        
        if val > second_max and val != curr_max:
            second_max = val
    
    print(second_max)