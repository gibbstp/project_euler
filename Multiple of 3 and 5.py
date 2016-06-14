def multiples():
    i = 1
    nums = []
    while i < 1000:
        if i%3 == 0 and i%5 == 0:
            nums.append(i)
        i += 1
    print(sum(nums))
multiples()