---
id: 19c__UTL_NLA.LAPACK_STEV
name: UTL_NLA.LAPACK_STEV
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.LAPACK_STEV

This procedure computes all eigenvalues and, optionally, eigenvectors of a real symmetric tridiagonal matrix A .

## Syntax

```sql
UTL_NLA.LAPACK_STEV (
   jobz     IN      flag,
   n        IN      POSITIVEN,
   d        IN OUT  UTL_NLA_ARRAY_DBL,
   e        IN OUT  UTL_NLA_ARRAY_DBL,
   z        IN OUT  UTL_NLA_ARRAY_DBL,
   ldz      IN      POSITIVEN,
   info     OUT     INTEGER,
   pack     IN      flag DEFAULT 'C');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| jobz | flag | IN | 'N' : Compute eigenvalues only. 'V' : Compute eigenvalues and eigenvectors. |
| n | POSITIVEN | IN | The order of the matrix a. N >= 0 . |
| d | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (n) . On entry, the n diagonal elements of the tridiagonal matrix A . On exit, if info = 0 , the eigenvalues in ascending order. |
| e | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (n) . On entry, the (n-1) subdiagonal elements of the tridiagonal matrix A , stored in elements 1 to n-1 of e . e(n) need not be set, but is used by the subprogram. On exit, the contents of e are destroyed. |
| z | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldz, n) . If jobz = 'V' , then if info = 0 , z contains the orthonormal eigenvectors of the matrix A , with the i -th column of z holding the eigenvector associated with d(i) . If jobz = 'N' , then z is not referenced. |
| ldz | POSITIVEN | IN | The leading dimension of the array z . ldz >= 1 , and if jobz = 'v' , ldz >= max(1,n) . |
| info | INTEGER | OUT | = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , the algorithm failed to converge; i off-diagonal elements of an intermediate tridiagonal form did not converge to zero |
| pack | flag | IN | (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major |

## Usage Notes

See Also: LAPACK Driver Routines (LLS and Eigenvalue Problems) Subprograms for other subprograms in this group See Also: LAPACK Driver Routines (LLS and Eigenvalue Problems) Subprograms for other subprograms in this group Syntax UTL_NLA.LAPACK_STEV ( jobz IN flag, n IN POSITIVEN, d IN OUT UTL_NLA_ARRAY_DBL, e IN OUT UTL_NLA_ARRAY_DBL, z IN OUT UTL_NLA_ARRAY_DBL, ldz IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); UTL_NLA.LAPACK_STEV ( jobz IN flag, n IN POSITIVEN, d IN OUT UTL_NLA_ARRAY_FLT, e IN OUT UTL_NLA_ARRAY_FLT, z IN OUT UTL_NLA_ARRAY_FLT, ldz IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); Parameters Table 271-56 LAPACK_STEV Procedure Parameters Parameter Description jobz 'N' : Compute eigenvalues only. 'V' : Compute eigenvalues and eigenvectors. n The order of the matrix a. N >= 0 . d UTL_NLA_ARRAY_FLT/DBL , DIMENSION (n) . On entry, the n diagonal elements of the tridiagonal matrix A . On exit, if info = 0 , the eigenvalues in ascending order. e UTL_NLA_ARRAY_FLT/DBL , DIMENSION (n) . On entry, the (n-1) subdiagonal elements of the tridiagonal matrix A , stored in elements 1 to n-1 of e . e(n) need not be set, but is used by the subprogram. On exit, the contents of e are destroyed. z UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldz, n) . If jobz = 'V' , then if info = 0 , z contains the orthonormal eigenvectors of the matrix A , with the i -th column of z holding the eigenvector associated with d(i) . If jobz = 'N' , then z is not referenced. ldz The leading dimension of the array z . ldz >= 1 , and if jobz = 'v' , ldz >= max(1,n) . info = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , the algorithm failed to converge; i off-diagonal elements of an intermediate tridiagonal form did not converge to zero pack (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major