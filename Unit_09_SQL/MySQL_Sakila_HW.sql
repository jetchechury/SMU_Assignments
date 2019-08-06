USE sakila;

-- Display the first and last names of all actors from the table actor.
SELECT first_name,
last_name
FROM actor;

-- Display the first and last name of each actor in a single column 
-- in upper case letters. Name the column Actor Name.
SELECT UPPER (CONCAT(first_name,' ', last_name)) AS 'Actor Name'
FROM actor;

-- You need to find the ID number, first name, and last name of an 
-- actor, of whom you know only the first name, "Joe." What is one 
-- query would you use to obtain this information?
SELECT actor_id,
first_name,
last_name
FROM actor
WHERE first_name = 'Joe';

-- Find all actors whose last name contain the letters GEN:
SELECT first_name,
last_name,
actor_id
FROM actor
WHERE last_name LIKE '%gen%';

-- Find all actors whose last names contain the letters LI. This time,
-- order the rows by last name and first name, in that order:
SELECT first_name,
last_name,
actor_id
FROM actor
WHERE last_name LIKE '%li%'
ORDER BY last_name ASC, first_name ASC;

-- Using IN, display the country_id and country columns of the 
-- following countries: Afghanistan, Bangladesh, and China:
SELECT country_id,
country
FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

-- You want to keep a description of each actor. You don't think
-- you will be performing queries on a description, so create a 
-- column in the table actor named description and use the data 
-- type BLOB (Make sure to research the type BLOB, as the difference 
-- between it and VARCHAR are significant).
ALTER TABLE actor
ADD COLUMN description blob AFTER last_name;

SELECT *
FROM actor;

-- Very quickly you realize that entering descriptions for each 
-- actor is too much effort. Delete the description column.
ALTER TABLE actor
DROP COLUMN description;

SELECT *
FROM actor;

-- List the last names of actors, as well as how many actors 
-- have that last name.
SELECT last_name,
COUNT(*) AS 'Number of Actors'
FROM actor
GROUP BY last_name;

-- List last names of actors and the number of actors who have that
-- last name, but only for names that are shared by at 
-- least two actors
SELECT last_name,
COUNT(*) AS 'Number of Actors'
FROM actor
GROUP BY last_name
HAVING COUNT(*) >=2;

-- The actor HARPO WILLIAMS was accidentally entered in the actor 
-- table as GROUCHO WILLIAMS. Write a query to fix the record.

-- Check to see how many actors with first name GROUCHO before making
-- change.
SELECT actor_id,
last_name,
first_name
FROM actor
WHERE first_name='Groucho';

-- Multiple actors with first name GROUCHO, therefore first and last
-- name needs to be used when refering to actor.

UPDATE actor
SET first_name='HARPO'
WHERE first_name='GROUCHO' 
AND last_name='WILLIAMS';

-- Perhaps we were too hasty in changing GROUCHO to HARPO. 
-- It turns out that GROUCHO was the correct name after all! 
-- In a single query, if the first name of the actor is currently
-- HARPO, change it to GROUCHO.
UPDATE actor
SET first_name=
CASE
	WHEN first_name ='HARPO'
    THEN 'GROUCHO'
    ELSE 'MUCHO GROUCHO'
END
WHERE actor_id=172;

SELECT actor_id,
last_name,
first_name
FROM actor
WHERE first_name='Groucho';

-- You cannot locate the schema of the address table. Which query 
-- would you use to re-create it?
SHOW CREATE TABLE address;

-- Use JOIN to display the first and last names, as well as the 
-- address, of each staff member. Use the tables staff and address:
SELECT *
FROM address;

SELECT *
FROM staff;

SELECT s.first_name,
s.last_name,
a.address_id,
a.address,
a.address2,
a.district,
a.city_id,
a.postal_code,
a.location
FROM address AS a
INNER JOIN staff AS s
ON a.address_id=s.address_id;

-- Use JOIN to display the total amount rung up by each staff 
-- member in August of 2005. Use tables staff and payment.
SELECT *
FROM staff;

SELECT SUM(amount)
FROM payment
WHERE staff_id=1;


SELECT s.staff_id AS 'Staff ID',
s.first_name AS 'First Name',
s.last_name AS 'Last Name',
SUM(p.amount) AS 'Total Rung'
FROM staff AS s
INNER JOIN payment AS p
ON s.staff_id=p.staff_id
WHERE month(p.payment_date)=8 AND year(p.payment_date)=2005
GROUP BY s.staff_id;

-- List each film and the number of actors who are listed for 
-- that film. Use tables film_actor and film. Use inner join.
SELECT *
FROM film_actor;

SELECT *
FROM film;

SELECT f.title AS 'Film Title',
COUNT(fa.actor_id) AS 'Number of Actors'
FROM film_actor as fa
INNER JOIN film AS f
ON f.film_id=fa.film_id
GROUP BY f.title;

-- How many copies of the film Hunchback Impossible exist in
-- the inventory system?
SELECT title,
COUNT(*) AS 'Number of Copies'
FROM film
WHERE title='Hunchback Impossible';

-- Using the tables payment and customer and the JOIN command, 
-- list the total paid by each customer. List the customers 
-- alphabetically by last name:
SELECT *
FROM payment;

SELECT *
FROM customer;

SELECT c.first_name,
c.last_name,
SUM(p.amount) AS 'Total Amount Paid'
FROM customer as c
INNER JOIN payment AS p
ON c.customer_id=p.customer_id
GROUP BY c.customer_id
ORDER BY last_name ASC, first_name ASC;

-- The music of Queen and Kris Kristofferson have seen an unlikely 
-- resurgence. As an unintended consequence, films starting with the 
-- letters K and Q have also soared in popularity. Use subqueries to 
-- display the titles of movies starting with the letters K and Q whose 
-- language is English.

-- Find laugage_id for English
SELECT *
FROM language
WHERE name='English';

-- Find films starting with K and Q whose langauge is English
SELECT title
FROM film 
WHERE title
LIKE 'K%' OR title LIKE 'Q%'
    AND title IN
		(SELECT title
		FROM film
		WHERE language_id=1)
;

-- Use subqueries to display all actors who appear in the film Alone Trip.
SELECT first_name,
last_name
FROM actor
WHERE actor_id IN
	(SELECT actor_id
    FROM film_actor
    WHERE film_id IN
		(SELECT film_id
        FROM film
        WHERE title='Alone Trip'))
	;
    
-- You want to run an email marketing campaign in Canada, for which 
-- you will need the names and email addresses of all Canadian customers. 
-- Use joins to retrieve this information.
-- customer 

SELECT cu.first_name,
cu.last_name,
cu.email,
co.country
FROM customer AS cu
	INNER JOIN address AS a
		ON cu.address_id=a.address_id
    INNER JOIN city as ci
		ON a.city_id=ci.city_id
    INNER JOIN country as co
		ON ci.country_id=co.country_id
    WHERE co.country='Canada';

-- Sales have been lagging among young families, and you wish to target
-- all family movies for a promotion. Identify all movies categorized as 
-- family films.

SELECT *
FROM category;

SELECT title
FROM film
WHERE film_id IN
	(SELECT film_id
    FROM film_category
    WHERE category_id IN
		(SELECT category_id
        FROM category
        WHERE name='Family'))
;
    
-- Display the most frequently rented movies in descending order.

SELECT f.title,
COUNT(r.rental_id) AS 'Number of Times Rented'
FROM rental as r
INNER JOIN inventory AS i
ON r.inventory_id=i.inventory_id
INNER JOIN film as f
ON i.film_id=f.film_id
GROUP BY f.title
ORDER BY COUNT(r.rental_id) DESC;

-- Write a query to display how much business, in dollars, each store
-- brought in.

SELECT s.store_id,
SUM(p.amount) AS 'Total Revenue'
FROM store as s
INNER JOIN staff AS st
ON s.store_id=st.store_id
INNER JOIN rental AS r
ON st.staff_id=r.staff_id
INNER JOIN payment AS p
ON r.rental_id=p.rental_id
GROUP BY s.store_id;

-- Write a query to display for each store its store ID, city, and country.

SELECT s.store_id,
c.city,
co.country
FROM store AS s
INNER JOIN address as a
ON s.address_id=a.address_id
INNER JOIN city as c
ON a.city_id=c.city_id
INNER JOIN country as co
ON c.country_id=co.country_id;

-- List the top five genres in gross revenue in descending order. 
-- (Hint: you may need to use the following tables: category, film_category, 
-- inventory, payment, and rental.)

SELECT c.name AS 'Genre',
SUM(p.amount) AS 'Gross Revenue'
FROM category AS c
INNER JOIN film_category AS fc
ON c.category_id=fc.category_id
INNER JOIN inventory AS i
ON fc.film_id=i.film_id
INNER JOIN rental AS r
ON i.inventory_id=r.inventory_id
INNER JOIN payment AS p
ON r.rental_id=p.rental_id
GROUP BY c.category_id
ORDER BY SUM(p.amount) DESC LIMIT 5;

-- In your new role as an executive, you would like to have an easy way
-- of viewing the Top five genres by gross revenue. Use the solution from
-- the problem above to create a view. If you haven't solved 7h, you can 
-- substitute another query to create a view.

CREATE VIEW vw_gross_revenue_by_genre AS
SELECT c.name AS 'Genre',
SUM(p.amount) AS 'Gross Revenue'
FROM category AS c
INNER JOIN film_category AS fc
ON c.category_id=fc.category_id
INNER JOIN inventory AS i
ON fc.film_id=i.film_id
INNER JOIN rental AS r
ON i.inventory_id=r.inventory_id
INNER JOIN payment AS p
ON r.rental_id=p.rental_id
GROUP BY c.category_id
ORDER BY SUM(p.amount) DESC LIMIT 5;

-- How would you display the view that you created in 8a?

SELECT *
FROM vw_gross_revenue_by_genre;

-- You find that you no longer need the view top_five_genres. 
-- Write a query to delete it.

DROP VIEW vw_gross_revenue_by_genre;