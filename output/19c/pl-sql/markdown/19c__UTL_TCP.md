---
id: 19c__UTL_TCP
name: UTL_TCP
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_TCP
tags: [utl_tcp]
source_file: UTL_TCP.html
---

# UTL_TCP

Some possible uses for UTL_TCP include retrieving a Web page over HTTP or sending an e-mail.

## Syntax

```sql
DECLARE
  c  utl_tcp.connection;  -- TCP/IP connection to the Web server
  ret_val pls_integer; 
BEGIN
  c := utl_tcp.open_connection(remote_host => 'www.acme.com',
                               remote_port =>  80,
                               charset     => 'US7ASCII');  -- open connection
  ret_val := utl_tcp.write_line(c, 'GET / HTTP/1.0');    -- send HTTP request
  ret_val := utl_tcp.write_line(c);
  BEGIN
    LOOP
      dbms_output.put_line(utl_tcp.get_line(c, TRUE));  -- read result
    END LOOP;
  EXCEPTION
    WHEN utl_tcp.end_of_input THEN
      NULL; -- end of input
  END;
  utl_tcp.close_connection(c);
END;
```

## Usage Notes

The following code example illustrates how the TCP/IP package can be used to retrieve a Web page over HTTP. It connects to a Web server listening at port 80 (standard port for HTTP) and requests the root document. DECLARE c utl_tcp.connection; -- TCP/IP connection to the Web server ret_val pls_integer; BEGIN c := utl_tcp.open_connection(remote_host => 'www.acme.com', remote_port => 80, charset => 'US7ASCII'); -- open connection ret_val := utl_tcp.write_line(c, 'GET / HTTP/1.0'); -- send HTTP request ret_val := utl_tcp.write_line(c); BEGIN LOOP dbms_output.put_line(utl_tcp.get_line(c, TRUE)); -- read result END LOOP; EXCEPTION WHEN utl_tcp.end_of_input THEN NULL; -- end of input END; utl_tcp.close_connection(c); END; The following code example illustrates how the TCP/IP package can be used by an application to send e-mail (also known as email from PL/SQL). The application connects to an SMTP server at port 25 and sends a simple text message. PROCEDURE send_mail (sender IN VARCHAR2, recipient IN VARCHAR2, message IN VARCHAR2) IS mailhost VARCHAR2(30) := 'mailhost.mydomain.com'; smtp_error EXCEPTION; mail_conn utl_tcp.connection; PROCEDURE smtp_command(command IN VARCHAR2, ok IN VARCHAR2 DEFAULT '250') IS response varchar2(3); len pls_integer; BEGIN len := utl_tcp.write_line(mail_conn, command); response := substr(utl_tcp.get_line(mail_conn), 1, 3); IF (response <> ok) THEN RAISE smtp_error; END IF; END; BEGIN mail_conn := utl_tcp.open_connection(remote_host => mailhost, remote_port => 25, charset => 'US7ASCII'); smtp_command('HELO ' || mailhost); smtp_command('MAIL FROM: ' || sender); smtp_command('RCPT TO: ' || recipient); smtp_command('DATA', '354'); smtp_command(message); smtp_command('QUIT', '221'); utl_tcp.close_connection(mail_conn); EXCEPTION WHEN OTHERS THEN -- Handle the error END;