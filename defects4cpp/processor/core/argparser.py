import argparse
from os import getcwd

from taxonomy import MetaData, Taxonomy


class ValidateProject(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        t = Taxonomy()
        if values not in t.keys():
            raise KeyError(f"Taxonomy '{values}' does not exist")
        setattr(namespace, self.dest, t[values])


class ValidateIndex(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        try:
            metadata: MetaData = namespace.metadata
        except AttributeError:
            raise AttributeError(
                f"project is not set, but {__class__.__name__} is invoked first"
            )

        if len(metadata.defects) < values:
            raise IndexError(f"invalid index '{values}' of defects")

        setattr(namespace, self.dest, values)


def create_taxonomy_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--project",
        required=True,
        help="specified project",
        dest="metadata",
        action=ValidateProject,
    )
    parser.add_argument(
        "-n",
        "--no",
        type=int,
        required=True,
        help="specified bug number",
        dest="index",
        action=ValidateIndex,
    )
    parser.add_argument(
        "-b",
        "--buggy",
        dest="buggy",
        help="whether buggy version or not",
        action="store_true",
    )
    # 'dest', 'root', 'workspace', 'checkout_directory'...
    parser.add_argument(
        "-t",
        "--target",
        dest="workspace",
        type=str,
        default=f"{getcwd()}",
        help="checkout directory",
    )
    return parser
