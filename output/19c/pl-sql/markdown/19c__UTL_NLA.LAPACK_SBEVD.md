---
id: 19c__UTL_NLA.LAPACK_SBEVD
name: UTL_NLA.LAPACK_SBEVD
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.LAPACK_SBEVD

This procedure computes all the eigenvalues and, optionally, eigenvectors of a real symmetric matrix A . If eigenvectors are desired, it uses a divide and conquer algorithm that makes mild assumptions about floating point arithmetic.

## Syntax

```sql
UTL_NLA.LAPACK_SBEVD (
   jobz     IN      flag,
   uplo     IN      flag,
   n        IN      POSITIVEN,
   kd       IN      NATURALN,
   ab       IN OUT  UTL_NLA_ARRAY_DBL,
   ldab     IN      POSITIVEN,
   w        IN OUT  UTL_NLA_ARRAY_DBL,
   z        IN OUT  UTL_NLA_ARRAY_DBL,
   ldz       IN      POSITIVEN,
   info     OUT     INTEGER,
   pack     IN      flag DEFAULT 'C');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| jobz | flag | IN | 'N' : Compute eigenvalues only. 'V' : Compute eigenvalues and eigenvectors. |
| uplo | flag | IN | 'U' : Upper triangle of A is stored. 'L' : Lower triangle of A is stored. |
| n | POSITIVEN | IN | The order of the matrix a. N >= 0 . |
| kd | NATURALN | IN | The number of superdiagonals of the matrix A if uplo = 'U' , or the number of subdiagonals if uplo = 'L' . kd >= 0 . |
| ab | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (ldab, n) . On entry, the upper or lower triangle of the symmetric band matrix A stored in the first kd+1 rows of the array. The j -th column of A is stored in the j -th column of the array ab : If uplo = 'U' , ab(kd+1+i-j,j) = a(i,j) for max(1,j-kd)<=i<=j . If uplo = 'L' , AB(1+i-j,j) = A(i,j) for j<=i<=min(n,j+kd) . On exit, ab is overwritten by values generated during the reduction to tridiagonal form: If uplo = 'U' , the diagonal and first superdiagonal of the tridiagonal matrix T are returned in rows kd and kd+1 of ab . If uplo = 'L' , the diagonal and first subdiagonal of T are returned in the first two rows of ab . |
| ldab | POSITIVEN | IN | The leading dimension of the array ab. ldab >= kd + 1 . |
| w | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldz,n) . If info = 0 , the eigenvalues in ascending order. |
| z | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (n) . If jobz = 'V' , then if info = 0 , z contains the orthonormal eigenvectors of the matrix A , with the i -th column of z holding the eigenvector associated with w(i) . If jobz = 'N' , then z is not referenced. |
| ldz | POSITIVEN | IN | The leading dimension of the array z . ldz >= 1 , and if jobz = 'v' , ldz >= max(1,n) . |
| info | INTEGER | OUT | = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , the algorithm failed to converge; i off-diagonal elements of an intermediate tridiagonal form did not converge to zero |
| pack | flag | IN | (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major |

## Usage Notes

See Also: LAPACK Driver Routines (LLS and Eigenvalue Problems) Subprograms for other subprograms in this group See Also: LAPACK Driver Routines (LLS and Eigenvalue Problems) Subprograms for other subprograms in this group Syntax UTL_NLA.LAPACK_SBEVD ( jobz IN flag, uplo IN flag, n IN POSITIVEN, kd IN NATURALN, ab IN OUT UTL_NLA_ARRAY_DBL, ldab IN POSITIVEN, w IN OUT UTL_NLA_ARRAY_DBL, z IN OUT UTL_NLA_ARRAY_DBL, ldz IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); UTL_NLA.LAPACK_SBEVD ( jobz IN flag, uplo IN flag, n IN POSITIVEN, kd IN NATURALN, ab IN OUT UTL_NLA_ARRAY_FLT, ldab IN POSITIVEN, w IN OUT UTL_NLA_ARRAY_FLT, z IN OUT UTL_NLA_ARRAY_FLT, ldz IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); Parameters Table 271-52 LAPACK_SBEVD Procedure Parameters Parameter Description jobz 'N' : Compute eigenvalues only. 'V' : Compute eigenvalues and eigenvectors. uplo 'U' : Upper triangle of A is stored. 'L' : Lower triangle of A is stored. n The order of the matrix a. N >= 0 . kd The number of superdiagonals of the matrix A if uplo = 'U' , or the number of subdiagonals if uplo = 'L' . kd >= 0 . ab UTL_NLA_ARRAY_FLT / DBL, DIMENSION (ldab, n) . On entry, the upper or lower triangle of the symmetric band matrix A stored in the first kd+1 rows of the array. The j -th column of A is stored in the j -th column of the array ab : If uplo = 'U' , ab(kd+1+i-j,j) = a(i,j) for max(1,j-kd)<=i<=j . If uplo = 'L' , AB(1+i-j,j) = A(i,j) for j<=i<=min(n,j+kd) . On exit, ab is overwritten by values generated during the reduction to tridiagonal form: If uplo = 'U' , the diagonal and first superdiagonal of the tridiagonal matrix T are returned in rows kd and kd+1 of ab . If uplo = 'L' , the diagonal and first subdiagonal of T are returned in the first two rows of ab . ldab The leading dimension of the array ab. ldab >= kd + 1 . w UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldz,n) . If info = 0 , the eigenvalues in ascending order. z UTL_NLA_ARRAY_FLT/DBL , DIMENSION (n) . If jobz = 'V' , then if info = 0 , z contains the orthonormal eigenvectors of the matrix A , with the i -th column of z holding the eigenvector associated with w(i) . If jobz = 'N' , then z is not referenced. ldz The leading dimension of the array z . ldz >= 1 , and if jobz = 'v' , ldz >= max(1,n) . info = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , the algorithm failed to converge; i off-diagonal elements of an intermediate tridiagonal form did not converge to zero pack (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major