class Movie():
    def __init__(self, title, created_date, genre, play_count):
        self.title = title
        self.created_date = created_date
        self.genre = genre
        self.play_count = play_count

        self.current_play_count = 0

    def __str__(self):
        return f"{self.title} {self.created_date} {self.genre} {self.play_count}"
    
    def __repr__(self):
        return f"Movie(title={self.title}, created_date={self.created_date}, genre={self.genre}, play_count={self.play_count})"
    
    def play(self):
        self.current_play_count += 1

    def panel(self):
        result = "--------------------------\n"
        result += f"{self.title}\n"
        result += f"{self.created_date} {self.genre} {self.play_count}\n"
        result += "--------------------------"
        return result

class Series(Movie):
    def __init__(self, nr_episode, nr_sezon, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nr_episode = nr_episode
        self.nr_sezon = nr_sezon

    def panel(self):
        result = "--------------------------\n"
        result += f"{self.title}\n"
        result += f"{self.created_date} {self.genre} {self.play_count}\n"
        result += f"{self.nr_sezon} {self.nr_episode}\n"
        result += "--------------------------"
        return result

def schedule():
    movies_list = []

    for i in range(3):
        movie = Movie(title='Superman', created_date='2024-12-3', genre='horror', play_count='200')
        movies_list.append(movie)

    for i in range(3):
        series = Series(title='Batman', created_date='2024-12-3', genre='horror', play_count='200', nr_episode='E06', nr_sezon='S01')
        movies_list.append(series)
        
    for movie in movies_list:
        if isinstance(movie, Movie):
            movie.panel()
        elif isinstance(movie, Series):
            movie.panel()
    
    return movies_list

def get_movies(schedule_list):
    return [movie for movie in schedule_list if isinstance(movie, Movie)]

def get_series(schedule_list):
    return [series for series in schedule_list if isinstance(series, Series)]

schedule_list = schedule()
movies = get_movies(schedule_list)
print("Movies: ")
for movie in movies:
    print(movie.panel())

series = get_series(schedule_list)
print("Series: ")
for serie in series:
    print(serie.panel())