from abc import ABC, abstractmethod


class IExportable(ABC):
    @abstractmethod
    def export_to_pdf(self) -> None:
        pass


class IPricable(ABC):
    @abstractmethod
    def calculate_cost(self) -> float:
        pass


class IAvailable(ABC):
    @abstractmethod
    def check_availability(self) -> bool:
        pass


class PrintedPublicationBase:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def get_metadata(self):
        return f"{self.title}, {self.author}, {self.pages} стр., {self.year} г."


class Book(PrintedPublicationBase, IExportable, IPricable, IAvailable):
    def export_to_pdf(self):
        print(f"Экспорт книги '{self.title}' в PDF")

    def calculate_cost(self):
        return self.pages * 0.5

    def check_availability(self):
        return True


class Magazine(PrintedPublicationBase, IAvailable):
    def check_availability(self):
        return False


class Textbook(PrintedPublicationBase, IExportable, IPricable, IAvailable):
    def export_to_pdf(self):
        print(f"Экспорт учебника '{self.title}' в PDF с защитой")

    def calculate_cost(self):
        return self.pages * 0.8 + 100

    def check_availability(self):
        return True


class LibrarySystem:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def export_available_items(self):
        print("\nЭкспорт доступных изданий:")
        for item in self.items:
            if isinstance(item, IExportable):
                print(item.get_metadata())
                item.export_to_pdf()

    def calculate_total_cost(self):
        print("\nРасчет стоимости:")
        total = 0
        for item in self.items:
            if isinstance(item, IPricable):
                cost = item.calculate_cost()
                print(f"{item.get_metadata()}: {cost} руб.")
                total += cost
        print(f"Итого: {total} руб.")

    def check_all_availability(self):
        print("\nПроверка доступности:")
        for item in self.items:
            if isinstance(item, IAvailable):
                status = "доступно" if item.check_availability() else "недоступно"
                print(f"{item.get_metadata()}: {status}")


def main():
    system = LibrarySystem()
    system.add_item(Book("Война и мир", "Толстой", 1200, 1869))
    system.add_item(Magazine("Vogue", "Редакция", 150, 2024))
    system.add_item(Textbook("Математика", "Пискунов", 500, 2020))
    
    system.export_available_items()
    system.calculate_total_cost()
    system.check_all_availability()


if __name__ == "__main__":
    main()