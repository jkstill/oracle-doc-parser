---
id: 19c__DBMS_MGWMSG
name: DBMS_MGWMSG
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWMSG
tags: [dbms_mgwmsg]
source_file: DBMS_MGWMSG.html
---

# DBMS_MGWMSG

DBMS_MGWMSG uses types to specify certain information.

## Syntax

```sql
TYPE SYS.MGW_NAME_VALUE_T IS OBJECT(
   name               VARCHAR2(250),
   type               INTEGER,
   integer_value      INTEGER,
   number_value       NUMBER,
   text_value         VARCHAR2(4000),
   raw_value          RAW(2000),
   date_value         DATE,

-- Methods
STATIC FUNCTION CONSTRUCT
RETURN SYS.MGW_NAME_VALUE_T,

STATIC FUNCTION CONSTRUCT_BOOLEAN (
   name   IN VARCHAR2,
   value  IN INTEGER )
RETURN SYS.MGW_NAME_VALUE_T,

STATIC FUNCTION CONSTRUCT_BYTE (
   name   IN VARCHAR2,
   value  IN INTEGER )
RETURN SYS.MGW_NAME_VALUE_T,

STATIC FUNCTION CONSTRUCT_SHORT (
   name   IN VARCHAR2,
   value  IN INTEGER )
RETURN SYS.MGW_NAME_VALUE_T,

STATIC FUNCTION CONSTRUCT_INTEGER (
   name   IN VARCHAR2,
   value  IN INTEGER )
RETURN SYS.MGW_NAME_VALUE_T,

STATIC FUNCTION CONSTRUCT_LONG (
   name   IN VARCHAR2,
   value  IN NUMBER )
RETURN SYS.MGW_NAME_VALUE_T,

STATIC FUNCTION CONSTRUCT_FLOAT (
   name   IN VARCHAR2,
   value  IN NUMBER )
RETURN SYS.MGW_NAME_VALUE_T,

STATIC FUNCTION CONSTRUCT_DOUBLE (
   name   IN VARCHAR2,
   value  IN NUMBER )
RETURN SYS.MGW_NAME_VALUE_T,

STATIC FUNCTION CONSTRUCT_TEXT (
   name   IN VARCHAR2,
   value  IN VARCHAR2 )
RETURN SYS.MGW_NAME_VALUE_T,

STATIC FUNCTION CONSTRUCT_RAW (
   name   IN VARCHAR2,
   value  IN RAW )
RETURN SYS.MGW_NAME_VALUE_T,

STATIC FUNCTION CONSTRUCT_DATE (
   name   IN VARCHAR2,
   value  IN DATE )
RETURN SYS.MGW_NAME_VALUE_T );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2(250) | IN | Field name |
| id |  |  | Field identifier |
| value | INTEGER | IN | Field data |

**Returns:** `SYS.MGW_NAME_VALUE_T`

## Usage Notes

SYS.MGW_NAME_VALUE_T Type SYS.MGW_NAME_VALUE_T Type-Attribute Mapping SYS.MGW_NAME_TYPE_ARRAY_T Type SYS.MGW_TEXT_VALUE_T Type SYS.MGW_RAW_VALUE_T Type SYS.MGW_BASIC_MSG_T Type SYS.MGW_NUMBER_ARRAY_T Type SYS.MGW_TIBRV_FIELD_T Type SYS.MGW_TIBRV_MSG_T Type The name attribute, type attribute, and one of the <>_value attributes are typically not NULL . Syntax TYPE SYS.MGW_NAME_VALUE_T IS OBJECT( name VARCHAR2(250), type INTEGER, integer_value INTEGER, number_value NUMBER, text_value VARCHAR2(4000), raw_value RAW(2000), date_value DATE, -- Methods STATIC FUNCTION CONSTRUCT RETURN SYS.MGW_NAME_VALUE_T, STATIC FUNCTION CONSTRUCT_BOOLEAN ( name IN VARCHAR2, value IN INTEGER ) RETURN SYS.MGW_NAME_VALUE_T, STATIC FUNCTION CONSTRUCT_BYTE ( name IN VARCHAR2, value IN INTEGER ) RETURN SYS.MGW_NAME_VALUE_T, STATIC FUNCTION CONSTRUCT_SHORT ( name IN VARCHAR2, value IN INTEGER ) RETURN SYS.MGW_NAME_VALUE_T, STATIC FUNCTION CONSTRUCT_INTEGER ( name IN VARCHAR2, value IN INTEGER ) RETURN SYS.MGW_NAME_VALUE_T, STATIC FUNCTION CONSTRUCT_LONG ( name IN VARCHAR2, value IN NUMBER ) RETURN SYS.MGW_NAME_VALUE_T, STATIC FUNCTION CONSTRUCT_FLOAT ( name IN VARCHAR2, value IN NUMBER ) RETURN SYS.MGW_NAME_VALUE_T, STATIC FUNCTION CONSTRUCT_DOUBLE ( name IN VARCHAR2, value IN NUMBER ) RETURN SYS.MGW_NAME_VALUE_T, STATIC FUNCTION CONSTRUCT_TEXT ( name IN VARCHAR2, value IN VARCHAR2 ) RETURN SYS.MGW_NAME_VALUE_T, STATIC FUNCTION CONSTRUCT_RAW ( name IN VARCHAR2, value IN RAW ) RETURN SYS.MGW_NAME_VALUE_T, STATIC FUNCTION CONSTRUCT_DATE ( name IN VARCHAR2, value IN DATE ) RETURN SYS.MGW_NAME_VALUE_T ); Attributes Table 111-5 SYS.MGW_NAME_VALUE_T Attributes Attribute Description name Name associated with the value type Value type. Refer to the DBMS_MGWMSG.<>_VALUE constants in Table 111-1 . This indicates which Java datatype and class are associated with the value. It also indicates which attribute stores the value. integer_value Stores a numeric integer value number_value Stores a numeric float or large integer value text_value Stores a text value raw_value Stores a RAW (bytes) value date_value Stores a date value SYS.MGW_NAME_VALUE_T Type-Attribute Mapping Table 111-6 shows the mapping between the value type and the attribute used to store the value. Table 111-6 SYS.MGW_NAME_VALUE_T Type Attribute Mapping Type Value Stored in Attribute DBMS_MGWMSG.TEXT_VALUE text_value DBMS_MGWMSG.RAW_VALUE raw_value DBMS_MGWMSG.BOOLEAN_VALUE integer_value DBMS_MGWMSG.BYTE_VALUE integer_value DBMS_MGWMSG.SHORT_VALUE integer_value DBMS_MGWMSG.INTEGER_VALUE integer_value DBMS_MGWMSG.LONG_VALUE number_value DBMS_MGWMSG.FLOAT_VALUE number_value DBMS_MGWMSG.DOUBLE_VALUE number_value DBMS_MGWMSG.DATE_VALUE date_value