violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

songs_time = 0
count = 1
song_count = int(input('Сколько песен выбрать? '))
while song_count > 0:
    song_name = input(f'Название {count} песни: ')
    songs_time += float(violator_songs[song_name])
    song_count -= 1
    count += 1

print(f'Общее время звучания песен: {round(songs_time, 2)} минуты')


