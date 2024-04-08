SELECT subjects.name AS course, teachers.first_name, teachers.last_name
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE teachers.last_name = 'Цушко';