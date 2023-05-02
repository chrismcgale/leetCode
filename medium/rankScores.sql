SELECT 
    sc1.score, 
    COUNT(DISTINCT sc2.score) AS 'rank'
FROM 
    Scores as sc1
    INNER JOIN Scores sc2 ON sc1.score <= sc2.score
GROUP BY
    sc1.id,
    sc1.score
ORDER BY 
    sc1.score DESC


# Faster but requires sql 8.0
SELECT
    S.score,
    DENSE_RANK() OVER (
        ORDER BY S.score DESC
    ) AS 'rank'
FROM
    Scores S;