""" Edit the function below to implement the String Calculator TDD Kata """

def add(numbers):
    if numbers == "":
        return 0
    if "," in numbers:
        nums = numbers.split(",")
        return str(int(nums[0]) + int(nums[1]))
    return numbers
