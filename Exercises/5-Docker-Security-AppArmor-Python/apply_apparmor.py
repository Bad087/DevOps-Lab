
import docker

client = docker.from_env()

IMAGE = "flask-apparmor"
CONTAINER_NAME = "flask-apparmor-sdk"
PROFILE = "my-apparmor-profile"

try:
    print("Building Docker image...")
    client.images.build(path=".", tag=IMAGE)

    print("Starting container with AppArmor profile...")
    container = client.containers.run(
        IMAGE,
        name=CONTAINER_NAME,
        ports={"5000/tcp": 5000},
        security_opt=[f"apparmor={PROFILE}"],
        detach=True
    )

    container.reload()
    info = client.api.inspect_container(container.id)

    print("Container started:", container.short_id)
    print("Requested security options:",
          info["HostConfig"]["SecurityOpt"])
    print("Running state:", info["State"]["Status"])

except docker.errors.DockerException as error:
    print("Docker operation failed:", error)

finally:
    try:
        container.stop(timeout=5)
        container.remove()
        print("Container stopped and removed.")
    except (NameError, docker.errors.NotFound):
        pass
