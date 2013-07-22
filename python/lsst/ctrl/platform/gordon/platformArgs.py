class OptionalArgs:

    def __init__(self, parser):
        parser.add_argument("-n", "--node-set", action="store",
                    default=None, dest="nodeSet", 
                    help="name of collection of nodes to use", required=True)

    def addCommandLineInfo(self, opts, defaults):
        if opts.nodeSet is None:
            defaults["NODE_SET"] = ""
        else:
            defaults["NODE_SET"] = opts.nodeSet
