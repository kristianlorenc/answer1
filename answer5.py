from exam_lib import Book

class EBook(Book):
    def __init__(self, title, author, page_count, size, registration_code):
        super().__init__(title, author, page_count)
        self.size = size
        self._registration_code = registration_code if self.check_code(registration_code) else None

    @staticmethod
    def check_code(reg_code):
        return isinstance(reg_code, str) and len(reg_code) == 16

    @property
    def registration_code(self):
        return self._registration_code

    @registration_code.setter
    def registration_code(self, new_code):
        if self.check_code(new_code):
            self._registration_code = new_code
        else:
            raise ValueError("Invalid registration code")

# Example usage
if __name__ == "__main__":
    ebook = EBook("Python Basics", "Kristian Lorenc", 250, 5, "1234567890123456")
    print(ebook.title)  # Output: Python Basics
    print(ebook.registration_code)  # Output: 1234567890123456

    ebook.registration_code = "6543210987654321"  # Valid update
    print(ebook.registration_code)  # Output: 6543210987654321

    try:
        ebook.registration_code = "invalid_code"  # This will raise ValueError
    except ValueError as e:
        print(e)  # Output: Invalid registration code

