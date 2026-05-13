import streamlit as st
import pandas as pd
import os
import random

file = "results.csv"

st.title("Адаптивное тестирование по информатике")

# ---------------- ВОПРОСЫ ----------------

questions = [
    # EASY
    {"question": "Что такое алгоритм?",
     "options": ["Набор случайных действий",
                 "Последовательность команд для решения задачи",
                 "Тип данных"],
     "answer": "Последовательность команд для решения задачи",
     "difficulty": "easy",
     "hint": "Алгоритм — это последовательность шагов."},

    {"question": "Какая структура данных работает FIFO?",
     "options": ["Стек", "Очередь", "Массив"],
     "answer": "Очередь",
     "difficulty": "easy",
     "hint": "First In First Out."},

    {"question": "Какая структура данных LIFO?",
     "options": ["Стек", "Очередь", "Список"],
     "answer": "Стек",
     "difficulty": "easy",
     "hint": "Last In First Out."},

    {"question": "Что такое массив?",
     "options": ["Набор элементов одного типа",
                 "Графика",
                 "ОС"],
     "answer": "Набор элементов одного типа",
     "difficulty": "easy",
     "hint": "Одинаковые элементы."},

    {"question": "Какой поиск последовательный?",
     "options": ["Бинарный", "Линейный", "Хеш"],
     "answer": "Линейный",
     "difficulty": "easy",
     "hint": "По одному элементу."},

    # MEDIUM
    {"question": "Сложность линейного поиска?",
     "options": ["O(log n)", "O(n)", "O(1)"],
     "answer": "O(n)",
     "difficulty": "medium",
     "hint": "Проход по всем элементам."},

    {"question": "Бинарный поиск работает на?",
     "options": ["Случайном", "Отсортированном", "Пустом"],
     "answer": "Отсортированном",
     "difficulty": "medium",
     "hint": "Нужна сортировка."},

    {"question": "Что такое рекурсия?",
     "options": ["Хранение", "Функция себя вызывает", "Сортировка"],
     "answer": "Функция себя вызывает",
     "difficulty": "medium",
     "hint": "Самовызов."},

    {"question": "Связный список?",
     "options": ["Массив", "Узлы со связями", "Графика"],
     "answer": "Узлы со связями",
     "difficulty": "medium",
     "hint": "Узлы + ссылки."},

    {"question": "O(log n)?",
     "options": ["Логарифм", "Линейная", "Константа"],
     "answer": "Логарифм",
     "difficulty": "medium",
     "hint": "Медленный рост."},

    # HARD
    {"question": "Divide & Conquer?",
     "options": ["Bubble", "QuickSort", "Selection"],
     "answer": "QuickSort",
     "difficulty": "hard",
     "hint": "Разделяй и властвуй."},

    {"question": "QuickSort сложность?",
     "options": ["O(n²)", "O(n log n)", "O(log n)"],
     "answer": "O(n log n)",
     "difficulty": "hard",
     "hint": "Средняя."},

    {"question": "Дерево?",
     "options": ["Линейная", "Иерархия", "Массив"],
     "answer": "Иерархия",
     "difficulty": "hard",
     "hint": "Родитель-ребёнок."},

    {"question": "Хеш-таблица?",
     "options": ["Сортировка", "Ключ-значение", "Граф"],
     "answer": "Ключ-значение",
     "difficulty": "hard",
     "hint": "key → value."},

    {"question": "Поиск в hash?",
     "options": ["O(1)", "O(n)", "O(log n)"],
     "answer": "O(1)",
     "difficulty": "hard",
     "hint": "Очень быстро."}
]

# ---------------- UI ----------------

name = st.text_input("Имя")

group = st.selectbox("Группа", ["Контрольная", "Экспериментальная"])

# ---------------- STATE ----------------

if "score" not in st.session_state:
    st.session_state.score = 0
if "q_num" not in st.session_state:
    st.session_state.q_num = 1
if "difficulty" not in st.session_state:
    st.session_state.difficulty = "medium"
if "used" not in st.session_state:
    st.session_state.used = []
if "current_q" not in st.session_state:
    st.session_state.current_q = None
if "hint" not in st.session_state:
    st.session_state.hint = False
if "hint_text" not in st.session_state:
    st.session_state.hint_text = ""

# ---------------- FINISH ----------------

if st.session_state.q_num > 15:
    st.session_state.finished = True
else:
    st.session_state.finished = False

# ---------------- QUESTION PICK ----------------

if not st.session_state.finished:

    if st.session_state.current_q is None:

        pool = [q for q in questions if q["question"] not in st.session_state.used]

        if group == "Экспериментальная":
            pool = [q for q in pool if q["difficulty"] == st.session_state.difficulty]

        if not pool:
            st.session_state.finished = True
            st.rerun()

        st.session_state.current_q = random.choice(pool)

    q = st.session_state.current_q

    st.subheader(f"Вопрос {st.session_state.q_num}")
    st.progress(st.session_state.q_num / 15)

    if group == "Экспериментальная":
        st.info(f"Сложность: {st.session_state.difficulty}")

    st.write(q["question"])

    answer = st.radio("Ответ:", q["options"], key=st.session_state.q_num)

    # ---------------- HINT ----------------

    if st.session_state.hint:
        st.warning(st.session_state.hint_text)

        if st.button("Далее"):
            st.session_state.hint = False
            st.session_state.hint_text = ""
            st.session_state.q_num += 1
            st.session_state.current_q = None
            st.rerun()

    # ---------------- ANSWER ----------------

    if st.button("Ответить"):

        if answer is None:
            st.warning("Выбери ответ")
            st.stop()

        st.session_state.used.append(q["question"])

        if answer == q["answer"]:

            st.success("Верно!")
            st.session_state.score += 1

            if group == "Экспериментальная":
                order = ["easy", "medium", "hard"]
                i = order.index(st.session_state.difficulty)

                if i < 2:
                    st.session_state.difficulty = order[i + 1]

        else:

            st.error("Неверно!")

            if group == "Экспериментальная":
                st.session_state.hint = True
                st.session_state.hint_text = q["hint"]

                if st.session_state.difficulty == "hard":
                    st.session_state.difficulty = "medium"
                elif st.session_state.difficulty == "medium":
                    st.session_state.difficulty = "easy"

        st.session_state.q_num += 1
        st.session_state.current_q = None
        st.rerun()

# ---------------- RESULT ----------------

else:

    st.success(f"{name}: {st.session_state.score} / 15")
