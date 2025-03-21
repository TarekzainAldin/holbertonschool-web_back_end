-- 3-old_school.sql

SELECT band_name, 
       (IFNULL(split, YEAR(CURDATE())) - formed) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
