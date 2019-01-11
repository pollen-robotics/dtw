import unittest


class ImportTestCase(unittest.TestCase):
    def test_import(self):
        import dtw

    def test_has_version(self):
        from dtw import __version__
