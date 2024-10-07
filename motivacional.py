import random

def get_random_motivacional():
    motivacional = [
        "Você é mais forte do que pensa!",
        "Cada passo conta, continue!",
        "A persistência é o caminho do êxito.",
        "Faça hoje o que outros não querem, faça amanhã o que outros não conseguem.",
        "A disciplina é a ponte entre metas e conquistas.",
        "Desafios são o que tornam a vida interessante; superá-los é o que faz a vida significativa.",
        "Não desista, o início é sempre o mais difícil.",
        "O sucesso é a soma de pequenos esforços repetidos dia após dia."
    ]
    return random.choice(motivacional)