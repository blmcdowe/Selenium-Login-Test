import subprocess
import sys

def run_tests():
    """Run pytest tests."""
    try:
        print("Running Selenium login tests with pytest...")
        result = subprocess.run([sys.executable, "-m", "pytest"], check=True)
        if result.returncode == 0:
            print("All tests passed successfully!")
        else:
            print("Some tests failed.")
    except subprocess.CalledProcessError as e:
        print(f"Test run failed: {e}")

if __name__ == "__main__":
    run_tests()
