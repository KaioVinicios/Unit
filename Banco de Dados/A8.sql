--1 
SELECT 
    A.NOM_ALU AS Nome,
    A.MAT_ALU AS Matricula,
    H.MEDIA AS MGP,
    A.DAT_NASC AS Data_Nascimento
FROM 
    ALUNOS A
JOIN 
    MATRICULAS M ON A.MAT_ALU = M.MAT_ALU
JOIN 
    HISTORICOS H ON M.ANO = H.ANO AND M.SEMESTRE = H.SEMESTRE AND M.COD_DISC = H.COD_DISC
WHERE 
    A.COD_CURSO = 26 
    AND M.ANO = 2013 
    AND M.SEMESTRE = 1
ORDER BY 
    H.MEDIA DESC;

--2
SELECT 
    M.MAT_ALU AS Matricula,
    A.NOM_ALU AS Nome,
    M.MEDIA AS Media,
    M.FALTAS_Q1 + M.FALTAS_Q2 + M.FALTAS_Q3 AS Total_Faltas
FROM 
    MATRICULAS M
JOIN 
    ALUNOS A ON M.MAT_ALU = A.MAT_ALU
WHERE 
    M.COD_DISC = 3817 
    AND M.ANO = 2008 
    AND M.SEMESTRE = 1;

--3
SELECT 
    D.COD_DISC AS Codigo,
    D.NOM_DISC AS Nome,
    M.PERIODO AS Periodo
FROM 
    DISCIPLINAS D
JOIN 
    MATRIZES M ON D.COD_DISC = M.COD_DISC
WHERE 
    M.COD_CURSO = 52;

--4
SELECT 
    AVG(MONTHS_BETWEEN(TO_DATE('2011-07-01', 'YYYY-MM-DD'), A.DAT_NASC) / 12) AS Media_Idade
FROM 
    MATRICULAS M
JOIN 
    ALUNOS A ON M.MAT_ALU = A.MAT_ALU
WHERE 
    M.COD_DISC = 5472 
    AND M.ANO = 2011 
    AND M.SEMESTRE = 3;

--5
SELECT 
    A.MAT_ALU AS Matricula,
    A.NOM_ALU AS Nome_Aluno,
    C.NOM_CURSO AS Nome_Curso,
    P.NOM_PROF AS Coordenador
FROM 
    ALUNOS A
JOIN 
    CURSOS C ON A.COD_CURSO = C.COD_CURSO
JOIN 
    PROFESSORES P ON C.IDT_PROF = P.IDT_PROF
WHERE 
    A.TOT_CRED = C.TOT_CRED
ORDER BY 
    C.NOM_CURSO, A.NOM_ALU;

--6
SELECT 
    C.NOM_CURSO AS Nome_Curso,
    D.NOM_DISC AS Nome_Disciplina,
    AVG(H.MEDIA) AS Media_Geral
FROM 
    HISTORICOS H
JOIN 
    DISCIPLINAS D ON H.COD_DISC = D.COD_DISC
JOIN 
    CURSOS C ON D.COD_CURSO = C.COD_CURSO
WHERE 
    C.COD_CURSO = 13 
    AND H.ANO = 2007 
    AND H.SEMESTRE = 3
GROUP BY 
    C.NOM_CURSO, D.NOM_DISC;