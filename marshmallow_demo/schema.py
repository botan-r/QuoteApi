from marshmallow import Schema, fields, validate, post_load
from tmp.author import Author


# Схема сериализации
# JSON --> dict --> object
# И Десериализацмм
# Object --> dict --> JSON
class AuthorSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    email = fields.Email()

    @post_load
    def make_user(self, data, **kwargs):
        return Author(**data)

#                                      .to_dict()       Flask
# Сериализация: obj --> text. ObjModel ----------> dict -----> JSON

#                                    reqparser        class Model
# Десериализация: text --> obj. JSON ----------> dict ---------> ObjModel

# Сериализаторы: Marshmallow / Pydantic
