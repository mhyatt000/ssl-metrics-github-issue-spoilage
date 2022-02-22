import json
from argparse import ArgumentParser, Namespace
from datetime import datetime
from os.path import exists
from typing import Any

import matplotlib.pyplot as plt
from dateutil.parser import parse
from intervaltree import IntervalTree
from matplotlib.figure import Figure
from progress.spinner import MoonSpinner
from tqdm import tqdm


from args import get_args


def issue_processor(filename: str) -> list:

    issues, data = [], []

    try:
        with open(file=filename, mode="r") as file:
            issues: list = json.load(file)
            file.close()
    except FileNotFoundError:
        print(f"{filename} does not exist.")
        quit(4)

    day0: datetime = parse(issues["created_at"]["0"]).replace(tzinfo=None)
    dayN: datetime = datetime.today().replace(tzinfo=None)

    for i in range(len(list((issues)))):
        value: dict = {
            "issue_number": issues["number"][str(i)],
            "created_at": issues["created_at"][str(i)],
            "created_at_day": None,
            "closed_at": None,
            "closed_at_day": None,
            "state": issues["state"][str(i)],
        }

        if issues["closed_at"][str(i)] is None:
            value["closed_at"] = dayN.strftime("%Y-%m-%dT%H:%M:%SZ")
        else:
            value["closed_at"] = issues["closed_at"][str(i)]

        createdAtDay: datetime = parse(issues["created_at"][str(i)]).replace(
            tzinfo=None
        )

        value["created_at_day"] = (createdAtDay - day0).days

        if value["state"] == "open":
            value["closed_at_day"] = (dayN - day0).days
        else:
            value["closed_at_day"] = (
                parse(issues["closed_at"][str(i)]).replace(tzinfo=None) - day0
            ).days

        data.append(value)

    return data


def createIntervalTree(data: list) -> IntervalTree:
    tree: IntervalTree = IntervalTree()

    for issue in tqdm(data):
        begin: int = issue["created_at_day"]
        end: int = issue["closed_at_day"]

        try:
            issue["endDayOffset"] = 0
            tree.addi(begin=begin, end=end, data=issue)
        except ValueError:
            issue["endDayOffset"] = 1
            tree.addi(begin=begin, end=end + 1, data=issue)

    return tree


def issue_spoilage_data(data: IntervalTree):

    # startDay: int = data.begin()
    endDay: int = data.end()
    spoilage_values, intervals = [], []

    '''TODO: what about 0?'''
    for i in range(endDay):
        if i == 1:
            temp_set = data.overlap(0, 1)
            proc_overlap = []
            for issue in temp_set:
                # if issue.data["state"] == "open":
                #     proc_overlap.append(issue)
                if issue.begin != issue.end - 1 and issue.data["endDayOffset"] != 1:
                    proc_overlap.append(issue)
                    # intervals.append(issue.end - startDay)
            spoilage_values.append(
                {
                    "day": i + 1,
                    "number_open": len(proc_overlap),
                    "intervals": intervals,
                }
            )
        else:
            temp_set = data.overlap(i - 1, i)

            '''can change the step size by making the -1 a variable and
            chaning the top if statement overlap to 0, step size'''

            proc_overlap = []

            for issue in temp_set:
                # if issue.data["state"] == "open":
                #     proc_overlap.append(issue)
                if issue.begin != issue.end - 1 and issue.data["endDayOffset"] != 1:
                    proc_overlap.append(issue)
                    # intervals.append(issue.end - startDay)
            spoilage_values.append(
                {"day": i + 1, "number_open": len(proc_overlap), "intervals": intervals}
            )

    return spoilage_values


def shrink_graph(keys=None):
    '''window method ... see ssl-graph'''

    args: Namespace = getArgparse()

    xmax = args.upper_window_bound if args.upper_window_bound else len(keys)
    xmin = args.lower_window_bound if args.lower_window_bound else 0

    '''TODO: window needs to be on data not plt'''
    plt.xlim(xmin, xmax)


def plot(*, data: list, filename: str, graph_type):

    quit() if graph_type not in ["Spoiled", "Open", "Closed"] else None

    figure: Figure = plt.figure()

    plt.set(title=f"Number of {graph_type} Issues Per Day", xlabel="Day", ylabel="Number of Issues")
    plt.plot(data.keys(), data.values())
    shrink_graph(keys=keys)

    figure.savefig(filename)


def fillDictBasedOnKeyValue(dictionary: dict, tree: IntervalTree, key: str, value: Any) -> dict:

    data: dict = {}

    for x in range(min(dictionary.keys()), max(dictionary.keys())):
        try:
            data[x] = dictionary[x]
        except KeyError:
            count = 0
            interval: IntervalTree
            for interval in tree.at(x):
                if interval.data[key] == value:
                    count += 1
            data[x] = count

    return data


def main() -> None:

    args = get_args()

    if args.input[-5::] != ".json":
        print("Invalid input file type. Input file must be JSON")
        quit(1)

    jsonData: list = issue_processor(filename=args.input)
    tree: IntervalTree = createIntervalTree(data=jsonData, filename=args.input)

    startDay: int = tree.begin()
    endDay: int = tree.end()

    if len(tree.at(endDay)) == 0:
        endDay -= 1

    baseDict = {startDay: len(tree.at(startDay)), endDay: len(tree.at(endDay))}

    openIssues: dict = fillDictBasedOnKeyValue(
        dictionary=baseDict, tree=tree, key="state", value="open"
    )

    closedIssues: dict = fillDictBasedOnKeyValue(
        dictionary=baseDict, tree=tree, key="state", value="closed"
    )

    new_list: list = issue_spoilage_data(data=tree)

    '''plots:'''

    plot(data=openIssues, filename=args.open_issues_graph_filename, graph_type="Open")
    plot(data=closedIssues, filename=args.closed_issues_graph_filename graph_type="Closed")
    plot(data=new_list, filename=args.line_of_issues_spoilage_filename, graph_type="Spoiled")


if __name__ == "__main__":
    main()
