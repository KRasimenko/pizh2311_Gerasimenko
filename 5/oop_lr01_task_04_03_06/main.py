# Программирование на языке высокого уровня (Python).
# Задание №______. Вариант !!!
#
# Выполнил: Фамилия И.О.
# Группа: !!!
# E-mail: !!!

from players import AudioPlayer, VideoPlayer, DvdPlayer
def main():
    print("=== Тест аудиоплеера ===")
    audio = AudioPlayer("Sony Audio")
    audio.запустить("музыка.mp3")
    audio.остановить()

    print("\n=== Тест видеоплеера ===")
    video = VideoPlayer("LG Video")
    video.запустить("фильм.mp4")
    video.остановить()

    print("\n=== Тест DVD-плеера ===")
    dvd = DvdPlayer("Panasonic DVD")
    dvd.запустить("Matrix DVD")
    dvd.остановить()
    dvd.извлечь_диск()

if __name__ == "__main__":
    main()
