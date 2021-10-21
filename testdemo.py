from Question import Question
import random

question_prompts = [
"All I ask in return is that you ______ to me.\n(a) have been listening\n(b) listen\n(c) are listening\n(d) have listened\n\n",
"Sue is allergic  ______ peanuts.\n(a) to\n(b) for\n(c) with\n(d) in\n\n",
"Bob decided to buy 50  ______ to add to his ranch.\n(a) ox\n(b) oxies\n(c) oxes\n(d) oxen\n\n",
"I  ______ book you might like.\n(a) came up with\n(b) came out\n(c) came across\n(d) came along\n\n",
"Have you been  in contact  ____ your old school mates?\n(a) with\n(b) in\n(c) of\n(d) about\n\n",
"I  _________  my therapist next week.\n(a) have seen\n(b) am seeing\n(c) saw\n(d) see\n\n",
"Brooke  _________ on my nerves!\n(a) gets always\n(b) had got\n(c) always is getting\n(d) is always getting\n\n",
"The questions were  _______ easy!\n(a) such\n(b) a very so\n(c) so very\n(d) such a\n\n",
"We  _______ the fence _______ tomorrow.\n(a) are … painting\n(b) are having … painted\n(c) had … had\n(d) are having … paint\n\n",
"I wish you  _______ making assumptions about me!\n(a) would stop\n(b) stop\n(c) will stop\n(d) have had stopped\n\n",
"If we are going to expand, we will need to find an___ to back up our project.\n(a) investor\n(b) investment\n(c) invested\n(d) invester\n\n",
"Her children are two adorable  ________ girls.\n(a) six years old\n(b) six years of age\n(c) six-years-old\n(d) six-year-old\n\n",
"You  _______ put this much salt in the pot!\n(a) ought not\n(b) ought to not\n(c) ought not to\n(d) oughtn't to\n\n",
"Snow _____ the ball to Ingman, and he scores!\n(a) a) has passed\n(b) b) passed\n(c) is passing\n(d) passes\n\n",
"The boat _____ in 2 hours! Hurry!\n(a) leaves\n(b) is leaving\n(c) will leave\n(d) has left\n\n",
"He very rarely _____ swimming during the winter.\n(a) doesn't go\n(b) is\n(c) goes\n(d) is going\n\n",
"I _____ how to fix the washig machine. Will you take a look at it for me?\n(a) didn't know\n(b) don't know\n(c) know\n(d) knew\n\n",
"I _____ you are trying very hard. Well done!\n(a) saw\n(b) am seeing\n(c) see\n(d) have saw\n\n",
"Claire absolutely _____ rock music.\n(a) will adore\n(b) adore\n(c) is adoring\n(d) adores\n\n",
"_____ you _____ some time to help me with my homework?\n(a) Have .... had\n(b) Are ....having\n(c) Did....have\n(d) Have...got\n\n",
"This soup _____ bland at all.\n(a) doesn't taste\n(b) tasted\n(c) has tasted\n(d) tasting\n\n",
"_____ the Browns _____ a house in the countryside?\n(a) Don't...own\n(b) Are...own\n(c) Did...owned\n(d) Are...owning\n\n",
"Sandra _____ her make-up every morning.\n(a) is doing\n(b) does\n(c) has done\n(d) had done\n\n",
"Jack _____ his keys at home!\n(a) forgets\n(b) is constantly forgetting\n(c) is going to forget\n(d) will have forgotten\n\n",
"We _____ at my uncle's for the time being.\n(a) stay\n(b) stayed\n(c) are staying\n(d) have stayed\n\n",
"Nowdays, people _____ much more efficiently.\n(a) are being examined\n(b) are examining\n(c) will be examining\n(d) will have been examined\n\n",
"Our firm _____ a big project.\n(a) undertakes current\n(b) currently is undertaking\n(c) currently undertakes\n(d) is currently undertaking\n\n",
"I can't come to the meeting as I _____ my doctor this afternoon.\n(a) am seeing\n(b) see\n(c) will have seen\n(d) am not seeing\n\n",
"I _____ a bit under the weather today. I think I'll stay home.\n(a) felt\n(b) had been feeling\n(c) am feeling\n(d) will have felt\n\n",
"Could you pick up the phone? I _____ a shower!\n(a) have been taking\n(b) could be taken\n(c) am taking\n(d) will take\n\n",
"While I was walking in the forest, I _____ a strange sound coming from afar.\n(a) hear\n(b) was hearing\n(c) heard\n(d) had heard\n\n",
"Rembrandt _____ famous after his death.\n(a) will become\n(b) become\n(c) had become\n(d) became\n\n",
"Last night I _____ the strangest of dreams.\n(a) had had\n(b) had\n(c) have had\n(d) was having\n\n",
"The CEO _____ of the Board's decision this morning.\n(a) was informed\n(b) informed\n(c) had informed\n(d) was informing\n\n",
"The young couple, madly in love, got into their car and _____ into the sunset.\n(a) set of\n(b) will set of\n(c) setted off\n(d) set off\n\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "d"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "d"),
    Question(question_prompts[7], "c"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "a"),
    Question(question_prompts[10], "a"),
    Question(question_prompts[11], "d"),
    Question(question_prompts[12], "c"),
    Question(question_prompts[13], "d"),
    Question(question_prompts[14], "a"),
    Question(question_prompts[15], "c"),
    Question(question_prompts[16], "b"),
    Question(question_prompts[17], "c"),
    Question(question_prompts[18], "d"),
    Question(question_prompts[19], "d"),
    Question(question_prompts[20], "a"),
    Question(question_prompts[21], "a"),
    Question(question_prompts[22], "b"),
    Question(question_prompts[23], "b"),
    Question(question_prompts[24], "c"),
    Question(question_prompts[25], "a"),
    Question(question_prompts[26], "d"),
    Question(question_prompts[27], "a"),
    Question(question_prompts[28], "c"),
    Question(question_prompts[29], "c"),
    Question(question_prompts[30], "c"),
    Question(question_prompts[31], "d"),
    Question(question_prompts[32], "b"),
    Question(question_prompts[33], "a"),
    Question(question_prompts[34], "d")
]

random.shuffle(questions)

def run_test(questions):
    score = 0

    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    if score >= 32:
        print("Well Done! Your grade is A")
    elif score >= 29:
        print("Good job! Your grade is B")
    elif score >= 23:
        print("Your grade is C")
    else:
        print("Sorry! You have failed the test.")


run_test(questions)

