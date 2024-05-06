import requests

server_address = "http://0.0.0.0:8999" 

message = "hello please train a resnet18 model on cifar100 dataset with gpu"

response = requests.get(f"{server_address}/chat", params={"message": message})

print(response.text)
