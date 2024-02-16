-- Selecting the city and calculating the average temperature
SELECT
    `city`,                             -- City column
    AVG(`value`) AS `avg_temp`          -- Average temperature column (aliased as avg_temp)
FROM
    `temperatures`                      -- From the temperatures table
WHERE
    `month` = 7 OR `month` = 8         -- Filtering data for July (month = 7) or August (month = 8)
GROUP BY
    `city`                             -- Grouping the results by city
ORDER BY
    `avg_temp`                         -- Ordering the results by average temperature
LIMIT
    3;                                  -- Limiting the number of results to 3
