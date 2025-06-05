#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>
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

    int getYear() const {
        return year;
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



template <typename T>
class MyArray {
    T* data;
    int capacity;
    int size;

public:
    MyArray(int n) : capacity(n), size(0) {
        data = new T[capacity];
    }

    void add(T element) {
        if (size < capacity) {
            data[size++] = element;
        }
        else {
            cout << "Массив переполнен!" << endl;
        }
    }

    T get(int index) const {
        if (index >= 0 && index < size) {
            return data[index];
        }
        
    }

    T min() const {

        T minElement = data[0];
        for (int i = 1; i < size; ++i) {
            if (data[i] < minElement) {
                minElement = data[i];
            }
        }
        return minElement;
    }

    T max() const {

        T maxElement = data[0];
        for (int i = 1; i < size; ++i) {
            if (data[i] > maxElement) {
                maxElement = data[i];
            }
        }
        return maxElement;
    }

    ~MyArray() {
        delete[] data;
    }
};



template <>
Film* MyArray<Film*>::min() const {
    Film* minFilm = data[0];
    for (int i = 1; i < size; ++i) {
        if (data[i]->getYear() < minFilm->getYear()) {
            minFilm = data[i];
        }
    }
    return minFilm;
}

template <>
Film* MyArray<Film*>::max() const {
    Film* maxFilm = data[0];
    for (int i = 1; i < size; ++i) {
        if (data[i]->getYear() > maxFilm->getYear()) {
            maxFilm = data[i];
        }
    }
    return maxFilm;
}



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
    for (const auto& film : fc.films) {
        film->printInfo();
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
    ++collection;   // Добавляет пустой Favorite
    collection++;   // Добавляет пустой Blocked

    Film* film = collection[0];
    if (film) {
        cout << "\nПервый фильм в коллекции (через []):" << endl;
        film->printInfo();
    }

    cout << collection;

    cout << "\nСоздано объектов (после добавления): " << Film::getTotalObjects() << endl;
    cout << "Объектов в коллекции (после добавления): " << FilmCollection::getStoredObjects() << endl;

    
    cout << "\n=== Шаблон с int ===" << endl;
    MyArray<int> intArr(5);
    intArr.add(5);
    intArr.add(2);
    intArr.add(9);
    cout << "MIN: " << intArr.min() << ", MAX: " << intArr.max() << endl;

    cout << "\n=== Шаблон с char ===" << endl;
    MyArray<char> charArr(4);
    charArr.add('x');
    charArr.add('a');
    charArr.add('m');
    cout << "MIN: " << charArr.min() << ", MAX: " << charArr.max() << endl;

    cout << "\n=== Шаблон с указателями на Film ===" << endl;
    MyArray<Film*> filmArr(3);
    filmArr.add(new Favorite("Inception", "Sci-Fi", 2010, "Крутой фильм"));
    filmArr.add(new Favorite("Avatar", "Fantasy", 2009, "Красивая графика"));
    filmArr.add(new Blocked("Test", "Drama", 2022, "Плохой актёр"));

    cout << "Самый старый фильм:\n";
    filmArr.min()->printInfo();
    cout << "Самый новый фильм:\n";
    filmArr.max()->printInfo();

   
    for (int i = 0; i < 3; ++i) {
        delete filmArr.get(i);
    }

    return 0;
}
