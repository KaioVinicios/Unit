select * from alunos;
select * from cursos;
select * from professores;


--1
select mat_alu as matricula, nom_alu as aluno, dat_nasc as data_nascimento 
from alunos
where cod_curso = 44
order by dat_nasc;

--2
select 
    cursos.cod_curso as codigo_curso, 
    alunos.mat_alu as matricula, 
    alunos.nom_alu as aluno
from alunos
left join cursos on 
    (cursos.nom_curso = 'Sistemas de Informacao - Noite' or cursos.nom_curso = 'Ciencia da Computacao%') and
    (cursos.cod_curso = alunos.cod_curso) and (alunos.mgp > 7)
order by cursos.nom_curso, alunos.nom_alu;

SELECT 
    cursos.cod_curso AS codigo_curso, 
    alunos.mat_alu AS matricula, 
    alunos.nom_alu AS aluno
FROM alunos
LEFT JOIN cursos ON cursos.cod_curso = alunos.cod_curso
WHERE 
    (cursos.nom_curso = 'Sistemas de Informacao - Noite' 
     OR cursos.nom_curso LIKE 'Ciencia da Computacao%')
    AND alunos.mgp > 7
ORDER BY 
    cursos.nom_curso, 
    alunos.nom_alu;


--3
select mat_alu as matricula, nom_alu as aluna 
from alunos 
where upper(nom_alu) = upper('ana%')
order by nom_alu;

--4
select 
	cursos.cod_curso as codigo_curso, 
	cursos.nom_curso as curso, 
	professores.nom_prof as professor 
from cursos 
left join professores on cursos.idt_prof = professores.idt_prof;

--5
select 
	nom_alu as aluno, 
	mat_alu as matricula, 
	mgp as media, 
	dat_nasc as data_de_nascimento
from alunos
where cod_curso = 26
order by mgp desc;

--6
select 
	cursos.cod_curso as codigo_curso,
	cursos.nom_curso as curso,
	professores.mat_prof as mat_professor,
	professores.nom_prof as professor
from cursos
left join professores on cursos.idt_prof = professores.idt_prof
order by cursos.cod_curso;

--8 
select 
    professores.idt_prof as codigo_professor, 
    professores.nom_prof as professor
from professores
inner join cursos on professores.idt_prof = cursos.idt_prof
inner join alunos on alunos.cod_curso = cursos.cod_curso
where cursos.cod_curso = 10;

--10
select 
	alunos.mat_alu as matricula,
	alunos.nom_alu as aluno
from alunos
left join disciplinas on disciplinas.cod_disc = 302 or disciplinas.cod_disc = 289;