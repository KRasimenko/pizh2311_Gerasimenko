#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Film {
protected:
    string title;
    string genre;
    int year;

private:
    static int totalObjects;

public:
    Film(string t, string g, int y) : title(t), genre(g), year(y) {
        totalObjects++;
    }

    virtual void printInfo() const = 0;

    virtual ~Film() {
        totalObjects--;
    }

    static int getTotalObjects() {
        return totalObjects;
    }
};

int Film::totalObjects = 0;

class Favorite : public Film {
    string comment;
public:
    Favorite(string t, string g, int y, string c)
        : Film(t, g, y), comment(c) {
    }

    
    Favorite() : Film("Без названия", "Без жанра", 2000), comment("Нет комментария") {}

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

    
    Blocked() : Film("Без названия", "Без жанра", 2000), reason("Без причины") {}

    void printInfo() const override {
        cout << "[Заблокировано] " << title << " (" << year << "), жанр: " << genre
            << ". Причина блокировки: " << reason << endl;
    }
};

class FilmCollection {
    vector<Film*> films;
    static int storedObjects;

public:
    void add(Film* film) {
        films.push_back(film);
        storedObjects++;
    }

    void printAll() const {
        cout << "=== Коллекция фильмов ===" << endl;
        for (const auto& film : films) {
            film->printInfo();
        }
    }

    static int getStoredObjects() {
        return storedObjects;
    }

    
    FilmCollection& operator+(Film* film) {
        add(film);
        return *this;
    }

    
    FilmCollection& operator++() {
        add(new Favorite());
        return *this;
    }

    
    FilmCollection& operator++(int) {
        add(new Blocked());
        return *this;
    }

    
    Film* operator[](size_t index) {
        if (index < films.size()) return films[index];
        return nullptr;
    }

    friend ostream& operator<<(ostream& os, const FilmCollection& fc);

    ~FilmCollection() {
        for (auto f : films) delete f;
    }
};

int FilmCollection::storedObjects = 0;


ostream& operator<<(ostream& os, const FilmCollection& fc) {
    os << "=== Вывод через << ===" << endl;
    for (size_t i = 0; i < fc.films.size(); ++i) {
        fc.films[i]->printInfo();
    }
    return os;
}

int main() {
    setlocale(LC_ALL, "rus");

    cout << "Создано объектов (изначально): " << Film::getTotalObjects() << endl;
    cout << "Объектов в коллекции (изначально): " << FilmCollection::getStoredObjects() << endl;

    FilmCollection collection;

    
    collection + new Favorite("Интерстеллар", "Фантастика", 2014, "Любимый фильм");
    collection + new Blocked("Очень страшное кино", "Комедия", 2000, "Не нравится юмор");

    
    ++collection;

    
    collection++;

    
    Film* film = collection[0];
    if (film) {
        cout << "\nПервый фильм в коллекции (через []):" << endl;
        film->printInfo();
    }

    
    

    cout << "\nСоздано объектов (после добавления): " << Film::getTotalObjects() << endl;
    cout << "Объектов в коллекции (после добавления): " << FilmCollection::getStoredObjects() << endl;

    return 0;
}
