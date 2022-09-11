from author import Author
from schema import AuthorSchema
from marshmallow.exceptions import ValidationError

json_data = """
[
   {
       "id": 1,
       "name": "Alex",
       "email": "alex@mail.ru"
   },
   {
       "id": 2,
       "name": "Ivan",
       "email": "ivan@mail.ru"
   },
   {
       "id": 4,
       "name": "Tom",
       "email": "tom@mail.ru"
   }
]
"""


schema = AuthorSchema(many=True)
try:
    authors = schema.loads(json_data)
    # authors = []
    # for author_dict in authors_dict:
    #     author = Author(**author_dict)
    #     authors.append(author)
    # print(result)
    # author = Author(**result)
    print(authors)
except ValidationError as e:
    print(e)
