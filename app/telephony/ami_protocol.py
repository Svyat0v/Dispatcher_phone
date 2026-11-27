
def parse_ami_frames(buffer):
    """
    Принимает накопленные байты AMI.
    Возвращает список сообщений и остаток буфера.
    """

    messages = []

    while b"\r\n\r\n" in buffer:
        frame, buffer = buffer.split(b"\r\n\r\n", 1)

        message = {}

        for line in frame.decode(
            "utf-8", errors="replace"
        ).split("\r\n"):

            if ":" not in line:
                continue

            key, value = line.split(":", 1)
            message[key.strip()] = value.strip()

        if message:
            messages.append(message)

    return messages, buffer
