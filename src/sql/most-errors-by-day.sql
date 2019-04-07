select 
	to_char(errors.date, 'Mon DD, YYYY'), 
	errors.total_errors, 
	totals.total_requests, 
	round((cast(errors.total_errors as decimal)/totals.total_requests) * 100, 5) as error_rate
from 
(
	select 
		date_trunc('day', time) as date, 
		count(*) as total_errors
	from 
		log
	where 
		status <> '200 OK'
	group by date
) as errors
inner join 
(
	select 
		date_trunc('day', time) as date, 
		count(*) as total_requests
	from 
		log
	group by date
	
) as totals on errors.date = totals.date
where 
	round((cast(errors.total_errors as decimal)/totals.total_requests) * 100, 5) > 1
order by 
	errors.date;