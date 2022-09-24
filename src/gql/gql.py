from flask import Blueprint
from flask import request, jsonify


from ariadne import make_executable_schema, load_schema_from_path, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML

from api.queries import list_posts_resolver, get_post_resolver
from api.mutations import create_post_resolver, update_post_resolver, delete_post_resolver


query = ObjectType("Query")
mutation = ObjectType("Mutation")

query.set_field("listPosts", list_posts_resolver)
query.set_field("getPost", get_post_resolver)

mutation.set_field("createPost", create_post_resolver)
mutation.set_field("updatePost", update_post_resolver)
mutation.set_field("deletePost", delete_post_resolver)

type_definition = load_schema_from_path("schema.graphql")


schema = make_executable_schema(
    type_definition, query, mutation, snake_case_fallback_resolvers
)

gql = Blueprint('gql', __name__, template_folder='templates')


@gql.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@gql.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code
