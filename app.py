import pyrogram
import tkinter as tk
from urllib.parse import urlparse

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Постер телеграмм")

        self.root.geometry("600x600")

        self.label_link = tk.Label(root, text="Ссылка на канал:")
        self.label_link.pack()

        self.link_entry = tk.Entry(root, width=50)
        self.link_entry.pack()

        self.label_comment = tk.Label(root, text="Комментарий:")
        self.label_comment.pack()

        self.comment_entry = tk.Text(root, width=50, height=25)
        self.comment_entry.pack()

        self.send_button = tk.Button(root, text="Отправить", width=25, height=5, bg="green", command=self.send_comment)
        self.send_button.pack()

    def extract(self, link):
        parsed_url = urlparse(link)
        path_parts = parsed_url.path.split("/")
        return path_parts[-1] if path_parts[-1] else path_parts[-2] if path_parts[-2] else link

    def get_last_message_id(self, app, username):
        chat = username
        history = app.get_chat_history(chat, limit=1)
        if history:
            for msg in history:
                return msg.id
        return None

    def send_comment(self):
        link = self.link_entry.get()
        comment = self.comment_entry.get(1.0, tk.END)
        username = self.extract(link)

        with pyrogram.Client("my_account") as app:
            last_message_id = self.get_last_message_id(app, username)
            if last_message_id:
                post = app.get_discussion_message(username, last_message_id)
                post.reply(comment)
                print("Комментарий успешно отправлен!")
            else:
                print("Не удалось найти последний пост в канале.")

root = tk.Tk()
app = App(root)
root.mainloop()
