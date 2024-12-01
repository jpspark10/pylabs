from lab6.task14.MailClient import MailClient
from lab6.task14.MailServer import MailServer


def test():
    server1 = MailServer("Server1")
    server2 = MailServer("Server2")

    client1 = MailClient(server1, "user1")
    client2 = MailClient(server2, "user2")

    client1.send_mail(server2, "user2", "Привет, это user1!")
    client2.send_mail(server1, "user1", "Привет, это user2!")
    print("Письма user1:", client1.receive_mail())
    print("Письма user2:", client2.receive_mail())

    server3 = MailServer("Server3")
    client1.send_mail(server3, "user3", "123")


if __name__ == "__main__":
    test()
