import streamlit as st
import pandas as pd
import os
import random

file = "results.csv"

st.title("Адаптивное тестирование по информатике")

# ---------------- ВОПРОСЫ ----------------

questions = [

    # ---------------- EASY ----------------

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
        "hint": "FIFO означает: First In First Out."
    },

    {
        "question": "Какая структура данных работает по принципу LIFO?",
        "options": ["Стек", "Очередь", "Список"],
        "answer": "Стек",
        "difficulty": "easy",
        "hint": "LIFO означает: Last In First Out."
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
        "hint": "Массив хранит элементы одного типа."
    },

    {
        "question": "Какой поиск проверяет элементы по порядку?",
        "options": ["Бинарный поиск", "Линейный поиск", "Хеширование"],
        "answer": "Линейный поиск",
        "difficulty": "easy",
        "hint": "Проверяет элементы по одному."
    },

    # ---------------- MEDIUM ----------------

    {
        "question": "Какова сложность линейного поиска?",
        "options": ["O(log n)", "O(n)", "O(1)"],
        "answer": "O(n)",
        "difficulty": "medium",
        "hint": "Линейный поиск проходит по всем элементам."
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
        "hint": "Бинарный поиск работает только с отсортированными данными."
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
        "hint": "Рекурсия — это вызов функцией самой себя."
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
        "hint": "Связный список состоит из узлов и ссылок."
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
        "hint": "O(log n) растет медленнее, чем O(n)."
    },

    # ---------------- HARD ----------------

    {
        "question": "Какой алгоритм сортировки использует принцип 'разделяй и властвуй'?",
        "options": [
            "Пузырьковая сортировка",
            "Быстрая сортировка",
            "Сортировка выбором"
        ],
        "answer": "Быстрая сортировка",
        "difficulty": "hard",
        "hint": "Quick Sort использует разбиение массива."
    },

    {
        "question": "Какова средняя сложность быстрой сортировки?",
        "options": ["O(n²)", "O(n log n)", "O(log n)"],
        "answer": "O(n log n)",
        "difficulty": "hard",
        "hint": "Быстрая сортировка обычно работает быстрее O(n²)."
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
        "hint": "Дерево имеет родительские и дочерние элементы."
    },

    {
        "question": "Что такое хеш-таблица?",
        "options": [
            "Таблица для сортировки",
            "Структура данных для хранения пар ключ-значение",
            "Тип графа"
        ],
        "answer": "Структура данных для хранения пар ключ-значение",
        "difficulty": "hard",
        "hint": "Хеш-таблица хранит данные по ключу."
    },

    {
        "question": "Какова средняя сложность поиска в хеш-таблице?",
        "options": ["O(1)", "O(n)", "O(log n)"],
        "answer": "O(1)",
        "difficulty": "hard",
        "hint": "Хеш-таблицы обеспечивают очень быстрый доступ."
    }
]

# ---------------- ВВОД ----------------

name = st.text_input("Введите имя")

group = st.selectbox(
    "Выберите группу",
    ["Контрольная", "Экспериментальная"]
)

# ---------------- SESSION STATE ----------------

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

if st.session_state.question_number > 5:
    st.session_state.finished = True

# ---------------- ФИЛЬТР ----------------

if group == "Экспериментальная":

    available_questions = [
        q for q in questions
        if q["difficulty"] == st.session_state.difficulty
        and q["question"] not in st.session_state.used_questions
    ]

    if not available_questions:
        available_questions = [
            q for q in questions
            if q["question"] not in st.session_state.used_questions
        ]

else:

    available_questions = [
        q for q in questions
        if q["question"] not in st.session_state.used_questions
    ]

# ---------------- ТЕСТ ----------------

if not st.session_state.finished:

    if available_questions:

        if st.session_state.current_question is None:

            if group == "Контрольная":
                st.session_state.current_question = available_questions[0]
            else:
                st.session_state.current_question = random.choice(available_questions)

        q = st.session_state.current_question

        st.subheader(f"Вопрос {st.session_state.question_number}")
        st.progress((st.session_state.question_number - 1) / 5)

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

        elif st.button("Ответить"):

            if answer is None:
                st.warning("Выберите ответ!")
                st.stop()

            st.session_state.used_questions.append(q["question"])

            if answer == q["answer"]:

                st.success("Верно!")
                st.session_state.score += 1

                if group == "Экспериментальная":
                    if st.session_state.difficulty == "easy":
                        st.session_state.difficulty = "medium"
                    elif st.session_state.difficulty == "medium":
                        st.session_state.difficulty = "hard"

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

                else:
                    st.session_state.question_number += 1
                    st.session_state.current_question = None

                st.rerun()

# ---------------- РЕЗУЛЬТАТ ----------------

else:

    st.success(f"{name}, результат: {st.session_state.score} из 5")

    df = pd.DataFrame({
        "Имя": [name],
        "Группа": [group],
        "Баллы": [st.session_state.score]
    })

    if os.path.exists(file):
        old = pd.read_csv(file)
        new = pd.concat([old, df], ignore_index=True)
        new.to_csv(file, index=False)
    else:
        df.to_csv(file, index=False)

    st.info("Результат сохранён")
    if os.path.exists(file):

        with open(file, "rb") as f:

            st.download_button(
            label="Скачать результаты CSV",
            data=f,
            file_name="results.csv",
            mime="text/csv"
        )

    if st.button("Начать заново"):
        st.session_state.score = 0
        st.session_state.question_number = 1
        st.session_state.difficulty = "medium"
        st.session_state.used_questions = []
        st.session_state.finished = False
        st.session_state.current_question = None
        st.session_state.show_hint = False
        st.session_state.last_hint = ""

if st.button("Очистить результаты"):

    if os.path.exists(file):

        os.remove(file)

        st.success("results.csv удалён")
        st.rerun()
