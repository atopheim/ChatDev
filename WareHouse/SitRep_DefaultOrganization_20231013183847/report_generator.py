'''
This file contains functions to generate a report summarizing the work.
'''
def generate_report(events, commits, pull_requests):
    # Generate a report summarizing the work
    report = "Work Summary:\n\n"
    # Add events from Microsoft Calendar to the report
    report += "Events:\n"
    for event in events:
        report += f"- {event}\n"
    report += "\n"
    # Add commit texts from GitHub to the report
    report += "Commit Texts:\n"
    for commit in commits:
        report += f"- {commit}\n"
    report += "\n"
    # Add pull request descriptions from GitHub to the report
    report += "Pull Request Descriptions:\n"
    for pull_request in pull_requests:
        report += f"- {pull_request}\n"
    # Print the report
    print(report)