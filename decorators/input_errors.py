def input_errors(func):
    """Decorator to handle input errors.

        Args:
            func (function): The function to decorate.

        Returns:
            function: The decorated function that handles input errors.
        """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as error:
            return f"{error}."
        except ValueError as error:
            return f"{error}."
        except IndexError as e:
            return f"{error}."
    return wrapper