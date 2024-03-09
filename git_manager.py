from datetime import datetime
import git
import time

def commit_and_push():
    repo = git.Repo('.')  # Assuming the script is in the root directory of your Git repository
    repo.git.add('--all')
    commit_message = "Auto commit made by Git script: "+ str(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
    repo.index.commit(commit_message)
    origin = repo.remote(name='origin')
    origin.push('master')
    print(commit_message)

def main():
    while True:
        commit_and_push()
        print("Changes committed and pushed successfully.")
        time.sleep(300)  # Sleep for 5 minutes (300 seconds)

if __name__ == "__main__":
    main()
