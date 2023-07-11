"""
This is a Rock Paper Scissors game vs COM
"""
import random 

RPS_OPTIONS = ["rock", "paper", "scissors"]

score = {
    "player": 0,
    "com": 0
}


def choose_weapon() -> str:
    while 1:
        weapon = input("Choose 'rock', 'paper' or 'scissors': ")
        if weapon not in ["rock", "paper", "scissors"]:
            print("\nPlease type your option correctly.\n")
            continue
        break

    return weapon


def get_winner(player: str, com: str, score: dict):
    if player == com:
        print("\nIt's a tie!")
        return score
    if player == "rock" and com == "scissors":
        print("\nYou win!")
        score["player"] += 1
        return score
    if player == "rock" and com == "paper":
        print("\nYou lose...")
        score["com"] += 1
        return score
    if player == "paper" and com == "rock":
        print("\nYou win!")
        score["player"] += 1
        return score
    if player == "paper" and com == "scissors":
        print("\nYou lose...")
        score["com"] += 1
        return score
    if player == "scissors" and com == "rock":
        print("\nYou lose...")
        score["com"] += 1
        return score
    if player == "scissors" and com == "paper":
        print("\nYou win!")
        score["player"] += 1
        return score
    return False


def rock_paper_scissors(weapon: str, score: dict):
    com_weapon = random.choice(RPS_OPTIONS)
    print(f"The COM chose: {com_weapon}!")
    get_winner(weapon, com_weapon, score)
    
    return None


def display_score(score: dict):
    print("")
    print("The total score is:")
    print("\tPlayer: ", score["player"])
    print("\tCOM: ", score["com"])


if __name__ == "__main__":
    print("Hello!", end=" ")
    print("This is the game of Rock Paper Scissors.")
    print("\n---You are playing vs COM---")
    while 1:
        cmd = input("\nEnter any key to continue... (q to quit) >")
        if cmd == 'q': break
        print("")
        weapon = choose_weapon()
        print(f"\nYour weapon of choice is: {weapon}!")
        rock_paper_scissors(weapon, score)
        display_score(score)