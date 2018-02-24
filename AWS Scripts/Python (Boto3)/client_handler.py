import boto3


class BotoHandler:
    def __init__(self, service):
        self.client = boto3.client(service)
    
    def execute_command(self, api_call_to_make, parameters):
        try:
            method_to_invoke = self.client.getattr(self, api_call_to_make)
            response = self.client.method_to_invoke(parameters)
            return response
        except AttributeException as exception:
            exception.message = 'Command does not exist or is wrong'
            return exception

         