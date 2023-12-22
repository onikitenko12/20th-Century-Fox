# 20th-Century-Fox
Test project for 20th-Century-Fox team

# Project
Implement personal contacts terminal bot.

# Requirements

1. Save contacts with names, addresses, phone numbers, email and birthdays to the contact book;
2. Display a list of contacts whose birthday is a specified number of days from the current date;
3. Check the correctness of the entered phone number and email when creating or editing a record and notify the user in case of incorrect entry;
4. Search for specified contacts in book contacts;
5. Edit and delete entries from the contact book;
6. Save notes with text information;
7. Search for notes;
8. Edit and delete notes;
9. Add "tags" to notes, keywords describing the topic and subject of the record;
10. Search and sort notes by keywords (tags);
11. Sort files in the specified folder by category (images, documents, videos, etc.).
12. Analyze the entered text and try to guess what the user wants from it and suggest the nearest command for execution 

# Release plan
1. Release 1.0  - implement features from 1 to 11
2. Release 1.1 - implement feature 12
3. Release 2.0 - implement user iteraction interface (replace terminal commands iteraction)

# Work guidance for project repository
# Branch naming
Use feature / release flow style
Example: branch name to work on feature feature/20thFox-Ticket##
		 branch name for releale        releale/release-1.0
		 major branch always            main

1. Keep main always in working condition (No errors,failures allowed) , merge into main releale branches only
after PR approves from team members , merged branch should be green . 
2. Never!!!!! rename main branch
3. To start work on new feature ticket , create new branch from upcoming release branch . When work on 
feature done , create Pull Request into release branch , add reviewers into your PR. After work on PR comments and final approves from team merge feature branch into release branch. 
4. Do not temper to add comments into your code . Team members will appreciate your work.