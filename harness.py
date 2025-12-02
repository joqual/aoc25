#!/usr/bin/env python3
"""
Harness script for running Advent of Code solutions.
Usage: python3 harness.py <input_file> <solution_file>
"""

import sys
import subprocess
import os
import tempfile
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Run Advent of Code solutions with input files"
    )
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("solution_file", help="Path to the solution file (.cpp or .py)")
    
    args = parser.parse_args()
    input_file = args.input_file
    solution_file = args.solution_file

    # Validate input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file not found: {input_file}", file=sys.stderr)
        sys.exit(1)

    # Validate solution file exists
    if not os.path.exists(solution_file):
        print(f"Error: Solution file not found: {solution_file}", file=sys.stderr)
        sys.exit(1)

    # Determine file extension to identify language
    _, ext = os.path.splitext(solution_file)

    if ext == ".cpp":
        run_cpp(input_file, solution_file)
    else:
        print(f"Error: Unsupported file type: {ext}", file=sys.stderr)
        sys.exit(1)


def run_cpp(input_file, solution_file):
    """Compile and run a C++ solution."""
    # Create temporary executable
    with tempfile.NamedTemporaryFile(suffix="", delete=False) as temp:
        executable = temp.name

    try:
        # Compile
        print(f"Compiling {solution_file}...", file=sys.stderr)
        compile_result = subprocess.run(
            ["g++", "-o", executable, solution_file],
            capture_output=True,
            text=True
        )

        if compile_result.returncode != 0:
            print(f"Compilation failed:", file=sys.stderr)
            print(compile_result.stderr, file=sys.stderr)
            sys.exit(1)

        # Run with input
        print(f"Running solution with input from {input_file}...", file=sys.stderr)
        with open(input_file, "r") as f:
            run_result = subprocess.run(
                [executable],
                stdin=f,
                capture_output=True,
                text=True
            )

        if run_result.returncode != 0:
            print(f"Execution failed:", file=sys.stderr)
            print(run_result.stderr, file=sys.stderr)
            sys.exit(1)

        # Output result
        print(run_result.stdout, end="")

    finally:
        # Clean up temporary executable
        if os.path.exists(executable):
            os.remove(executable)

if __name__ == "__main__":
    main()
