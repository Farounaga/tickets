import plotly.graph_objects as go

# Пример данных
x_values = [1, 2, 3, 4, 5]  # Значения по оси X
y_values = [10, 20, 15, 25, 30]  # Значения по оси Y

# Создание графика
fig = go.Figure(data=go.Scatter(
    x=x_values,
    y=y_values,
    mode='markers',  # Только точки
    marker=dict(
        size=10,  # Размер точек
        color='blue',  # Цвет точек
        line=dict(
            width=2,
            color='black'  # Цвет границы точек
        )
    )
))

# Настройки графика
fig.update_layout(
    title='Простой точечный график',
    xaxis_title='Ось X',
    yaxis_title='Ось Y',
    template='plotly_white'  # Светлая тема
)

# Показать график
fig.show()
