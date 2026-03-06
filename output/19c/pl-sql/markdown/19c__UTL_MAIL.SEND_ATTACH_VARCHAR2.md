---
id: 19c__UTL_MAIL.SEND_ATTACH_VARCHAR2
name: UTL_MAIL.SEND_ATTACH_VARCHAR2
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_MAIL
tags: [utl_mail]
source_file: UTL_MAIL.html
---

# UTL_MAIL.SEND_ATTACH_VARCHAR2

This procedure is the SEND Procedure overloaded for VARCHAR2 attachments.

## Syntax

```sql
UTL_MAIL.SEND_ATTACH_VARCHAR2 (
   sender            IN    VARCHAR2 CHARACTER SET ANY_CS,
   recipients        IN    VARCHAR2 CHARACTER SET ANY_CS,
   cc                IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   bcc               IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   subject           IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   message           IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   mime_type         IN    VARCHAR2 CHARACTER SET ANY_CS 
                                           DEFAULT 'text/plain; charset=us-ascii',
   priority          IN    PLS_INTEGER DEFAULT 3,
   attachment        IN    VARCHAR2 CHARACTER SET ANY_CS, ,
   att_inline        IN    BOOLEAN DEFAULT TRUE,
   att_mime_type     IN    VARCHAR2 CHARACTER SET ANY_CS 
                                           DEFAULT 'text/plain; charset=us-ascii,
   att_filename      IN    VARCHAR2CHARACTER SET ANY_CS DEFAULT NULL,
   replyto           IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL);
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
| mime_type | VARCHAR2 | IN | Mime type of the message, default is 'text/plain; charset=us-ascii |
| priority | PLS_INTEGER | IN | Message priority, which maps to the X-priority field. 1 is the highest priority and 5 the lowest. The default is 3. |
| attachment | VARCHAR2 | IN | Text attachment |
| att_inline | BOOLEAN | IN | Specifies whether the attachment is inline, default TRUE |
| att_mime_type | VARCHAR2 | IN | Mime type of the attachment, default is 'text/plain; charset=us-ascii' |
| att_filename | VARCHAR2CHARACTER | IN | String specifying a filename containing the attachment, default is NULL |
| replyto | VARCHAR2 | IN | Defines to whom the reply email is to be sent |

## Usage Notes

Syntax UTL_MAIL.SEND_ATTACH_VARCHAR2 ( sender IN VARCHAR2 CHARACTER SET ANY_CS, recipients IN VARCHAR2 CHARACTER SET ANY_CS, cc IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL, bcc IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL, subject IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL, message IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL, mime_type IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT 'text/plain; charset=us-ascii', priority IN PLS_INTEGER DEFAULT 3, attachment IN VARCHAR2 CHARACTER SET ANY_CS, , att_inline IN BOOLEAN DEFAULT TRUE, att_mime_type IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT 'text/plain; charset=us-ascii, att_filename IN VARCHAR2CHARACTER SET ANY_CS DEFAULT NULL, replyto IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL); Parameters Table 269-4 SEND_ATTACH_VARCHAR2 Procedure Parameters Parameter Description sender Email address of the sender recipients Email addresses of the recipient(s), separated by commas cc Email addresses of the CC recipient(s), separated by commas, default is NULL bcc Email addresses of the BCC recipient(s), separated by commas, default is NULL subject String to be included as email subject string, default is NULL message Text message body mime_type Mime type of the message, default is 'text/plain; charset=us-ascii priority Message priority, which maps to the X-priority field. 1 is the highest priority and 5 the lowest. The default is 3. attachment Text attachment att_inline Specifies whether the attachment is inline, default TRUE att_mime_type Mime type of the attachment, default is 'text/plain; charset=us-ascii' att_filename String specifying a filename containing the attachment, default is NULL replyto Defines to whom the reply email is to be sent