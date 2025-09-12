import os
import subprocess
import sys

# IMPORTANT: The path below has been updated to the location you provided.
GIT_EXECUTABLE_PATH = r"C:\Program Files\Git\mingw64\bin\git.exe"


def get_latest_day_folder(path='.'):
    """Detects and returns the latest 'Day_X' folder and its number."""
    try:
        folders = [f for f in os.listdir(path) if f.startswith('Day_') and os.path.isdir(f)]
        if not folders:
            return None, None
        folders.sort(key=lambda x: int(x.split('_')[1]))
        latest_folder = folders[-1]
        day_number = int(latest_folder.split('_')[1])
        return latest_folder, day_number
    except Exception as e:
        print(f"⚠️ An error occurred while detecting folders: {e}", file=sys.stderr)
        return None, None


def generate_readme(folders):
    """Generates the README.md content as a string."""
    table_rows = []
    for i, folder in enumerate(folders, start=1):
        name = folder.replace('_', ' ').replace('Day ', '').title()
        status = '✅' if os.path.isdir(folder) else '❌'
        table_rows.append(f"| {i} | {name} | {status} |")

    # Add the next day's placeholder
    next_day_number = len(folders) + 1
    table_rows.append(f"| {next_day_number} | [Next Challenge Name] | ❌ |")

    folders_list_md = "\n".join([f"- `{folder}`" for folder in folders])

    readme_content = f"""# Daily Python Challenges 🐍

Welcome to my Python practice repository!  
I solve **one coding challenge per day** to improve my Python skills, from basics to advanced.

---

## Progress Tracker

| Day | Challenge Name | Status |
|-----|----------------|--------|
{''.join(table_rows)}

---

## Folder Structure
Each folder contains the Python file(s) for that day’s challenge:

{folders_list_md}

## About Me
I am practicing Python daily and sharing my progress here to build my programming skills and portfolio.
"""
    return readme_content


def run_git_command(command_parts, folder=None):
    """Runs a git command with error handling."""
    # Prepend the absolute path to the git executable
    command_parts = [GIT_EXECUTABLE_PATH] + command_parts
    print(f"  - Running: {' '.join(command_parts)}...")
    try:
        if folder:
            result = subprocess.run(command_parts, check=True, cwd=folder, capture_output=True, text=True)
        else:
            result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        print(f"    ✅ Success.")
        return result
    except subprocess.CalledProcessError as e:
        print(f"    ❌ Error running command: {e.cmd}", file=sys.stderr)
        print(f"       STDOUT: {e.stdout}", file=sys.stderr)
        print(f"       STDERR: {e.stderr}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(f"❌ Could not find Git executable at '{GIT_EXECUTABLE_PATH}'. Please check the path.", file=sys.stderr)
        sys.exit(1)


def main():
    print("🚀 Starting Git automation...")

    # Get all Day folders
    all_folders = [f for f in os.listdir('.') if f.startswith('Day_') and os.path.isdir(f)]
    if not all_folders:
        print("⚠️ No Day_ folders found! Make sure your challenge folders exist.")
        sys.exit()

    all_folders.sort(key=lambda x: int(x.split('_')[1]))

    # Get info on the latest folder
    latest_folder, day_number = get_latest_day_folder()
    if not latest_folder:
        sys.exit()  # Exit if no folder was found

    day_name = latest_folder.replace('_', ' ').replace('Day ', '').title()
    print(f"📂 Detected latest folder: {latest_folder} (Day {day_number}: {day_name})")

    # Build and write README.md
    print("📝 Generating README.md...")
    readme_content = generate_readme(all_folders)
    # The fix: open the file with explicit UTF-8 encoding
    try:
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print("✅ README.md updated successfully!")
    except Exception as e:
        print(f"❌ Failed to write README.md: {e}", file=sys.stderr)
        sys.exit(1)

    # Git add, commit, push
    print("📤 Running Git commands...")
    run_git_command(['add', latest_folder])
    run_git_command(['add', 'README.md'])

    commit_message = f"Day {day_number}: {day_name} added and README updated"
    run_git_command(['commit', '-m', commit_message])
    run_git_command(['push'])

    print("🎯 All done! Changes pushed to GitHub.")


if __name__ == "__main__":
    main()