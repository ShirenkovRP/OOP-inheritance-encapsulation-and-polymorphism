# Задача №2 "Аудиоколлекция"

class Track:
    def __init__(self, name, time_minute):
        self.name = name
        self.time_minute = time_minute
    
    # вывод информации
    def get_name(self):
        return self.name

    def get_time_minute(self):
        return self.time_minute
        
    def __str__(self):
        return self.name + " - " + str(self.time_minute) + " минут"

    def __gt__(self, other):
        return self.time_minute > other.time_minute
    

class Album:
    def __init__(self, name, tracks):
        self.name = name
        self.tracks = tracks

    # get_tracks - выводит информацию по всем трекам(используется метод show).
    def get_tracks(self):
        return self.tracks

    # add_track - добавление нового трека в список треков.
    def add_track(self):
        name_track = input("Введите название трека : ").title()
        time_track = int(input("Введите длительность трека: "))
        track = Track(name_track, time_track)
        self.tracks.append(track)
        
    def __str__(self):
        list_traks = "\nСписок треков: \n"
        total = 0 
        for track in self.tracks:
            list_traks += "\t" + track.get_name() + " - " + str(track.get_time_minute()) + " минут\n"
            total += track.get_time_minute()
        return "\nНазвание альбома: " + self.name + list_traks + "Продолжительнсть альбома" + str(total) + " минут"
        
            

audio_collection = {"Альбом_1": Album("Альбом_1", [Track("Ночь", 4), Track("Весна", 5), Track("Дождь", 3)]),
                    "Альбом_2": Album("Альбом_2", [Track("Пирожки", 1), Track("Осень", 2), Track("Туман", 4)])}


def main():
    chose = get_chose()
    while chose != 5:
        if chose == 1:
            create_album(audio_collection)
        elif chose == 2:
            create_track(audio_collection)
        elif chose == 3:            
            album_list(audio_collection)
        elif chose == 4:            
            comparison(audio_collection)        
        else:
            print("Такого пункта нет в меню")
        chose = get_chose()
    

def get_chose():
    
    print("""
            1 - добавить новый альбом
            2 - добавить треки в альбом
            3 - вывести список треков
                и длительность альбома
            4 - найти самый длинный трек
                в альбоме
            5 - выход""")
    chose = int(input("Выберите пункт меню: "))
    return chose


def album_list(arg_1):
    name_album = input("Введите названиеальбома: ").title()
    if name_album in arg_1:
        print(audio_collection[name_album])
    else:
        print(f"Нет альбома с названием {name_album}")


def create_album(arg_1):
    name_album = input("Введите названиеальбома: ").title()
    if name_album not in arg_1:
        arg_1[name_album] = Album(name_album, [])
        track_num = int(input("Сколько треков в альбоме: "))
        for i in range(0, track_num):
            arg_1[name_album].add_track()

    else:
        print(f"Альбом с названием {name_album} уже есть")
        print(f"Попробуйте другое имя")


def create_track(arg_1):
    name_album = input("Введите названиеальбома: ").title()
    if name_album in arg_1:
        track_num = int(input("Сколько треков хотите добавить: "))
        for i in range(0, track_num):
            arg_1[name_album].add_track()
        
    else:
        print(f"Альбом с названием {name_album} не существует")
        print(f"Попробуйте другое имя")        

def comparison(arg_1): # Сравнение длительности треков
    cost = Track("0", 0)
    name_album = input("Введите названиеальбома: ").title()
    for track in arg_1[name_album].get_tracks():
        if cost > track:
            cost
        else:
            cost = track
    print(f"Самый длинный трек в альбоме: {cost}")
main()

