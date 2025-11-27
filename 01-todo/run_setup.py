import subprocess
import sys

def run_command(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    return result.returncode

# Run makemigrations
print("=" * 50)
print("Creating migrations...")
print("=" * 50)
run_command("uv run python manage.py makemigrations")

# Run migrate
print("\n" + "=" * 50)
print("Applying migrations...")
print("=" * 50)
run_command("uv run python manage.py migrate")

# Run tests
print("\n" + "=" * 50)
print("Running tests...")
print("=" * 50)
run_command("uv run python manage.py test")
