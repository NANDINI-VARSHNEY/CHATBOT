import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_CODE = "Start by typing: 'How to learn coding' on Google."
R_eat = "You can eat fruits,healthy for you"
def unknown():
    response = ["Please try writing something more descriptive.",
        "Oh! It appears you wrote something I don't understand yet",
        "Do you mind trying to rephrase that?",
        "I'm terribly sorry, I didn't quite catch that.",
        "I can't answer that yet, please try asking something else.",
        "Could you please re-phrase that? ",
        "Sounds about right.",
        "What does that mean?"][
        random.randrange(8)]
    return response