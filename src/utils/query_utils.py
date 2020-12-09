import os


def get_query(name, *args):
    script_dir = os.path.dirname(__file__)
    rel_path = "queries/" + name + ".graphql"
    abs_file_path = os.path.join(script_dir, rel_path)
    abs_file_path = abs_file_path.replace("utils", "services")
    with open(abs_file_path, "r") as f:
        q = f.read()
    return q % args
