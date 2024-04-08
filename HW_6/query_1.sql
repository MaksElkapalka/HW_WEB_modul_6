SELECT s.first_name || ' ' || s.last_name AS student_name,
       (SELECT AVG(mark) FROM grades WHERE student_id = s.id) AS average_mark
FROM students AS s
ORDER BY average_mark DESC
LIMIT 5;
