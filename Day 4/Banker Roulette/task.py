friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random
# CODE 1
# who_will_pay=random.randint(0,4)
# if who_will_pay==0:
#     print("Alice will pay")
# if who_will_pay==1:
#     print("Bob will pay")
# if who_will_pay==2:
#     print("Charlie will pay")
# if who_will_pay==3:
#     print("David will pay")
# if who_will_pay==4:
#     print("Emanuel will pay")
# CODE 2
# random.choice(friends)
# print(random.choice(friends)+" will pay")
random_index = random.randint(0,4)
print(friends[random_index] + " will pay")