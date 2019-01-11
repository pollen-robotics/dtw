import unittest


class ImportTestCase(unittest.TestCase):
    def test_import(self):
        import dtw
        from dtw import dtw as dist
        from dtw import accelerated_dtw

    def test_has_version(self):
        from dtw import __version__
