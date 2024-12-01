class MailClient:
    available_servers = {}

    def __init__(self, server, user):
        if server.name not in MailClient.available_servers:
            raise ValueError(f"Сервер {server.name} недоступен.")
        self.server = server
        self.user = user
        server.register_user(user)

    def receive_mail(self):
        return self.server.receive_mail(self.user)

    def send_mail(self, server, recipient, message):
        if server.name not in MailClient.available_servers:
            print(f"Сервер {server.name} недоступен для отправки писем.")
            return
        try:
            server.send_mail(recipient, message)
            print(f"Письмо отправлено {recipient} на сервере {server.name}.")
        except ValueError as e:
            print(e)