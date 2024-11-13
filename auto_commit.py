import os
from datetime import datetime, timedelta

repo_path = r"C:\Users\user\Desktop\Fake commit\my-fake-commit-repo" # আপনার রিপোজিটরির পাথ
os.chdir(repo_path)

# ৫০টি কমিট করার জন্য লুপ
for i in range(50):
    with open("fake_contribution.txt", "a") as file:
        file.write(f"Fake contribution {i + 1}\n")
    
    os.system("git add fake_contribution.txt")
    commit_message = f"Fake commit {i + 1}"
    commit_date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%dT%H:%M:%S")
    os.system(f'git commit -m "{commit_message}" --date "{commit_date}"')

os.system("git push -u origin main")
