select
	c.name as country,
	(
	select
		count(d.id)
	from
		developer d
	where
		'C++' = any(d.worked_with)
		and c.id = d.country_id
	) as cpp_devs,
	(
	select
		count(d.id)
	from
		developer d
	where
		'Python' = any(d.worked_with)
			and c.id = d.country_id
	) as python_developers,
	(
	select
		count(d.id)
	from
		developer d
	where
		('HTML/CSS' = any(d.worked_with)
			or 'CSS' = any(d.worked_with))
			and c.id = d.country_id
	) as html_css_developers
from
	country c
inner join developer d 
	on
	c.id = d.country_id
group by
	c.id