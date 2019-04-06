select
	aut.name, 
	count(*) as article_count 
from 
	log l
inner join 
	articles art on substring(l.path,10) = art.slug
inner join 
	authors aut on art.author = aut.id
group by 
	aut.name
order by 
	article_count desc;
