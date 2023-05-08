# Write a program that determines the maximum grade
# for each student and the date and time it was received

import json
import csv

with open('exam_results.csv', 'r', encoding='utf-8') as file:
    rows, all_scores, result = csv.DictReader(file), {}, []
    for row in rows:
        all_scores.setdefault((row['email'], row['name'], row['surname']), []).append(
            [int(row['score']), row['date_and_time']])
    for k, v in sorted(all_scores.items()):
        result.append(
            {'name': k[1], 'surname': k[2], 'best_score': max(v)[0], 'date_and_time': max(v)[1], 'email': k[0]})

with open('best_scores.json', 'w', encoding='utf-8') as out:
    json.dump(result, out, indent=3)

