import docker
import logging
import socket

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

PORT = 8770
HOST = "0.0.0.0"


def main():
    client = docker.from_env()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    logging.info(f"socket binded to port: {PORT}")

    server.listen()
    logging.info("socket is listening")
    while True:
        connection, addr = server.accept()
        logging.info(f"Connetion from {addr}")

        while True:
            data = connection.recv(1024)
            if data:
                data = eval(data)
                logging.info(data)

                if data["command"] == "pause":
                    client.containers.get(data["id"]).pause()
                    logging.info(f"Pause container {data['id']}")
                elif data["command"] == "unpause":
                    client.containers.get(data["id"]).unpause()
                    logging.info(f"Unpause container {data['id']}")

                break


if __name__ == "__main__":
    main()
