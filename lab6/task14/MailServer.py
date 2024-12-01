from lab6.task14.MailClient import MailClient


class MailServer:
    def __init__(self, name):
        self.name = name
        self.users = {}
        MailClient.available_servers[name] = self

    def register_user(self, user):
        if user not in self.users:
            self.users[user] = []
        else:
            raise ValueError(f"Пользователь {user} уже зарегистрирован на сервере {self.name}.")

    def receive_mail(self, user):
        if user in self.users:
            mail = self.users[user]
            self.users[user] = []
            return mail
        else:
            raise ValueError(f"Пользователь {user} не зарегистрирован на сервере {self.name}.")

    def send_mail(self, recipient, message):
        if recipient in self.users:
            self.users[recipient].append(message)
        else:
            raise ValueError(f"Пользователь {recipient} не зарегистрирован на сервере {self.name}.")