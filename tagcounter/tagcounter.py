from optparse import OptionParser

from console.application import runGet, runView
from gui.application import run


def main():
    parser = OptionParser()
    parser.add_option("--get",
                      dest="get",
                      help="Get the statistic for the resource")
    parser.add_option("--view",
                      dest="view",
                      help="View the statistic for the resource")

    (options, _) = parser.parse_args()

    if options.get is not None:
        runGet(options.get)
    elif options.view is not None:
        runView(options.view)
    else:
        run()


if __name__ == '__main__':
    main()
