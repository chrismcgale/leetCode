# Could replace each SUM with CASE cond THEN 1 ELSE 0 END but was slower
# Another option is to use "with cte as (select Wimbledon as won FROM Championships UNION ALL...)" and then inner join

SELECT *
FROM (
    SELECT player_id, player_name, SUM(player_id = Wimbledon) + SUM(player_id = Fr_Open) + SUM(player_id = US_Open) + SUM(player_id = Au_Open) AS grand_slams_count 
    FROM Players
    INNER JOIN Championships GROUP BY player_id, player_name) T
WHERE grand_slams_count > 0