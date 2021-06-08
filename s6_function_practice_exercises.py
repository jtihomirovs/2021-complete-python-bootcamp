# 1 - LESSER OF TWO EVENS
def lesser_of_two_evens(a, b):
    # check if both are even
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else:
            return b
    # else - one or both numbers are odd
    else:
        if a > b:
            return a
        else:
            return b


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(1, 4))


# 2 - simpplified logic - use min() and max()
def lesser_of_two_evens_v2(a, b):
    # check if both are even
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    # else - one or both numbers are odd
    else:
        return max(a, b)


print(lesser_of_two_evens_v2(2, 4))
print(lesser_of_two_evens_v2(1, 4))


# 3 - ANIMAL CRACKERS
def animal_crackers(txt):
    word_list = txt.split()
    if len(word_list) == 2:
        if word_list[0][0].lower() == word_list[1][0].lower():
            return True
        else:
            return False
    else:
        print("Not two words!")


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))


# 4 - MAKES TWENTY
def makes_twenty(n1, n2):
    if n1 + n2 == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False


print(makes_twenty(20, 10))
print(makes_twenty(2, 3))


# 5 - OLD MACDONALD
def old_macdonald(name):
    name_list = list(name)
    name_list[0] = name_list[0].upper()
    name_list[3] = name_list[3].upper()
    return "".join(name_list)


print(old_macdonald('macdonald'))


# 6 - Not creating a list - just split word into 2 parts and capitalize first letters of these 2 words
def old_macdonald_v2(name):
    first_half = name[:3]
    second_half = name[3:]

    return first_half.capitalize() + second_half.capitalize()


print(old_macdonald_v2('macdonald'))


# 7 - MASTER YODA


def master_yoda(s):
    r = s.split(' ')
    r.reverse()
    result = ' '.join(r)
    return result


print(master_yoda('I am home'))
print(master_yoda('We are ready'))

# 8 - ALMOST THERE
print('Almost there')


def almost_there(n):
    if ((n >= 100 - 10) and (n <= 100 + 10)) or ((n >= 200 - 10) and (n <= 200 + 10)):
        return True
    else:
        return False


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

# 9 - FIND 33
print('Find 33')


def has_33(nums):
    for num in nums:
        try:
            if nums[num] == nums[num + 1]:
                return True
            else:
                return False
        except:
            pass


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

print('Find 33 v2')


# 10 - No try and except logic, just create range from 0 till -1 element. Because no need to check last element.


def has_33_v2(nums):
    for num in range(0, len(nums) - 1):
        if nums[num] == nums[num + 1]:
            return True
        else:
            return False


# 11 - PAPER DOLL
def paper_doll(text):
    outstr = ''
    for char in text:
        outstr = outstr + char + char + char
    return outstr


def paper_doll_v2(text):
    outstr = ''
    for char in text:
        outstr += char * 3
    return outstr


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))


# 12 - BLACKJACK
def blackjack(a, b, c):
    x = 0
    sum = a + b + c
    if sum <= 21:
        return sum
    if sum > 21 and (a == 11 or b == 11 or c == 11):
        sum = sum - 10
        if sum > 21:
            return 'BUST'
        else:
            return sum
    else:
        return 'BUST'


def blackjack_v2(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in [a, b, c] and sum([a, b, c]) - 10 <= 21:
        return sum([a, b, c]) - 10
    else:
        return 'BUST'


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))

# 13 - SUMMER OF '69

print('SUMMER OF 69')


def summer_69(arr):
    total = 0
    for i in range(len(arr)):
        if arr[i] == 6 or arr[i] == 7 or arr[i] == 8 or arr[i] == 9:
            pass
        else:
            total = total + arr[i]
    return total


def summer_69_v2(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break  # break from while loop. Bring back to for loop
            else:
                add = False  # and now i am waiting for the 9 - algorithm goes to while no section
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

print("Some test cases:")


def test(arr):
    for item in arr:
        print(item)


test([9, 2, 7])


def test2(arr):
    for i in range(len(arr)):
        print(arr[i - 1])


test2([9, 2, 7])


# 14 - spy game
def spy_game(nums):
    st1 = ''.join(str(e) for e in nums)
    if '007' in st1:
        return True
    else:
        return False


def spy_game_v2(nums):
    # create a mask - we will need this for comparison
    code = [0, 0, 7, 'x']
    # [0,7,'x']
    # [7,'x']
    # ['x'] - that means length = 1
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# 15 - COUNT PRIMES
print('COUNT PRIMES')


def count_primes(nums):
    count = 0
    for num in range(2, nums):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            count = count + 1
    return count


print(count_primes(100))
