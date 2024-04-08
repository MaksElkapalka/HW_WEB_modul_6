SELECT s.group_id, ROUND(AVG(g.mark), 2) AS average_mark
FROM grades g
JOIN students s ON g.student_id = s.id
WHERE g.subject_id = 1 -- запит id предмета
GROUP BY s.group_id;
