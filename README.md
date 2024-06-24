# Email to PDF Converter

## Description

This project is a Python application that reads emails from a Gmail account and converts them into PDF format. It uses the Gmail API to fetch emails and pdfkit to convert HTML emails into PDFs. The PyPDF2 library is used to limit the number of pages in the final PDF. The application is designed to fetch emails from a specific sender and within a specific date range, making it a useful tool for archiving and organizing important emails.

## Features

- Fetch emails from a Gmail account using the Gmail API.
- Convert HTML emails into PDFs using pdfkit.
- Limit the number of pages in the final PDF using PyPDF2.
- Filter emails based on sender and date range.
## Gmail API Setup

Before running the script, you need to set up the Gmail API for your account. Follow these steps:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).

2. Create a new project or select an existing one.

3. In the sidebar on the left, select APIs & Services > Library.

4. Search for 'Gmail API' and enable it for your project.

5. In the sidebar on the left, select APIs & Services > Credentials.

6. Click on 'Create Credentials' and select 'OAuth client ID'.

7. If you haven't configured the OAuth consent screen yet, you will be prompted to do so. Fill in the required fields. You can set the 'User Type' to 'External' and 'Application Type' to 'Public'.

8. Once the OAuth consent screen is configured, you will be able to create the OAuth client ID. Set the 'Application Type' to 'Desktop app' and give it a name. Click 'Create'.

9. After the OAuth client ID is created, you can download the `credentials.json` file by clicking on the download icon next to the client ID in the 'OAuth 2.0 Client IDs' section.

10. Place the `credentials.json` file in the same directory as the script.

Please note that the first time you run the script, it will open a new window asking for permissions. After granting permissions, a new file `token.pickle` will be created. This file will be used for authentication in subsequent runs.
## Prerequisites

- Python 3.11 or higher
- Gmail account with API enabled
- Libraries: google-auth, google-auth-oauthlib, google-auth-httplib2, google-api-python-client, pdfkit, PyPDF2, BeautifulSoup4, html2text

## Setup

1. Clone the repository.
2. Install the required Python libraries using pip:

```bash
pip install -r requirements.txt