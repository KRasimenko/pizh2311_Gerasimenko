#include <iostream>
#include <string>
using namespace std;

class MovieStatus {
protected:
    string title;
    int year;

public:
    MovieStatus(string t = "Без названия", int y = 0) : title(t), year(y) {
        cout << "Вызван конструктор MovieStatus\n";
    }

    virtual ~MovieStatus() {
        cout << "Вызван деструктор MovieStatus\n";
    }

    virtual void input() {
        cout << "Введите название фильма: ";
        cin >> ws;
        getline(cin, title);
        cout << "Введите год выпуска: ";
        cin >> year;
    }

    virtual void output() const {
        cout << "Фильм: " << title << ", Год: " << year << endl;
    }
};
class Favorite : public MovieStatus {
private:
    string genre;

public:
    Favorite(string t = "Без названия", int y = 0, string g = "Не указан")
        : MovieStatus(t, y), genre(g) {
        cout << "Вызван конструктор Favorite\n";
    }

    ~Favorite() {
        cout << "Вызван деструктор Favorite\n";
    }

    void input() override {
        MovieStatus::input();
        cout << "Введите жанр: ";
        cin >> ws;
        getline(cin, genre);
    }

    void output() const override {
        MovieStatus::output();
        cout << "Жанр: " << genre << endl;
    }
};
class Blocked : public MovieStatus {
private:
    string reason;

public:
    Blocked(string t = "Без названия", int y = 0, string r = "Не указана")
        : MovieStatus(t, y), reason(r) {
        cout << "Вызван конструктор Blocked\n";
    }

    ~Blocked() {
        cout << "Вызван деструктор Blocked\n";
    }

    void input() override {
        MovieStatus::input();
        cout << "Введите причину блокировки: ";
        cin >> ws;
        getline(cin, reason);
    }

    void output() const override {
        MovieStatus::output();
        cout << "Причина блокировки: " << reason << endl;
    }
};
int main() {
    setlocale(LC_ALL, "rus");

    MovieStatus baseMovie("Матрица", 1999);
    Favorite favMovie("Начало", 2010, "Фантастика");
    Blocked blkMovie("Ужастик", 2001, "Слишком страшный");

    cout << "\nВывод объектов напрямую:\n";
    baseMovie.output();
    favMovie.output();
    blkMovie.output();


    cout << "\nМассив из базового класса:\n";
    MovieStatus* movies[3];
    movies[0] = new MovieStatus("Терминатор", 1984);
    movies[1] = new Favorite("Аватар", 2009, "Фэнтези");
    movies[2] = new Blocked("Фильм Х", 2020, "Нарушение авторских прав");

    for (int i = 0; i < 3; i++) {
        movies[i]->output();
        cout << endl;
    }


    for (int i = 0; i < 3; i++) {
        delete movies[i];
    }


    cout << "\n🔸 Массив объектов Favorite:\n";
    Favorite favArray[2] = {
        Favorite("Интерстеллар", 2014, "Научная фантастика"),
        Favorite("Вверх", 2009, "Мультфильм")
    };

    for (int i = 0; i < 2; i++) {
        favArray[i].output();
        cout << endl;
    }
    return 0;
}
