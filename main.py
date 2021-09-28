def valid_email(email):
    """Проверка корректности почты(регулярка)."""
    import re
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))


def log(file_name, text):
    """Запись логов в файл."""
    with open(file_name, 'a') as f:
        f.write(text)
