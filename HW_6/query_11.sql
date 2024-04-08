SELECT AVG(g.mark) AS average_mark
FROM grades g
JOIN subjects s ON g.subject_id = s.id
JOIN teachers t ON s.teacher_id = t.id
WHERE g.student_id = 1
AND t.id = 1
