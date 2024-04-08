SELECT teachers.first_name, teachers.last_name, AVG(grades.mark) AS average_mark
FROM teachers
JOIN subjects ON teachers.id = subjects.teacher_id
JOIN grades ON subjects.id = grades.subject_id
GROUP BY teachers.id, teachers.first_name, teachers.last_name;
