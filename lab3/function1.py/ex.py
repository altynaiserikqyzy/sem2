# Import functions from tasks
from task_8 import spy_game
from task_4 import filter_prime
from task_2 import centigrade_temperature
from task_13 import guess_the_number
from task_11 import palimdrom

def main():
    # Use the imported functions

    # Test spy_game function
    nums = [0, 0, 7, 1, 2, 3]
    print(f"spy_game({nums}): {spy_game(nums)}")

    # Test filter_prime function
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"filter_prime({numbers}): {filter_prime(numbers)}")

    # Test centigrade_temperature function
    fahrenheit = 100
    print(f"centigrade_temperature({fahrenheit}): {centigrade_temperature(fahrenheit)}")

    # Test palimdrom function
    string = "A man a plan a canal Panama"
    print(f"palimdrom('{string}'): {palimdrom(string)}")

    # Test guess_the_number function
    # Note: This function requires user interaction, so it's commented out here
    # guess_the_number()

if __name__ == "__main__":
    main()
