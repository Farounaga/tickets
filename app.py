from dash import Dash, dcc, html, Input, Output, dash_table
import os
import pandas as pd
import plotly.graph_objects as go
import json
from datetime import datetime

# Определяем базовую директорию (папку, где находится app.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Чтение данных для первого графика
excel_file1 = os.path.join(BASE_DIR, "day_week_distribution.xlsx")
data1 = pd.read_excel(excel_file1)
data1['day_distribution'] = data1['day_distribution'].apply(json.loads)
data1['hour_distribution'] = data1['hour_distribution'].apply(json.loads)
data1['date'] = pd.to_datetime(pd.date_range(start="2023-10-01", periods=len(data1), freq="D"))

# Чтение данных для второго графика
excel_file2 = os.path.join(BASE_DIR, "clusters_general_stats.xlsx")
data2 = pd.read_excel(excel_file2)
data2['median_response_time'] = data2['median_response_time'].astype(float)
data2['min_response_time'] = data2['min_response_time'].astype(float)
data2['max_response_time'] = data2['max_response_time'].astype(float)

# Чтение данных для третьего графика
csv_file3 = os.path.join(BASE_DIR, "avg_response_time.csv")
data3 = pd.read_csv(csv_file3, sep=';')
data3['average_response_time_hours'] = data3['average_response_time_hours'].str.replace(',', '.').astype(float)
data3['ticket_id'] = data3['ticket_id'].fillna(0).astype(int)

# Создание приложения Dash
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Analyse des tickets", style={'text-align': 'center'}),

    dcc.Tabs([
        dcc.Tab(label='Liste des clusters', children=[
            dash_table.DataTable(id='clusters',
            columns=[
                 {"name": "Cluster", "id": "cluster"},
                {"name": "Description", "id": "description"},
                {"name": "Nombre de tickets", "id": "nombre"},
            ],
            data=[
                {"cluster": "1", "description": "Questions utilisation logiciel", "nombre": "68"},
                {"cluster": "2", "description": "Rectifications informations", "nombre": "21"},
                {"cluster": "3", "description": "Problèmes/questions application", "nombre": "44"},
                {"cluster": "4", "description": "Preuve de profession", "nombre": "138"},
                {"cluster": "5", "description": "Problèmes connexion / application", "nombre": "96"},
                {"cluster": "6", "description": "Bordereau de vaccination / problèmes variés", "nombre": "77"},
                {"cluster": "7", "description": "Questions/problèmes différents", "nombre": "73"},
                {"cluster": "8", "description": "Demande de suppression compte", "nombre": "52"},
                {"cluster": "9", "description": "Questions vaccination expertise", "nombre": "3"},
                {"cluster": "10", "description": "Erreurs / suivi", "nombre": "34"},
                {"cluster": "11", "description": "Preuve de profession", "nombre": "339"},
                {"cluster": "12", "description": "Problème réception mail", "nombre": "126"},
                {"cluster": "13", "description": "MAJ RPPS/ Infos", "nombre": "62"},
                {"cluster": "14", "description": "Collèges / autorisations / élèves", "nombre": "37"},
                {"cluster": "15", "description": "Problèmes connexion / réception messages/SMS", "nombre": "84"},
                {"cluster": "16", "description": "Questions/problèmes vaccins", "nombre": "66"},
                {"cluster": "17", "description": "Création/gestion équipe/compte/admin", "nombre": "53"},
                {"cluster": "18", "description": "Demandes suppression/modification compte / envoie preuve de profession", "nombre": "56"},
                {"cluster": "19", "description": "Changement numéro téléphone, problèmes de connexion suite à cela", "nombre": "81"},
                {"cluster": "20", "description": "Problèmes connexion / identifiants / équipe", "nombre": "81"},
                {"cluster": "21", "description": "Preuve de profession", "nombre": "79"},
                {"cluster": "22", "description": "Demandes", "nombre": "2"},
                {"cluster": "23", "description": "Question/problèmes collèges", "nombre": "64"},
                {"cluster": "24", "description": "Problèmes connexion / changement numero téléphone", "nombre": "188"},
                {"cluster": "25", "description": "Questions/problèmes connexion / compte", "nombre": "111"},
                {"cluster": "26", "description": "Message de correction d'erreur CVN", "nombre": "24"},
                {"cluster": "27", "description": "MAJ équipe / RPPS", "nombre": "127"},
                {"cluster": "28", "description": "Questions/problèmes compte / mail", "nombre": "144"},
                {"cluster": "29", "description": "Dossiers (doublons/suppression)", "nombre": "20"},
                {"cluster": "30", "description": "Statistiques", "nombre": "18"},
                {"cluster": "31", "description": "Questions/problèmes compte / preuve de profession", "nombre": "76"},
                {"cluster": "32", "description": "Questions/problèmes vaccins", "nombre": "93"},
                {"cluster": "33", "description": "Gestion équipe / administrateur", "nombre": "44"},
                {"cluster": "34", "description": "Datamatrix", "nombre": "11"},
                {"cluster": "35", "description": "Problèmes connexion / réception mail / utilisation", "nombre": "106"},
                {"cluster": "36", "description": "Import/Export", "nombre": "21"},
                {"cluster": "37", "description": "Questions/problèmes carnets/utilisation", "nombre": "123"},
                {"cluster": "38", "description": "Questions vaccination /campagne HPV", "nombre": "44"},
                {"cluster": "39", "description": "Problèmes connexion / identifiants", "nombre": "49"},
                {"cluster": "40", "description": "Preuve de profession", "nombre": "118"},
                {"cluster": "41", "description": "Version anglaise", "nombre": "7"},
                {"cluster": "42", "description": "Agenda", "nombre": "18"},
                {"cluster": "43", "description": "Preuve de profession / suppression compte", "nombre": "82"},
                {"cluster": "44", "description": "Preuve de profession", "nombre": "14"},
                {"cluster": "45", "description": "Tags", "nombre": "51"},
                {"cluster": "46", "description": "Gestion/problème équipe / administrateur / RPPS", "nombre": "104"},
                {"cluster": "47", "description": "Questions HPV", "nombre": "154"},
                {"cluster": "48", "description": "MAJ RPPS/ Preuve de profession", "nombre": "63"},
                {"cluster": "49", "description": "Différentes question/sollicitations", "nombre": "55"},
                {"cluster": "50", "description": "Erreur invitation équipe", "nombre": "1"},
            ],
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'left'},
            style_header={'fontWeight': 'bold', 'backgroundColor': 'lightblue'}
            ), dcc.Graph(id='clusters-graphic')
        ]),
        
        dcc.Tab(label='Repartition par jour de semaine', children=[
            dcc.DatePickerRange(
                id="date-range-picker",
                start_date=datetime(2023, 10, 1),
                end_date=datetime(2023, 10, 7),
                display_format="YYYY-MM-DD",
            ),
            dcc.Graph(id="main-graph"),
            dcc.Graph(id="detail-graph")
        ]),

        dcc.Tab(label='Statistiques de clusteurs', children=[
            dcc.Graph(id="clusters-graph")
        ]),

        dcc.Tab(label='Temps de reponse moyen', children=[
            dcc.Graph(id="response-time-graph")
        ])
    ])
])

# Callback pour le graphique de la table des clusters

@app.callback(
    Output('clusters-graphic', 'figure'),  # Обновляем график
    Input('clusters', 'data')           # Берём данные из таблицы
)
def update_graph(data):
    # Преобразуем данные в DataFrame для обработки
    df = pd.DataFrame(data)
    df['nombre'] = df['nombre'].astype(int)  # Приводим к числовому типу, если нужно

    # Создаём график
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df['cluster'],  # Кластеры по оси X
        y=df['nombre'],   # Количество тикетов по оси Y
        marker=dict(color='rgba(0, 123, 255, 0.6)'),
        name="Nombre de tickets"
    ))

    # Настройки графика
    fig.update_layout(
        title="Nombre de tickets par cluster",
        xaxis_title="Cluster",
        yaxis_title="Nombre de tickets",
        template="plotly_white"
    )
    return fig



# Callback для первого графика
# Callback для обновления основного графика
@app.callback(
    Output("main-graph", "figure"),
    Input("date-range-picker", "start_date"),
    Input("date-range-picker", "end_date")
)
def update_main_graph(start_date, end_date):
    # Фильтруем данные по выбранному диапазону дат
    filtered_data = data1[(data1['date'] >= start_date) & (data1['date'] <= end_date)]

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
    filtered_data = data1[(data1['date'] >= start_date) & (data1['date'] <= end_date)]

    hours = list(range(24))  # Часы от 0 до 23
    hour_values = [0] * 24  # Инициализация массива для подсчета тикетов

    if click_data:
        # Извлечение информации о выбранном дне недели
        day_name = click_data["points"][0]["x"]  # Название дня недели (например, "Monday")
        day_index = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"].index(day_name)
        
        # Находим даты, которые соответствуют выбранному дню недели
        selected_dates = filtered_data[filtered_data['date'].dt.weekday == day_index]['date'].dt.strftime('%Y-%m-%d').unique()

        if len(selected_dates) > 0:
            # Используем первую дату из списка, если их несколько
            selected_date = selected_dates[0]
        else:
            selected_date = "нет данных"

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

# Callback для второго графика
@app.callback(
    Output("clusters-graph", "figure"),
    Input("clusters-graph", "id")  # Заглушка для запуска
)
def update_clusters_graph(_):
    fig = go.Figure()
    for cluster in data2['cluster'].unique():
        cluster_data = data2[data2['cluster'] == cluster]
        min_value = cluster_data['min_response_time'].values[0]
        max_value = cluster_data['max_response_time'].values[0]
        median_value = cluster_data['median_response_time'].values[0]

        fig.add_trace(go.Scatter(
            x=[f"Cluster {cluster}", f"Cluster {cluster}"],
            y=[min_value, max_value],
            mode='lines+markers',
            line=dict(width=2, color='rgba(0, 123, 255, 0.6)'),
            marker=dict(size=1, color='rgba(0, 123, 255, 0.6)'),
            name="Min/Max"
        ))
        fig.add_trace(go.Scatter(
            x=[f"Cluster {cluster}"],
            y=[median_value],
            mode='markers',
            marker=dict(size=10, color='rgba(255, 0, 0, 0.8)'),
            name="Médiane"
        ))

    fig.update_layout(
        title="Temps de réponse par cluster",
        xaxis_title="Clusters",
        yaxis_title="Temps de réponse (heures)",
        updatemenus=[
            dict(
                type="dropdown",
                showactive=True,
                buttons=[
                    dict(
                        label="Tout",
                        method="update",
                        args=[{"visible": [True, True] * len(data2['cluster'].unique())},
                              {"title": "Toutes les données"}]
                    ),
                    dict(
                        label="Min/Max",
                        method="update",
                        args=[{"visible": [True, False] * len(data2['cluster'].unique())},
                              {"title": "Seulement minimum et maximum"}]
                    ),
                    dict(
                        label="Médiane",
                        method="update",
                        args=[{"visible": [False, True] * len(data2['cluster'].unique())},
                              {"title": "Seulement médiane"}]
                    )
                ]
            )
        ],
        template="plotly_white"
    )
    return fig

# Callback для третьего графика
@app.callback(
    Output("response-time-graph", "figure"),
    Input("response-time-graph", "id")  # Заглушка для запуска
)
def update_response_time_graph(_):
    fig = go.Figure(data=go.Scatter(
        x=data3['ticket_id'],
        y=data3['average_response_time_hours'],
        mode='markers',
        marker=dict(
            size=10,
            color=data3['average_response_time_hours'],
            colorscale='oryel',
            showscale=True,
            line=dict(width=2, color='black')
        )
    ))
    fig.update_layout(
        title="Temps de réponse moyen par ticket", xaxis_title="Ticket ID", yaxis_title="Temps de réponse (heure)", template="plotly_white"
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
