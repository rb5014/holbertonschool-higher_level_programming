-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tvs.`title`, tvg.`name` FROM `tv_shows` AS tvs
LEFT JOIN `tv_show_genres` AS tvsg ON tvs.`id` = tvsg.`show_id`
LEFT JOIN `tv_genres`AS tvg ON tvsg.`genre_id` = tvg.`id`
ORDER BY tvs.`title`, tvg.`name` ASC;