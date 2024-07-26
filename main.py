from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import FOAF, XSD

from utils.parseArguments import AppArgumentParser
from utils.utils import example_01, example_02, example_03

def main():
    args = AppArgumentParser().parse_args()
    if args.example == 1:
        example_01()
    elif args.example == 2:
        example_02()
    elif args.example == 3:
        example_03()

if __name__ == "__main__":
    main()
example_02()
