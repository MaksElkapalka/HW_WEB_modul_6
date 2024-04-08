SELECT s.first_name, s.last_name, g.mark
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN subjects subj ON g.subject_id = subj.id
JOIN teachers t ON subj.teacher_id = t.id
JOIN groups gr ON s.group_id = gr.id
WHERE subj.id = 2
AND gr.id = 3
AND g.date = (
    SELECT MAX(date)
    FROM grades
    WHERE subject_id = 2
)
