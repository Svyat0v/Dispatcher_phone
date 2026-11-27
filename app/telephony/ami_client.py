
import socket
import threading

from PySide6.QtCore import QThread, Signal

from app.telephony.ami_protocol import parse_ami_frames


class AmiClient(QThread):

    event_received = Signal(object)
    connected = Signal()
    connection_error = Signal(str)
    disconnected = Signal()

    def __init__(
        self,
        host,
        port,
        username,
        password,
        parent=None
    ):
        super().__init__(parent)

        self.host = host
        self.port = int(port)
        self.username = username
        self.password = password

        self._stop_event = threading.Event()

    def run(self):

        buffer = b""
        authenticated = False

        try:
            with socket.create_connection(
                (self.host, self.port),
                timeout=5
            ) as sock:

                sock.settimeout(1)

                login = (
                    "Action: Login\r\n"
                    f"Username: {self.username}\r\n"
                    f"Secret: {self.password}\r\n"
                    "Events: on\r\n"
                    "\r\n"
                )

                sock.sendall(login.encode("utf-8"))

                while not self._stop_event.is_set():

                    try:
                        data = sock.recv(4096)

                    except socket.timeout:
                        continue

                    if not data:
                        break

                    buffer += data

                    if len(buffer) > 1024 * 1024:
                        raise ValueError(
                            "Слишком большой буфер AMI"
                        )

                    messages, buffer = parse_ami_frames(
                        buffer
                    )

                    for message in messages:

                        if not authenticated:

                            response = message.get("Response")

                            if response == "Success":
                                authenticated = True
                                self.connected.emit()

                            elif response == "Error":
                                raise ConnectionError(
                                    "Ошибка авторизации AMI"
                                )

                            continue

                        if "Event" in message:
                            self.event_received.emit(message)

                if not authenticated:
                    raise ConnectionError(
                        "AMI-соединение не авторизовано"
                    )

        except (OSError, ValueError) as error:

            if not self._stop_event.is_set():
                self.connection_error.emit(str(error))

        finally:
            self.disconnected.emit()

    def stop(self):
        self._stop_event.set()
