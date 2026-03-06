---
id: 19c__NLS_ISO_CURRENCY
name: NLS_ISO_CURRENCY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
source_file: NLS_ISO_CURRENCY.html
---

# NLS_ISO_CURRENCY

NLS_ISO_CURRENCY determines the string to use as the international currency symbol corresponding to the C number format element in a call to the TO_CHAR function.

## Usage Notes

Local currency symbols can be ambiguous. For example, a dollar sign ($) can refer to U.S. dollars or Australian dollars. ISO Specification 4217 defines unique "international" currency symbols for the currencies of specific territories or countries. The value of the NLS_ISO_CURRENCY parameter is the Oracle name of the territory whose ISO currency symbol is returned in place of the C number format element. For example, if NLS_ISO_CURRENCY is set to AMERICA , the string 'USD' is returned by TO_CHAR where the C element is specified in the format. Note: The value of this initialization parameter NLS_ISO_CURRENCY is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the NLS_LANG client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored. See Also: Oracle Database Globalization Support Guide for more information about this parameter Oracle Database SQL Language Reference for information on number format elements Note: The value of this initialization parameter NLS_ISO_CURRENCY is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the NLS_LANG client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored. See Also: Oracle Database Globalization Support Guide for more information about this parameter Oracle Database SQL Language Reference for information on number format elements