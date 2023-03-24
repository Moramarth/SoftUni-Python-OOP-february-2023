"""
E-mail automation with Python!!!

Test examples provided at the end of file.

!Spoiler alert! Not creative content
"""

from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def formatting(self):
        pass


class MyContent(IContent):
    def formatting(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class YourContent(IContent):
    def formatting(self):
        return '\n'.join(['<yourML>', self.text, '</yourML>'])


class TheirContent(IContent):
    def formatting(self):
        return '\n'.join(['<theirML>', self.text, '</theirML>'])


class IProtocol(ABC):
    @abstractmethod
    def get_protocol(self):
        pass


class IMProtocol(IProtocol):
    def get_protocol(self):
        return "I'm "


class YouProtocol(IProtocol):
    def get_protocol(self):
        return "You're "


class TheyProtocol(IProtocol):
    def get_protocol(self):
        return "They're "


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):
    def __init__(self, protocol: IProtocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = ''.join([self.protocol.get_protocol(), sender])

    def set_receiver(self, receiver):
        self.__receiver = ''.join([self.protocol.get_protocol(), receiver])

    def set_content(self, content):
        self.__content = content.formatting()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


# remove comments by section for better tester experience
protocol_i = IMProtocol()
protocol_you = YouProtocol()
protocol_they = TheyProtocol()

my_content = MyContent("This is my content")
your_content = YourContent("This is your content")
their_content = TheirContent("This is their content")

first_email = Email(protocol_i)
first_email.set_sender("Gosho")
first_email.set_receiver("not Pesho")
first_email.set_content(my_content)
print(first_email)
print()

# second_email = Email(protocol_you)
# second_email.set_sender("not me")
# second_email.set_receiver("the receiver")
# second_email.set_content(your_content)
# print(second_email)
# print()

# third_email = Email(protocol_they)
# third_email.set_sender("student with homework at SoftUni")
# third_email.set_receiver("student to code review at SoftUni")
# third_email.set_content(their_content)
# print(third_email)

# Thank you for your time. Keep up the good work!
