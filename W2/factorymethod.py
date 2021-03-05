from abc import ABC, abstractmethod


class Logistic(ABC):

    @abstractmethod
    def transaction_element_creator(self):
        pass

    def delivery(self, jens):
        print("farayand amadesazi transaction")
        product = self.transaction_element_creator()
        product.operation(jens)


class SeaLogistic(Logistic):

    def transaction_element_creator(self):
        return SeaProduct()


class RoadLogistic(Logistic):

    def transaction_element_creator(self):
        return RoadLogistic()


class Product(ABC):
    @abstractmethod
    def operation(self):
        pass


class SeaProduct(Product):

    def operation(self, jens):
        print(f"man keshti angelica hastam. {jens} ro gereftamo rah oftadam")


class RoadProduct(Product):

    def operation(self, jens):
        print(f"man kamiun khoshrekab. {jens} ro gereftamo rah oftadam")


def client():
    print("bar baraye daryaei")
    sea_elem = SeaLogistic()
    sea_elem.delivery("bar kharbozeh")

    # print("bar baraye jadeh")
    # road_elem = RoadLogistic()
    # road_elem.delivery("tirahan")


if __name__ == "__main__":
    client()
