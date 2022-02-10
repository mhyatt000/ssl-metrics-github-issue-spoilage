# Software Systems Laboratory Metrics GitHub Issue Spoilage

> A `python` tool to calculate the issue spoilage of a GitHub repository

![[https://img.shields.io/badge/python-3.9.6%20%7C%203.10-blue](https://img.shields.io/badge/python-3.9.6%20%7C%203.10-blue)](https://img.shields.io/badge/python-3.9.6%20%7C%203.10-blue)
[![DOI](https://zenodo.org/badge/427477727.svg)](https://zenodo.org/badge/latestdoi/427477727)
[![Release Project](https://github.com/SoftwareSystemsLaboratory/ssl-metrics-github-issue-spoilage/actions/workflows/release.yml/badge.svg?branch=main)](https://github.com/SoftwareSystemsLaboratory/ssl-metrics-github-issue-spoilage/actions/workflows/release.yml)
![[https://img.shields.io/badge/license-BSD--3-yellow](https://img.shields.io/badge/license-BSD--3-yellow)](https://img.shields.io/badge/license-BSD--3-yellow)

## Table of Contents

- [Software Systems Laboratory Metrics GitHub Issue Spoilage](#software-systems-laboratory-metrics-github-issue-spoilage)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Developer Tooling](#developer-tooling)
    - [Operating System](#operating-system)
  - [How To Use](#how-to-use)
    - [Installation](#installation)
    - [Command Line Arguements](#command-line-arguements)

## About

The Software Systems Laboratory (SSL) GitHub Issue Spoilage Project is a `python` tool to calculate the issue spoilage of a GitHub repository. It is reliant upon the output of the [GitHub Issue](https://github.com/SoftwareSystemsLaboratory/ssl-metrics-github-issues) tool.

This project is licensed under the BSD-3-Clause. See the [LICENSE](LICENSE) for more information.

## Developer Tooling

To maximize the utility of this project and the greater SSL Metrics project, the following software packages are **required**:

### Operating System

All tools developed for the greater SSL Metrics project **must target** Mac OS and Linux. SSL Metrics software is not supported or recommended to run on Windows *but can be modified to do so at your own risk*.

It is recomendded to develop on Mac OS or Linux. However, if you are on a Windows machine, you can use WSL to develop as well.

## How To Use

### Installation

You can install the tool via `pip` with either of the two following one-liners:

- `pip install --upgrade pip ssl-metrics-meta`
- `pip install --upgrade pip ssl-metrics-github-issue-spoilage`

### Command Line Arguements

`ssl-metrics-github-issue-spoilage-graph -h`

```shell
options:
  -h, --help            show this help message and exit
  -u UPPER_WINDOW_BOUND, --upper-window-bound UPPER_WINDOW_BOUND
                        Argument to specify the max number of days to look at. NOTE: window bounds are inclusive.
  -l LOWER_WINDOW_BOUND, --lower-window-bound LOWER_WINDOW_BOUND
                        Argument to specify the start of the window of time to analyze. NOTE: window bounds are inclusive.
  -c CLOSED_ISSUES_GRAPH_FILENAME, --closed-issues-graph-filename CLOSED_ISSUES_GRAPH_FILENAME
                        The filename of the output graph of closed issues
  -i INPUT, --input INPUT
                        The input JSON file that is to be used for graphing
  -d LINE_OF_ISSUES_SPOILAGE_FILENAME, --line-of-issues-spoilage-filename LINE_OF_ISSUES_SPOILAGE_FILENAME
                        The filename of the output graph of spoiled issues
  -o OPEN_ISSUES_GRAPH_FILENAME, --open-issues-graph-filename OPEN_ISSUES_GRAPH_FILENAME
                        The filename of the output graph of open issues
  -x JOINT_GRAPH_FILENAME, --joint-graph-filename JOINT_GRAPH_FILENAME
                        The filename of the joint output graph of open and closed issues
```
