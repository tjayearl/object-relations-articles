from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed():
    a1 = Author("Tjay")
    a1.save()

    m1 = Magazine("Tech Weekly", "Technology")
    m1.save()

    art1 = Article("Python Tips", a1.id, m1.id)
    art1.save()

if __name__ == "__main__":
    seed()
