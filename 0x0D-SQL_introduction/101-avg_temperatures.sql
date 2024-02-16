-- Selecting the city and calculating the average temperature
SELECT
    `city`,                           -- City column
    AVG(`value`) AS `avg_temp`        -- Average temperature column (aliased as avg_temp)
FROM
    `temperatures`                    -- From the temperatures table
GROUP BY
    `city`                            -- Grouping the results by city
ORDER BY
    `avg_temp` DESC;                  -- Ordering the results by average temperature in descending order
