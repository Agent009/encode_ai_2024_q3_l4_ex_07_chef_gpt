from sys import intern


def multiline_input(prompt: str) -> str:
    """
    Captures multi-line user input. Input is terminated by pressing ENTER twice.
    :param prompt: The prompt asking for user input
    :return: The multiline user input
    """
    print(prompt)  # Display the prompt once
    lines = []

    while True:
        line = input()  # No need to show the prompt again
        if line == "":
            break
        lines.append(line)

    user_input = "\n".join(lines)
    return user_input
