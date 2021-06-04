import json

from nameko.web.handlers import http
from nameko.rpc import RpcProxy


class GatewayService:
    name = 'gateway_service'

    driver_rpc = RpcProxy('driver_service')
    passenger_rpc = RpcProxy('passenger_service')
    trip_rpc = RpcProxy('trip_service')

    @http('GET', '/driver/<string:driver_id>')
    def get_driver(self, request, driver_id):
        driver = self.driver_rpc.get(driver_id)
        return json.dumps({'driver': driver})

    @http('POST', '/driver')
    def post_driver(self, request):
        data = json.loads(request.get_data(as_text=True))
        driver_id = self.driver_rpc.create(data['driver'])

        return driver_id

    @http("GET", "/trip/<string:trip_id>")
    def trip_info(self, request, trip_id):
        trip = self.trip_rpc.get(trip_id)
        return json.dumps({'passenger_name': trip["passenger_name"], "driver_name": trip["driver_name"], "from_loc": trip["from_loc"], "to_loc": trip["to_loc"]})

    @http('POST', '/trip/')
    def post_driver(self, request):
        data = json.loads(request.get_data(as_text=True))
        driver_id = self.trip_rpc.create(
            data['passenger_name'], data["driver_name"], data["from_loc"], data["to_loc"])

        return driver_id
