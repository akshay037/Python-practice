from Question import Question

question_prompts = [
    "what color are apple? \n(a)red \n(b)Purple \n(c)Blue \n(d)Yellow\n",
    "What color are Banana? \n(a)red\n(b)Purple\n(c)Blue \n(d)Yellow\n",
    "What color are strawberries? \n(a)Yellow \n(b)red \n(c)Purple \n(d)Blue\n"
    #"Whicn typr of programming does python supports? \n(a)object-oriented programming \n(b) structured programming \n(c) functional programming \n(d) all of the mentioned\n"
    #"What will be the value of the following Python expression? \n(a) 4 \n(b) 2 \n(c) 7 \n(d)1\n"
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"d"),
    Question(question_prompts[2],"b"),
    #Question(question_prompts[3],"d"),
    #Question(question_prompts[4],"c")  
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got" + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)