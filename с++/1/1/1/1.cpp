#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Book {
private:
    string title;
    string genre;
    string author;

public:
    
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
    
    void setName(string n) {
        name = n;
    }

    void setAddress(string a) {
        address = a;
    }

    
    void addBook(const Book& b) {
        books.push_back(b);
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
    
    Library lib;
    lib.setName("Центральная библиотека");
    lib.setAddress("ул. Пушкина, д. 10");

    
    Book book1;
    book1.setData("Преступление и наказание", "Роман", "Ф. М. Достоевский");

    Book book2;
    book2.setData("Мастер и Маргарита", "Фантастика", "М. А. Булгаков");

    lib.addBook(book1);
    lib.addBook(book2);

    
    lib.showInfo();
    Book book3;
    book3.setData("Основы ООП");
    Library lib2;
    lib2.setName("Библиотека СКФУ");
    lib2.setAddress("Кулакова 2");
    lib2.addBook(book1);
    lib2.addBook(book3);
    lib2.showInfo();

    return 0;
}
