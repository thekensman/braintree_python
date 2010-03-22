import os

class Environment(object):
    def __init__(self, server, port, is_ssl):
        self.__server = server
        self.__port = port
        self.is_ssl = is_ssl

    @property
    def server_and_port(self):
        return self.__server + ":" + self.__port

    @property
    def protocol(self):
        return self.__port == "443" and "https://" or "http://"

Environment.DEVELOPMENT = Environment("localhost", os.getenv("GATEWAY_PORT") or '3000', False)
Environment.SANDBOX = Environment("sandbox.braintreegateway.com", '443', True)
Environment.PRODUCTION = Environment("www.braintreegateway.com", '443', True)
