
import docker

client = docker.from_env()

IMAGE = "flask-apparmor"
CONTAINER_NAME = "flask-apparmor-test"
PROFILE = "my-apparmor-profile"

container = None

try:
    container = client.containers.run(
        IMAGE,
        name=CONTAINER_NAME,
        ports={"5000/tcp": 5000},
        security_opt=[f"apparmor={PROFILE}"],
        detach=True
    )

    print("Container started:", container.short_id)

    tests = [
        ["cat", "/etc/passwd"],
        ["/bin/sh", "-c", "echo shell-execution-test"]
    ]

    for command in tests:
        result = container.exec_run(command)
        output = result.output.decode(errors="replace")

        print("Command:", " ".join(command))
        print("Exit code:", result.exit_code)
        print("Output:", output or "(no output)")
        print("-" * 40)

finally:
    if container is not None:
        container.stop(timeout=5)
        container.remove()
        print("Container stopped and removed.")
