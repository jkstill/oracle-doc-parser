---
id: 19c__UTL_MAIL.SEND
name: UTL_MAIL.SEND
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_MAIL
tags: [utl_mail]
source_file: UTL_MAIL.html
---

# UTL_MAIL.SEND

This procedure packages an email message into the appropriate format, locates SMTP information, and delivers the message to the SMTP server for forwarding to the recipients.

## Syntax

```sql
UTL_MAIL.SEND (
   sender      IN    VARCHAR2 CHARACTER SET ANY_CS,
   recipients  IN    VARCHAR2 CHARACTER SET ANY_CS,
   cc          IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   bcc         IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   subject     IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   message     IN    VARCHAR2 CHARACTER SET ANY_CS,
   mime_type   IN    VARCHAR2 DEFAULT 'text/plain; charset=us-ascii',
   priority    IN    PLS_INTEGER DEFAULT 3,
   replyto     IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sender | VARCHAR2 | IN | Email address of the sender |
| recipients | VARCHAR2 | IN | Email addresses of the recipient(s), separated by commas |
| cc | VARCHAR2 | IN | Email addresses of the CC recipient(s), separated by commas, default is NULL |
| bcc | VARCHAR2 | IN | Email addresses of the BCC recipient(s), separated by commas, default is NULL |
| subject | VARCHAR2 | IN | String to be included as email subject string, default is NULL |
| message | VARCHAR2 | IN | Text message body |
| mime_type | VARCHAR2 | IN | Mime type of the message, default is 'text/plain; charset=us-ascii' |
| priority | PLS_INTEGER | IN | Message priority, which maps to the X-priority field. 1 is the highest priority and 5 the lowest. The default is 3. |
| replyto | VARCHAR2 | IN | Defines to whom the reply email is to be sent |

## Usage Notes

It hides the SMTP API and exposes a one-line email facility for ease of use. Syntax UTL_MAIL.SEND ( sender IN VARCHAR2 CHARACTER SET ANY_CS, recipients IN VARCHAR2 CHARACTER SET ANY_CS, cc IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL, bcc IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL, subject IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL, message IN VARCHAR2 CHARACTER SET ANY_CS, mime_type IN VARCHAR2 DEFAULT 'text/plain; charset=us-ascii', priority IN PLS_INTEGER DEFAULT 3, replyto IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL); Parameters Table 269-2 SEND Procedure Parameters Parameter Description sender Email address of the sender recipients Email addresses of the recipient(s), separated by commas cc Email addresses of the CC recipient(s), separated by commas, default is NULL bcc Email addresses of the BCC recipient(s), separated by commas, default is NULL subject String to be included as email subject string, default is NULL message Text message body mime_type Mime type of the message, default is 'text/plain; charset=us-ascii' priority Message priority, which maps to the X-priority field. 1 is the highest priority and 5 the lowest. The default is 3. replyto Defines to whom the reply email is to be sent