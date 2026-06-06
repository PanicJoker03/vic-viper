# vic viper v1.0.2
import time

# remember: study is more efficient when there's
# interest in the topic we are studying
print("Hello world")

print("Enumerate academic tasks:")

tasks = ["", "", ""]

a = 0
while a < 3:
    tasks[a] = input("Tell me which: ")
    a = a + 1
    
print("Which one is mandatory?")

mandatory_task = input()

print("Your answer is")
print(mandatory_task)

print("")
print(f"Ok, focus only on {mandatory_task}, accordingly, no traps!")

while 1:
    time.sleep(1)
    print(f"Ok, focus only on {mandatory_task}, accordingly, no traps!")

