import streamlit as st
import random

st.title("Адаптивное тестирование")

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


# ---------------- STATE ----------------

if "qnum" not in st.session_state:
    st.session_state.qnum = 1
if "score" not in st.session_state:
    st.session_state.score = 0
if "difficulty" not in st.session_state:
    st.session_state.difficulty = "easy"
if "used" not in st.session_state:
    st.session_state.used = []
if "current" not in st.session_state:
    st.session_state.current = None
if "hint" not in st.session_state:
    st.session_state.hint = None

group = st.selectbox("Группа", ["Контрольная", "Экспериментальная"])

# ---------------- ВЫБОР ВОПРОСА ----------------

if st.session_state.current is None:

    if group == "Контрольная":
        pool = [q for q in questions if q["question"] not in st.session_state.used]
        st.session_state.current = random.choice(pool)

    else:
        pool = [
            q for q in questions
            if q["difficulty"] == st.session_state.difficulty
            and q["question"] not in st.session_state.used
        ]

        if not pool:
            pool = [q for q in questions if q["question"] not in st.session_state.used]

        st.session_state.current = random.choice(pool)

q = st.session_state.current

st.subheader(f"Вопрос {st.session_state.qnum}")
st.write(q["question"])

answer = st.radio("Ответ:", q["options"], index=None, key=st.session_state.qnum)

# ---------------- ОТВЕТ ----------------

if st.button("Ответить"):

    if answer is None:
        st.warning("Выбери ответ")
        st.stop()

    st.session_state.used.append(q["question"])

    if answer == q["answer"]:
        st.success("Верно!")
        st.session_state.score += 1

        if group == "Экспериментальная":
            if st.session_state.difficulty == "easy":
                st.session_state.difficulty = "medium"
            elif st.session_state.difficulty == "medium":
                st.session_state.difficulty = "hard"

    else:
        st.error("Неверно!")
        st.session_state.hint = q["hint"]

        if group == "Экспериментальная":
            if st.session_state.difficulty == "hard":
                st.session_state.difficulty = "medium"
            elif st.session_state.difficulty == "medium":
                st.session_state.difficulty = "easy"

    st.session_state.qnum += 1
    st.session_state.current = None
    st.rerun()

# ---------------- ПОДСКАЗКА ----------------

if st.session_state.hint:
    st.info(f"Подсказка: {st.session_state.hint}")

    if st.button("Далее"):
        st.session_state.hint = None
        st.rerun()
