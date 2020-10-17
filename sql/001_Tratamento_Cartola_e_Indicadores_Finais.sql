
--CRIANDO A TABELA FORCA TIMES CARTOLA
DROP TABLE IF EXISTS forca_times_cartola;
SELECT * INTO forca_times_cartola FROM (

SELECT LOWER(clubeid) AS clube,	
	ano,
	rodada,
	SUM(pontos) AS pontos,
	SUM(preco) 	AS preco
FROM imp_cartola
GROUP BY 1,2,3
UNION ALL
SELECT LOWER(clubeid) AS clube,	
	2018::integer 	AS ano,
	rodada, 
	SUM(pontos) AS pontos,
	SUM(preco) AS preco
FROM imp_cartola_2 
GROUP BY 1,3
UNION ALL
SELECT LOWER(clubeid) AS clube,	
	2019::integer 	AS ano,
	rodada, 
	SUM(pontos) AS pontos,
	SUM(preco) 	AS preco
FROM imp_cartola_3 
GROUP BY 1,3
ORDER BY 1,2,3
) AS A;


------------AJUSTES PARA BUSCAR DA RODADA ANTERIOR
SELECT * fROM forca_times_cartola

UPDATE forca_times_cartola
SET clube = REPLACE(clube,'botafogo','botafogo-rj')
WHERE clube = 'botafogo';


insert into forca_times_cartola
select clube, ano, 13, pontos, preco 
from forca_times_cartola 
where 	rodada = 12 and 
	ano = 2016 AND 
	clube ilike '%américa-mg%';

insert into forca_times_cartola
select clube, ano, 17, pontos, preco 
from forca_times_cartola 
where 	rodada = 16 and 
	ano = 2016 AND 
	clube ilike '%américa-mg%';


insert into forca_times_cartola
select clube, ano, 21, pontos, preco 
from forca_times_cartola 
where 	rodada = 20 and 
	ano = 2016 AND 
	clube ilike '%américa-mg%';

insert into forca_times_cartola
select clube, ano, 31, pontos, preco 
from forca_times_cartola 
where 	rodada = 30 and 
	ano = 2016 AND 
	clube ilike '%américa-mg%';

insert into forca_times_cartola
select clube, ano, 38, pontos, preco 
from forca_times_cartola 
where 	rodada = 37 and 
	ano = 2016 AND 
	clube ilike '%américa-mg%';


---------------------------------------------------------------------
with probabilidades as (
	SELECT time, ano, rodada, data_confronto, preco, pontos FROM dados_2019
	union all
	SELECT time, ano, rodada, data_confronto, preco, pontos FROM dados_2018
	union all
	SELECT time, ano, rodada, data_confronto, preco, pontos FROM dados_2017
	union all
	SELECT time, ano, rodada, data_confronto, preco, pontos FROM dados_2016
	union all
	SELECT time, ano, rodada, data_confronto, preco, pontos FROM dados_2015
	union all
	SELECT time, ano, rodada, data_confronto, preco, pontos FROM dados_2014
)
select a.*, 
	b.preco as preco_mandante, 
	b.pontos as ponto_mandante,
	c.preco AS preco_visitante,
	c.pontos as ponto_visitante
into final_indicadores_jogos	
from imp_indicadores a
left join probabilidades b
		on a.data_confronto = b.data_confronto and
			a.rodada = b.rodada and
			a.time_casa = b.time
left join probabilidades c
		on a.data_confronto = c.data_confronto and
			a.rodada = c.rodada and
			a.time_visitante = c.time			

select * from final_indicadores_jogos
----------------------------------------------------------------------------


select  --to_char(data_confronto,'YYYY')::integer as ano,
	sum(gol_1)
from final_indicadores_jogos
where tipo_vencedor = 'M'
group by 1 
order by 1