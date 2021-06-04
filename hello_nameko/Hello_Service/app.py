from nameko.rpc import rpc
import time


class HelloService:
    name = "hello_service"

    @rpc
    def hello(self, name):
        time.sleep(10)
        return f"hello {name}"
