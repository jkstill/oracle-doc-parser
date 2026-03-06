---
id: 19c__DBMS_STATS.PREPARE_COLUMN_VALUES
name: DBMS_STATS.PREPARE_COLUMN_VALUES
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.PREPARE_COLUMN_VALUES

These procedures convert user-specified minimum, maximum, and histogram endpoint actual values into Oracle's internal representation for future storage using SET_COLUMN_STATS .

## Syntax

```sql
DBMS_STATS.PREPARE_COLUMN_VALUES (
   srec     IN OUT StatRec, 
   charvals        CHARARRAY);

DBMS_STATS.PREPARE_COLUMN_VALUES (
   srec      IN OUT StatRec, 
   datevals         DATEARRAY);

DBMS_STATS.PREPARE_COLUMN_VALUES ( 
   srec     IN OUT StatRec, 
   dblvals         DBLARRAY);

DBMS_STATS.PREPARE_COLUMN_VALUES ( 
   srec     IN OUT StatRec, 
   fltvals         FLTARRAY);

DBMS_STATS.PREPARE_COLUMN_VALUES (
   srec     IN OUT StatRec, 
   numvals         NUMARRAY);

DBMS_STATS.PREPARE_COLUMN_VALUES ( 
   srec     IN OUT StatRec, 
   rawvals         RAWARRAY);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| srec.epc |  |  | Number of values specified in charvals , datevals , dblvals , fltvals , numvals , or rawvals . This value must be between 2 and 2050, inclusive, and it should be set to 2 for procedures which do not allow histogram information ( nvarchar and rowid ). The first corresponding array entry should hold the minimum value for the column, and the last entry should hold the maximum. If there are more than two entries, then all the others hold the remaining height-balanced or frequency histogram endpoint values (with in-between values ordered from next-smallest to next-largest). This value may be adjusted to account for compression, so the returned value should be left as is for a call to SET_COLUMN_STATS . |
| srec.bkvals |  |  | If you want a frequency or hybrid histogram, this array contains the number of occurrences of each distinct value specified in charvals , datevals , dblvals , fltvals , numvals , or rawvals . Otherwise, it is merely an output parameter, and it must be set to NULL when this procedure is called. |
| srec.rpcnts |  |  | If you want a hybrid histogram, this array contains the total frequency of values that are less than or equal to each distinct value specified in charvals , datevals , numvals , or rawvals . Otherwise, it is merely an output argument and must be set to NULL when this procedure is called. As an example, for a given array numvals with numvals(i)=4, rpcnts(i)=13 means that there are 13 rows in the column which are less than or equal to 4. Note: Whenever srec.rpcnts is populated, srec.bkvals must be populated as described above. Whenever bkvals and/or rpcnts are populated, there should not be any duplicates in charvals , datevals , numvals , or rawvals . |

## Usage Notes

Syntax DBMS_STATS.PREPARE_COLUMN_VALUES ( srec IN OUT StatRec, charvals CHARARRAY); DBMS_STATS.PREPARE_COLUMN_VALUES ( srec IN OUT StatRec, datevals DATEARRAY); DBMS_STATS.PREPARE_COLUMN_VALUES ( srec IN OUT StatRec, dblvals DBLARRAY); DBMS_STATS.PREPARE_COLUMN_VALUES ( srec IN OUT StatRec, fltvals FLTARRAY); DBMS_STATS.PREPARE_COLUMN_VALUES ( srec IN OUT StatRec, numvals NUMARRAY); DBMS_STATS.PREPARE_COLUMN_VALUES ( srec IN OUT StatRec, rawvals RAWARRAY); Parameters Table 171-87 PREPARE_COLUMN_VALUES Procedure Parameters Parameter Description srec.epc Number of values specified in charvals , datevals , dblvals , fltvals , numvals , or rawvals . This value must be between 2 and 2050, inclusive, and it should be set to 2 for procedures which do not allow histogram information ( nvarchar and rowid ). The first corresponding array entry should hold the minimum value for the column, and the last entry should hold the maximum. If there are more than two entries, then all the others hold the remaining height-balanced or frequency histogram endpoint values (with in-between values ordered from next-smallest to next-largest). This value may be adjusted to account for compression, so the returned value should be left as is for a call to SET_COLUMN_STATS . srec.bkvals If you want a frequency or hybrid histogram, this array contains the number of occurrences of each distinct value specified in charvals , datevals , dblvals , fltvals , numvals , or rawvals . Otherwise, it is merely an output parameter, and it must be set to NULL when this procedure is called. srec.rpcnts If you want a hybrid histogram, this array contains the total frequency of values that are less than or equal to each distinct value specified in charvals , datevals , numvals , or rawvals . Otherwise, it is merely an output argument and must be set to NULL when this procedure is called. As an example, for a given array numvals with numvals(i)=4, rpcnts(i)=13 means that there are 13 rows in the column which are less than or equal to 4. Note: Whenever srec.rpcnts is populated, srec.bkvals must be populated as described above. Whenever bkvals and/or rpcnts are populated, there should not be any duplicates in charvals , datevals , numvals , or rawvals . Datatype-specific input parameters (use one) are shown in Table 171-88 . Table 171-88 Datatype-Specific Input Parameters Type Description charvals The array of values when the column type is character-based. Up to the first 64 bytes of each string should be provided. Arrays must have between 2 and 2050 entries, inclusive. If the datatype is fixed CHAR , the strings must be space-padded to 15 characters for correct normalization. datevals Array of values when the column type is date-based dblvals Array of values when the column type is double-based fltvals Array of values when the column type is float-based numvals Array of values when the column type is numeric-based rawvals Array of values when the column type is RAW . Up to the first 64 bytes of each value should be provided. nvmin, nvmax Minimum and maximum values when the column type is national character set based. No histogram information can be provided for a column of this type. If the datatype is fixed CHAR , the strings must be space-padded to 15 characters for correct normalization. rwmin, rwmax Minimum and maximum values when the column type is rowid . No histogram information is provided for a column of this type. Output Parameters Table 171-89 PREPARE_COLUMN_VALUES Procedure Output Parameters Parameter Description srec.minval Internal representation of the minimum suitable for use in a call to SET_COLUMN_STATS srec.maxval Internal representation of the maximum suitable for use in a call to SET_COLUMN_STATS srec.bkvals Array suitable for use in a call to SET_COLUMN_STATS srec.novals Array suitable for use in a call to SET_COLUMN_STATS srec.eavals Array suitable for use in a call to SET_COLUMN_STATS srec.rpcnts Array suitable for use in a call to SET_COLUMN_STATS Exceptions ORA-20001 : Invalid or inconsistent input values Usage Notes No special privilege or role is needed to invoke this procedure.