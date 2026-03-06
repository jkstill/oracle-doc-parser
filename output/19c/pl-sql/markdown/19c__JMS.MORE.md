---
id: 19c__JMS.MORE
name: JMS.MORE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: JMS
tags: [jms]
source_file: JMS-Types.html
---

# JMS.MORE

Oracle uses Java stored procedure to implement some of the procedures of AQ$_MAP_MESSAGE , AQ$_JMS_STREAM_MESSAGE , and AQ$_JMS_BYTES_MESSAGE types. These types have some common functionality that are different from AQ$_JMS_TEXT_MESSAGE type. This section discusses this common functionality.

## Syntax

```sql
set_bytes(payload IN BLOB)
set_bytes(payload IN RAW)
get_bytes(payload OUT BLOB)
get_bytes(payload OUT RAW)
```

## Usage Notes

This section contains these topics: Using Java Stored Procedures to Encode and Decode Oracle Database Advanced Queuing Messages Initialize the Jserv Static Variable Get the Payload Data Back to PL/SQL Garbage Collect the Static Variable Use a Message Store: A Static Variable Collection Typical Calling Sequences Read-Only and Write-Only Modes Enforced for Stream and Bytes Messages Differences Between Bytes and Stream Messages Getting and Setting Bytes, Map, and Stream Messages as RAW Bytes Using Java Stored Procedures to Encode and Decode Oracle Database Advanced Queuing Messages The major difference between map, stream, bytes, and other messages is that the message payload is encoded as a byte stream by JAVA. Retrieving and updating these payloads in PL/SQL therefore requires Oracle JAVA stored procedures. A message payload is stored in two places during processing. On the PL/SQL side it is stored as the data members of a JMS message ADT, and on the Jserv side it is stored as a static variable. (Jserv is the JVM inside Oracle Database.) When the payload is processed, the payload data is first transformed to a static variable on the Jserv side. Once the static variable is initialized, all later updates on the message payload are performed on this static variable. At the end of processing, payload data is flushed back to the PL/SQL side. Oracle provides member procedures that maintain the status of the Jserv static variable and enforce rules when calling these member procedures. These procedures are in the following ADTs: aq$_jms_bytes_message aq$_jms_map_message aq$_jms_stream_message Initialize the Jserv Static Variable Before you make any other calls to manipulate the payload data, the Jserv static variable must be properly initialized. This is done by calling the prepare or clear_body procedure. The prepare procedure uses the payload data in PL/SQL ADTs to initialize the static variable, while clear_body initializes the static variable to an empty payload (empty hashtable or stream). Note: It is important to call the prepare or clear_body procedure before any other calls to properly initialize the Jserv static variables. Usually these two methods are called once at the beginning. But they can be called multiple times for one message. Any call of these two methods without first calling the flush procedure wipes out all updates made to the messages. Note: It is important to call the prepare or clear_body procedure before any other calls to properly initialize the Jserv static variables. Usually these two methods are called once at the beginning. But they can be called multiple times for one message. Any call of these two methods without first calling the flush procedure wipes out all updates made to the messages. Get the Payload Data Back to PL/SQL Calling the flush procedure synchronizes changes made to the Jserv static variable back to the PL/SQL ADTs. The flush call is required when you want the changes made to be reflected in the ADT payload. It is important to synchronize the changes back to the ADT, because it is the ADT payload that matters.