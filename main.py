import base64
import logging
import os
import pickle
from datetime import datetime, timedelta

import html2text
import pdfkit
from PyPDF2 import PdfReader, PdfWriter
from bs4 import BeautifulSoup
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Setup logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
# get today's date in YYYY-MM-DD format
# current_date = datetime.now().strftime('%Y-%m-%d')
current_date = datetime.strptime('2024-06-21', '%Y-%m-%d')  # For testing purposes
# get previous day's date in YYYY-MM-DD format and next day's date in YYYY-MM-DD format based on current date
previous_date = (current_date - timedelta(1)).strftime('%Y-%m-%d')
next_date = (current_date + timedelta(1)).strftime('%Y-%m-%d')

filter_query = f"from:mail@email.paytmmoney.com after:{previous_date} before:{next_date} WEEKLY NEWSLETTER"
logging.info(f'Filter query: {filter_query}')


def split_pdf(input_pdf_path, output_pdf_path, start_page, end_page):
    with open(input_pdf_path, "rb") as filehandle_input:
        pdf = PdfReader(filehandle_input)
        pdf_writer = PdfWriter()
        for page_number in range(start_page, end_page):
            pdf_writer.add_page(pdf.pages[page_number])
        with open(output_pdf_path, "wb") as filehandle_output:
            pdf_writer.write(filehandle_output)


def read_email_from_gmail():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    try:
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().messages().list(userId='me',
                                                  q=filter_query).execute()
        messages = results.get('messages', [])

        if not messages:
            logging.info('No new emails.')
        else:
            logging.info(f'Emails: {len(messages)}')
            for message in messages:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                email_data = msg['payload']['headers']
                for values in email_data:
                    name = values['name']
                    if name == 'From':
                        from_name = values['value']
                        for part in msg['payload']['parts']:
                            if 'data' in part['body'] and part['mimeType'] == 'text/html':
                                try:
                                    data_text = part['body']["data"]
                                    first_email_data = data_text.split('[')[0]
                                    byte_code = base64.urlsafe_b64decode(first_email_data)
                                    text = byte_code.decode("utf-8")
                                    soup = BeautifulSoup(text, "lxml")
                                    body = soup.body()
                                    pdfkit.from_string(str(body), 'temp.pdf')
                                    split_pdf('temp.pdf', 'out.pdf', 0, 4)  # Only keep the first 4 pages
                                    logging.info('Email converted to PDF.')
                                    break  # Exit the loop after processing the first part with data

                                except Exception as error:
                                    logging.error('An error occurred: {}'.format(error))
                        break  # Exit the loop after processing the first email
    except BaseException as error:
        logging.error('An exception occurred: {}'.format(error))


if __name__ == '__main__':
    read_email_from_gmail()
