#!/usr/bin/env python3
import unittest
import coverage
import os


def run_tests():
    cov = coverage.Coverage()
    cov.start()
    test_dir = os.path.join(os.path.dirname(__file__), 'source', 'tests')
    if not os.path.exists(test_dir):
        print(f"Error: Test directory not found at {test_dir}")
        return False

    loader = unittest.TestLoader()
    suite = loader.discover(test_dir, pattern='test_*.py')

    print("Running tests...")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    cov.stop()
    cov.save()

    print("\nCoverage Report:")
    cov.report()

    html_dir = 'coverage_report'
    os.makedirs(html_dir, exist_ok=True)
    cov.html_report(directory=html_dir)
    print(f"\nHTML coverage report generated in {html_dir}/index.html")

    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)