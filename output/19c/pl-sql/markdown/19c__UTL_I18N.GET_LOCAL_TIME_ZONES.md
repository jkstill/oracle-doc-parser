---
id: 19c__UTL_I18N.GET_LOCAL_TIME_ZONES
name: UTL_I18N.GET_LOCAL_TIME_ZONES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_I18N
tags: [utl_i18n]
source_file: UTL_I18N.html
---

# UTL_I18N.GET_LOCAL_TIME_ZONES

This function returns the local time zone IDs for the specified territory.

## Syntax

```sql
UTL_I18N.GET_LOCAL_TIME_ZONES ( 
   territory      IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL)
RETURN STRING_ARRAY;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| territory | VARCHAR2 | IN | Specifies a valid Oracle territory. It is case-insensitive. |

**Returns:** `STRING_ARRAY`

## Usage Notes

Syntax UTL_I18N.GET_LOCAL_TIME_ZONES ( territory IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL) RETURN STRING_ARRAY; Parameters Table 265-10 GET_LOCAL_TIME_ZONES Function Parameters Parameter Description territory Specifies a valid Oracle territory. It is case-insensitive. Usage Notes If the user specifies an invalid territory name, then the function returns a NULL string. Examples Creates a function that returns the list of time zones locally used in the territory AZERBAIJAN followed by the general common time zones. This is useful for when the user's territory is known and the application still allows the user to choose other time zones as a user's preference. CREATE OR REPLACE FUNCTION get_time_zones (territory IN VARCHAR2 CHARACTER SET ANY_CS) RETURN utl_i18n.string_array IS retval utl_i18n.string_array; retval2 utl_i18n.string_array; stpos INTEGER; BEGIN retval := utl_i18n.get_local_time_zones( territory); retval2 := utl_i18n.get_common_time_zones; stpos := retval.LAST + 1; retval(stpos) := '-----'; -- a separator FOR i IN retval2.FIRST..retval2.LAST LOOP stpos := stpos + 1; retval(stpos) := retval2(i); END LOOP; RETURN retval; END; / Returns the list of local time zones for AZERBAIJAN followed by the common time zones with a separator string of five dashes (-----). DECLARE retval UTL_I18N.STRING_ARRAY; cnt INTEGER; BEGIN DBMS_OUTPUT.ENABLE(100000); retval UTL_I18N.GET_TIME_ZONES('AZERBAIJAN'); cnt := retval.FIRST; WHILE cnt IS NOT NULL LOOP DBMS_OUTPUT.PUT_LINE(retval(cnt)); cnt := retval.NEXT(cnt); END LOOP; END; / Asia/Baku ----- Pacific/Pago_Pago Pacific/Honolulu America/Anchorage America/Vancouver America/Los_Angeles America/Tijuana America/Edmonton America/Denver America/Phoenix America/Mazatlan America/Winnipeg America/Regina America/Chicago America/Mexico_City America/Guatemala America/El_Salvador America/Managua America/Costa_Rica America/Montreal ...