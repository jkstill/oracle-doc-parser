---
id: 19c__JMS.JAVA
name: JMS.JAVA
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: JMS
tags: [jms]
source_file: JMS-Types.html
---

# JMS.JAVA

Datatypes do not map one-to-one between PL/SQL and Java.

## Usage Notes

Some Java types, such as BYTE and SHORT , are not present in PL/SQL. PL/SQL type INT was chosen to represent these types. If a PL/SQL INT value intended to hold a Java BYTE or SHORT value exceeds the corresponding range Java enforces, an out-of-range error is thrown. Other Java types have more than one counterpart in PL/SQL with different capabilities. A Java String can be represented by both VARCHAR2 and CLOB , but VARCHAR2 has a maximum limit of 4000 bytes. When retrieving TEXT data from map, stream, and bytes message types, a CLOB is always returned. When updating the map, stream and bytes message types, users can submit either a VARCHAR2 or CLOB . Similarly, a Java BYTE ARRAY can be represented by both RAW and BLOB , with RAW having a maximum size of 32767. When retrieving BYTE ARRAY data from map, stream, and bytes message types, a BLOB is always returned. When updating the map, stream and bytes message types, users can submit either a RAW or BLOB . See Also: JMS specification 3.11.3, Conversion Provided by StreamMessage and MapMessage See Also: JMS specification 3.11.3, Conversion Provided by StreamMessage and MapMessage New JMS Support in Oracle Database 10 g In Oracle Database 10 g , a new AQ$_JMS_VALUE ADT has been added in the SYS schema for OJMS PL/SQL users. It is specifically used to implement the read_object procedure of aq$_jms_stream_message and get_object procedure of aq$_jms_map_message , to mimic the Java general object class Object . AQ$_JMS_VALUE ADT can represent any datatype that JMS StreamMessage and MapMessage can hold. The collection ADT AQ$_JMS_NAMEARRAY was added for the getNames method of MapMessage . It holds an array of names. In this release the ADT AQ$_JMS_EXCEPTION was added to represent a Java exception thrown in an OJMS JAVA stored procedure on the PL/SQL side. Now you can retrieve a Java exception thrown by an OJMS stored procedure and analyze it on the PL/SQL side.