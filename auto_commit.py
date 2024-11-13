import os
from datetime import datetime, timedelta

# রিপোজিটরির পাথটি নির্ধারণ করুন
repo_path = r"C:\Users\user\Desktop\Fake commit\my-fake-commit-repo"  # আপনার রিপোজিটরির পাথটি এখানে দিন
os.chdir(repo_path)

# প্রথম কমিটের তারিখ নির্ধারণ করুন
start_date = datetime.now() - timedelta(days=50)

# ৫০টি কমিট করার জন্য লুপ
for i in range(50):
    # ফাইলটি আপডেট করে নতুন কমিটের জন্য পরিবর্তন যোগ করুন
    with open("auto_fake_file.txt", "a") as file:
        file.write(f"Fake commit number {i + 1}\n")
    
    # ফাইল স্টেজ করুন
    os.system("git add auto_fake_file.txt")
    
    # কাস্টম তারিখ সহ কমিট করুন
    commit_date = start_date + timedelta(days=i)
    commit_message = f"Auto fake commit {i + 1}"
    commit_date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
    os.system(f'git commit -m "{commit_message}" --date "{commit_date_str}"')

# সব কমিট পুশ করুন
os.system("git push -u origin main")
