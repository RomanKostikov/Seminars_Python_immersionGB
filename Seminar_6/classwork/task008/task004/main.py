import guess_riddle_module

riddle = "City in France?"
answers = ["Paris", "Lyon", "Marseille"]
num_attempts = 3
if __name__ == '__main__':
    result = guess_riddle_module.guess_riddle(riddle, answers, num_attempts)
    print("The riddle was guessed in attempt", result)
