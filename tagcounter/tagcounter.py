from optparse import OptionParser

from console.application import runGet, runView, runAppendSynonym
from gui.application import run


def main():
    parser = OptionParser()
    parser.add_option("--get",
                      dest="get",
                      help="Get the statistic for the resource")
    parser.add_option("--view",
                      dest="view",
                      help="View the statistic for the resource")
    parser.add_option("--shortname",
                      dest="shortName",
                      help="Append short name for the resource")
    parser.add_option("--fullname",
                      dest="fullName",
                      help="Append full name for the resource")

    (options, _) = parser.parse_args()

    if options.get is not None:
        runGet(options.get)
    elif options.view is not None:
        runView(options.view)
    elif options.shortName is not None and options.fullName is not None:
        runAppendSynonym(options.shortName, options.fullName)
    else:
        run()


if __name__ == '__main__':
    main()
