class GuessingGame():

    def __init__(self,answer,answer_number=0):
        self.answer_number = answer_number
        self.answer = answer

    def guess(self,user_guess,answer_number=0):
        user_guess=int(user_guess)
        answer_number += 1
        # self.user_guess = user_guess
        if user_guess > self.answer:
            # answer_number += 1
            print('high')
    
        if user_guess == self.answer:
            print("correct!")

        if user_guess < self.answer:
            # answer_number += 1
            print("low")
        return self.answer_number
    
    def solved(self,user_guess):
        user_guess = int(user_guess)
        if user_guess == self.answer:
            return True
            # print("Congratulations!")
        else:
            return False
            # print("try it again!")
            # new_guess= input("guess another number: ")
            # self.guess(new_guess)
            # self.solved(new_guess)
    



game=GuessingGame(10)
# user_guess= input("guess a number: ")
# game.guess(user_guess)
# print(game.solved(user_guess))

# game.guess(5)  # => 'low'
# game.guess(20) # => 'high'
# print(game.solved(user_guess) )  # => False

game.guess(10) # => 'correct'
print(game.solved(10))




