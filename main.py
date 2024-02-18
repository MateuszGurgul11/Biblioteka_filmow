class Film():
    def __init__(self, title, created_date, genre, play_count):
        self.title = title
        self.created_date = created_date
        self.genre = genre
        self.play_count = play_count

        self.current_play_count = 0

    def __str__(self):
        return f"{self.title} {self.created_date} {self.genre} {self.play_count}"
    
    def __repr__(self):
        return f"Film(title={self.title}, created_date={self.created_date}, genre={self.genre}, play_count={self.play_count})"
    
    def play(self):
        self.current_play_count += 1

class Series(Film):
    def __init__(self, nr_episode, nr_sezon, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nr_episode = nr_episode
        self.nr_sezon = nr_sezon