#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# GUI setup
root = tk.Tk()
root.title("Supporters Frame - Bug Report Manager")
root.geometry("1000x800")
root.configure(bg="#f0f4f8")

# Main title
title_label = tk.Label(root, text="Supporters Frame - Bug Report Manager", font=("Helvetica", 18, "bold"), bg="#f0f4f8", fg="#1a1a1a")
title_label.pack(pady=10)

# Table for bug reports
frame_table = tk.Frame(root)
frame_table.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Style for Treeview
style = ttk.Style()
style.configure("Treeview", rowheight=25, font=("Helvetica", 10))
style.configure("Treeview.Heading", font=("Helvetica", 11, "bold"))

tree = ttk.Treeview(frame_table, columns=("ID", "Title", "Severity"), show='headings')
tree.heading("ID", text="Bug ID")
tree.heading("Title", text="Bug Title")
tree.heading("Severity", text="Severity")
tree.column("ID", width=70, anchor='center')
tree.column("Title", width=600)
tree.column("Severity", width=100, anchor='center')
tree.pack(fill=tk.BOTH, expand=True)

# Plot frame
frame_chart = tk.Frame(root)
frame_chart.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

fig = plt.Figure(figsize=(6,3))
canvas = FigureCanvasTkAgg(fig, master=frame_chart)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Hardcoded bug reports
bug_reports = [
    {"Bug ID":"B-01","Bug Title":"Broken / Placeholder Images on Homepage","Steps to Reproduce":"1. Open supportersframe.com\n2. Scroll to Trending section","Expected Result":"Campaign and profile images should load correctly","Actual Result":"Image placeholders or missing images are shown","Severity":"Medium"},
    {"Bug ID":"B-02","Bug Title":"UI Rendering Shows Image Text Instead of Proper Layout","Steps to Reproduce":"1. Visit homepage\n2. Observe campaign cards","Expected Result":"Cards should render images and text in proper format","Actual Result":"Text like 'Image: Campaign cover' is visible","Severity":"Low"},
    {"Bug ID":"B-03","Bug Title":"Missing Validation or Helper Text in Campaign Creation Form","Steps to Reproduce":"1. Go to /create/campaign\n2. Observe input fields","Expected Result":"Clear validation and helper text should be present","Actual Result":"No visible validation hints or required indicators","Severity":"Low"},
    {"Bug ID":"B-04","Bug Title":"Inconsistent CTA Text Styling","Steps to Reproduce":"1. Visit homepage\n2. Observe primary CTA","Expected Result":"CTA text should be consistent and descriptive","Actual Result":"CTA text is generic and inconsistent in style","Severity":"Low"},
    {"Bug ID":"B-05","Bug Title":"Potential Broken or Non-Functional Navigation Links","Steps to Reproduce":"1. Click menu items under Discover/Resources/Company","Expected Result":"Links should navigate to valid pages","Actual Result":"Some links may not navigate or lack URLs","Severity":"Medium"},
    {"Bug ID":"B-06","Bug Title":"Missing or Improper Alt Text for Images","Steps to Reproduce":"1. Inspect images on homepage","Expected Result":"Images should have meaningful alt text","Actual Result":"Alt text is missing or non-descriptive","Severity":"Low"},
    {"Bug ID":"B-07","Bug Title":"Password Updated Without Confirmation Match","Steps to Reproduce":"1. Go to Profile\n2. Account Settings\n3. Enter new password\n4. Leave confirm password empty or mismatched\n5. Click Update","Expected Result":"Password update should fail with validation error","Actual Result":"Password updates successfully without confirmation match","Severity":"High"},
    {"Bug ID":"B-08","Bug Title":"Required Fields Not Indicated for Password & Email","Steps to Reproduce":"1. Open Account Settings\n2. Observe password and email fields","Expected Result":"Required fields should be marked clearly","Actual Result":"No required field indicators are shown","Severity":"Medium"},
    {"Bug ID":"B-09","Bug Title":"Email Updates Even When Same Email Is Re-entered","Steps to Reproduce":"1. Open Account Settings\n2. Enter same signup email\n3. Confirm and update","Expected Result":"System should block or show 'no change' message","Actual Result":"Email update succeeds with unchanged email","Severity":"Low"},
    {"Bug ID":"B-10","Bug Title":"Account Upgrade Feature Not Working","Steps to Reproduce":"1. Navigate to Upgrade Account section\n2. Click upgrade button","Expected Result":"Upgrade process should start","Actual Result":"Nothing happens","Severity":"High"},
    {"Bug ID":"B-11","Bug Title":"Image Resolution Validation Not Enforced","Steps to Reproduce":"Upload profile or banner image with wrong resolution","Expected Result":"Upload should fail with resolution error","Actual Result":"Upload succeeds without validation","Severity":"Medium"},
    {"Bug ID":"B-12","Bug Title":"Leaderboard Filters Show Same Data","Steps to Reproduce":"1. Go to Leaderboard\n2. Switch between 7 days/30 days/All","Expected Result":"Each filter should show different data","Actual Result":"All filters show same list","Severity":"Medium"},
    {"Bug ID":"B-13","Bug Title":"Leaderboard User Profiles Expose Editing Tools","Steps to Reproduce":"1. Open leaderboard\n2. Click any user profile\n3. Open photos","Expected Result":"Profiles should be view-only","Actual Result":"Editing tools are visible","Severity":"High"},
    {"Bug ID":"B-14","Bug Title":"Leaderboard Photo Editing Controls Not Working","Steps to Reproduce":"1. Add text to photo\n2. Try bold/italic/underline/remove","Expected Result":"Controls should work properly","Actual Result":"Controls do not function","Severity":"Medium"},
    {"Bug ID":"B-15","Bug Title":"Campaign Page Exposes Photo Editing Tools to External Users","Steps to Reproduce":"1. Create and share campaign\n2. Open as external user","Expected Result":"Campaign should be view-only","Actual Result":"Photo editing UI appears","Severity":"High"},
    {"Bug ID":"B-16","Bug Title":"Incorrect Supporter Count for New Creator","Steps to Reproduce":"1. Create new campaign\n2. View supporter count","Expected Result":"Supporter count should be zero","Actual Result":"System shows 100 supporters","Severity":"High"},
    {"Bug ID":"B-17","Bug Title":"Campaign & Creator Filters Return Same Results","Steps to Reproduce":"1. Go to Campaigns or Creators\n2. Switch filters","Expected Result":"Different filters should show different results","Actual Result":"All filters return same content","Severity":"Medium"},
    {"Bug ID":"B-18","Bug Title":"Footer Navigation Links Not Working","Steps to Reproduce":"Click footer links (For Creators, Media Assets, About, Contact)","Expected Result":"Links should navigate to respective pages","Actual Result":"Links do not respond","Severity":"Medium"},
    {"Bug ID":"B-19","Bug Title":"Social Share Icons Redirect Incorrectly","Steps to Reproduce":"Click each campaign share icon","Expected Result":"Each icon should redirect to correct platform","Actual Result":"Multiple icons redirect to same page","Severity":"Medium"},
    {"Bug ID":"B-20","Bug Title":"Footer Copyright Links Redirect Incorrectly","Steps to Reproduce":"Click copyright-related footer links","Expected Result":"Links should behave as intended","Actual Result":"All redirect to Bangla Puzzle page","Severity":"Low"},
    {"Bug ID":"B-21","Bug Title":"Search Feature Does Not Work","Steps to Reproduce":"1. Enter any search query\n2. Click search","Expected Result":"Search results or validation should appear","Actual Result":"Nothing happens","Severity":"High"},
    {"Bug ID":"B-22","Bug Title":"Profile Settings Visible Only on Mobile","Steps to Reproduce":"View site on desktop and mobile","Expected Result":"Profile settings should appear on all devices","Actual Result":"Visible only on mobile","Severity":"Medium"},
    {"Bug ID":"B-23","Bug Title":"Animation Missing on Mobile","Steps to Reproduce":"Open site on desktop and mobile","Expected Result":"Animation behavior should be consistent","Actual Result":"Animation missing on mobile","Severity":"Low"},
    {"Bug ID":"B-24","Bug Title":"Duplicate Accounts Created With Same Email","Steps to Reproduce":"1. Sign up using same email twice\n2. Login and view profile","Expected Result":"Duplicate registration should be blocked","Actual Result":"Different accounts appear with same email","Severity":"High"},
    {"Bug ID":"B-25","Bug Title":"Signup Allows Password Mismatch","Steps to Reproduce":"1. Enter different password and confirm password\n2. Submit signup","Expected Result":"Signup should fail with validation error","Actual Result":"Signup succeeds without error","Severity":"High"},
    {"Bug ID":"B-26","Bug Title":"Signup Redirects Without Logging In","Steps to Reproduce":"1. Complete signup form\n2. Submit","Expected Result":"User should be logged in or verified","Actual Result":"Redirected to homepage without login","Severity":"High"},
    {"Bug ID":"B-27","Bug Title":"No Verification Email or OTP Sent After Signup","Steps to Reproduce":"1. Register new account\n2. Check email inbox","Expected Result":"Verification email should be sent","Actual Result":"No email or OTP received","Severity":"High"},
    {"Bug ID":"B-28","Bug Title":"Login Without Password Redirects Silently","Steps to Reproduce":"1. Enter email only\n2. Click login","Expected Result":"Validation error should appear","Actual Result":"Redirects to homepage without error","Severity":"High"},
    {"Bug ID":"B-29","Bug Title":"Invalid Login Attempts Fail Without Error Message","Steps to Reproduce":"1. Enter wrong credentials\n2. Click login","Expected Result":"Error message should appear","Actual Result":"Silent failure occurs","Severity":"High"},
    {"Bug ID":"B-30","Bug Title":"Authentication Fields Lack Required Indicators","Steps to Reproduce":"Open login/signup pages","Expected Result":"Required fields should be marked","Actual Result":"No required field indicators","Severity":"Medium"},
    {"Bug ID":"B-31","Bug Title":"No Language / Translation Support for Bangla Users","Steps to Reproduce":"Open site Look for language selector","Expected Result":"Language options should include Bangla","Actual Result":"No translation or language switcher available","Severity":"Medium"},
    {"Bug ID":"B-32","Bug Title":"Forms Lack Proper Titles and Rely on Placeholder Text","Steps to Reproduce":"Open any form Observe labels and titles","Expected Result":"Forms should have clear titles and labels","Actual Result":"Forms have no titles and minimal placeholders","Severity":"Medium"},
    {"Bug ID":"B-33","Bug Title":"No Indication of Required vs Optional Fields Across Forms","Steps to Reproduce":"Open forms Observe input fields","Expected Result":"Required and optional fields should be clearly distinguished","Actual Result":"No indication provided anywhere","Severity":"High"},
    {"Bug ID":"B-34","Bug Title":"Inconsistent Required Field Rules for Similar Inputs","Steps to Reproduce":"Compare username/password fields across pages","Expected Result":"Same inputs should follow consistent validation rules","Actual Result":"Some fields required in one place but optional elsewhere","Severity":"High"}
]

# Functions
def update_table():
    for row in tree.get_children():
        tree.delete(row)
    for bug in bug_reports:
        tree.insert("", tk.END, values=(bug["Bug ID"], bug["Bug Title"], bug["Severity"]))
    update_chart()

def update_chart():
    severities = [b["Severity"] for b in bug_reports]
    counts = {s: severities.count(s) for s in ["Low","Medium","High"]}
    fig.clear()
    ax = fig.add_subplot(111)
    colors = ['green','orange','red']
    bars = ax.bar(counts.keys(), counts.values(), color=colors)
    ax.set_title("Bug Severity Distribution", color='blue')
    ax.set_ylabel("Count")
    # Add labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1, '%d' % int(height), ha='center', va='bottom', fontsize=10)
    canvas.draw()

def add_bug():
    bug_id = entry_id.get().strip()
    title = entry_title.get().strip()
    steps = entry_steps.get("1.0", tk.END).strip()
    expected = entry_expected.get("1.0", tk.END).strip()
    actual = entry_actual.get("1.0", tk.END).strip()
    severity = severity_var.get()
    if not bug_id or not title or not severity:
        messagebox.showerror("Error", "Bug ID, Title, and Severity are required!")
        return
    bug_reports.append({
        "Bug ID": bug_id,
        "Bug Title": title,
        "Steps to Reproduce": steps,
        "Expected Result": expected,
        "Actual Result": actual,
        "Severity": severity
    })
    update_table()
    clear_inputs()

def clear_inputs():
    entry_id.delete(0, tk.END)
    entry_title.delete(0, tk.END)
    entry_steps.delete("1.0", tk.END)
    entry_expected.delete("1.0", tk.END)
    entry_actual.delete("1.0", tk.END)
    severity_var.set("Low")

# Inputs frame
frame_inputs = tk.Frame(root, bg="#dbe7f3", bd=2, relief=tk.RIDGE)
frame_inputs.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

tk.Label(frame_inputs, text="Bug ID:", bg="#dbe7f3").grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry_id = tk.Entry(frame_inputs, width=15)
entry_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Bug Title:", bg="#dbe7f3").grid(row=0, column=2, padx=5, pady=5, sticky='e')
entry_title = tk.Entry(frame_inputs, width=40)
entry_title.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_inputs, text="Severity:", bg="#dbe7f3").grid(row=0, column=4, padx=5, pady=5, sticky='e')
severity_var = tk.StringVar(value="Low")
severity_options = ttk.Combobox(frame_inputs, textvariable=severity_var, values=["Low","Medium","High"], width=10)
severity_options.grid(row=0, column=5, padx=5, pady=5)

tk.Label(frame_inputs, text="Steps to Reproduce:", bg="#dbe7f3").grid(row=1, column=0, padx=5, pady=5, sticky='nw')
entry_steps = tk.Text(frame_inputs, width=30, height=4)
entry_steps.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Expected Result:", bg="#dbe7f3").grid(row=1, column=2, padx=5, pady=5, sticky='nw')
entry_expected = tk.Text(frame_inputs, width=30, height=4)
entry_expected.grid(row=1, column=3, padx=5, pady=5)

tk.Label(frame_inputs, text="Actual Result:", bg="#dbe7f3").grid(row=1, column=4, padx=5, pady=5, sticky='nw')
entry_actual = tk.Text(frame_inputs, width=30, height=4)
entry_actual.grid(row=1, column=5, padx=5, pady=5)

tk.Button(frame_inputs, text="Add Bug Report", bg="#4CAF50", fg="white", command=add_bug).grid(row=2, column=0, columnspan=6, pady=10)

# Populate table on launch
update_table()

root.mainloop()

