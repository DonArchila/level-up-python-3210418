# Send an Email using smtplib

This documentation provides an example of how to send an email using the `smtplib` library and an SMTP server. In this example, `mailtrap.io` is used as the SMTP server.

## Function: `send_email`

The `send_email` function takes three parameters:

- `receiver_email`: The email address of the recipient.
- `subject`: The subject of the email.
- `body`: The body of the email.

The function creates a message with the subject and body, and sends it to the `receiver_email` using the SMTP server of the sender's email provider.

### Example Usage

```python
import smtplib

SENDER_EMAIL = 'Sender <from@example.com>'  # replace with your email address
SENDER_USERNAME = 'b58689e2a4233d'  # replace with your email username
SENDER_PASSWORD = '07f970d446f4f7'  # replace with your email password
RECEIVER_EMAIL = '<Receiver to@example.com>'  # replace with receiver email address

def send_email(receiver_email, subject, body):
  message = f'Subject: {subject}\n\n{body}'
  with smtplib.SMTP('smtp.mailtrap.io', 2525) as server:
    server.starttls()
    server.login(SENDER_USERNAME, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, receiver_email, message)

if __name__ == '__main__':
  # replace receiver email address
  send_email(RECEIVER_EMAIL, 'Notification', 'Everything is awesome!')
```

### Notes

- Replace `SENDER_EMAIL`, `SENDER_USERNAME`, `SENDER_PASSWORD`, and `RECEIVER_EMAIL` with actual values.
- Ensure that the SMTP server details (`smtp.mailtrap.io`, 2525) are correct for your email provider.

This example uses `mailtrap.io` for testing purposes. For production use, replace the SMTP server details with those of your email provider.