class ArticleModel:
    def __init__(self, title, author, num_characters, publication, description):
        self.title = title
        self.author = author
        self.num_characters = num_characters
        self.publication = publication
        self.description = description


class ArticleView:
    @staticmethod
    def display_article(article):
        print(f"Title: {article.title}")
        print(f"Author: {article.author}")
        # More print statements for other attributes


class ArticleController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_article_title(self, title):
        self.model.title = title

    # More methods to modify the model

    def display_article(self):
        self.view.display_article(self.model)
