# BASIC SQL

show tables;

use world;


# C.R.U.D
select * from countrylanguage;

# table describe
describe city;


# SELECT 구문
select * from city;
select * from country;


# COLUMN 가져오기
select Population, Name 
	from city;
    
select Name, Continent 
	from country;


# table alias 
select c.Name, c.Population 
	from city as c; 

select c.Name, c.Population 
	from city c;
    
# table이 한개인 경우에는 table. 무의미
select Name, Population 
	from city c;

# column alias
select Name n, Population p
	from city;

# count 함수
select now();
select 2 + 5;

select count(*) cnt
	from city;


# WHERE 조건문

select Name, Population 
	from city
    where  (CountryCode = 'KOR'
		or CountryCode = 'JPN')
        and Population > 5000000;

# 여러 조건 명시 하기

# BETWEEN
select * from city
	where Population >= 5000000
    and Population <= 5500000;
    
select * from city
	where Population 
    between 5000000
    and 5500000;

# IN 
select *
	from city 
    where CountryCode in ('KOR', 'JPN', 'CHN');


select * 
	from city
    where CountryCode = 'KOR' 
		or CountryCode = 'JPN'
        or CountryCode = 'CHN';


# LIKE
select * 
	from city
    where Name like 'Se%';

select * 
	from city
    where Name like '%Se%';
    
select * 
	from city
    where Name like '%ce';
    
select * 
	from city
    where Name like 'Se___';
    
    
    
    
# ORDER BY
select * 
	from city
    where CountryCode = 'KOR'
    order by Population desc;
    
# LIMIT
select * 
	from city
    where CountryCode = 'KOR'
    order by Population desc
    limit 3;

select * 
	from city
    where CountryCode = 'KOR'
    order by Population desc
    limit 1, 3;


select * from city
	where CountryCode = 'KOR';

# case when 
select Name, Population, 
	case 
		when Population >= 5000000 then '인구많음'
		when Population >= 2000000 then '인구중간'
		else '인구 적음' end as Pop_category
	from city; 

# max, min, avg, count 함수
select max(Population) from city;
select min(Population) from city;

select avg(Population) from city;













# group by 
select CountryCode, max(Population)
	from city
    group by CountryCode;
    
select Continent, avg(Population) mp
	from country
    group by Continent
    order by mp desc;






# group by w/ agg function






# subquery
select avg(Population)
	from country;
    
select * 
	from country 
    where Population > 25434098.1172;


select * 
	from country 
    where Population > (select avg(Population)
							from country);
select * from country
	where LifeExpectancy < 
					(select avg(LifeExpectancy)
						from country);
                            
     
select * from 
	(select Name, Population, LifeExpectancy 
		from country) t;











# correlated subquery
select * from city;

select CountryCode, Name, Population
	from city c1
    where Population = 
		(select max(Population)
			from city c2
            where c1.CountryCode = c2.CountryCode);





# join
select * from country;
# primary key 
# foreign key

# cross join(교차 조인)
select *
	from city, country;

# inner join (내부조인)
select co.Name, ci.Name, ci.Population
	from city ci
    join country co
    on ci.CountryCode = co.Code;
    
select * from city
	where ID = 8000;

#insert into city 
#	values(8000, 'ZZang', 'ZZZ', 'ZZZZ', 2000);
    


select * 
	from city ci
    join country co
    on ci.CountryCode = co.Code
    where ci.ID = 8000;
    
    
# outer join 
# left 
select * 
	from country co
    join city ci
    on ci.CountryCode = co.Code
    join countrylanguage cl
    on co.Code = cl.CountryCode;
    
    
select * from countrylanguage;    
    
    

select * 
	from city ci
    right join country co
    on ci.CountryCode = co.Code
    where ci.ID = 8000;



# right 




# cross-join

# inner-join

# left-outer-join

# right-outer-join



select t.Continent, c2.Name, c2.Population 
	from country c2 
	join (select Continent, max(Population) mp
			from country c 
			group by Continent) t
	on c2.Continent = t.Continent 
		and c2.Population = t.mp
	order by Population desc;







# union

# table creation

# insert data

# update row(s)

# delete row(s)