from uuid import uuid4

def generate_id(length=6):
    """
    Generate a random id to append to the slug
    """
    random_id = str(uuid4())
    return random_id[:length]