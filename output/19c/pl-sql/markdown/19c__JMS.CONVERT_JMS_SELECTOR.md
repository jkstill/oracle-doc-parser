---
id: 19c__JMS.CONVERT_JMS_SELECTOR
name: JMS.CONVERT_JMS_SELECTOR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: JMS
tags: [jms]
source_file: JMS-Types.html
---

# JMS.CONVERT_JMS_SELECTOR

Oracle Database includes three stored procedures to help users convert JMS selectors into Oracle Database Advanced Queuing rules. These rules can be used in ADD_SUBSCRIBER operations as subscriber rules or in DEQUEUE operations as dequeue conditions. These procedures are in the SYS.dbms_jms_plsql package.

## Syntax

```sql
Function convert_jms_selector(selector IN VARCHAR2) RETURN VARCHAR2
```

**Returns:** `VARCHAR2`

## Usage Notes

Convert with Minimal Specification The first procedure assumes the destination payload type is one of the JMS ADTs whose corresponding constant is dbms_jms_plsql.DESTPLOAD_JMSTYPE and also assumes that the J2EE compliant mode is true. Function convert_jms_selector(selector IN VARCHAR2) RETURN VARCHAR2 The converted Oracle Database Advanced Queuing rule or null if there is any conversion error. ORA-24197 if the Java stored procedure throws an exception during execution. Convert with Destination Payload Type Specified The second procedure takes one more parameter: dest_pload_type . The conversion of a JMS selector to an Oracle Database Advanced Queuing rule happens only if this parameter is SYS.dbms_jms_plsql.DESTPLOAD_JMSTYPE or SYS.dbms_jms_plsql.DESTPLOAD_ANYDATA . The function returns exactly the same VARCHAR2 value as the selector parameter if the dest_pload_type parameter is SYS.dbms_jms_plsql.DESTPLOAD_USERADT . The function returns null if dest_pload_type parameter is none of these three constants. This function assumes that the J2EE compliant mode is true.