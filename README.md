# Email to PDF Converter

## Description

This project is a Python application that reads emails from a Gmail account and converts them into PDF format. It uses the Gmail API to fetch emails and pdfkit to convert HTML emails into PDFs. The PyPDF2 library is used to limit the number of pages in the final PDF. The application is designed to fetch emails from a specific sender and within a specific date range, making it a useful tool for archiving and organizing important emails.

## Features

- Fetch emails from a Gmail account using the Gmail API.
- Convert HTML emails into PDFs using pdfkit.
- Limit the number of pages in the final PDF using PyPDF2.
- Filter emails based on sender and date range.

## Prerequisites

- Python 3.11 or higher
- Gmail account with API enabled
- Libraries: google-auth, google-auth-oauthlib, google-auth-httplib2, google-api-python-client, pdfkit, PyPDF2, BeautifulSoup4, html2text

## Setup

1. Clone the repository.
2. Install the required Python libraries using pip:

```bash
pip install -r requirements.txt