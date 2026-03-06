---
id: 19c__NLS_CALENDAR
name: NLS_CALENDAR
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
source_file: NLS_CALENDAR.html
---

# NLS_CALENDAR

NLS_CALENDAR specifies which calendar system Oracle uses.

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content NLS_CALENDAR can have one of the following values: Arabic Hijrah English Hijrah Gregorian Japanese Imperial Persian ROC Official (Republic of China) Thai Buddha For example, suppose NLS_CALENDAR is set to "Japanese Imperial", the date format is "E YY-MM-DD". ("E" is the date format element for the abbreviated era name.) If the date is May 15, 1997, then the SYSDATE is displayed as follows: SELECT SYSDATE FROM DUAL; SYSDATE -------- H 09-05-15 Note: The value of the initialization parameter NLS_CALENDER is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. If the initialization parameter is not specified, the initial session value becomes GREGORIAN . This initial value is overridden by a client-side value if the client is OCI-based and the NLS_LANG client setting (environment variable) is defined. See Also: Oracle Database Globalization Support Guide for a listing of available calendar systems Note: The value of the initialization parameter NLS_CALENDER is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. If the initialization parameter is not specified, the initial session value becomes GREGORIAN . This initial value is overridden by a client-side value if the client is OCI-based and the NLS_LANG client setting (environment variable) is defined. See Also: Oracle Database Globalization Support Guide for a listing of available calendar systems