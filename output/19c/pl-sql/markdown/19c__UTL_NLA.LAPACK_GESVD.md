---
id: 19c__UTL_NLA.LAPACK_GESVD
name: UTL_NLA.LAPACK_GESVD
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.LAPACK_GESVD

This procedures computes the singular value decomposition (SVD) of a real m by n matrix A , optionally computing the left and/or right singular vectors.

## Syntax

```sql
A = U * SIGMA * transpose(V)
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| jobu |  |  | Specifies options for computing all or part of the matrix U : 'A' : All m columns of U are returned in array U . 'S' : The first min(m,n) columns of U (the left singular vectors) are returned in the array U . 'O' : The first min(m,n) columns of U (the left singular vectors) are overwritten on the array a . jobu and jobvt cannot both be 'O' 'N' : No columns of U (no left singular vectors) are computed. |
| jobvt |  |  | Specifies options for computing all or part of the matrix V**T : 'A' : All n rows of V**T are returned in the array vt . 'S' : The first min(m,n) rows of V**T (the right singular vectors) are returned in the array vt . 'O' : The first min(m,n) rows of V**T (the right singular vectors) are overwritten on the array a . jobvt and jobu cannot both be 'O'. 'N' : No rows of V**T (no right singular vectors) are computed. |
| m |  |  | The order of the matrix a. M >= 0 . |
| n |  |  | The order of the matrix a. N >= 0 . |
| a |  |  | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (lda, n) . On entry, the n by n matrix A . On exit: If jobu = 'O' , A is overwritten with the first min(m,n) columns of U (the left singular vectors, stored columnwise); If jobvt = 'O' , A is overwritten with the first min(m,n) rows of V**T (the right singular vectors, stored rowwise); If jobu.ne.'O' and jobvt.ne.'O' , the contents of A are destroyed. |
| lda |  |  | The leading dimension of the array a. lda >= max(1,n) . |
| s |  |  | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (min(m,n)) . The singular values of A , sorted so that S(i) >= S(i+1) . |
| u |  |  | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldu,ucol).(ldu,m) if jobu = 'A' or (ldu,min(m,n)) if jobu = 'S' . If jobu = 'A' , U contains the m by m orthogonal matrix U . If jobu = 'S' , U contains the first min(m,n) columns of U (the left singular vectors, stored columnwise). If jobu = 'N' or 'O' , U is not referenced. |
| ldu |  |  | The leading dimension of the array U. ldu >= 1. If jobu = 'S' or ' a' , ldu >= m . |
| vt |  |  | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldvt, n) . If jobvt = 'A' , vt contains the n by n orthogonal matrix V**T . If jobvt = 'S' , vt contains the first min(m,n) rows of V**T (the right singular vectors, stored rowwise). If jobvt = 'N' or 'O' , vt is not referenced. |
| ldvt |  |  | The leading dimension of the array vt . ldvt >= 1 . If jobvt = 'A' , ldvt >= n . If jobvt = 'S' , ldvt >= min(m,n) . |
| info |  |  | = 0 : successful exit < 0 : If info = -i , the i -th argument had an illegal value > 0 : If SBDSQR did not converge, info specifies how many superdiagonals of an intermediate bidiagonal form B did not converge to zero. |
| pack |  |  | (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major |

## Usage Notes

The SVD is written A = U * SIGMA * transpose(V) where SIGMA is an m by n matrix which is zero except for its min(m,n) diagonal elements, U is an m by m orthogonal matrix, and V is an n by n orthogonal matrix. The diagonal elements of SIGMA are the singular values of A , they are real and non-negative, and are returned in descending order. The first min(m,n) columns of U and V are the left and right singular vectors of A . Note that the routine returns V**T , not V . See Also: LAPACK Driver Routines (LLS and Eigenvalue Problems) Subprograms for other subprograms in this group See Also: LAPACK Driver Routines (LLS and Eigenvalue Problems) Subprograms for other subprograms in this group Syntax UTL_NLA.LAPACK_GESVD ( jobu IN flag, jobvt IN flag, m IN POSITIVEN, n IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, s IN OUT UTL_NLA_ARRAY_DBL, u IN OUT UTL_NLA_ARRAY_DBL, ldu IN POSITIVEN, vt IN OUT UTL_NLA_ARRAY_DBL, ldvt IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); UTL_NLA.LAPACK_GESVD ( jobu IN flag, jobvt IN flag, m IN POSITIVEN, n IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, s IN OUT UTL_NLA_ARRAY_FLT, u IN OUT UTL_NLA_ARRAY_FLT, ldu IN POSITIVEN, vt IN OUT UTL_NLA_ARRAY_FLT, ldvt IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); Parameters Table 271-44 LAPACK_GESVD Procedure Parameters Parameter Description jobu Specifies options for computing all or part of the matrix U : 'A' : All m columns of U are returned in array U . 'S' : The first min(m,n) columns of U (the left singular vectors) are returned in the array U . 'O' : The first min(m,n) columns of U (the left singular vectors) are overwritten on the array a . jobu and jobvt cannot both be 'O' 'N' : No columns of U (no left singular vectors) are computed. jobvt Specifies options for computing all or part of the matrix V**T : 'A' : All n rows of V**T are returned in the array vt . 'S' : The first min(m,n) rows of V**T (the right singular vectors) are returned in the array vt . 'O' : The first min(m,n) rows of V**T (the right singular vectors) are overwritten on the array a . jobvt and jobu cannot both be 'O'. 'N' : No rows of V**T (no right singular vectors) are computed. m The order of the matrix a. M >= 0 . n The order of the matrix a. N >= 0 . a UTL_NLA_ARRAY_FLT/DBL , DIMENSION (lda, n) . On entry, the n by n matrix A . On exit: If jobu = 'O' , A is overwritten with the first min(m,n) columns of U (the left singular vectors, stored columnwise); If jobvt = 'O' , A is overwritten with the first min(m,n) rows of V**T (the right singular vectors, stored rowwise); If jobu.ne.'O' and jobvt.ne.'O' , the contents of A are destroyed. lda The leading dimension of the array a. lda >= max(1,n) . s UTL_NLA_ARRAY_FLT/DBL , DIMENSION (min(m,n)) . The singular values of A , sorted so that S(i) >= S(i+1) . u UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldu,ucol).(ldu,m) if jobu = 'A' or (ldu,min(m,n)) if jobu = 'S' . If jobu = 'A' , U contains the m by m orthogonal matrix U . If jobu = 'S' , U contains the first min(m,n) columns of U (the left singular vectors, stored columnwise). If jobu = 'N' or 'O' , U is not referenced. ldu The leading dimension of the array U. ldu >= 1. If jobu = 'S' or ' a' , ldu >= m . vt UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldvt, n) . If jobvt = 'A' , vt contains the n by n orthogonal matrix V**T . If jobvt = 'S' , vt contains the first min(m,n) rows of V**T (the right singular vectors, stored rowwise). If jobvt = 'N' or 'O' , vt is not referenced. ldvt The leading dimension of the array vt . ldvt >= 1 . If jobvt = 'A' , ldvt >= n . If jobvt = 'S' , ldvt >= min(m,n) . info = 0 : successful exit < 0 : If info = -i , the i -th argument had an illegal value > 0 : If SBDSQR did not converge, info specifies how many superdiagonals of an intermediate bidiagonal form B did not converge to zero. pack (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major