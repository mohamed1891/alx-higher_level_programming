-- Selecting the state and finding the maximum temperature
SELECT
    state,                        -- State column
    MAX(value) AS max_temp        -- Maximum temperature column (aliased as max_temp)
FROM
    temperatures                  -- From the temperatures table
GROUP BY
    state                         -- Grouping the results by state
ORDER BY
    state;                        -- Ordering the results by state

