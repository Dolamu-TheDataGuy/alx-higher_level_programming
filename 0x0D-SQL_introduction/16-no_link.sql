-- List all records of the table grouped by scores and names
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
