class PrintedPublication:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def get_metadata(self):
        return f"{self.title}, {self.author}, {self.pages} стр., {self.year} г."

    def export_to_pdf(self):
        pass

    def calculate_cost(self):
        pass

    def check_availability(self):
        pass


class Book(PrintedPublication):
    def export_to_pdf(self):
        print(f"Экспорт книги '{self.title}' в PDF")

    def calculate_cost(self):
        return self.pages * 0.5

    def check_availability(self):
        return True


class Magazine(PrintedPublication):
    def export_to_pdf(self):
        raise NotImplementedError("Журналы не экспортируются в PDF")

    def calculate_cost(self):
        raise NotImplementedError("Для журналов стоимость не рассчитывается")

    def check_availability(self):
        return False


class Textbook(PrintedPublication):
    def export_to_pdf(self):
        print(f"Экспорт учебника '{self.title}' в PDF с защитой")

    def calculate_cost(self):
        return self.pages * 0.8 + 100

    def check_availability(self):
        return True


class LibrarySystem:
    def __init__(self):
        self.books = []
        self.magazines = []
        self.textbooks = []

    def add_item(self, item):
        if isinstance(item, Book):
            self.books.append(item)
        elif isinstance(item, Magazine):
            self.magazines.append(item)
        elif isinstance(item, Textbook):
            self.textbooks.append(item)

    def process_catalog(self):
        print("\nОбработка каталога:")
        
        for b in self.books:
            print(b.get_metadata())
            b.export_to_pdf()
            print(f"Стоимость: {b.calculate_cost()} руб.")
            
        for m in self.magazines:
            print(m.get_metadata())
            try:
                m.export_to_pdf()
                print(f"Стоимость: {m.calculate_cost()} руб.")
            except NotImplementedError as e:
                print(f"Ошибка: {e}")
                
        for t in self.textbooks:
            print(t.get_metadata())
            t.export_to_pdf()
            print(f"Стоимость: {t.calculate_cost()} руб.")


def main():
    system = LibrarySystem()
    system.add_item(Book("Война и мир", "Толстой", 1200, 1869))
    system.add_item(Magazine("Vogue", "Редакция", 150, 2024))
    system.add_item(Textbook("Математика", "Пискунов", 500, 2020))
    system.process_catalog()


if __name__ == "__main__":
    main()