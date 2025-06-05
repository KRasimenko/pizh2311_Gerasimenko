#include <vector>

#include <iostream>
using namespace std;

class Book {
private:
    string title;
    string genre;
    string author;

public:
    
    Book() {
        cout << "[Book] Конструктор без параметров" << endl;
        title = genre = author = "Не указано";
    }

    
    Book(string t, string g, string a) {
        cout << "[Book] Конструктор с параметрами" << endl;
        title = t;
        genre = g;
        author = a;
    }

    
    Book(const Book& other) {
        cout << "[Book] Конструктор копирования" << endl;
        title = other.title;
        genre = other.genre;
        author = other.author;
    }

    
    ~Book() {
        cout << "[Book] Деструктор" << endl;
    }

    
    void setData(string t) {
        title = t;
    }

    void setData(string t, string g) {
        title = t;
        genre = g;
    }

    void setData(string t, string g, string a) {
        title = t;
        genre = g;
        author = a;
    }

    
    string getInfo() const {
        return "Название: " + title + ", Жанр: " + genre + ", Автор: " + author;
    }
};
class Library {
private:
    string name;
    string address;
    vector<Book> books;

public:
    
    Library() {
        cout << "[Library] Конструктор без параметров" << endl;
        name = address = "Не указано";
    }

    
    Library(string n, string a) {
        cout << "[Library] Конструктор с параметрами" << endl;
        name = n;
        address = a;
    }

    
    Library(const Library& other) {
        cout << "[Library] Конструктор копирования" << endl;
        name = other.name;
        address = other.address;
        books = other.books; // копируем книги
    }

    
    ~Library() {
        cout << "[Library] Деструктор" << endl;
    }

    
    void setName(string n) {
        name = n;
    }

    void setAddress(string a) {
        address = a;
    }

    
    void addBook(const Book& b) {
        books.push_back(b);
    }

    
    void addBookFromData(string title, string genre, string author) {
        Book b(title, genre, author); 
        addBook(b);
    }

    
    void addCopies(const Book& b, int count) {
        for (int i = 0; i < count; ++i) {
            Book copy(b); 
            addBook(copy);
        }
    }

 
    void showInfo() const {
        cout << "Библиотека: " << name << endl;
        cout << "Адрес: " << address << endl;
        cout << "Книги:" << endl;

        for (const Book& book : books) {
            cout << " - " << book.getInfo() << endl;
        }
    }
};

int main() {
    setlocale(LC_ALL, "rus");

    
    
    cout << "\n=== Первая библиотека ===\n";
    Library lib;

    
    Book book1("Преступление и наказание", "Роман", "Ф. М. Достоевский");
    lib.addBook(book1);

    lib.addCopies(book1, 2);
    
    lib.addBookFromData("Мастер и Маргарита", "Фантастика", "М. А. Булгаков");

    
    

    lib.showInfo();

    cout << "\n=== Вторая библиотека ===\n";

   
    Library lib2("Библиотека СКФУ", "Кулакова 2");

    
    Book book3;
    book3.setData("Основы ООП");

    lib2.addCopies(book1,1);
    lib2.addBook(book3);

    lib2.showInfo();

    cout << "\n=== Третья библиотека ===\n";
    Library lib3(lib);
    lib3.setAddress("Ставрополь, Ворошилова 2");
    lib3.addBookFromData("Основы языка С++", "Образование", "Бьёрн Страуструп");
    lib3.showInfo();
    return 0;
    

   

    
}

