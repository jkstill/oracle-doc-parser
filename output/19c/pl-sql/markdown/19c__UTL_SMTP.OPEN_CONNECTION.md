---
id: 19c__UTL_SMTP.OPEN_CONNECTION
name: UTL_SMTP.OPEN_CONNECTION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_SMTP
tags: [utl_smtp]
source_file: UTL_SMTP.html
---

# UTL_SMTP.OPEN_CONNECTION

These functions open a connection to an SMTP server.

## Syntax

```sql
UTL_SMTP.OPEN_CONNECTION (
   host                            IN  VARCHAR2, 
   port                            IN  PLS_INTEGER DEFAULT 25, 
   c                               OUT connection, 
   tx_timeout                      IN  PLS_INTEGER DEFAULT NULL,
   wallet_path                     IN  VARCHAR2 DEFAULT NULL,
   wallet_password                 IN  VARCHAR2 DEFAULT NULL, 
   secure_connection_before_smtp   IN  BOOLEAN DEFAULT FALSE,
   secure_host                     IN  VARCHAR2 DEFAULT NULL)
 RETURN reply; 

UTL_SMTP.OPEN_CONNECTION (
   host                           IN  VARCHAR2, 
   port                           IN  PLS_INTEGER DEFAULT 25, 
   tx_timeout                     IN  PLS_INTEGER DEFAULT NULL,
   wallet_path                    IN  VARCHAR2 DEFAULT NULL,
   wallet_password                IN  VARCHAR2 DEFAULT NULL, 
   secure_connection_before_smtp  IN  BOOLEAN DEFAULT FALSE,
   secure_host                    IN  VARCHAR2 DEFAULT NULL) 
RETURN connection;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| host | VARCHAR2 | IN | Name of the SMTP server host |
| port | PLS_INTEGER | IN | Port number on which SMTP server is listening (usually 25) |
| c | connection | OUT | SMTP connection |
| tx_timeout | PLS_INTEGER | IN | Time in seconds that the UTL_SMTP package waits before timing out in a read or write operation for this connection. In read operations, this package times out if no data is available for reading immediately. In write operations, this package times out if the output buffer is full and no data is to be sent into the network without being blocked. 0 indicates not to wait at all. NULL indicates to wait forever. |
| wallet_path | VARCHAR2 | IN | Directory path that contains the Oracle wallet for SSL/TLS. The format is file : <directory-path> |
| wallet_password | VARCHAR2 | IN | Password to open the wallet. When the wallet is auto-login enabled, the password can be set to NULL . |
| secure_connection_before_smtp | BOOLEAN | IN | If TRUE , a secure connection with SSL/TLS is made before SMTP communication. If FALSE , no connection is made. |
| secure_host | VARCHAR2 | IN | The host name to be matched against the common name (CN) of the SMTP server's certificate when a secure connection is used. It can also be a domain name like "*.example.com" . If NULL , the SMTP host name to connect to will be used. |

**Returns:** `reply`

## Usage Notes

Syntax UTL_SMTP.OPEN_CONNECTION ( host IN VARCHAR2, port IN PLS_INTEGER DEFAULT 25, c OUT connection, tx_timeout IN PLS_INTEGER DEFAULT NULL, wallet_path IN VARCHAR2 DEFAULT NULL, wallet_password IN VARCHAR2 DEFAULT NULL, secure_connection_before_smtp IN BOOLEAN DEFAULT FALSE, secure_host IN VARCHAR2 DEFAULT NULL) RETURN reply; UTL_SMTP.OPEN_CONNECTION ( host IN VARCHAR2, port IN PLS_INTEGER DEFAULT 25, tx_timeout IN PLS_INTEGER DEFAULT NULL, wallet_path IN VARCHAR2 DEFAULT NULL, wallet_password IN VARCHAR2 DEFAULT NULL, secure_connection_before_smtp IN BOOLEAN DEFAULT FALSE, secure_host IN VARCHAR2 DEFAULT NULL) RETURN connection; Parameters Table 276-29 OPEN_CONNECTION Functions Parameters Parameter Description host Name of the SMTP server host port Port number on which SMTP server is listening (usually 25) c SMTP connection tx_timeout Time in seconds that the UTL_SMTP package waits before timing out in a read or write operation for this connection. In read operations, this package times out if no data is available for reading immediately. In write operations, this package times out if the output buffer is full and no data is to be sent into the network without being blocked. 0 indicates not to wait at all. NULL indicates to wait forever. wallet_path Directory path that contains the Oracle wallet for SSL/TLS. The format is file : <directory-path> wallet_password Password to open the wallet. When the wallet is auto-login enabled, the password can be set to NULL . secure_connection_before_smtp If TRUE , a secure connection with SSL/TLS is made before SMTP communication. If FALSE , no connection is made. secure_host The host name to be matched against the common name (CN) of the SMTP server's certificate when a secure connection is used. It can also be a domain name like "*.example.com" . If NULL , the SMTP host name to connect to will be used. Return Values Table 276-30 OPEN_CONNECTION Functions Return Values Return Value Description reply Reply of the command (see REPLY_ REPLIES Record Types in UTl_SMTP Types ). In cases where there are multiple replies, the last reply is returned. Usage Notes The expected response from the server is a message beginning with status code 220. The version of OPEN_CONNECTION that returns UTL_SMTP . CONNECTION record checks the reply code returned by an SMTP server when the connection is first established. It raises an exception when the reply indicates an error. Otherwise, it discards the reply. If you want to examine the reply, invoke the version of OPEN_CONNECTION that returns REPLY . tx_timeout is intended to govern both the read operations and the write operations. However, an implementation restriction prevents tx_timeout from governing write operations in the current release. Examples DECLARE c utl_smtp.connection; BEGIN c := UTL_SMTP.OPEN_CONNECTION( host => 'smtp.example.com', port => 465, wallet_path => 'file:/oracle/wallets/smtp_wallet', wallet_password => ' password ', secure_connection_before_smtp => TRUE); END;