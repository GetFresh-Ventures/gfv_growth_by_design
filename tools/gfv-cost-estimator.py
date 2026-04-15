#!/usr/bin/env python3
import os
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 gfv-cost-estimator.py <file_or_directory>")
        sys.exit(1)

    target = sys.argv[1]

    if not os.path.exists(target):
        print(f"Error: {target} is not a valid file or directory")
        sys.exit(1)

    chars = 0
    if os.path.isdir(target):
        print(f"Scanning directory: {target}")
        for root, dirs, files in os.walk(target):
            # Ignore hidden directories like .git
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for file in files:
                if file.startswith('.'):
                    continue
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        chars += len(f.read())
                except Exception:
                    pass
    elif os.path.isfile(target):
        print(f"Scanning file: {target}")
        try:
            with open(target, "r", encoding="utf-8", errors="ignore") as f:
                chars = len(f.read())
        except Exception as e:
            print(f"Error reading file {target}: {e}")
            sys.exit(1)

    tokens = chars // 4
    cost_estimate = (tokens / 1000000) * 3.0

    print("-" * 48)
    print(f"📊 Token Estimate: ~{tokens} tokens")
    print(f"💰 Estimated Cost: ~${cost_estimate:.4f} USD (assuming $3/1M input pricing)")
    print("-" * 48)
    print("If this cost is high (> $1.00), consider pre-filtering your CRM data using Python scripts before passing to the Agent.")

if __name__ == "__main__":
    main()
