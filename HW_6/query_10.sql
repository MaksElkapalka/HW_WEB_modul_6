SELECT DISTINCT s.name AS course_name
FROM grades g
JOIN subjects s ON g.subject_id = s.id
JOIN students stu ON g.student_id = stu.id
WHERE s.teacher_id = 1
AND stu.id = 3