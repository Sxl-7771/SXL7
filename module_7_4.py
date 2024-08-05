team1_num = 6
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

result_1 = "В команде Мастера кода участников: %d !" % team1_num
result_2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)

result_3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
result_4 = "Волшебники данных решили задачи за {:.1f} с !".format(team2_time)

result_5 = f"Команды решили {score_1} и {score_2} задач."
result_6 = f"Результат битвы: {challenge_result}"
result_7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!"

print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)
print(result_6)
print(result_7)
