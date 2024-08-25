from sys import intern


def multiline_input(prompt: str) -> str:
    """
    Captures multi-line user input. Input is terminated by pressing ENTER twice.
    :param prompt: The prompt asking for user input
    :return: The multiline user input
    """
    lines = []
    iteration = 0

    while True:
        iteration = iteration + 1
        line = input(prompt if iteration > 1 else "")

        if line == "":
            break

        lines.append(line)

    user_input = "\n".join(lines)
    return user_input