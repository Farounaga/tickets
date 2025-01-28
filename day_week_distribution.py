from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.graph_objects as go
import json
from datetime import datetime

# Чтение данных
excel_file = "C:/Programmation/Ruby/Tickets/graphics/day_week_distribution.xlsx"
data = pd.read_excel(excel_file)

# Преобразование колонок day_distribution и hour_distribution в словари
data['day_distribution'] = data['day_distribution'].apply(json.loads)
data['hour_distribution'] = data['hour_distribution'].apply(json.loads)

# Добавим колонку с датами (пример, можно заменить на ваши реальные данные)
data['date'] = pd.to_datetime(pd.date_range(start="2023-10-01", periods=len(data), freq="D"))

# Приложение Dash
app = Dash(__name__)

# Layout приложения
app.layout = html.Div([
    html.H1("Analyse de la distribution des tickets"),
    html.Div([
        dcc.DatePickerRange(
            id="date-range-picker",
            start_date=datetime(2023, 10, 1),
            end_date=datetime(2023, 10, 7),
            display_format="YYYY-MM-DD",
        ),
        dcc.Graph(id="main-graph"),
        dcc.Graph(id="detail-graph")
    ])
])

# Callback для обновления основного графика
@app.callback(
    Output("main-graph", "figure"),
    Input("date-range-picker", "start_date"),
    Input("date-range-picker", "end_date")
)
def update_main_graph(start_date, end_date):
    # Фильтруем данные по выбранному диапазону дат
    filtered_data = data[(data['date'] >= start_date) & (data['date'] <= end_date)]

    # Суммируем тикеты по дням недели
    days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    day_values = [0] * 7

    for _, row in filtered_data.iterrows():
        date_obj = row['date']
        day_index = date_obj.weekday()  # Определяем день недели
        if str(day_index) in row['day_distribution']:
            day_values[day_index] += row['day_distribution'][str(day_index)]

    # Создаём график
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=days,
        y=day_values,
        marker=dict(color='rgba(255, 0, 0, 0.6)'),
        name="Nombre de tickets"
    ))

    fig.update_layout(
        title=f"Distribution des tickets par jour de la semaine ({start_date} - {end_date})",
        xaxis_title="Jours de la semaine",
        yaxis_title="Nombre de tickets",
        template="plotly_white"
    )
    return fig

# Callback для обновления детализированного графика
@app.callback(
    Output("detail-graph", "figure"),
    Input("main-graph", "clickData"),          # Клик на основном графике
    Input("date-range-picker", "start_date"),  # Начальная дата
    Input("date-range-picker", "end_date")     # Конечная дата
)
def update_detail_graph(click_data, start_date, end_date):
    # Фильтруем данные по выбранному диапазону дат
    filtered_data = data[(data['date'] >= start_date) & (data['date'] <= end_date)]

    hours = list(range(24))  # Часы от 0 до 23
    hour_values = [0] * 24  # Инициализация массива для подсчета тикетов

    if click_data:
        # Извлечение информации о выбранном дне недели
        day_name = click_data["points"][0]["x"]  # Название дня недели (например, "Monday")
        day_index = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"].index(day_name)

        # Суммируем данные только для выбранного дня недели
        for _, row in filtered_data.iterrows():
            date_obj = row['date']
            if date_obj.weekday() == day_index:  # Сравниваем день недели
                hour_dist = row['hour_distribution']
                for hour, count in hour_dist.items():
                    hour_values[int(hour)] += count

        title = f"Distribution des tickets par heure (Jour {day_name}, {start_date} - {end_date})"
    else:
        # Если день не выбран, отображаем данные за весь диапазон
        for _, row in filtered_data.iterrows():
            hour_dist = row['hour_distribution']
            for hour, count in hour_dist.items():
                hour_values[int(hour)] += count

        title = f"Distribution des tickets par heure ({start_date} - {end_date})"

    # Создаем график
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=hours,
        y=hour_values,
        marker=dict(color='rgba(0, 123, 255, 0.6)'),
        name="Nombre de tickets"
    ))

    fig.update_layout(
        title=title,
        xaxis_title="Heures",
        yaxis_title="Nolbre de tickets",
        template="plotly_white"
    )

    return fig

# Запуск приложения
if __name__ == "__main__":
    app.run_server(debug=True)
