from abc import ABC, abstractmethod

class NotificationSender(ABC):

  @abstractmethod
  def send_notification(self, msg: str) -> None: pass

# #########################################################

class EmailNotificationSender(NotificationSender):

  def send_notification(self, msg: str) -> None:
    print(f'Email --- {msg}')

# #########################################################

class SMSNotificationSender(NotificationSender):

  def send_notification(self, msg: str) -> None:
    print(f'SMS --- {msg}')

# #########################################################

class Notificator:
  def __init__(self, notification_sender: NotificationSender) -> None:
    self.__notification_sender = notification_sender

  def send(self, msg: str) -> None:
    self.__notification_sender.send_notification(msg)

obj = Notificator(EmailNotificationSender())
obj.send('olá')

obj = Notificator(SMSNotificationSender())
obj.send('olá')
