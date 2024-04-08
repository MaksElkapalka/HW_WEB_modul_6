SELECT s.first_name || ' ' || s.last_name AS student_name,
       AVG(g.mark) AS average_mark
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
JOIN subjects AS sub ON g.subject_id = sub.id
WHERE g.subject_id = 1
GROUP BY s.id
ORDER BY average_mark DESC
LIMIT 1;