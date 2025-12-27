def ai_study_agent(topic, subject,level="simple"):
    return f"{topic} in {subject} can be understood at a {level} level  it explains hwo things works step by step "





# Load memory
try:
    with open("memory.txt", "r") as file:
        past_memory = file.read()
except:
    past_memory = ""
# yurrrrrrrr education tutor agent is hereeeeeeeeeee


print("Welcome to Ai study agent ")
name=input("What is your name? ")
print(f"Hello, {name}! Let's study together." )

subject=input("What subject would you like to study ? ")
topic=input("which topic in "+subject+" do you want to focus on? ")

print("\n study session started")
print(f"subject: {subject}")
print(f"topic: {topic}")    

print("\n I will explain the topic and ask you some questions to test your understanding.")

print(f"\nExplanation of:")
print(f"{topic} is an important concept in {subject}. .")
print("i will explain it in simple words so you can easily understand it.     ")

understanding=input("\n did you understand thus explanation? (yes/no) ")

if understanding.lower() == "yes":
    print("Great! Let's move on forward.")
else:
    print("No worries! Let's go over it again.")
    print(f"{topic} helps us understand how things work in {subject}.")
    print("\n📝 Quick Test Time")

answer1 = input(f"Q1: Write one thing you learned about {topic}: ")

if answer1.strip() == "":
    print("❌ You didn’t answer. We need revision.")
    needs_revision = True
else:
    print("✅ Good attempt!")
    needs_revision = False


answer2 = input(f"\nQ2: Why is {topic} important in {subject}? ")

if answer2.strip() == "":
    print("❌ Weak answer detected.")
    needs_revision = True
else:
    print("👍 Nice explanation!")


if needs_revision:
    print("\n🔁 Revision Mode Activated")
    print(f"Let’s revise {topic} again more simply.")
else:
    print("\n🎉 Great! You understand the topic well.")

if needs_revision:
    with open("memory.txt", "a") as file:
        file.write(f"Weak topic: {topic} in {subject}\n")
