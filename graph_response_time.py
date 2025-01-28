import plotly.graph_objects as go
import pandas as pd

# Чтение данных из CSV
csv_file = "C:/Programmation/Ruby/Tickets/graphics/avg_response_time.csv"  # Укажите путь к файлу
data = pd.read_csv(csv_file, sep=';')  # Чтение CSV

# Замена запятой на точку и преобразование чисел
data['average_response_time_hours'] = data['average_response_time_hours'].str.replace(',', '.').astype(float)

# Обработка пустых значений и определение осей
data['ticket_id'] = data['ticket_id'].fillna(0).astype(int)
x_values = data['ticket_id']  # Колонка для оси X
y_values = data['average_response_time_hours']  # Колонка для оси Y

# Создаём график с кастомной цветовой схемой
fig = go.Figure(data=go.Scatter(
    x=x_values,
    y=y_values,
    mode='markers',
    marker=dict(
        size=15,  # Увеличиваем размер точек
        color=y_values,  # Цвет точек зависит от значений на оси Y
        colorscale='Viridis',  # Градиентная цветовая схема
        showscale=True,  # Отображение цветовой шкалы
        line=dict(
            width=2,
            color='black'  # Чёрная граница вокруг точек
        )
    )
))

# Настройки графика
fig.update_layout(
    title=dict(
        text='Temps de réponse par ticket',  # Заголовок графика
        font=dict(size=20, color='black'),
        x=0.5  # Центрируем заголовок
    ),
    xaxis=dict(
        title='Ticket ID',
        titlefont=dict(size=16, color='black'),
        gridcolor='lightgrey',  # Цвет сетки
        zerolinecolor='grey',
        tickangle=45  # Угол подписи значений оси X
    ),
    yaxis=dict(
        title='Temps de réponse (heures)',
        titlefont=dict(size=16, color='black'),
        gridcolor='lightgrey',
        zerolinecolor='grey',
        range=[0, max(y_values)]  # Диапазон от 0 до максимального значения
    ),
    plot_bgcolor='white',  # Фон внутри графика
    paper_bgcolor='white',  # Фон вокруг графика
    font=dict(
        family="Arial, sans-serif",
        size=12,
        color="black"  # Цвет текста для светлого фона
    )
)

# Показать график
fig.show()
