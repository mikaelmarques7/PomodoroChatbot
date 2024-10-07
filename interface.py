import tkinter as tk
from tkinter import font, messagebox
from tkinter import ttk
from chatbot import PomodoroChatbot

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Chatbot")
        self.root.geometry("600x600")
        self.root.configure(bg="#ececec")

        self.custom_font = font.Font(family="Roboto", size=14, weight="bold")
        self.timer_font = font.Font(family="Roboto", size=48, weight="bold")

        self.chatbot = PomodoroChatbot()
        self.is_timer_running = False
        self.is_paused = False  # verifica se o cronometro foi pausado (tava em loop)
        self.work_duration = 25 * 60
        self.short_break = 5 * 60
        self.long_break = 15 * 60
        self.current_cycle = 0
        self.remaining_time = self.work_duration
        self.timer_id = None

        # estrutura principal e de layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.main_frame = tk.Frame(self.root, bg="#ececec")
        self.main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_propagate(False)

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

    
        self.progress_bar = ttk.Progressbar(
            self.main_frame,
            orient="horizontal",
            length=400,
            mode="determinate"
        )
        self.progress_bar.grid(row=0, column=0, columnspan=2, pady=(0, 20))


        self.timer_label = tk.Label(
            self.main_frame,
            text="25:00",
            bg="#ececec",
            font=self.timer_font,
            fg="#333333"
        )
        self.timer_label.grid(row=1, column=0, columnspan=2, pady=20)

        # Frame para botões
        self.button_frame = tk.Frame(self.main_frame, bg="#ececec")
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        self.start_button = tk.Button(
            self.button_frame,
            text="Iniciar",
            command=self.start_pomodoro,
            bg="#4caf50",
            fg="white",
            font=self.custom_font,
            relief="groove",
            borderwidth=2
        )
        self.start_button.grid(row=0, column=0, padx=2, pady=10, sticky=tk.W)

        self.stop_button = tk.Button(
            self.button_frame,
            text="Parar",
            command=self.stop_pomodoro,
            bg="#f44336",
            fg="white",
            font=self.custom_font,
            relief="groove",
            borderwidth=2
        )
        self.stop_button.grid(row=0, column=1, padx=2, pady=10, sticky=tk.E)

        self.reset_button = tk.Button(
            self.main_frame,
            text="Resetar Tempo",
            command=self.reset_timer,
            bg="#ff9880",
            fg="white",
            font=self.custom_font,
            relief="groove",
            borderwidth=2
        )
        self.reset_button.grid(row=3, column=0, columnspan=2, pady=10, ipadx=10, ipady=10)

        # label de informações
        self.info_label = tk.Label(
            self.main_frame,
            text="Pressione o botão para iniciar o Pomodoro",
            bg="#ececec",
            font=("Roboto", 12),
            fg="#555555"
        )
        self.info_label.grid(row=4, column=0, columnspan=2, pady=20)

        # entrada de perguntas e botões do chatbot
        self.question_entry = tk.Entry(
            self.main_frame,
            font=self.custom_font,
            width=40
        )
        self.question_entry.grid(row=5, column=0, columnspan=2, pady=10)

        self.ask_button = tk.Button(
            self.main_frame,
            text="Perguntar",
            command=self.ask_chatbot,
            bg="#2196f3",
            fg="white",
            font=self.custom_font,
            relief="groove",
            borderwidth=2
        )
        self.ask_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.answer_label = tk.Label(
            self.main_frame,
            text="Resposta do Chatbot:",
            bg="#ececec",
            font=("Roboto", 12),
            fg="#555555"
        )
        self.answer_label.grid(row=7, column=0, columnspan=2, pady=10)

        self.response_display = tk.Label(
            self.main_frame,
            text="",
            bg="#ececec",
            font=("Roboto", 12),
            fg="#333333",
            wraplength=400,
            justify="left",
            anchor="w"
        )
        self.response_display.grid(row=8, column=0, columnspan=2, pady=10)

    # Funções de controle do Pomodoro
    def start_pomodoro(self):
        if not self.is_timer_running:
            if self.is_paused:  
                self.info_label.config(text="Pomodoro retomado!")
            else:
                if self.current_cycle % 2 == 0 and self.current_cycle != 7:
                    self.remaining_time = self.work_duration
                    self.info_label.config(text="Pomodoro em andamento")
                elif self.current_cycle == 7:
                    self.remaining_time = self.long_break
                    self.info_label.config(text="Intervalo longo! Relaxe por alguns minutos.")
                else:
                    self.remaining_time = self.short_break
                    self.info_label.config(text="Intervalo curto! Respire um pouco")
            
        self.is_timer_running = True  
        self.is_paused = False  
        self.update_timer(self.remaining_time)

    def update_timer(self, remaining_time):
        if remaining_time >= 0:
            self.remaining_time = remaining_time
            minutes, seconds = divmod(remaining_time, 60)
            self.timer_label.config(text=f"{minutes:02}:{seconds:02}")

            # Atualizando o progresso
            total_time = (
                self.work_duration if self.current_cycle % 2 == 0
                else self.long_break if self.current_cycle == 7
                else self.short_break
            )
            progress_value = (total_time - self.remaining_time) / total_time * 100
            self.progress_bar["value"] = progress_value

            self.timer_id = self.root.after(1000, self.update_timer, remaining_time - 1)
        else:
            self.is_timer_running = False

            self.current_cycle += 1

            
            if self.current_cycle > 8:
                self.current_cycle = 0 
                self.info_label.config(text="Pomodoro completo! Descanse.")
                self.remaining_time = self.work_duration  # Reinicia o tempo de trabalho
            else:
                self.ask_to_continue()

    def ask_to_continue(self):
        response = messagebox.askyesno("Continuar?", "Deseja continuar com o próximo Pomodoro?")
        if response:
            # Se a pessoa quiser continuar, define o tempo restante para o próximo ciclo
            if self.current_cycle % 2 == 0:
                self.remaining_time = self.work_duration
                self.info_label.config(text="Pomodoro em andamento")
            else:
                if self.current_cycle == 7:
                    self.remaining_time = self.long_break
                    self.info_label.config(text="Intervalo longo! Relaxe por alguns minutos.")
                else:
                    self.remaining_time = self.short_break
                    self.info_label.config(text="Intervalo curto! Respire um pouco")

            self.update_timer(self.remaining_time)
        else:
            self.info_label.config(text="Pomodoro encerrado. Pressione Iniciar para reiniciar.")

    def stop_pomodoro(self):
        if self.is_timer_running:
            self.info_label.config(text="Pomodoro pausado.")
            self.is_timer_running = False
            self.is_paused = True
            if self.timer_id is not None:
                self.root.after_cancel(self.timer_id)

    def reset_timer(self):
        if self.is_timer_running:
            self.stop_pomodoro()

        self.is_paused = False
        self.remaining_time = self.work_duration
        self.timer_label.config(text="25:00")
        self.info_label.config(text="Pomodoro resetado. Pressione o botão para iniciar novamente.")
        self.progress_bar["value"] = 0  

    def ask_chatbot(self):
        question = self.question_entry.get()
        response = self.chatbot.get_response(question)
        self.response_display.config(text=response)
