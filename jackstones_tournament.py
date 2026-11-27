import time
score = []
for i in range(1,6):
    s = int(input(f"Enter score {i}: "))
    while s < 0 or s > 10:
        print("Enter a score from 1-10")
        s = int(input(f"Enter score {i}: "))
    score.append(s)

backup = score.copy()
print("BACKUP SAVED SUCCESSFULLY")

thing = True
while thing:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(f"Current score: {score}")

    elif choice == 2:
        s_add = int(input("Enter a score you want to add (1-10): "))
        while s_add < 0 or s_add > 10:
            print("Bad boy. Try again(only scores 1-10 will be accepted).")
            s_add = int(input("Enter a score you want to add (1-10): "))
        score.append(s_add)
        print(f"Updated score: {score}")

    elif choice == 3:
        index_add = int(input("Which index would you like to add a score to? "))
        while index_add not in score:
            print("Index not found, enter a score that exists in the list")
        score_add = int(input("Enter a score you want to add (1-10): "))
        while score_add < 0 or score_add > 10:
            print("Bad boy. Try again(only scores 1-10 will be accepted).")
            score_add = int(input("Enter a score you want to add (1-10): "))
        score.index(index_add, score_add)
        print(f"Updated score: {score}")

    elif choice == 4:
        score_remove = int(input("Which score would you like to remove? (Note that only its first instance will be removed):"))
        while score_remove not in score:
            print("Score not found, enter a score that exists in the list")
            score_remove = int(input("Which score would you like to remove?: "))
        score.remove(score_remove)
        print(f"Updated score: {score}")

    elif choice == 5:
        score.pop()
        print("Last score popped successfully")
        print(f"Updated score: {score}")

    elif choice == 6:
        s_score = int(input("What score would you like to search for?: "))
        while s_score not in score:
            print("Invalid score.")
            s_score = int(input("What score would you like to search for?: "))
        count = score.count(s_score)
        index = score.index(s_score)
        print(s_score)
        print(f"First index: {index}")
        print(f"Instances: {count}")

    elif choice == 7:
        print("===== SCORE STATISTICS =====")
        print(f"Current scores: {score}")
        print(f"Number of scores: {len(score)}")
        print(f"Total scores: {sum(score)}")
        print(f"Average scores: {sum(score)/len(score)}")
        print(f"Highest score: {max(score)}")
        print(f"Lowest score: {min(score)}")

    elif choice == 8:
        order = int(input("Which method would you like to sort by?(1 = ascending, 2 = descending): "))
        while order not in [1, 2]:
            order = int(input("Please enter a valid number: "))
        if order == 1:
            print(f"Ascending order: {sorted(score)}")
        elif order == 2:
            print(f"Descending order: {sorted(score, reverse=True)}")

    elif choice == 9:
        print("Reversing scores...")
        print("Scores reversed. Current Scores:")
        print(score.reverse())

    elif choice == 10:
        print("Scores cleared.")
        score.clear()
        print(f"Current scores: {score}")

    elif choice == 11:
        score = backup.copy()
        print("Scores recovered successfully.")

    elif choice == 12:
        cities = 0
        for h in range(3):
            city = input("Do you love the city that you live in? (yes/no): ").lower()
            if city == "yes":
                cities += 1
            elif city == "no":
                cities -= 1

        if cities == 3:
            time.sleep(5)
            print("Ending 1")
            time.sleep(5)
            print("Youve chosen wrong.")
            time.sleep(5)
            print("Initiating crash sequence.")
            while thing:
                print("Stupid")

        if cities == -3:
            print("True Ending")
            print("Ur free")
            thing = False

        else:
            print("Ending 2")
            while thing:
                input("Ur stuck here forever hahahaha")




