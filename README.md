# Introduction
This repository provides solution to problem shared by Damco Solutions solution during recruitment process. Problem was given as below:
Exercise:

"As a part of this assignment, we would like you to design a database model layer for a Django application based on the data provided in the attached Excel file. The database model should accurately represent the data and should be optimized for efficient querying and data retrieval.

Additionally, you are required to develop a custom management command in Django to import the data from the Excel file into the database. The command should also send an email to a designated recipient after the import is complete, providing details on the number of records that were imported and failed.

In case of import failures, the email should also include a CSV file containing the details of all records that failed to import and the reason for the failure. The CSV file should not be saved locally on the machine.

Please ensure that the database model, management command, and email functionality are all implemented to the highest professional standards. The solution should be shared either as a Git repository or a zip file, with detailed instructions for setting up and running the Django application.
1. To run setup clone git repo using following command
`git clone https://github.com/NikhilDJain/damco.git`
2. Create virtual environment and activate it. You can refer this [documentation on virtual environment](https://docs.python.org/3/library/venv.html).
3. Install required packages using command `pip install -r requirements.txt`. To run this command you should be in *Damco* folder
4. Go into *damco_test* folder using command `cd damco_test`
5. Make migrations using command `python manage.py makemigrations` and next run command `python manage.py migrate`. You can read more about [Django migrations](https://docs.djangoproject.com/en/4.2/topics/migrations/).
6. To allow to send email from sender account, you will need application password. Please refer on how to generate application password for [Gmail](https://support.google.com/mail/answer/185833?hl=en) and [Outlook](https://support.microsoft.com/en-us/account-billing/manage-app-passwords-for-two-step-verification-d6dc8c6d-4bf7-4851-ad95-6d07799387e9).
7. Setup environment variable *EMAIL_PASSWORD* to store application password generated in step 6. Refer on [how to set environment](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html)
8. Now you are ready to use developed utility.
## About
This utility can be used to import recipe data from excel to Django models. This data gets saved in *db.sqlite3* in different table. You can browse this data using [DB Browser](https://sqlitebrowser.org/dl/). Sample demo excel is available in repository.
This utility sends email once recipes are uploaded successfully or if there is any failure. Below are parameters which this tool can take:
| Parameter | type | Description | Default Value
| ----------- | ----------- | ----------- | ----------- |
| filepath | Mandatory | Filepath of excel which contains recipe data | NA
| --server | Optional | SMTP Server | smtp.gmail.com
| --port | Optional | SMTP Server port | smtp.gmail.com
| --from | Optional | Sender Email | jainnikhil0258@gmail.com
| --to | Optional | Receiver email list | jainnikhil0258@gmail.com

Examples:

`python manage.py importdata demo.xlsx`

`python manage.py importdata demo.xlsx --server smtp.gmail.com`

`python manage.py importdata demo.xlsx -s smtp.gmail.com`