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
    static int objectCount;  

public:
    Film(string t, string g, int y) : title(t), genre(g), year(y) {
        objectCount++;  
    }

    virtual void printInfo() const = 0;

    static int getObjectCount() {  
        return objectCount;
    }

    virtual ~Film() {
        objectCount--;  
    }
};


int Film::objectCount = 0;

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
    static int collectionCount; 

public:
    void add(Film* film) {
        films.push_back(film);
        collectionCount++;  
    }

    void printAll() const {
        cout << "=== Коллекция фильмов ===" << endl;
        for (const auto& film : films) {
            film->printInfo();
        }
    }

    static int getCollectionCount() {
        return collectionCount;
    }

    ~FilmCollection() {
        for (auto f : films) {
            delete f;
            collectionCount--;  
        }
    }
};


int FilmCollection::collectionCount = 0;

int main() {
    setlocale(LC_ALL, "rus");

    
    cout << "Всего объектов фильмов: " << Film::getObjectCount() << endl;
    cout << "Фильмов в коллекции: " << FilmCollection::getCollectionCount() << endl;

    
    FilmCollection collection;
    collection.add(new Favorite("Интерстеллар", "Фантастика", 2014, "Любимый фильм"));
    collection.add(new Blocked("Очень страшное кино", "Комедия", 2000, "Не нравится юмор"));
    collection.add(new Favorite("Матрица", "Фантастика", 1999, "Классика"));
    collection.add(new Blocked("Плохой фильм", "Ужасы", 2021, "Слишком страшный"));

    cout << "\n=== После добавления фильмов ===" << endl;
    collection.printAll();

    
    cout << "\nВсего объектов фильмов: " << Film::getObjectCount() << endl;
    cout << "Фильмов в коллекции: " << FilmCollection::getCollectionCount() << endl;

    return 0;
}
