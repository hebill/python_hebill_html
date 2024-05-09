from ...nodes import Tag


class A(Tag):
    output_break_inner = False

    def __init__(self, senior, text=None, url: str = None):
        super().__init__(senior, 'a')
        self.add_junior(text)
        self.attributes["href"] = ""
        if url is not None:
            self.attributes["href"] = url
