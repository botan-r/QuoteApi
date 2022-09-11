from api import api, app
from api.resources.quote import QuoteResource, QuoteListResource
from api.resources.author import AuthorResource
from config import Config

api.add_resource(QuoteListResource,
                 '/authors/<int:author_id>/quotes',
                 '/quotes'
                 )  # <-- GET
api.add_resource(QuoteResource,
                 '/authors/<int:author_id>/quotes/<int:quote_id>',
                 '/authors/<int:author_id>/quotes'
                 )  # <-- GET/POST/PUT/DELETE
api.add_resource(AuthorResource,
                 '/authors/<int:author_id>',
                 '/authors')  # <-- requests

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)
