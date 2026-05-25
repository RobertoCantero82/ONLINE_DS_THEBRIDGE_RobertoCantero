--1 Obtén los clientes de brasil
select customer_id, first_name, last_name, country from customer where country = 'Brazil'

--2 Obtén los empleados que son agentes de ventas
select employee_id, first_name, last_name from employee where title = 'Sales Support Agent'

--3 Obtén las canciones de 'AC/DC' 
select * from track as t
join album as a on t.album_id = a.album_id
join artist as ar on a.artist_id = ar.artist_id
where ar.name = 'AC/DC'

--4 Obtén los campos de los clientes que no sean de USA: Nombre completo, ID, País
select customer_id, first_name ||' '|| last_name as nombre_completo, country from customer where country != 'USA'

--5 Obtén los empleados que son agentes de ventas: Nombre completo, Dirección (Ciudad, Estado, País) y email 
select first_name || ' ' || last_name as nombre_completo, concat(city, ' ', state, ' ', country) as direccion, email 
from employee where title = 'Sales Support Agent'

--6 Obtén una lista con los países no repetidos a los que se han emitido facturas
select distinct billing_country from invoice	

--7 Obtén una lista con los estados de USA no repetidos de donde son los clientes y cuántos clientes en cada uno
select state, count(*) from customer where country = 'USA'
group by state

--8 Cuántos artículos tiene la factura 37 (función de agregación)
select sum(quantity) from invoice_line where invoice_id = 37        

--9 Cuántas canciones tiene 'AC/DC' 
select count(*) from track as t
join album as a on t.album_id = a.album_id
join artist as ar on a.artist_id = ar.artist_id
where ar.name = 'AC/DC'

--10 Cuántos artículos tiene cada factura
select invoice_id, count(*) from invoice_line
group by invoice_id

--11 Cuántas facturas hay de cada país
select billing_country, count(*) as n from invoice
group by billing_country
order by n

--12 Cuántas facturas ha habido en 2009 y 2011
select extract(year from invoice_date) as anio, count(*) as num_facturas
from invoice
where extract(year from invoice_date) in (2009, 2011)
group by anio

--13 Cuántas facturas ha habido entre 2009 y 2011
select count(*)
from invoice
where invoice_date between '2009-01-01' and '2011-12-31'

--14 Cuántos clientes hay de España y de Brasil
select country, count(*)
from customer
where country in ('Spain', 'Brazil')
group by country

--15 Obtén las canciones que su título empieza por 'You'
select * from track where name like 'You%'

-- SEGUNDA PARTE

--1 Facturas de Clientes de Brasil, Nombre del cliente, Id de factura, fecha de la factura y el país de la factura
select first_name, last_name, i.invoice_id, i.billing_country, i.invoice_date
from customer as c 
join invoice as i on c.customer_id = i.customer_id
where c.country = 'Brazil'

--2 Obtén cada factura asociada a cada agente de ventas con su nombre completo
select i.invoice_id, e.first_name || ' ' || e.last_name as agente_ventas
from invoice as i
join customer as c on i.customer_id = c.customer_id
join employee as e on c.support_rep_id = e.employee_id

--3 Obtén el nombre del cliente, el país, el nombre del agente y el total
select c.first_name || ' ' || c.last_name as nombre_cliente,
       c.country,
       e.first_name || ' ' || e.last_name as nombre_agente,
       i.total
from invoice as i
join customer as c on i.customer_id = c.customer_id
join employee as e on c.support_rep_id = e.employee_id

--4 Obtén cada artículo de la factura con el nombre de la canción
select il.invoice_id, il.invoice_line_id, t.name as cancion,
       il.unit_price, il.quantity
from invoice_line as il
join track as t on il.track_id = t.track_id

--5 Muestra todas las canciones con su nombre, formato, álbum y género
select t.name as cancion,
       mt.name as formato,
       al.title as album,
       g.name as genero
from track as t
join media_type as mt on t.media_type_id = mt.media_type_id
join album as al on t.album_id = al.album_id
join genre as g on t.genre_id = g.genre_id

--6 Cuántas canciones hay en cada playlist
select p.name as playlist, count(pt.track_id) as num_canciones
from playlist as p
join playlist_track as pt on p.playlist_id = pt.playlist_id
group by p.name
order by num_canciones desc

--7 Cuánto ha vendido cada empleado
select e.first_name || ' ' || e.last_name as empleado,
       round(sum(i.total)::numeric, 2) as total_ventas
from employee as e
join customer as c on e.employee_id = c.support_rep_id
join invoice as i on c.customer_id = i.customer_id
group by empleado
order by total_ventas desc

--8 ¿Quién ha sido el agente de ventas que más ha vendido en 2009? 
select e.first_name || ' ' || e.last_name as agente,
       round(sum(i.total)::numeric, 2) as total_ventas
from employee as e
join customer as c on e.employee_id = c.support_rep_id
join invoice as i on c.customer_id = i.customer_id
where extract(year from i.invoice_date) = 2009
group by agente
order by total_ventas desc
limit 1

--9 ¿Cuáles son los 3 grupos que más han vendido?   
select ar.name as artista,
       round(sum(il.unit_price * il.quantity)::numeric, 2) as total_ventas
from artist as ar
join album as al on ar.artist_id = al.artist_id
join track as t on al.album_id = t.album_id
join invoice_line as il on t.track_id = il.track_id
group by artista
order by total_ventas desc
limit 3