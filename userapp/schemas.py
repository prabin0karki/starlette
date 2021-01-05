from ariadne import ObjectType, QueryType, gql, make_executable_schema
from ariadne import MutationType


mutation = MutationType()


# Define types using Schema Definition Language (https://graphql.org/learn/schema/)
# Wrapping string in gql function provides validation and better error traceback
type_defs = gql(
    """
    type Query {
        user: [User!]!
    }

    type User {
        firstName: String
        lastName: String
        email: String
        fullName: String
    }
"""
)

# Map resolver functions to Query fields using QueryType
query = QueryType()

# Resolvers are simple python functions
@query.field("user")
async def resolve_user(*_):
    return [
        {"firstName": "John", "lastName": "Doe", "email": "Jhon@gmail.com"},
        {"firstName": "Bob", "lastName": "Boberson", "eamil": "Bob@gmail.com"},
    ]


# Map resolver functions to custom type fields using ObjectType
user = ObjectType("User")


@user.field("fullName")
async def resolve_user_fullname(user, *_):
    return "%s %s" % (user["firstName"], user["lastName"])


# Create executable GraphQL schema
schema = make_executable_schema(type_defs, query, user)


type_def = """
    type Mutation {
    createUser(input: UserInput!): UserPayload
}

input UserInput {
    id: ID!
    first_name: String!,
    last_name: String!,
    email: String!,
    password: String!,
}
type DiscussionPayload {
    status: Boolean!
    error: Error
    user: User
}
"""


@mutation.field("createUser")
async def resolve_create_discussion(_, info, input):
    clean_input = {
        "first_name": input["first_name"],
        "last_name": input["last_name"],
        "email": input["email"],
        "password": input["password"],
    }

    print(clean_input)
    try:
        return {
            "status": True,
            "discussion": "Success",
            # "discussion": create_new_discussion(info.context, clean_input),
        }
    except Exception as err:
        return {
            "status": False,
            "error": err,
        }