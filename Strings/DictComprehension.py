num = [1,2,3,4,5,6,7,8,9]

sq = {nums : nums*nums for nums in num}
print(sq)

books = [["python for beginner",500],["black book java",600],["C#",800]]
title_length = { item[0]:len(item[0]) for item in books }
print(title_length)