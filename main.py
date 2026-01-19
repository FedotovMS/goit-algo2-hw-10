from dataclasses import dataclass, field
from typing import Set, List, Optional


# Визначення класу Teacher
@dataclass
class Teacher:
    first_name: str
    last_name: str
    age: int
    email: str
    can_teach_subjects: Set[str]
    assigned_subjects: Set[str] = field(default_factory=set)


def create_schedule(subjects: Set[str], teachers: List[Teacher]) -> Optional[List[Teacher]]:
    uncovered = set(subjects)
    schedule: List[Teacher] = []

    # (На випадок повторного запуску з тими ж об'єктами)
    for t in teachers:
        t.assigned_subjects.clear()

    while uncovered:
        best_teacher = None
        best_cover: Set[str] = set()

        for t in teachers:
            cover = t.can_teach_subjects & uncovered
            if not cover:
                continue

            if (best_teacher is None or
                len(cover) > len(best_cover) or
                (len(cover) == len(best_cover) and t.age < best_teacher.age)):
                best_teacher = t
                best_cover = cover

        if best_teacher is None:
            # Ніхто не може покрити жоден із непокритих предметів
            return None

        best_teacher.assigned_subjects = set(best_cover)
        schedule.append(best_teacher)
        uncovered -= best_cover

        


    return schedule
    




if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    # Створення списку викладачів
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {"Математика", "Фізика"}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {"Інформатика", "Математика"}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {"Фізика", "Інформатика"}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    # Створення розкладу
    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(sorted(teacher.assigned_subjects))}\n")

        # 🔽 🔽 🔽 САМЕ ТУТ вставляємо код 🔽 🔽 🔽

        subject_to_teacher = {}

        for teacher in schedule:
            for subject in teacher.assigned_subjects:
                subject_to_teacher[subject] = f"{teacher.first_name} {teacher.last_name}"

        print("Призначення предметів:")
        for subject in sorted(subjects):
            print(f" - {subject}: {subject_to_teacher.get(subject, 'не призначено')}")

    else:
        print("Неможливо покрити всі предмети наявними викладачами.")