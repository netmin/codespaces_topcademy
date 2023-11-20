class FilmModel:
    def __init__(self, title, genre, director, release_year, duration, studio, actors):
        self.title = title
        # More attributes...


class FilmView:
    @staticmethod
    def display_film(film):
        ...


class FilmController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        ...

    def display_film(self):
        self.view.display_film(self.model)
