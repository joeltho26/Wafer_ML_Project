import os
import argparse
import yaml
import logging



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--config",default="default")
    parser.add_argument("--datasource",default=None)
    parsed_args = parser.parse_args()
    print(parsed_args.config,parsed_args.datasource)