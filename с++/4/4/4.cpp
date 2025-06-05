#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Film {
protected:
    string title;
    string genre;
    int year;
public:
    Film(string t, string g, int y) : title(t), genre(g), year(y) {}

    virtual void printInfo() const = 0; 

    virtual ~Film() {} 
};
class Favorite : public Film {
    string comment;
public:
    Favorite(string t, string g, int y, string c)
        : Film(t, g, y), comment(c) {
    }

    void printInfo() const override {
        cout << "[Избранное] " << title << " (" << year << "), жанр: " << genre
            << ". Комментарий: " << comment << endl;
    }
};

class Blocked : public Film {
    string reason;
public:
    Blocked(string t, string g, int y, string r)
        : Film(t, g, y), reason(r) {
    }

    void printInfo() const override {
        cout << "[Заблокировано] " << title << " (" << year << "), жанр: " << genre
            << ". Причина блокировки: " << reason << endl;
    }
};
class FilmCollection {
    vector<Film*> films;
public:
    void add(Film* film) {
        films.push_back(film);
    }

    void printAll() const {
        cout << "=== Коллекция фильмов ===" << endl;
        for (const auto& film : films) {
            film->printInfo();
        }
    }

    ~FilmCollection() {
        for (auto f : films) delete f;
    }
};

int main() {
    setlocale(LC_ALL, "rus");
    vector<Film*> catalog;

    catalog.push_back(new Favorite("Интерстеллар", "Фантастика", 2014, "Любимый фильм"));
    catalog.push_back(new Blocked("Очень страшное кино", "Комедия", 2000, "Не нравится юмор"));

    cout << "=== Каталог фильмов ===" << endl;
    for (Film* film : catalog) {
        film->printInfo(); // работает полиморфизм
    }

    
    for (Film* film : catalog) {
        delete film;
    }
    FilmCollection collection;
    collection.add(new Favorite("Матрица", "Фантастика", 1999, "Классика"));
    collection.add(new Blocked("Плохой фильм", "Ужасы", 2021, "Слишком страшный"));

    collection.printAll();

    return 0;
}
