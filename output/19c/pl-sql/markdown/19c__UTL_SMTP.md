---
id: 19c__UTL_SMTP
name: UTL_SMTP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP

This example illustrates how UTL_SMTP is used by an application to send e-mail. The application connects to an SMTP server at port 25 and sends a simple text message.

## Syntax

```sql
DECLARE
  c UTL_SMTP.CONNECTION;
 
  PROCEDURE send_header(name IN VARCHAR2, header IN VARCHAR2) AS
  BEGIN
    UTL_SMTP.WRITE_DATA(c, name || ': ' || header || UTL_TCP.CRLF);
  END;
 
BEGIN
  c := UTL_SMTP.OPEN_CONNECTION('smtp-server.acme.com');
  UTL_SMTP.HELO(c, 'foo.com');
  UTL_SMTP.MAIL(c, 'sender@foo.com');
  UTL_SMTP.RCPT(c, 'recipient@foo.com');
  UTL_SMTP.OPEN_DATA(c);
  send_header('From',    '"Sender" <sender@foo.com>');
  send_header('To',      '"Recipient" <recipient@foo.com>');
  send_header('Subject', 'Hello');
  UTL_SMTP.WRITE_DATA(c, UTL_TCP.CRLF || 'Hello, world!');
  UTL_SMTP.CLOSE_DATA(c);
  UTL_SMTP.QUIT(c);
EXCEPTION
  WHEN utl_smtp.transient_error OR utl_smtp.permanent_error THEN
    BEGIN
      UTL_SMTP.QUIT(c);
    EXCEPTION
      WHEN UTL_SMTP.TRANSIENT_ERROR OR UTL_SMTP.PERMANENT_ERROR THEN
        NULL; -- When the SMTP server is down or unavailable, we don't have
              -- a connection to the server. The QUIT call raises an
              -- exception that we can ignore.
    END;
    raise_application_error(-20000,
      'Failed to send mail due to the following error: ' || sqlerrm);
END;
```

## Usage Notes

DECLARE c UTL_SMTP.CONNECTION; PROCEDURE send_header(name IN VARCHAR2, header IN VARCHAR2) AS BEGIN UTL_SMTP.WRITE_DATA(c, name || ': ' || header || UTL_TCP.CRLF); END; BEGIN c := UTL_SMTP.OPEN_CONNECTION('smtp-server.acme.com'); UTL_SMTP.HELO(c, 'foo.com'); UTL_SMTP.MAIL(c, 'sender@foo.com'); UTL_SMTP.RCPT(c, 'recipient@foo.com'); UTL_SMTP.OPEN_DATA(c); send_header('From', '"Sender" <sender@foo.com>'); send_header('To', '"Recipient" <recipient@foo.com>'); send_header('Subject', 'Hello'); UTL_SMTP.WRITE_DATA(c, UTL_TCP.CRLF || 'Hello, world!'); UTL_SMTP.CLOSE_DATA(c); UTL_SMTP.QUIT(c); EXCEPTION WHEN utl_smtp.transient_error OR utl_smtp.permanent_error THEN BEGIN UTL_SMTP.QUIT(c); EXCEPTION WHEN UTL_SMTP.TRANSIENT_ERROR OR UTL_SMTP.PERMANENT_ERROR THEN NULL; -- When the SMTP server is down or unavailable, we don't have -- a connection to the server. The QUIT call raises an -- exception that we can ignore. END; raise_application_error(-20000, 'Failed to send mail due to the following error: ' || sqlerrm); END;