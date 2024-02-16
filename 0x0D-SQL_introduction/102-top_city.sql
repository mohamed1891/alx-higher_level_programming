-- Selecting the city and calculating the average temperature for months 7 and 8
SELECT
    city,                             -- City column
    AVG(value) AS avg_temp            -- Average temperature column (aliased as avg_temp)
FROM
    temperatures                      -- From the temperatures table
WHERE
    month = 7 OR month = 8             -- Filtering data for months 7 or 8
GROUP BY
    city                              -- Grouping the results by city
ORDER BY
    avg_temp DESC                     -- Ordering the results by average temperature in descending order
LIMIT 3;                             -- Limiting the output to the top 3 results
