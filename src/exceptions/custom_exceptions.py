import logging


class CustomException(Exception):
    pass

def log_section_not_found(category,e):
    return logging.error(category + "was not found: %s", str(e))

def log_element_not_found(element,e):
    return logging.error(element + "was not found: %s", str(e))

def handle_custom_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except CustomException as e:
            print(f"There was a custom exception of type: {str(e)}")

    return wrapper