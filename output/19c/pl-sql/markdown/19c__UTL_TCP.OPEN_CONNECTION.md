---
id: 19c__UTL_TCP.OPEN_CONNECTION
name: UTL_TCP.OPEN_CONNECTION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_TCP
tags: [utl_tcp]
source_file: UTL_TCP.html
---

# UTL_TCP.OPEN_CONNECTION

This function opens a TCP/IP connection to a specified service.

## Syntax

```sql
UTL_TCP.OPEN_CONNECTION  (
   remote_host          IN VARCHAR2,
   remote_port          IN PLS_INTEGER,
   local_host           IN VARCHAR2 DEFAULT NULL,
   local_port           IN PLS_INTEGER DEFAULT NULL,
   in_buffer_size       IN PLS_INTEGER DEFAULT NULL,
   out_buffer_size      IN PLS_INTEGER DEFAULT NULL,
   charset              IN VARCHAR2 DEFAULT NULL,
   newline              IN VARCHAR2 DEFAULT CRLF,
   tx_timeout           IN PLS_INTEGER DEFAULT NULL,
   wallet_path          IN  VARCHAR2 DEFAULT NULL,
   wallet_password      IN  VARCHAR2 DEFAULT NULL, 
  RETURN connection;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| remote_host | VARCHAR2 | IN | Name of the host providing the service. When remote_host is NULL , it connects to the local host. |
| remote_port | PLS_INTEGER | IN | Port number on which the service is listening for connections |
| local_host | VARCHAR2 | IN | Name of the host providing the service. NULL means does not care. |
| local_port | PLS_INTEGER | IN | Port number on which the service is listening for connections. NULL means don't care. |
| in_buffer_size | PLS_INTEGER | IN | The size of input buffer. The use of an input buffer can speed up execution performance in receiving data from the server. The appropriate size of the buffer depends on the flow of data between the client and the server, and the traffic/latency on the network. A zero value means no buffer should be used. A NULL value means the caller does not care if a buffer is used or not. The maximum size of the input buffer is 32767 bytes. |
| out_buffer_size | PLS_INTEGER | IN | The size of output buffer. The use of an output buffer can speed up execution performance in sending data to the server. The appropriate size of buffer depends on the flow of data between the client and the server, and the network condition. A zero value means no buffer should be used. A NULL value means the caller does not care if a buffer is used or not. The maximum size of the output buffer is 32767 bytes. |
| charset | VARCHAR2 | IN | The on-the-wire character set. Since text messages in the database may be encoded in a character set that is different from the one expected on the wire (that is, the character set specified by the communication protocol, or the one stipulated by the other end of the communication), text messages in the database are converted to and from the on-the-wire character set as they are sent and received on the network using READ_TEXT, READ_LINE, WRITE_TEXT and WRITE_LINE. Set this parameter to NULL when no conversion is needed. |
| newline | VARCHAR2 | IN | Newline character sequence. This newline character sequence is appended to the text line sent by WRITE_LINE API. |
| tx_timeout | PLS_INTEGER | IN | Time in seconds that the UTL_TCP package should wait before giving up in a read or write operations in this connection. In read operations, this package gives up if no data is available for reading immediately. In write operations, this package gives up if the output buffer is full and no data is to be sent in the network without being blocked. Zero (0) indicates not to wait at all. NULL indicates to wait forever. |
| wallet_path | VARCHAR2 | IN | Directory path that contains the Oracle wallet for SSL/TLS. The format is file : directory-path |
| wallet_password | VARCHAR2 | IN | Password to open the wallet. When the wallet is auto-login enabled, the password may be set to NULL . |

**Returns:** `connection`

## Usage Notes

Syntax UTL_TCP.OPEN_CONNECTION ( remote_host IN VARCHAR2, remote_port IN PLS_INTEGER, local_host IN VARCHAR2 DEFAULT NULL, local_port IN PLS_INTEGER DEFAULT NULL, in_buffer_size IN PLS_INTEGER DEFAULT NULL, out_buffer_size IN PLS_INTEGER DEFAULT NULL, charset IN VARCHAR2 DEFAULT NULL, newline IN VARCHAR2 DEFAULT CRLF, tx_timeout IN PLS_INTEGER DEFAULT NULL, wallet_path IN VARCHAR2 DEFAULT NULL, wallet_password IN VARCHAR2 DEFAULT NULL, RETURN connection; Parameters Table 277-12 OPEN_CONNECTION Function Parameters Parameter Description remote_host Name of the host providing the service. When remote_host is NULL , it connects to the local host. remote_port Port number on which the service is listening for connections local_host Name of the host providing the service. NULL means does not care. local_port Port number on which the service is listening for connections. NULL means don't care. in_buffer_size The size of input buffer. The use of an input buffer can speed up execution performance in receiving data from the server. The appropriate size of the buffer depends on the flow of data between the client and the server, and the traffic/latency on the network. A zero value means no buffer should be used. A NULL value means the caller does not care if a buffer is used or not. The maximum size of the input buffer is 32767 bytes. out_buffer_size The size of output buffer. The use of an output buffer can speed up execution performance in sending data to the server. The appropriate size of buffer depends on the flow of data between the client and the server, and the network condition. A zero value means no buffer should be used. A NULL value means the caller does not care if a buffer is used or not. The maximum size of the output buffer is 32767 bytes. charset The on-the-wire character set. Since text messages in the database may be encoded in a character set that is different from the one expected on the wire (that is, the character set specified by the communication protocol, or the one stipulated by the other end of the communication), text messages in the database are converted to and from the on-the-wire character set as they are sent and received on the network using READ_TEXT, READ_LINE, WRITE_TEXT and WRITE_LINE. Set this parameter to NULL when no conversion is needed. newline Newline character sequence. This newline character sequence is appended to the text line sent by WRITE_LINE API. tx_timeout Time in seconds that the UTL_TCP package should wait before giving up in a read or write operations in this connection. In read operations, this package gives up if no data is available for reading immediately. In write operations, this package gives up if the output buffer is full and no data is to be sent in the network without being blocked. Zero (0) indicates not to wait at all. NULL indicates to wait forever. wallet_path Directory path that contains the Oracle wallet for SSL/TLS. The format is file : directory-path wallet_password Password to open the wallet. When the wallet is auto-login enabled, the password may be set to NULL . Return Values A connection to the targeted TCP/IP service Usage Notes Note that connections opened by this UTL_TCP package can remain open and be passed from one database call to another in a shared server configuration. However, the connection must be closed explicitly. The connection remains open when the PL/SQL record variable that stores the connection goes out-of-scope in the PL/SQL program. Failing to close unwanted connections may result in unnecessary tying up of local and remote system resources. In the current release of the UTL_TCP package, the parameters local_host and local_port are ignored when open_connection makes a TCP/IP connection. It does not attempt to use the specified local host and port number when the connection is made. The local_host and local_port fields is not set in the connection record returned by the function. tx_timeout is intended to govern both the read operations and the write operations. However, an implementation restriction prevents tx_timeout from governing write operations in the current release. Examples DECLARE c UTL_TCP.CONNECTION; BEGIN c := UTL_TCP.OPEN_CONNECTION( host => 'www.example.com', port => 443, wallet_path => 'file:/oracle/wallets/smtp_wallet', wallet_password => '****'); UTL_TCP.SECURE_CONNECTION (c => c); END;