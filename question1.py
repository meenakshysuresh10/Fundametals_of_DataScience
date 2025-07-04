import numpy as np

# Sample 4x4 matrix: 4 students, 4 subjects (Math, Science, English, History)
student_scores = np.array([
    [85, 78, 92, 88],
    [76, 80, 85, 90],
    [90, 88, 91, 84],
    [70, 75, 80, 82]
])

# Calculate average score for each subject (column-wise mean)
avg_scores = np.mean(student_scores, axis=0)

# Find subject with highest average score
subjects = ['Math', 'Science', 'English', 'History']
highest_avg_index = np.argmax(avg_scores)
highest_avg_subject = subjects[highest_avg_index]

# Output
print("Average scores per subject:", dict(zip(subjects, avg_scores)))
print("Subject with highest average score:", highest_avg_subject)
