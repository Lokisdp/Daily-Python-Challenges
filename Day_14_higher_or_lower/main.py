from game_data import data
import random
import art
# count_one = 0
print(art.logo)
def compare():
    game = True
    count = 0
    two = random.randint(0, 49)
    while game:
        one = two
        two = random.randint(0,49)
        if one == two:
            two = random.randint(0,49)

        new_dic = {}
        print(f"Compare A: {data[one]["name"]},{data[one]["description"]}, {data[one]["country"]}")
        print(art.vs)
        print(f"Against B: {data[two]["name"]},{data[two]["description"]}, {data[two]["country"]}")
        # ask_user = input("who has more followers? Type 'A' or 'B': ").lower()

        # print(data[one]["follower_count"])
        # print(data[two]["follower_count"])
        count_one = data[one]["follower_count"]
        count_two = data[two]["follower_count"]
        # print(count_one)
        # print(count_two)
        new_dic["a"] = count_one
        new_dic["b"] = count_two
        res = max(new_dic, key=new_dic.get)
        ask_user = input("who has more followers? Type 'A' or 'B': ").lower()
        print("\n" *25)
        print(art.logo)
        if res == ask_user:
            count += 1
            # rad_two = random.randint(0, 49)
            print(f"Score: {count}")
        else:
            two = random.randint(0, 49)
            print("Sorry That's Wrong!! Game over.")
            print(f"Final Score: {count}")
            game = False

# compare(rad_one, rad_two)


compare()




# def higher_or_lower(ans):
#     count = 0
#     game = True
#     # compare(rad_one, rad_two)
#     while game:
#         compare(rad_one,rad_two)
#         ask_user = input("who has more followers? Type 'A' or 'B': ").lower()
#         if ans == ask_user:
#             count += 1
#             print(f"Score: {count}")
#         else:
#             print("Game over.")
#             print(f"Score: {count}")
#             game = False
#
# # result = compare(rad_one,rad_two)
# higher_or_lower(compare(rad_one,rad_two))
