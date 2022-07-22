#!/usr/bin/env python -u
# coding=utf-8

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--version", help="version to be packaged (#.#.#)", default="0.0.0")

if __name__ == "__main__":
    args = vars(parser.parse_args())
    print(args['version'])