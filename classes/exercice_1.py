class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"{self.title} by {self.author} ({self.pages})"
    
    def is_long(self):
        if self.pages > 300:
            return True
        else:
            return False

def main():
    book = Book("1984", "George Orwell", 350)
    print(book)
    print(book.is_long())


if __name__ == "__main__":
    main()


# Créez une classe Book avec :

# Attributs : title, author, pages
# Méthode __str__ qui retourne : "Title by Author (X pages)"
# Méthode is_long() qui retourne True si le livre a plus de 300 pages