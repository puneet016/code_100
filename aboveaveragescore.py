student_scores = [80, 60, 50, 65, 75, 55]

def sum_score_above_average(p_student_scores):
    sum_score=0
    number_of_student=0
    for score in p_student_scores:
        sum_score+=score
        number_of_student+=1
    average_score=sum_score/number_of_student
    sum_above_average=0
    for score in p_student_scores:
        if score>average_score:
           sum_above_average+=score
    return sum_above_average
print(sum_score_above_average(student_scores))
            
            
        