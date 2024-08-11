class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title 
        Article.all.append(self)
        if self.magazine not in Magazine.all_magazines:
            Magazine.all_magazines[self.magazine] = []
        Magazine.all_magazines[self.magazine].append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            raise AttributeError("Cannot modify title after it is set")
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        else:
            raise ValueError("Title must be a string between 5 and 50 characters inclusive")


class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            raise AttributeError("Cannot modify name after it is set")
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be of string value, and has at least 1 character")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = {article.magazine.category for article in self.articles()}
        return list(topics) if topics else None


class Magazine:
    all_magazines = {}
    
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name  
        self.category = category  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return Magazine.all_magazines.get(self, [])

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_article_count = {}
        for article in self.articles():
            if article.author in author_article_count:
                author_article_count[article.author] += 1
            else:
                author_article_count[article.author] = 1
        
        contributing_authors = [author for author, count in author_article_count.items() if count > 2]
        
        return contributing_authors if contributing_authors else None
