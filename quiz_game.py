print("welcome to  General Knowledge Quiz game")
print("---------------------------------------")

score = 0

print("1. What is the capital of India?")
print("A. Delhi")
print("B. Mumbai")
print("C. kolkatta")
print("D. Banglore")

answer = input("Enter your answer (A/B/C/D):").upper()

if answer == "A":
    print("Correct Answer")
    score = score + 1
else:
    print("Wrong Answer")


print("2. which language is used for web-development?")
print("A. Python")
print("B. HTML")
print("C. Java")
print("D. C++")

answer = input("Enter your answer (A/B/C/D)").upper()

if answer == "B":
    print("Correct Answer")
    score = score + 1
else:
    print("Wrong Answer")


print("3. which is the National Animal of India?")
print("A. Tiger")
print("B. Lion")
print("C. Cat")
print("D. Leopard")

answer = input("Enter your answer (A/B/C/D)").upper()

if answer == "A":
    print("Correct Answer")
    score = score + 1
else:
    print("Wrong Answer")


print("4. Who Invented Bulb?")
print("A. Sir C.V.Raman")
print("B. Albert Einstein")
print("C. Thomas Edision")
print("D. Issac Newton")

answer = input("Enter your answer (A/B/C/D)").upper()

if answer == "C":
    print("Correct Answer")
    score = score + 1
else:
    print("Wrong Answer")


print("5. Which is The Largest River in The World?")
print("A. Amazon")
print("B. Yangtza")
print("C. Mississippi-Missouri")
print("D. Nile")

answer = input("Enter your answer (A/B/C/D)").upper()

if answer == "D":
    print("Correct Answer")
    score = score + 1
else:
    print("Wrong Answer")


print("Your Final Score is:",score)