from game_data import data
from gameart import logo
from gameart import vs
import random

def get_random_account():
    return random.choice(data)
def format_data(account):
    name= account["name"]
    description= account["description"]
    country= account["country"]
    return f"{name} a {description} from {country}"
def check_answer():
    if a_follower_count>b_follower_count:
        return user_answer=="a"
    else:
        return user_answer=="b"


print(logo)
score=0
should_continue= True
while should_continue:
    account_a = get_random_account()
    compare_a= format_data(account_a)
    print(f"Compare A: {compare_a}")

    print(vs)
    account_b = get_random_account()
    compare_b= format_data(account_b)
    print(f"Compare B: {compare_b}")
    user_answer= input("\nWho has more followers? Type A or B ").lower()

    a_follower_count= account_a["follower_count"]
    b_follower_count= account_b["follower_count"]
    is_correct= check_answer()

    if is_correct:
        score+=1
        print(f"You're right! Current Score:{score}")
    else:
        should_continue = False
        print(f"Sorry that's wrong. Final Score:{score}")




