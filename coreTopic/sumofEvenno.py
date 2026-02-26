def solve():
    n = int(input())
    numbers = list(map(int, input().split()))
    
    even_sum = 0
    
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    
    print(even_sum)


if __name__ == "__main__":
    solve()



    # optimized code using list comprehension
#     def solve():
#     n = int(input())
#     numbers = list(map(int, input().split()))
    
#     even_sum = sum(num for num in numbers if num % 2 == 0)
    
#     print(even_sum)


# if __name__ == "__main__":
#     solve()