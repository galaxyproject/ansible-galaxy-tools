#!/usr/bin/env python
import argparse
from bioblend import galaxy

def main():
    """
        This script uses bioblend to import .ga workflow files into a running instance of Galaxy
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--workflow_path", help='Path to workflow file')
    parser.add_argument("-g", "--galaxy",
                        dest="galaxy_url",
                        help="Target Galaxy instance URL/IP address (required "
                             "if not defined in the tools list file)",)
    parser.add_argument("-a", "--apikey",
                        dest="api_key",
                        help="Galaxy admin user API key (required if not "
                             "defined in the tools list file)",)
    args = parser.parse_args()
    gi = galaxy.GalaxyInstance(url=args.galaxy_url, key=args.api_key)
    gi.workflows.import_workflow_from_local_path(args.workflow_path)

if __name__ == '__main__':
    main()
