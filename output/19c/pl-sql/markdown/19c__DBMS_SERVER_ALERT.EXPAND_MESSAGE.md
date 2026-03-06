---
id: 19c__DBMS_SERVER_ALERT.EXPAND_MESSAGE
name: DBMS_SERVER_ALERT.EXPAND_MESSAGE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SERVER_ALERT
tags: [dbms_server_alert]
source_file: DBMS_SERVER_ALERT.html
---

# DBMS_SERVER_ALERT.EXPAND_MESSAGE

This function expands alert messages.

## Syntax

```sql
DBMS_SERVER_ALERT.EXPAND_MESSAGE(
   user_language            IN   VARCHAR2,
   message_id               IN   NUMBER,
   argument_1               IN   VARCHAR2,
   argument_2               IN   VARCHAR2,
   argument_3               IN   VARCHAR2,
   argument_4               IN   VARCHAR2,
   argument_5               IN   VARCHAR2)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| user_language | VARCHAR2 | IN | The language of the current session. |
| message_id | NUMBER | IN | Id of the alert message |
| argument_1 | VARCHAR2 | IN | The first argument in the alert message. |
| argument_2 | VARCHAR2 | IN | The second argument in the alert message. |
| argument_3 | VARCHAR2 | IN | The third argument in the alert message. |
| argument_4 | VARCHAR2 | IN | The fourth argument in the alert message. |
| argument_5 | VARCHAR2) | IN | The fifth argument in the alert message. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_SERVER_ALERT.EXPAND_MESSAGE( user_language IN VARCHAR2, message_id IN NUMBER, argument_1 IN VARCHAR2, argument_2 IN VARCHAR2, argument_3 IN VARCHAR2, argument_4 IN VARCHAR2, argument_5 IN VARCHAR2) RETURN VARCHAR2; Parameters Table 152-5 EXPAND_MESSAGE Function Parameters Parameter Description user_language The language of the current session. message_id Id of the alert message argument_1 The first argument in the alert message. argument_2 The second argument in the alert message. argument_3 The third argument in the alert message. argument_4 The fourth argument in the alert message. argument_5 The fifth argument in the alert message.