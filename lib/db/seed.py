from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed():
    # Create authors
    a1 = Author("Alice")
    a1.save()
    a2 = Author("Bob")
    a2.save()

    # Create magazines
    m1 = Magazine("Tech Today", "Technology")
    m1.save()
    m2 = Magazine("Health Weekly", "Health")
    m2.save()

    # Create articles
    art1 = Article("Python Tips", a1.id, m1.id)
    art1.save()
    art2 = Article("Healthy Living", a2.id, m2.id)
    art2.save()

if __name__ == "__main__":
    seed()