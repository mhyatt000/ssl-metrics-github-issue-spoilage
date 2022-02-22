from argparse import ArgumentParser, Namespace


def get_args() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="Graph GitHub Issues",
        usage="This program outputs a series of graphs based on GitHub issue data.",
    )
    parser.add_argument(
        "-u",
        "--upper-window-bound",
        help="Argument to specify the max number of days to look at. NOTE: window bounds are inclusive.",
        type=int,
        required=False,
        default=None,
    )
    parser.add_argument(
        "-l",
        "--lower-window-bound",
        help="Argument to specify the start of the window of time to analyze. NOTE: window bounds are inclusive.",
        type=int,
        required=False,
        default=None,
    )
    parser.add_argument(
        "-c",
        "--closed-issues-graph-filename",
        help="The filename of the output graph of closed issues",
        type=str,
        required=False,
        default="closed.png",
    )
    parser.add_argument(
        "-i",
        "--input",
        help="The input JSON file that is to be used for graphing",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-d",
        "--line-of-issues-spoilage-filename",
        help="The filename of the output graph of spoiled issues",
        type=str,
        required=False,
        default="spoilage.png",
    )
    parser.add_argument(
        "-o",
        "--open-issues-graph-filename",
        help="The filename of the output graph of open issues",
        type=str,
        required=False,
        default="open.png",
    )
    parser.add_argument(
        "-x",
        "--joint-graph-filename",
        help="The filename of the joint output graph of open and closed issues",
        type=str,
        required=False,
        default="default.png",
    )

    return parser.parse_args()
