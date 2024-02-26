class Movie:
    def __init__(self,name,genre,minutes,rating) -> None:
        self.name = name 
        self.genre= genre
        self.minutes= minutes
        self.rating = rating
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
        return
    @property
    def genre(self):
        return self.__genre
    @genre.setter
    def genre(self,genre):
        self.__genre = genre
        return
    @property
    def minutes(self):
        return self.__minutes
    @minutes.setter
    def minutes(self,minutes):
        self.__minutes = minutes
        return
    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def __rating(self,rating):
        self.__rating = rating
        return
    pass