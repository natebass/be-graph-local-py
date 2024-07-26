import argparse


def AppArgumentParser() -> argparse.ArgumentParser:
    """
    Create an argument parser for processing RDF data.

    Returns:
        argparse.ArgumentParser: The argument parser object.
    """
    parser = argparse.ArgumentParser(description="Process some RDF data.")
    # parser.add_argument('-f', type=int, choices=[1, 2, 3], required=True, help="Choose which example to run: 1, 2, or 3")
    parser.add_argument('-f', type=str, required=False, help="Parse RDF or n3 file.")
    
    # parser.add_argument('integers', metavar='N', type=int, nargs='+', required=False,
    #                     help='an integer for the accumulator')
    
    # parser.add_argument('--sum', dest='accumulate', action='store_const', required=False,
    #                     const=sum, default=max,
    #                     help='sum the integers (default: find the max)')
    
    return parser