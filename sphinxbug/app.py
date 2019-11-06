class MyPrintClass:
    """
    This class adds two numbers.

    It is documented using the numpydoc convention.

    Parameters
    ----------
    msg : str
        The message to print.
    """

    def __init__(self, msg: str):
        self.msg = msg

    def print_msg(self) -> None:
        """This is a docstring."""
        print(self.msg)
