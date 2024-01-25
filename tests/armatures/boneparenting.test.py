# GPL License

import unittest
import sys
import bpy


class TestAddon(unittest.TestCase):
    def test_boneparenting(self):
        bpy.ops.cats_armature.fix()
        bpy.ops.cats_root.refresh_root_list()
        bpy.ops.cats_root.create_root()



suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAddon)
runner = unittest.TextTestRunner()
ret = not runner.run(suite).wasSuccessful()
sys.exit(ret)