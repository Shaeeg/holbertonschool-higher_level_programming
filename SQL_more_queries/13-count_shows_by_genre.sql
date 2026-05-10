-- Genres with show counts; genres with no shows omitted; one SELECT
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id, tv_genres.name
ORDER BY 2 DESC;
