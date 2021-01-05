from userapp import views
from starlette.routing import Route
from ariadne.asgi import GraphQL
from ariadne import make_executable_schema
from userapp.schemas import schema

# mutation.set_field("login", auth_mutations.resolve_login)
# mutation.set_field("logout", auth_mutations.resolve_logout)


routes = [
    # Route("/", views.home, name="home"),
    Route("/graphql", GraphQL(schema, debug=True))
]
