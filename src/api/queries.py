from api.models import Post
from ariadne import convert_kwargs_to_snake_case


def list_posts_resolver(obj, info):
    try:
        posts = [post.to_dict() for post in Post.query.all()]
        print(posts)
        payload = {
            "success": True,
            "posts": posts
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def get_post_resolver(obj, info, post_id):
    try:
        post = Post.query.get(post_id)
        payload = {
            "success": True,
            "post": post.to_dict()
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Post with id {post_id} not found"]
        }

    return payload
