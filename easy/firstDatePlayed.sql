SELECT act.player_id, device_id
FROM Activity as act
INNER JOIN
  (
    SELECT player_id, MIN(event_date) min_date
    FROM Activity
    GROUP BY player_id
  ) tbl1
ON act.player_id = tbl1.player_id
WHERE act.event_date = tbl1.min_date