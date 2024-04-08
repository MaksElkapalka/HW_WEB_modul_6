SELECT students.first_name, students.last_name
FROM students
JOIN groups ON students.group_id = groups.id
WHERE groups.name = 'Group A';