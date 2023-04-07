from git import Repo
import os
# pip install GitPython
# token = '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'
# g = Github(token)

file_list=os.listdir("/home/dhaman/backups/")
print (file_list)
for i in file_list:
        print(i)
        repo_dir = "/home/dhaman/backups/" + i
        print(repo_dir)
        # file_list1=os.listdir(repo_dir)
        repo = Repo(repo_dir)
        # file_list = ['folder2','folder3','folder4']
        commit_message = 'updates'
        # repo.index.add(file_list1)
        repo.git.add(all = True)
        repo.index.commit(commit_message)
        # repo_name = input("give name of repo")
        origin = repo.remote('origin')
        # origin.push()
        repo.git.push('origin', 'master')