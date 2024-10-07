import time
import threading
from motivacional import get_random_motivacional 
import random


class PomodoroChatbot:
    def __init__(self):
        self.pomodoro_duration = 25 * 60
        self.break_duration = 5 * 60
        self.running = False
        self.checkin_message = [
            "Como você está se sentindo até agora? Está focado?",
            "Precisa de uma dica para manter a concentração?",
            "Está tudo bem? Se precisar de uma pausa, estou aqui para te lembrar de voltar!"
        ]
        self.productivity_tips = [
            "Tente dividir suas tarefas em pequenas etapas para facilitar o progresso.",
            "Mantenha um ambiente de trabalho organizado e livre de distrações.",
            "Desligue notificações desnecessárias enquanto trabalha para manter o foco."
        ]
        self.break_tips = [
            "Aproveite para se alongar um pouco e relaxar seus músculos.",
            "Faça uma caminhada rápida ou beba um copo d'água.",
            "Respire fundo e relaxe a mente por alguns minutos."
        ]

    def start_pomodoro(self):
        if not self.running:
            self.running = True
            print("Pomodoro iniciado! Concentre-se por 25 minutos.")
            threading.Thread(target=self._run_pomodoro).start()
        else:
            print("Um pomodoro jé está em andamento.")

    def _run_pomodoro(self):
        time.sleep(self.pomodoro_duration)
        if self.running:
            self.end_pomodoro()

    def end_pomodoro(self):
        self.running = False
        print("Pomodoro concluído! Hora da pausa de 5 minutos.")
        print(get_random_motivacional())
        self._run_break()

    def _run_break(self):
        for remaining in range(self.break_duration, 0, -1):
            mins, secs = divmod(remaining, 60)
            print(f"Pausa: {mins:02d}:{secs:02d} restantes", end='\r')
            time.sleep(1)
        print("\nPausa de 5 minutos concluída! Pronto para um novo Pomodoro?")
        print(random.choice(self.break_tips))
        self.ask_restart()

    def ask_restart(self):
        user_input = input("Voce deseja iniciar um novo Pomodoro? (s/n):")
        if user_input.lower() == 's':
            self.start_pomodoro()
        else:
            print("Pomodoro encerrado, Até a  próxima!")

    def stop(self):
        self.running = False
        print("Pomodoro interrompido.")

    def check_in(self):
        if self.running:
            print(random.choice(self.checkin_menssage))

    def get_response(self, question):
        question = question.lower()
        response = {
            "oi": "Olá, como posso te ajudar?",
            "o que é o pomodoro?": "O Pomodoro é uma técnica de gerenciamento de tempo que utiliza um cronômetro para dividir o trabalho em intervalos, geralmente de 25 minutos, seguidos por uma pausa.",
            "como usar o pomodoro?": "Para usar o Pomodoro, escolha uma tarefa, defina um cronômetro para 25 minutos e trabalhe até que o tempo acabe. Depois, faça uma pausa de 5 minutos.",
            "quais são os benefícios do pomodoro?": "Os benefícios incluem maior foco, produtividade e redução da procrastinação.",
            "quanto tempo dura o pomodoro?": "Um ciclo de Pomodoro geralmente dura 25 minutos.",
            "qual é a duração da pausa?": "A pausa é geralmente de 5 minutos após cada Pomodoro.",
            "me diga uma frase motivacional": get_random_motivacional(),
            "como melhorar minha concentração?": random.choice(self.productivity_tips),
            "o que fazer durante o intervalo?": random.choice(self.break_tips),
            "como aumentar minha produtividade?": random.choice(self.productivity_tips),
            "pode me motivar?": get_random_motivacional(),
            "obrigado": "De nada! Estou aqui para ajudar.",
            "como posso ser mais produtivo?": random.choice(self.productivity_tips),
            "qual é o seu nome?": "Sou o chatbot Pomodoro, aqui para te ajudar a ser mais produtivo!",
            "como você está?": "Estou aqui para ajudar! O que posso fazer por você?",
        }
        return response.get(question, "Desculpe, não entendi sua pergunta.")