import guess_riddle_module

riddles = ["What is the capital of France?", "What is the largest planet in our solar system?"]
answers = ["Paris", "Jupiter"]
num_attempts = 3
if __name__ == '__main__':
    riddle_dict = guess_riddle_module.guess_riddle(riddles, answers, num_attempts)
    print("Riddle dictionary:", riddle_dict)
