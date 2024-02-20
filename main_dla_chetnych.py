from random import randrange, choice
from datetime import datetime

class Movie():
    def __init__(self, title, created_date, genre, play_count):
        self.title = title
        self.created_date = created_date
        self.genre = genre
        self.play_count = play_count

    def __str__(self):
        return f"{self.title} ({self.created_date})"
    
    def __repr__(self):
        return f"Movie(title={self.title}, created_date=({self.created_date}), genre={self.genre}, play_count={self.play_count})"
    
    def play(self):
        self.play_count += 1

    def panel(self):
        result = "--------------------------\n"
        result += f"{self.title}"
        result += f"({self.created_date})\n"
        result += "--------------------------"
        return result

class Series(Movie):
    def __init__(self, nr_episode, nr_sezon, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nr_episode = nr_episode
        self.nr_sezon = nr_sezon

    def panel(self):
        result = "--------------------------\n"
        result += f"{self.title} ({self.created_date})\n"
        result += f"{self.nr_sezon} {self.nr_episode}\n"
        result += f"Liczba wyswietlen: {self.play_count}\n"
        result += "--------------------------"
        return result
    
    def episode_count(self, schedule_list):
        count = sum(1 for item in schedule_list if isinstance(item, Series))
        print(f"Liczba odcinkow serialu '{self.title}' : {count}")

        return count

def schedule():
    movies_list = []

    movie_1 = Movie(title='Superman', created_date='2024', genre='horror', play_count=300)
    movie_2 = Movie(title='Flash', created_date='2024', genre='horror', play_count=50)
    movie_3 = Movie(title='Hulk', created_date='2024', genre='horror', play_count=100)
    movies_list.extend([movie_1, movie_2, movie_3])

    series_1 = Series(title='Batman', created_date='2019', genre='horror', play_count=400, nr_episode='E06', nr_sezon='S01')
    series_2 = Series(title='Spiderman', created_date='2019', genre='horror', play_count=250, nr_episode='E06', nr_sezon='S01')
    series_3 = Series(title='IronMan', created_date='2019', genre='horror', play_count=350, nr_episode='E06', nr_sezon='S01')
    movies_list.extend([series_1, series_2, series_3])
    
    return movies_list

def get_movies(schedule_list):
    return [movie for movie in schedule_list if isinstance(movie, Movie) and not isinstance(movie, Series)]

def get_series(schedule_list):
    return [series for series in schedule_list if isinstance(series, Series)]

def search(schedule_list, get_title):
    return [movie for movie in schedule_list if movie.title == get_title]

def get_title():
    get_title = input("Wpisz tytul: ")
    get_title = get_title.capitalize()
    search_result = search(schedule_list, get_title)

    for result in search_result:
        print(result)

def generate_views(schedule_list):
    rand = randrange(0, 101, 1)
    item = choice(schedule_list)
  
    if isinstance(item, Movie):
        item.play_count = rand
    elif isinstance(item, Series):
        item.play_count = rand

    return item.play_count

def generate_views_10x():
    schedule_list_rand = []
    for i in range(10):
        rand_item = generate_views(schedule_list)
        schedule_list_rand.append(rand_item)

    return schedule_list_rand

def top_titles(n):
    top_titles_list = schedule()
    top_titles_list.sort(key=lambda movie : movie.play_count, reverse=True)

    return top_titles_list[:n]

def full_sezon(sezon_title, creation_date, genre, nr_sezon, nr_episode_to_add):
    episodes = []
    for i in range(1, nr_episode_to_add + 1):
        episode_title = f"{sezon_title} S{nr_sezon} E{i:02d}"
        episode = Movie(title=episode_title, created_date=creation_date, genre=genre, play_count=0)
        episodes.append(episode)

    return episodes

schedule_list = schedule()
schedule_list.sort(key=lambda a : a.title)

generate_views_10x()

print("Biblioteka filmów")
movies = get_movies(schedule_list)
print("Movies: ")
for movie in movies:
    print(movie.panel())

series = get_series(schedule_list)
print("\nSeries: ")
for serie in series:
    print(serie.panel())

#search(schedule_list, get_title())
    
current_date = datetime.now().date()
formatted_date = current_date.strftime("%d.%m.%Y")
print("Najpopularniejsze filmy i seriale dnia:", formatted_date)

top_items = top_titles(3)
for top in top_items:
    print(top.panel())

print()
print("Sezon The Walking Dead")
episodes = full_sezon('The Walking Dead', '2004', 'horror', 1, 10)
for episode in episodes:
    print(episode.panel())
