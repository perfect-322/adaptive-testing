import streamlit as st
import pandas as pd
import os
import random

file = "results.csv"

st.title("Адаптивное тестирование по информатике")

# ---------------- ВОПРОСЫ ----------------

questions = [
    # EASY
    {
        "question": "Что такое алгоритм?",
        "options": [
            "Набор случайных действий",
            "Последовательность команд для решения задачи",
            "Тип данных"
        ],
        "answer": "Последовательность команд для решения задачи",
        "difficulty": "easy",
        "hint": "Алгоритм — это последовательность шагов для решения задачи."
    },
    {
        "question": "Какая структура данных работает по принципу FIFO?",
        "options": ["Стек", "Очередь", "Массив"],
        "answer": "Очередь",
        "difficulty": "easy",
        "hint": "FIFO = First In First Out."
    },
    {
        "question": "Какая структура данных работает по принципу LIFO?",
        "options": ["Стек", "Очередь", "Список"],
        "answer": "Стек",
        "difficulty": "easy",
        "hint": "LIFO = Last In First Out."
    },
    {
        "question": "Что такое массив?",
        "options": [
            "Набор элементов одного типа",
            "Графическая фигура",
            "Операционная система"
        ],
        "answer": "Набор элементов одного типа",
        "difficulty": "easy",
        "hint": "Массив хранит одинаковые элементы."
    },
    {
        "question": "Какой поиск проверяет элементы по порядку?",
        "options": ["Бинарный поиск", "Линейный поиск", "Хеширование"],
        "answer": "Линейный поиск",
        "difficulty": "easy",
        "hint": "По одному элементу."
    },

    # MEDIUM
    {
        "question": "Какова сложность линейного поиска?",
        "options": ["O(log n)", "O(n)", "O(1)"],
        "answer": "O(n)",
        "difficulty": "medium",
        "hint": "Проход по всем элементам."
    },
    {
        "question": "Для какого массива применяется бинарный поиск?",
        "options": [
            "Для случайного массива",
            "Для отсортированного массива",
            "Для пустого массива"
        ],
        "answer": "Для отсортированного массива",
        "difficulty": "medium",
        "hint": "Нужна сортировка."
    },
    {
        "question": "Что такое рекурсия?",
        "options": [
            "Метод хранения данных",
            "Функция, вызывающая саму себя",
            "Тип сортировки"
        ],
        "answer": "Функция, вызывающая саму себя",
        "difficulty": "medium",
        "hint": "Самовызов функции."
    },
    {
        "question": "Что представляет собой связный список?",
        "options": [
            "Набор несвязанных данных",
            "Последовательность узлов со ссылками",
            "Тип графика"
        ],
        "answer": "Последовательность узлов со ссылками",
        "difficulty": "medium",
        "hint": "Узлы + ссылки."
    },
    {
        "question": "Что означает O(log n)?",
        "options": [
            "Логарифмическая сложность",
            "Линейная сложность",
            "Постоянная сложность"
        ],
        "answer": "Логарифмическая сложность",
        "difficulty": "medium",
        "hint": "Медленный рост."
    },

    # HARD
    {
        "question": "Какой алгоритм сортировки использует принцип 'разделяй и властвуй'?",
        "options": [
            "Пузырьковая сортировка",
            "Быстрая сортировка",
            "Сортировка выбором"
        ],
        "answer": "Быстрая сортировка",
        "difficulty": "hard",
        "hint": "Разделение массива."
    },
    {
        "question": "Какова средняя сложность быстрой сортировки?",
        "options": ["O(n²)", "O(n log n)", "O(log n)"],
        "answer": "O(n log n)",
        "difficulty": "hard",
        "hint": "Средняя оптимальность."
    },
    {
        "question": "Что такое дерево в структурах данных?",
        "options": [
            "Линейная структура",
            "Иерархическая структура",
            "Тип массива"
        ],
        "answer": "Иерархическая структура",
        "difficulty": "hard",
        "hint": "Родитель-ребёнок."
    },
    {
        "question": "Что такое хеш-таблица?",
        "options": [
            "Таблица для сортировки",
            "Структура ключ-значение",
            "Тип графа"
        ],
        "answer": "Структура ключ-значение",
        "difficulty": "hard",
        "hint": "Ключ → значение."
    },
    {
        "question": "Какова сложность поиска в хеш-таблице?",
        "options": ["O(1)", "O(n)", "O(log n)"],
        "answer": "O(1)",
        "difficulty": "hard",
        "hint": "Мгновенный доступ."
    }
]

# ---------------- ВВОД ----------------

name = st.text_input("Введите имя")

group = st.selectbox(
    "Выберите группу",
    ["Контрольная", "Экспериментальная"]
)

# ---------------- STATE ----------------

if "score" not in st.session_state:
    st.session_state.score = 0
if "question_number" not in st.session_state:
    st.session_state.question_number = 1
if "difficulty" not in st.session_state:
    st.session_state.difficulty = "medium"
if "used_questions" not in st.session_state:
    st.session_state.used_questions = []
if "finished" not in st.session_state:
    st.session_state.finished = False
if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "show_hint" not in st.session_state:
    st.session_state.show_hint = False
if "last_hint" not in st.session_state:
    st.session_state.last_hint = ""

# ---------------- ЗАВЕРШЕНИЕ ----------------

if st.session_state.question_number > 15:
    st.session_state.finished = True

# ---------------- ВЫБОР ВОПРОСА ----------------

if not st.session_state.finished:

    if st.session_state.current_question is None:

        # ---------------- КОНТРОЛЬНАЯ ----------------
        if group == "Контрольная":

            if "control_order" not in st.session_state:
                st.session_state.control_order = random.sample(questions, 15)

            idx = st.session_state.question_number - 1
            st.session_state.current_question = st.session_state.control_order[idx]

        # ---------------- ЭКСПЕРИМЕНТАЛЬНАЯ ----------------
        else:

            candidates = [
                q for q in questions
                if q["difficulty"] == st.session_state.difficulty
                and q["question"] not in st.session_state.used_questions
            ]

            if not candidates:

                if st.session_state.difficulty == "hard":
                    st.session_state.difficulty = "medium"
                elif st.session_state.difficulty == "medium":
                    st.session_state.difficulty = "easy"

                candidates = [
                    q for q in questions
                    if q["difficulty"] == st.session_state.difficulty
                    and q["question"] not in st.session_state.used_questions
                ]

            if not candidates:
                candidates = [
                    q for q in questions
                    if q["question"] not in st.session_state.used_questions
                ]

            if not candidates:
                st.session_state.finished = True
                st.rerun()

            st.session_state.current_question = random.choice(candidates)

    q = st.session_state.current_question

    st.subheader(f"Вопрос {st.session_state.question_number}")
    st.progress((st.session_state.question_number - 1) / 15)

    if group == "Экспериментальная":
        st.info(f"Сложность: {st.session_state.difficulty}")

    st.write(q["question"])

    answer = st.radio(
        "Ответ:",
        q["options"],
        index=None,
        key=st.session_state.question_number
    )
# ---------------- ПОДСКАЗКА ----------------

if st.session_state.show_hint:
    st.warning(f"Подсказка: {st.session_state.last_hint}")

    if st.button("Далее"):
        st.session_state.show_hint = False
        st.session_state.last_hint = ""

        st.session_state.question_number += 1
        st.session_state.current_question = None
        st.rerun()

# ---------------- ОТВЕТ ----------------

if st.button("Ответить"):

    if answer is None:
        st.warning("Выберите ответ!")
        st.stop()

    st.session_state.used_questions.append(q["question"])

    if answer == q["answer"]:

        st.success("Верно!")
        st.session_state.score += 1

        if group == "Экспериментальная":

            levels = ["easy", "medium", "hard"]
            idx = levels.index(st.session_state.difficulty)

            if idx < 2:
                next_level = levels[idx + 1]

                if any(
                    q["difficulty"] == next_level
                    and q["question"] not in st.session_state.used_questions
                    for q in questions
                ):
                    st.session_state.difficulty = next_level

        st.session_state.question_number += 1
        st.session_state.current_question = None
        st.rerun()

    else:

        st.error("Неверно!")

        if group == "Экспериментальная":
            st.session_state.show_hint = True
            st.session_state.last_hint = q["hint"]

            if st.session_state.difficulty == "hard":
                st.session_state.difficulty = "medium"
            elif st.session_state.difficulty == "medium":
                st.session_state.difficulty = "easy"

        st.session_state.question_number += 1
        st.session_state.current_question = None
        st.rerun()

# ---------------- РЕЗУЛЬТАТ ----------------

else:

    st.success(f"{name}, результат: {st.session_state.score} из 15")

    df = pd.DataFrame([{
        "Имя": name,
        "Группа": group,
        "Баллы": st.session_state.score
    }])

    if os.path.exists(file):
        old = pd.read_csv(file)
        pd.concat([old, df], ignore_index=True).to_csv(file, index=False)
    else:
        df.to_csv(file, index=False)

    st.download_button(
        "Скачать CSV",
        open(file, "rb"),
        file_name="results.csv"
    )

    if st.button("Начать заново"):
        st.session_state.clear()
        st.rerun()

if st.button("Очистить результаты"):
    if os.path.exists(file):
        os.remove(file)
        st.rerun()
