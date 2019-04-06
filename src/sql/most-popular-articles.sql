select  
	art.title, 
	count(*) as article_count 
from 
	log l
inner join 
	articles art on substring(l.path,10) = art.slug
group by 
	path, art.title
order by 
	article_count desc
limit 3;
