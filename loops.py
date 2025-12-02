#loops...
#for loop..
game_sample = ["football", "basketball", "tennis", "cricket"]
for game in game_sample:
    print(f"I love playing {game}.")

# #for loop with range..
# n = int(input("Enter the number : "))
# for i in range(n, 10*n + n, n):
#     print(i)

# #while loop..
# key = 5
# while key != -1:
#     print("COUNTDOWN : ", key)
#     key -= 1    #key = key - 1
# print("LAUNCH !!!")

# #use of break function in loops..
# list_sam = [12, 23, 99, 76, 54, 45]
# search = int(input("Enter the item to be searched : "))
# for sam in list_sam:
#     print("Checking : ", sam)
#     if search == sam:
#         print("Item found ")
#         break
#     else: 
#         print("Item not found ")
# print("Loop Ended")

# #use of continue in loops.. 
# print("Even numbers from 1 to 10")
# for i in range(1,11):
#     if i % 2 != 0:
#         continue
#     print("Even Numbers : ", i)
