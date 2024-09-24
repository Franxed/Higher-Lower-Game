# Import libraries.

import data     # Make sure data.py is available in the same folder.
import random

# Extract the list from data.py (same folder).
celebs = data.list


def main():
    print("_____________________________________________________________\n"
          "\nWelcome to the classic Higher or Lower game!\n"
          "_____________________________________________________________")


    count = 0
    while True:
        try:
            celeb_a = random.choice(celebs)
            celeb_b = random.choice(celebs)

            # Ensure no two celebrities have been selected.
            if celeb_a == celeb_b:
                celeb_b = random.choice(celebs)

            print(f"{celeb_a['name']} VS {celeb_b['name']}!\n"
                  f"\n{celeb_a['name']} has {celeb_a['follower_count']}M followers.\n")

            user = input(f"Do you think {celeb_b['name']}'s followers is higher or lower than "
                         f"{celeb_a['name']}'s followers?\n(Higher or Lower): ").lower()

            if user == "higher":
                if celeb_b['follower_count'] > celeb_a['follower_count']:
                    count += 1
                    print(f"Correct! {celeb_b['name']} has {celeb_b['follower_count']}M followers!\n"
                          f"Which is Higher!\n________________________________________________________________"
                          f"\nPoints : {count}")
                    celeb_a = celeb_b
                    continue

                else:
                    print(f"Sorry, {celeb_b['name']} has {celeb_b['follower_count']}M followers.\n"
                          f"The correct answer was lower!")
                    break

            elif user == "lower":
                if celeb_b['follower_count'] < celeb_a['follower_count']:
                    count += 1
                    print(f"Correct! {celeb_b['name']} has {celeb_b['follower_count']}M followers!\n"
                          f"Which is Lower!\n________________________________________________________________"
                          f"\nPoints : {count}")
                    celeb_a = celeb_b
                    continue

                else:
                    print(f"Sorry, {celeb_b['name']} has {celeb_b['follower_count']}M followers.\n"
                          f"The correct answer was higher!")
                    break

        except Exception as e:
            print(f"Invalid input. Please enter 'Higher' or 'Lower': {e}")

main()
