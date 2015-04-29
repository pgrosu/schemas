"""
Runs tests that ensure protocol invariants
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest

import utils
import process_schemas


class TestProcessSchemas(unittest.TestCase):

    protocolDefinitionsPath = "tests/_protocol_definitions.py"

    def testProcessSchemas(self):
        # create the protocol definitions file and run a syntax check on it
        args = self._makeArgs()
        schemaProcessor = process_schemas.SchemaProcessor(args)
        try:
            schemaProcessor.run()
        finally:
            schemaProcessor.cleanup()
        utils.runCommand("flake8 {}".format(self.protocolDefinitionsPath))

    def _makeArgs(self):
        class FakeArgs(object):
            pass
        args = FakeArgs()
        args.outputFile = self.protocolDefinitionsPath
        args.version = "test"
        args.avro_tools_jar = None
        args.inputSchemasDirectory = "src/main/resources/avro/"
        args.verbose = 2
        return args
