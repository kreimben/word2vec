def get_data() -> str:
    """
    Generator that gives you data from txt file.
    :return: Line of contents of txt file.
    """
    with open('./data.txt', 'r') as file:
        for line in file:
            yield line.strip()
