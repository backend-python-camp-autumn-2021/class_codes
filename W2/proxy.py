from abc import ABC, abstractmethod


class Internet(ABC):

    @abstractmethod
    def connection(self):
        pass


class RealInternet(Internet):
    def connection(self):
        print("Hoooray. you are connected")


class ProxyInternet(Internet):

    def __init__(self):
        self.real_internet = RealInternet()

    def connection(self, IP):
        blocked_list = ['iran', 'cuba', 'north_korea', 'shalghamestan']

        if IP in blocked_list:
            return False
        else:
            self.real_internet.connection()
            return True


def client(proxy, IP):

    if proxy.connection(IP):
        print("Welcome")

    else:
        print("keshavar shoma be dalaiel khasmane tavasot amrica jenayatkar tahrim shode!")


if __name__ == "__main__":
    proxy = ProxyInternet()
    client(proxy, "alman")
