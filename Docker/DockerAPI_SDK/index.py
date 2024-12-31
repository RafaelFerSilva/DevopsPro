import docker

client = docker.from_env()

# client.containers.run("nginx", detach=True, ports={"80/tcp":("0.0.0.0", 8080)})

containers_list = client.containers.list(all=True)

for item in containers_list:
    print(f'{item.id} - {item.image.tags} - {item.name}')
