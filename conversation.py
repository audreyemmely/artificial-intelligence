import os
import aiml

BRAIN_FILE = "brain.dump"

k = aiml.Kernel()

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
else:
    k.bootstrap(learnFiles="learningFileList.aiml", commands="LEARN AIML")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)

    while True:
        input_text = input("USER > ")
        response = k.respond(input_text)
        print("BOT > ", response)


'''
k = aiml.Kernel()
k.learn("learningFileList.aiml")
k.respond("LEARN AIML")

while True:
    reply = k.respond(input("User > "))
    if reply:
        print("Bot > ", reply)
    else:
        print("Bot > :", )
'''