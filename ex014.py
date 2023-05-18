from sys import argv

script, username = argv

print(f"Hello I am {username}! I 'd like you to answer a few questions.")

prompt = "> "
name = input("What is you name.")
print(f"Hi {name}! Do you like me ? ")
likes = input(prompt)

print(f"Where do you stay {name}")
stays = input(prompt)

print(f"What kind of computer do you use?")
comp = input(prompt)

print(f"Okay so you use a {comp}, {name} and you stay in {stays}")
print(f"Did you say you like me? {likes}")
