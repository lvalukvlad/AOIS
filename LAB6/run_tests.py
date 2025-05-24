import unittest
import coverage

if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()

    loader = unittest.TestLoader()
    suite = loader.discover('app')
    runner = unittest.TextTestRunner()
    runner.run(suite)

    cov.stop()
    cov.save()
    cov.report()
    cov.html_report(directory='coverage_report')