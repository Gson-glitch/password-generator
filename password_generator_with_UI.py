import tkinter as tk
import pass_gen
import pyperclip

LIGHT_GRAY = '#F5F5F5'
MEDIUM_FONT_STYLE = ('Arial', 25, 'bold')
SMALL_FONT_STYLE = ('Times New Roman', 16, 'bold')
LABEL_COLOR = '#25265E'


class PasswordGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('400x100')
        self.window.title('Password Generator')
        self.window.resizable(0, 0)

        self.password_txt = ''
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.password_label = self.create_password_label()
        self.generate_button = {
            'Generate': (1, 1)
        }
        self.copy_button = {
            'Copy': (1, 2)
        }
        self.create_buttons()
        for x in range(1, 3):
            self.buttons_frame.columnconfigure(x, weight=1)
            self.buttons_frame.rowconfigure(x, weight=1)
        self.generate_passwd()
        self.update_label()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height='60', bg=LIGHT_GRAY)
        frame.pack(expand=True, fill='both')
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill='both')
        return frame

    def create_password_label(self):
        password_label = tk.Label(self.display_frame, text=self.password_txt, anchor=tk.W, bg=LIGHT_GRAY,
                                  fg=LABEL_COLOR, padx=8, font=MEDIUM_FONT_STYLE)
        password_label.pack(expand=True, fill='both')
        return password_label

    def create_buttons(self):
        for button, grid_value in self.generate_button.items():
            button = tk.Button(self.buttons_frame, text=button, borderwidth=5, font=SMALL_FONT_STYLE, pady=10,
                               command=self.generate_passwd)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW, columnspan=1)
        for button, grid_value in self.copy_button.items():
            button = tk.Button(self.buttons_frame, text=button, borderwidth=5, font=SMALL_FONT_STYLE, pady=10,
                               command=self.copy_func)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW, columnspan=2)

    def generate_passwd(self):
        self.password_txt = pass_gen.password_generator()
        self.update_label()

    def copy_func(self):
        pyperclip.copy(self.password_txt)
        print('Hello')

    def update_label(self):
        expression = self.password_txt
        self.password_label.config(text=expression)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    PG = PasswordGenerator()
    PG.run()
