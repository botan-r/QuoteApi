from tmp.author import Author
from tmp.schema import AuthorSchema

author = Author("1", "Alex", "testmail.ru")

serialize_schema = AuthorSchema()
data = serialize_schema.dump(author)
print(f"{data=}")