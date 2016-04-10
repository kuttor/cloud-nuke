#!/usr/bin/env python
"""Usage: cloud-nuke --file list_of_cf_stacks

Arguments:
    --file  <input file>

Options:
    --dryrun executes kill request as a test, doesn't actually execute
"""
from docopt import docopt
import boto3


def main():
    try:
        # parse arguments, use file docstring as a parameter definition
        arguments = docopt.docopt(__doc__)

        # file is a mandatory
        filename = int(arguments['--file'])

        # dryrun is optional
        dryrun = int(arguments['--dryrun'])

    except docopt.DocoptExit as e:
        print e.message

    if dryrun == True:
        print "do this"
    else:
        print "do that"


def delete_stack(stack):
    client = boto3.client('cloudformation')


response = client.delete_stack(
    StackName=stack,
)

return response

if __name__ == "__main__":
    main()
