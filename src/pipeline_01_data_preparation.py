import os
import argparse
import yaml
import logging

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def main(config_path, datasource):
    config = read_params(config_path)
    print(config)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    default_config = os.path.join("config","params.yaml")
    parser.add_argument("--config",default=default_config)
    parser.add_argument("--datasource",default=None)
    parsed_args = parser.parse_args()
    print(parsed_args.config,parsed_args.datasource)
    main(parsed_args.config,parsed_args.datasource)