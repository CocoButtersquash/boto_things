import boto3


class BotoHandler:
    def __init__(self):
        pass
    @staticmethod
    def execute_command(service, api_call_to_make, parameters):
        client = boto3.client(service)
        try:
            method_to_invoke = getattr(client, api_call_to_make)
            response = method_to_invoke(**parameters)
            return response
        except AttributeError as exception:
            exception.message = 'Command does not exist or is wrong'
            return exception
