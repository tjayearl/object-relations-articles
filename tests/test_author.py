from lib.models.author import Author

def test_author_creation_and_find():
    author = Author("Alice")
    author.save()
    found = Author.find_by_id(author.id)
    assert found.name == "Alice"
