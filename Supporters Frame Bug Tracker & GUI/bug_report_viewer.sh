#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo -e "\033[1;34mLaunching Bug Report Viewer...\033[0m\n"
python3 "$SCRIPT_DIR/bug_report_viewer.py"
