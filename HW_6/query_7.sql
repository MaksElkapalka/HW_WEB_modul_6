SELECT students.first_name, students.last_name, grades.mark
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN groups ON students.group_id = groups.id
WHERE groups.name = 'Group B' AND subjects.name = 'алхімія';