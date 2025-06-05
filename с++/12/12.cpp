#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <algorithm> 

using namespace std;

class MovieStatus {
protected:
    string title;
    int year;

public:
    MovieStatus(string t = "Без названия", int y = 0) : title(t), year(y) {}

    virtual ~MovieStatus() {}

    virtual void input() {
        cout << "Введите название фильма: ";
        cin >> ws;
        getline(cin, title);
        cout << "Введите год выпуска: ";
        cin >> year;
    }

    virtual void output() const {
        cout << "Фильм: " << title << ", Год: " << year;
    }

    int getYear() const { return year; } 
};


class Favorite : public MovieStatus {
private:
    string genre;

public:
    Favorite(string t = "Без названия", int y = 0, string g = "Не указан")
        : MovieStatus(t, y), genre(g) {
    }

    void input() override {
        MovieStatus::input();
        cout << "Введите жанр: ";
        cin >> ws;
        getline(cin, genre);
    }

    void output() const override {
        MovieStatus::output();
        cout << ", Жанр: " << genre << endl;
    }

    
    bool operator<(const Favorite& other) const {
        return year < other.year;
    }
};

int main() {
    setlocale(LC_ALL, "rus"); 

    
    vector<Favorite> favorites = {
        Favorite("Интерстеллар", 2014, "Научная фантастика"),
        Favorite("Вверх", 2009, "Мультфильм"),
        Favorite("Начало", 2010, "Фантастика"),
        Favorite("Матрица", 1999, "Фантастика"),
        Favorite("Груз 200", 2009, "Комедия")
    };

    //Сортируем по убыванию года (используем лямбда как компаратор)
    sort(favorites.begin(), favorites.end(), [](const Favorite& a, const Favorite& b) {
        return a.getYear() > b.getYear();
        });

    cout << "Фильмы отсортированы по убыванию года выпуска:\n";
    for (const auto& f : favorites) {
        f.output();
    }

    //Находим первый фильм с годом выпуска > 2010 (лямбда — условие поиска)
    auto it = find_if(favorites.begin(), favorites.end(), [](const Favorite& f) {
        return f.getYear() > 2010;
        });

    if (it != favorites.end()) {
        cout << "\nНайден фильм с годом выпуска > 2010:\n";
        it->output();
    }
    else {
        cout << "\nФильмы с годом выпуска > 2010 не найдены\n";
    }

    //Создаем второй контейнер (список) и копируем туда фильмы с годом > 2010
    list<Favorite> recentFavorites;
    remove_copy_if(favorites.begin(), favorites.end(), back_inserter(recentFavorites),
        [](const Favorite& f) { return f.getYear() <= 2010; }); // Копируем только фильмы с годом > 2010

    cout << "\nФильмы с годом выпуска > 2010 во втором контейнере (list):\n";
    for (const auto& f : recentFavorites) {
        f.output();
    }

    //Сортируем первый контейнер по возрастанию (используется operator <)
    sort(favorites.begin(), favorites.end());

    // Удаляем из первого контейнера фильмы с годом > 2010 (оставляем фильмы с годом <= 2010)
    favorites.erase(remove_if(favorites.begin(), favorites.end(),
        [](const Favorite& f) { return f.getYear() > 2010; }),
        favorites.end());

    // Сортируем второй контейнер (list) по возрастанию (list::sort использует operator <)
    recentFavorites.sort();

    cout << "\nПервый контейнер (фильмы с годом <= 2010), отсортирован по возрастанию:\n";
    for (const auto& f : favorites) {
        f.output();
    }

    cout << "\nВторой контейнер (фильмы с годом > 2010), отсортирован по возрастанию:\n";
    for (const auto& f : recentFavorites) {
        f.output();
    }

    return 0;
}

