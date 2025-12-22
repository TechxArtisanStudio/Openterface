#!/usr/bin/env python3
"""
Wrapper script to manage update counting and list generation.
This script runs both count_updates.py and generate_updates_list.py in sequence.
"""

import sys
from pathlib import Path

# Add the update-tools directory to the path so we can import the modules
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))

# Import the main functions from both scripts
from count_updates import main as count_updates_main
from generate_updates_list import main as generate_updates_main


def main():
    """Run both update scripts in sequence."""
    print("=" * 70)
    print("Update Management Script")
    print("=" * 70)
    
    # Step 1: Count updates and update mkdocs.yml
    print("\n" + "=" * 70)
    print("Step 1: Counting updates and updating mkdocs.yml")
    print("=" * 70)
    try:
        count_updates_main()
        print("\n✅ Step 1 completed successfully")
    except SystemExit as e:
        if e.code != 0:
            print(f"\n❌ Step 1 failed with exit code {e.code}")
            sys.exit(e.code)
        print("\n✅ Step 1 completed successfully")
    except Exception as e:
        print(f"\n❌ Step 1 failed with error: {e}")
        sys.exit(1)
    
    # Step 2: Generate updates lists
    print("\n" + "=" * 70)
    print("Step 2: Generating updates lists")
    print("=" * 70)
    try:
        generate_updates_main()
        print("\n✅ Step 2 completed successfully")
    except SystemExit as e:
        if e.code != 0:
            print(f"\n❌ Step 2 failed with exit code {e.code}")
            sys.exit(e.code)
        print("\n✅ Step 2 completed successfully")
    except Exception as e:
        print(f"\n❌ Step 2 failed with error: {e}")
        sys.exit(1)
    
    print("\n" + "=" * 70)
    print("✅ All update management tasks completed successfully")
    print("=" * 70)


if __name__ == "__main__":
    main()

