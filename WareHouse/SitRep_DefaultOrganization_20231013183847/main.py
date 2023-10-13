'''
This is the main file that runs the script to summarize the work from Microsoft Calendar and GitHub.
'''
import calendar_reader
import github_reader
import report_generator
def main():
    # Read events from Microsoft Calendar
    events = calendar_reader.read_events()
    # Read commit texts and pull request descriptions from GitHub
    commits = github_reader.read_commits()
    pull_requests = github_reader.read_pull_requests()
    # Generate a report summarizing the work
    report_generator.generate_report(events, commits, pull_requests)
if __name__ == "__main__":
    main()