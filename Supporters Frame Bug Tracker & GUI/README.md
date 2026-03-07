# SupportersFrame Bug Report Manager

A lightweight desktop tool built in Python + Tkinter to view, add, edit, and visualize bug reports found during manual QA testing of https://supportersframe.com/.

![Bug Report Viewer Screenshot](https://drive.google.com/uc?export=view&id=1J2nocaUSfx_b2C0T165Ig4plyIPI2tZo)
  

## Features
- View all 34 discovered bugs in a clean, sortable table
- See severity distribution chart (Low / Medium / High)
- Add new bugs directly from the UI
- Minimal, user-friendly interface
- Export-ready format for QA reports or Jira/Excel import

## Bugs Discovered (Summary)
Tested on desktop + mobile viewports. Found **34 issues** including:

- High severity: Broken password confirmation logic, duplicate account creation with same email, silent login failures, exposed editing tools to external users, incorrect supporter count display
- Medium severity: Missing required field indicators, inconsistent navigation, filter inconsistencies, image resolution validation bypass
- Low severity: UI/alt text issues, placeholder text reliance, missing language support

Full list available in `Supporters_Frame_Bug_Report.xlsx`

## Tech Stack
- Python 3
- Tkinter (GUI)
- Matplotlib (embedded chart)
- Pandas (optional – for future Excel read/write)

## How to Run
```bash
# Option 1: Run Python script directly
python bug_report_viewer.py

# Option 2: Run the .sh launcher (Linux/macOS)
chmod +x bug_report_viewer.sh
./bug_report_viewer.sh
