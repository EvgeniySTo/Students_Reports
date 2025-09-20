import csv
import argparse
import statistics
from tabulate import tabulate


def get_headers(filepath: str) -> list:
    with open(filepath, 'r', newline='', encoding='utf-8') as f_path:
        return next(csv.reader(f_path))


def get_data(filepath: str) -> list:
    with open(filepath, 'r', newline='', encoding='utf-8') as f_path:
        reader = csv.reader(f_path)
        next(reader, None)
        return list(reader)


# Reports
def students_performance(report_headers: list, all_students: list) -> list:
    result = {}
    for student in all_students:
        if student[0] not in result:
            result[student[0]] = [int(student[4])]
        else:
            result[student[0]].append(int(student[4]))
    data_for_report = []
    for key, value in result.items():
        data_for_report.append([key, statistics.mean(value)])
    data_for_report.sort(key=lambda x: x[1], reverse=True)
    print(tabulate(data_for_report, headers=[report_headers[0], report_headers[4]]))
    return data_for_report


REPORTS = {
    'students-performance': students_performance,
}


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='parameters for script start')
    parser.add_argument('--files', nargs='+', type=str, help='enter file path')
    parser.add_argument('--report', choices=REPORTS.keys())
    arguments = parser.parse_args()

    try:
        headers = get_headers(arguments.files[0])
        data = []
        for file in arguments.files:
            data += get_data(file)
        function = REPORTS[arguments.report]
        function(headers, data)
    except FileNotFoundError as e:
        print(f'Файл {e.filename} не найден! Отчет не сформирован.')
