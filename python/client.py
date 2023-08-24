import grpc

# import the generated classes
import datetime_pb2
import datetime_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = datetime_pb2_grpc.GetDateTimeStub(channel)
        response = stub.SayDateTime(datetime_pb2.RequestString(value="maxiron"))
    print("Client received: " + response.value)


if __name__ == '__main__':
    run()

