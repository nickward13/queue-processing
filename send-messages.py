import os
from azure.storage.queue import QueueServiceClient, QueueClient, BinaryBase64DecodePolicy, BinaryBase64EncodePolicy

def send_message(queue_client):
    message = '{"id":"1", "message": "something"}'
    queue_client.send_message(bytes(message, 'utf-8'))
    print("Message sent")

# get connection_string from environment variable
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

# queue_service = QueueServiceClient.from_connection_string(conn_str=connection_string)
# queue_client = queue_service.get_queue_client("myqueue")

base64_queue_client = QueueClient.from_connection_string(
    conn_str=connection_string,
    queue_name="myqueue",
    message_encode_policy=BinaryBase64EncodePolicy(),
    message_decode_policy=BinaryBase64DecodePolicy())

for i in range(2000):
    send_message(base64_queue_client)