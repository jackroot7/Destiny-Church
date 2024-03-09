import git
import time

def commit_and_push():
    repo = git.Repo('.')  # Assuming the script is in the root directory of your Git repository
    repo.git.add('--all')
    commit_message = input("Enter commit message: ")
    repo.index.commit(commit_message)
    origin = repo.remote(name='origin')
    origin.push('master')

def main():
    while True:
        commit_and_push()
        print("Changes committed and pushed successfully.")
        time.sleep(600)  # Sleep for 10 minutes (600 seconds)

if __name__ == "__main__":
    main()
