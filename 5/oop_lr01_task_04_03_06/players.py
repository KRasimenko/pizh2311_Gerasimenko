from abc import ABC, abstractmethod
from typing import Optional


class Player(ABC):
    """
    Абстрактный базовый класс для всех типов плееров.
    Содержит общие поля и методы, которые наследуются потомками.
    """

    def __init__(self, name: str):
        """
        Инициализирует плеер с именем.

        :param name: Имя плеера (например, 'Sony Audio Player')
        """
        self._name = name  # защищенное поле
        self.__is_playing = False  # закрытое поле

    @abstractmethod
    def запустить(self, media: Optional[str] = None) -> None:
        """
        Абстрактный метод запуска воспроизведения.
        Должен быть переопределён в дочерних классах.

        :param media: Имя медиафайла (может быть None по умолчанию)
        """
        pass

    @abstractmethod
    def остановить(self) -> None:
        """
        Абстрактный метод остановки воспроизведения.
        Должен быть переопределён в дочерних классах.
        """
        pass

    def _set_playing(self, state: bool) -> None:
        """
        Внутренний метод для установки состояния воспроизведения.

        :param state: True — плеер воспроизводит, False — остановлен
        """
        self.__is_playing = state

    def _is_playing(self) -> bool:
        """
        Проверяет текущее состояние плеера.

        :return: True, если воспроизводится, иначе False
        """
        return self.__is_playing


class AudioPlayer(Player):
    """
    Класс для аудиоплеера. Наследуется от Player.
    """

    def __init__(self, name: str):
        """
        Инициализация аудиоплеера с заданным именем.

        :param name: Название плеера
        """
        super().__init__(name)
        self.volume = 50  # публичное поле громкости

    def запустить(self, media: Optional[str] = "аудиофайл.mp3") -> None:
        """
        Запускает воспроизведение аудиофайла.

        :param media: Имя аудиофайла
        """
        self._set_playing(True)
        print(f"[AudioPlayer] Воспроизведение аудио: {media} (громкость: {self.volume})")

    def остановить(self) -> None:
        """
        Останавливает аудиоплеер.
        """
        self._set_playing(False)
        print("[AudioPlayer] Аудио остановлено.")


class VideoPlayer(Player):
    """
    Класс для видеоплеера. Наследуется от Player.
    """

    def __init__(self, name: str):
        """
        Инициализация видеоплеера с заданным именем.

        :param name: Название плеера
        """
        super().__init__(name)
        self.resolution = "1920x1080"  # публичное поле разрешения

    def запустить(self, media: Optional[str] = "видео.mp4") -> None:
        """
        Запускает воспроизведение видео.

        :param media: Имя видеофайла
        """
        self._set_playing(True)
        print(f"[VideoPlayer] Воспроизведение видео: {media} (разрешение: {self.resolution})")

    def остановить(self) -> None:
        """
        Останавливает воспроизведение видео.
        """
        self._set_playing(False)
        print("[VideoPlayer] Видео остановлено.")


class DvdPlayer(Player):
    """
    Класс для DVD-плеера. Наследуется от Player.
    """

    def __init__(self, name: str):
        """
        Инициализация DVD-плеера с заданным именем.

        :param name: Название плеера
        """
        super().__init__(name)
        self.__current_position = 0  # закрытое поле позиции
        self._disk_loaded = None     # защищённое поле — текущий диск

    def запустить(self, media: Optional[str] = "Фильм на DVD") -> None:
        """
        Запускает воспроизведение DVD-диска.

        :param media: Название вставленного диска
        """
        self._disk_loaded = media
        self._set_playing(True)
        print(f"[DVDPlayer] Запущен диск: {media} с позиции {self.__current_position} сек.")

    def остановить(self) -> None:
        """
        Останавливает воспроизведение и сохраняет текущую позицию.
        """
        self.__current_position += 60  # имитация проигрывания
        self._set_playing(False)
        print(f"[DVDPlayer] Проигрывание остановлено. Позиция сохранена: {self.__current_position} сек.")

    def извлечь_диск(self) -> None:
        """
        Извлекает диск, если он вставлен.
        """
        if self._disk_loaded:
            print(f"[DVDPlayer] Диск \"{self._disk_loaded}\" извлечен.")
            self._disk_loaded = None
        else:
            print("[DVDPlayer] Нет вставленного диска.")