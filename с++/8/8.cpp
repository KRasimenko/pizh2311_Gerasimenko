
#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>
using namespace std;


class MyCustomError : public runtime_error {
public:
    MyCustomError(const string& msg) : runtime_error(msg) {}
};

class AnotherCustomError : public logic_error {
public:
    AnotherCustomError(const string& msg) : logic_error(msg) {}
};


class Film {
protected:
    string title;
    string genre;
    int year;

private:
    static int totalObjects;

public:
    Film(string t, string g, int y) : title(t), genre(g), year(y) {
        if (year < 1888) throw invalid_argument("Неверный год выпуска фильма!");
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
            << ". Причина: " << reason << endl;
    }
};

// === Шаблонный класс массива ===
template <typename T>
class MyArray {
    T* data;
    int capacity;
    int size;

public:
    MyArray(int n) : capacity(n), size(0) {
        if (n <= 0) throw length_error("Размер массива должен быть положительным!");
        data = new T[capacity];
    }

    void add(T element) {
        if (size < capacity) {
            data[size++] = element;
        }
        else {
            throw out_of_range("Массив переполнен!");
        }
    }

    T get(int index) const {
        if (index >= 0 && index < size) {
            return data[index];
        }
        else {
            throw out_of_range("Неверный индекс массива!");
        }
    }

    T min() const {
        if (size == 0) throw runtime_error("Массив пуст!");
        T minElement = data[0];
        for (int i = 1; i < size; ++i) {
            if (data[i] < minElement) {
                minElement = data[i];
            }
        }
        return minElement;
    }

    T max() const {
        if (size == 0) throw runtime_error("Массив пуст!");
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
    if (size == 0) throw runtime_error("Массив фильмов пуст!");
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
    if (size == 0) throw runtime_error("Массив фильмов пуст!");
    Film* maxFilm = data[0];
    for (int i = 1; i < size; ++i) {
        if (data[i]->getYear() > maxFilm->getYear()) {
            maxFilm = data[i];
        }
    }
    return maxFilm;
}

// === Класс коллекции фильмов ===
class FilmCollection {
    vector<Film*> films;
    static int storedObjects;

public:
    void add(Film* film) {
        if (!film) throw MyCustomError("Попытка добавить nullptr в коллекцию!");
        films.push_back(film);
        storedObjects++;
    }

    void printAll() const {
        cout << "=== Коллекция фильмов ===" << endl;
        for (const auto& film : films) film->printInfo();
    }

    static int getStoredObjects() { return storedObjects; }

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
        throw out_of_range("Индекс вне диапазона коллекции!");
    }

    friend ostream& operator<<(ostream& os, const FilmCollection& fc);

    ~FilmCollection() {
        for (auto f : films) delete f;
    }
};

int FilmCollection::storedObjects = 0;

ostream& operator<<(ostream& os, const FilmCollection& fc) {
    os << "=== Вывод через << ===" << endl;
    for (const auto& film : fc.films) film->printInfo();
    return os;
}

int main() {
    try {
        setlocale(LC_ALL, "rus");

        
        try {
            Film* f = new Favorite("Старый фильм", "Драма", 1800, "Невозможно");
            delete f;
        }
        catch (const invalid_argument& e) {
            cout << "[Ошибка invalid_argument]: " << e.what() << endl;
        }

        
        try {
            MyArray<int> badArr(0);  
        }
        catch (const length_error& e) {
            cout << "[Ошибка length_error]: " << e.what() << endl;
        }

       
        try {
            MyArray<int> testArr(2);
            testArr.add(10);
            testArr.add(20);
            testArr.add(30);  // Переполнение
        }
        catch (const out_of_range& e) {
            cout << "[Ошибка out_of_range]: " << e.what() << endl;
        }

        
        try {
            MyArray<int> emptyArr(2);
            emptyArr.min();  // Нельзя взять минимум из пустого массива
        }
        catch (const runtime_error& e) {
            cout << "[Ошибка runtime_error]: " << e.what() << endl;
        }

        
        try {
            FilmCollection coll;
            coll.add(nullptr);  // Специально подаём nullptr
        }
        catch (const MyCustomError& e) {
            cout << "[Моя ошибка]: " << e.what() << endl;
        }

        // === Проверка: AnotherCustomError (искусственно) ===
        try {
            throw AnotherCustomError("Проверка AnotherCustomError");
        }
        catch (const AnotherCustomError& e) {
            cout << "[Другая моя ошибка]: " << e.what() << endl;
        }

        
        try {
            throw 42;
        }
        catch (const int& x) {
            cout << "[Перехвачено исключение int]: " << x << endl;
        }

        try {
            throw string("Ошибка типа string");
        }
        catch (const string& msg) {
            cout << "[Перехвачено исключение string]: " << msg << endl;
        }

       
        FilmCollection collection;
        collection + new Favorite("Интерстеллар", "Фантастика", 2014, "Любимый фильм");
        collection + new Blocked("Очень страшное кино", "Комедия", 2000, "Не нравится юмор");
        ++collection; // Добавляет пустой Favorite
        collection++; // Добавляет пустой Blocked

        cout << collection;

        try {
            Film* film = collection[100];  // Нарушение диапазона
            film->printInfo();
        }
        catch (const exception& e) {
            cout << "[Локальная ошибка доступа к элементу]: " << e.what() << endl;
        }

    }
    catch (...) {
        cout << "=== Перехвачено неизвестное исключение ===" << endl;
    }

    return 0;
}

