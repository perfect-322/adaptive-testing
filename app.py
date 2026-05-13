import streamlit as st
import pandas as pd
import os
import random

file = "results.csv"
st.title("Адаптивное тестирование по информатике")

# ---------------- ВОПРОСЫ (15 штук) ----------------
# (Здесь тот же список из 15 вопросов: 5 easy, 5 medium, 5 hard)
questions = [
    {"question": "Что такое алгоритм?", "options": ["Набор случайных действий", "Последовательность команд для решения задачи", "Тип данных"], "answer": "Последовательность команд для решения задачи", "difficulty": "easy", "hint": "Алгоритм — это последовательность шагов для решения задачи."},
    {"question": "Какая структура данных работает по принципу FIFO?", "options": ["Стек", "Очередь", "Массив"], "answer": "Очередь", "difficulty": "easy", "hint": "FIFO означает: First In First Out."},
    {"question": "Какая структура данных работает по принципу LIFO?", "options": ["Стек", "Очередь", "Список"], "answer": "Стек", "difficulty": "easy", "hint": "LIFO означает: Last In First Out."},
    {"question": "Что такое массив?", "options": ["Набор элементов одного типа", "Графическая фигура", "Операционная система"], "answer": "Набор элементов одного типа", "difficulty": "easy", "hint": "Массив хранит элементы одного типа."},
    {"question": "Какой поиск проверяет элементы по порядку?", "options": ["Бинарный поиск", "Линейный поиск", "Хеширование"], "answer": "Линейный поиск", "difficulty": "easy", "hint": "Проверяет элементы по одному."},
    {"question": "Какова сложность линейного поиска?", "options": ["O(log n)", "O(n)", "O(1)"], "answer": "O(n)", "difficulty": "medium", "hint": "Линейный поиск проходит по всем элементам."},
    {"question": "Для какого массива применяется бинарный поиск?", "options": ["Для случайного массива", "Для отсортированного массива", "Для пустого массива"], "answer": "Для отсортированного массива", "difficulty": "medium", "hint": "Бинарный поиск работает только с отсортированными данными."},
    {"question": "Что такое рекурсия?", "options": ["Метод хранения данных", "Функция, вызывающая саму себя", "Тип сортировки"], "answer": "Функция, вызывающая саму себя", "difficulty": "medium", "hint": "Рекурсия — это вызов функцией самой себя."},
    {"question": "Что представляет собой связный список?", "options": ["Набор несвязанных данных", "Последовательность узлов со ссылками", "Тип графика"], "answer": "Последовательность узлов со ссылками", "difficulty": "medium", "hint": "Связный список состоит из узлов и ссылок."},
    {"question": "Что означает O(log n)?", "options": ["Логарифмическая сложность", "Линейная сложность", "Постоянная сложность"], "answer": "Логарифмическая сложность", "difficulty": "medium", "hint": "O(log n) растет медленнее, чем O(n)."},
    {"question": "Какой алгоритм сортировки использует принцип 'разделяй и властвуй'?", "options": ["Пузырьковая сортировка", "Быстрая сортировка", "Сортировка выбором"], "answer": "Быстрая сортировка", "difficulty": "hard", "hint": "Quick Sort использует разбиение массива."},
    {"question": "Какова средняя сложность быстрой сортировки?", "options": ["O(n²)", "O(n log n)", "O(log n)"], "answer": "O(n log n)", "difficulty": "hard", "hint": "Быстрая сортировка обычно работает быстрее O(n²)."},
    {"question": "Что такое дерево в структурах данных?", "options": ["Линейная структура", "Иерархическая структура", "Тип массива"], "answer": "Иерархическая структура", "difficulty": "hard", "hint": "Дерево имеет родительские и дочерние элементы."},
    {"question": "Что такое хеш-таблица?", "options": ["Таблица для сортировки", "Структура данных для хранения пар ключ-значение", "Тип графа"], "answer": "Структура данных для хранения пар ключ-значение", "difficulty": "hard", "hint": "Хеш-таблица хранит данные по ключу."},
    {"question": "Какова средняя сложность поиска в хеш-таблице?", "options": ["O(1)", "O(n)", "O(log n)"], "answer": "O(1)", "difficulty": "hard", "hint": "Хеш-таблицы обеспечивают очень быстрый доступ."}
]

# ---------------- INITIAL STATE ----------------
if "score" not in st.session_state: st.session_state.score = 0
if "question_number" not in st.session_state: st.session_state.question_number = 1
if "difficulty" not in st.session_state: st.session_state.difficulty = "medium"
if "used_questions" not in st.session_state: st.session_state.used_questions = []
if "finished" not in st.session_state: st.session_state.finished = False
if "current_question" not in st.session_state: st.session_state.current_question = None
if "show_hint" not in st.session_state: st.session_state.show_hint = False

# ---------------- ВВОД ----------------
name = st.text_input("Введите имя")
group = st.selectbox("Выберите группу", ["Контрольная", "Экспериментальная"])

# ---------------- ЛОГИКА ТЕСТА ----------------
if st.session_state.question_number > 15:
    st.session_state.finished = True

if not st.session_state.finished:
    # Выбор вопроса, если он еще не выбран для текущего шага
    if st.session_state.current_question is None:
        if group == "Экспериментальная":
            # Фильтруем вопросы нужной сложности
            available = [q for q in questions if q["difficulty"] == st.session_state.difficulty and q["question"] not in st.session_state.used_questions]
            
            # Если такой сложности нет (закончились), берем любой оставшийся
            if not available:
                available = [q for q in questions if q["question"] not in st.session_state.used_questions]
            
            st.session_state.current_question = random.choice(available)
        else:
            # Контрольная группа: просто рандом из всех
            available = [q for q in questions if q["question"] not in st.session_state.used_questions]
            st.session_state.current_question = random.choice(available)

    q = st.session_state.current_question
    st.subheader(f"Вопрос {st.session_state.question_number} из 15")
    if group == "Экспериментальная": st.info(f"Сложность: {q['difficulty']}")
    
    st.write(q["question"])
    answer = st.radio("Ответ:", q["options"], index=None, key=f"q_{st.session_state.question_number}")

    # Логика подсказки
    if st.session_state.show_hint:
        st.warning(f"Подсказка: {q['hint']}")
        if st.button("Далее"):
            st.session_state.show_hint = False
            st.session_state.current_question = None
            st.session_state.question_number += 1
            st.rerun()

    # Кнопка ответа
    elif st.button("Ответить"):
        if answer:
            st.session_state.used_questions.append(q["question"])
            if answer == q["answer"]:
                st.success("Верно!")
                st.session_state.score += 1
                # Адаптация: вверх
                if group == "Экспериментальная":
                    if st.session_state.difficulty == "easy": st.session_state.difficulty = "medium"
                    elif st.session_state.difficulty == "medium": st.session_state.difficulty = "hard"
                
                st.session_state.current_question = None
                st.session_state.question_number += 1
                st.rerun()
            else:
                st.error("Неверно!")
                if group == "Экспериментальная":
                    st.session_state.show_hint = True
                    # Адаптация: вниз
                    if st.session_state.difficulty == "hard": st.session_state.difficulty = "medium"
                    elif st.session_state.difficulty == "medium": st.session_state.difficulty = "easy"
                else:
                    st.session_state.current_question = None
                    st.session_state.question_number += 1
                st.rerun()
        else:
            st.warning("Выберите вариант!")

# ---------------- ФИНАЛ ----------------
else:
    st.success(f"Тест завершен, {name}! Баллы: {st.session_state.score} / 15")
    # Тут можно добавить сохранение в CSV (как в твоем исходнике)
    if st.button("Начать заново"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
