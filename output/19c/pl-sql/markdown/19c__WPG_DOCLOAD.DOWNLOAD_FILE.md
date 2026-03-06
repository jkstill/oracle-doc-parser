---
id: 19c__WPG_DOCLOAD.DOWNLOAD_FILE
name: WPG_DOCLOAD.DOWNLOAD_FILE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: WPG_DOCLOAD
tags: [wpg_docload]
source_file: WPG_DOCLOAD.html
---

# WPG_DOCLOAD.DOWNLOAD_FILE

There are three versions of this download file procedure.

## Syntax

```sql
WPG_DOCLOAD.DOWNLOAD_FILE(
   p_filename      IN             VARCHAR2, 
   p_bcaching      IN             BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_filename | VARCHAR2 | IN | The file to download from the document table. |
| p_blob |  |  | The BLOB to download. |
| p_bfile |  |  | The BFILE to download (see Usage Notes ). |
| p_bcaching | BOOLEAN | IN | Whether browser caching is enabled (see Usage Notes ). |

## Usage Notes

The first version downloads files and is invoked from within a document download procedure to signal the PL/SQL Gateway that p_filename is to be downloaded from the document table to the client's browser. The second version can be called from within any procedure to signal the PL/SQL Gateway that p_blob is to be downloaded to the client's browser. The third version can be called from within any procedure to signal the PL/SQL Gateway that p_bfile is to be downloaded to the client's browser. Syntax WPG_DOCLOAD.DOWNLOAD_FILE( p_filename IN VARCHAR2, p_bcaching IN BOOLEAN DEFAULT TRUE); WPG_DOCLOAD.DOWNLOAD_FILE( p_blob IN OUT NOCOPY BLOB); WPG_DOCLOAD.DOWNLOAD_FILE( p_bfile IN OUT BFILE); Parameters Table 279-2 DOWNLOAD_FILE Procedure Parameters Parameter Description p_filename The file to download from the document table. p_blob The BLOB to download. p_bfile The BFILE to download (see Usage Notes ). p_bcaching Whether browser caching is enabled (see Usage Notes ). Usage Notes Normally, a document will be downloaded to the browser unless the browser sends an 'If-Modified-Since' header to the gateway indicating that it has the requested document in its cache. In that case, the gateway will determine if the browser's cached copy is up to date, and if it is, it will send an HTTP 304 status message to the browser indicating that the browser should display the cached copy. However, because a document URL and a document do not necessarily have a one-to-one relationship in the PL/SQL Web Gateway, in some cases it may be undesirable to have the cached copy of a document displayed. In those cases, the p_bcaching parameter should be set to FALSE to indicate to the gateway to ignore the 'If-Modified-Since' header, and download the document. p_bfile and p_blob are declared as IN OUT because the locator is initially opened to check for file accessibility and existence. The open operation can only be performed if the locator is writable and readable.