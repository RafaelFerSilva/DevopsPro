import docker

client = docker.from_env()

client.containers.run("nginx", detach=True, ports={"80/tcp":("0.0.0.0", 8080)})

containers_list = client.containers.list(all=True)

for item in containers_list:
    print(f'{item.id} - {item.image.tags} - {item.name}')

container = client.containers.get("2a2bb0c8a933705f0c143fd35d3b2e44a15c326f3ddf7290d7b0f45b4feef968")
print(f'{container.id} - {container.image.tags} - {container.name}')

print(container.logs())

container.remove(force=True)
