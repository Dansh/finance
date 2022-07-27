class Page:
    def __init__(self, window, width, height):
        self._window = window
        self._width = width
        self._height = height
        self._window.geometry("{}x{}".format(width, height))
        self._window.resizable(False,False)
