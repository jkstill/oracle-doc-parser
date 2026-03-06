---
id: 19c__NLS_TIMESTAMP_TZ_FORMAT
name: NLS_TIMESTAMP_TZ_FORMAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
source_file: NLS_TIMESTAMP_TZ_FORMAT.html
---

# NLS_TIMESTAMP_TZ_FORMAT

NLS_TIMESTAMP_TZ_FORMAT defines the default timestamp with time zone format to use with the TO_CHAR and TO_TIMESTAMP_TZ functions.

## Usage Notes

The value must be surrounded by quotation marks as follows: NLS_TIMESTAMP_TZ_FORMAT = 'YYYY-MM-DD HH:MI:SS.FF TZH:TZM' You can specify the value of NLS_TIMESTAMP_TZ_FORMAT by setting it in the initialization parameter file. You can specify its value for a client as a client environment variable. You can also alter the value of NLS_TIMESTAMP_TZ_FORMAT by changing its value in the initialization parameter and then restarting the instance. To alter the value during a session use the ALTER SESSION SET statement. Note: The value of this initialization parameter NLS_TIMESTAMP_TZ_FORMAT is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the NLS_LANG client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored. See Also: Oracle Database Globalization Support Guide for more information about this parameter Note: The value of this initialization parameter NLS_TIMESTAMP_TZ_FORMAT is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the NLS_LANG client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored. See Also: Oracle Database Globalization Support Guide for more information about this parameter