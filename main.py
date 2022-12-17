import random 


excuses = [ "I forgot my homework at school.", "I was sick and couldn't do it.", "I'm sorry, I didn't mean to be late. I got stuck in traffic on the way here.", "I'm sorry, I didn't have time to finish the project. I've been really busy with work and family responsibilities" ]

def generate_excuse():
 return random.choice(excuses)

excuse = generate_excuse()
print(excuse)