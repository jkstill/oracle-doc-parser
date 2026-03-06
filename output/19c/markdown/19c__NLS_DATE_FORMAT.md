---
id: 19c__NLS_DATE_FORMAT
name: NLS_DATE_FORMAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
source_file: NLS_DATE_FORMAT.html
---

# NLS_DATE_FORMAT

NLS_DATE_FORMAT = " format "

## Usage Notes

The value of this parameter can be any valid date format mask, and the value must be surrounded by double quotation marks. For example: NLS_DATE_FORMAT = "MM/DD/YYYY" Note: The value of this initialization parameter NLS_DATE_FORMAT is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the NLS_LANG client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored. See Also: Oracle Database Globalization Support Guide for more information about this parameter Note: The value of this initialization parameter NLS_DATE_FORMAT is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the NLS_LANG client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored. See Also: Oracle Database Globalization Support Guide for more information about this parameter