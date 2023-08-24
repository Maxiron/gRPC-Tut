import time
import grpc
from concurrent import futures

# import the generated classes
import datetime_pb2
import datetime_pb2_grpc

# import the original main.py
import main

# Create a class to define the server functions
# derived from datetime_pb2_grpc.GetDateTimeServicer

class DateTimeServicer(datetime_pb2_grpc.GetDateTimeServicer):

    # This function will be called when a client calls the SayDateTime function
    # It is already defined in the proto file (datetime.proto)
    def SayDateTime(self, request, context):
        # define the buffer of the response
        response = datetime_pb2.ResponseString()

        # Get the username from the request
        username = request.value

        # get the value of the response by calling the desired function
        response.value = main.getDateTime(username)
        return response
    

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # add the defined class to the server
    datetime_pb2_grpc.add_GetDateTimeServicer_to_server(
        DateTimeServicer(), 
        server
    )    
    server.add_insecure_port('[::]:50051')
    print('Starting server. Listening on port 50051.')
    server.start()

    # set timeout to 60 seconds
    server.wait_for_termination(timeout=60)


if __name__ == '__main__':
    serve()
    

