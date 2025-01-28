import plotly.graph_objects as go
import pandas as pd

# Чтение данных из Excel
excel_file = "C:/Programmation/Ruby/Tickets/graphics/clusters_general_stats.xlsx"
data = pd.read_excel(excel_file)

# Преобразование данных
data['median_response_time'] = data['median_response_time'].astype(float)
data['min_response_time'] = data['min_response_time'].astype(float)
data['max_response_time'] = data['max_response_time'].astype(float)

# Создаём график
fig = go.Figure()

# Добавляем данные для каждого кластера
for cluster in data['cluster'].unique():
    cluster_data = data[data['cluster'] == cluster]
    min_value = cluster_data['min_response_time'].values[0]
    max_value = cluster_data['max_response_time'].values[0]
    median_value = cluster_data['median_response_time'].values[0]
    
    # Линия от минимума до максимума
    fig.add_trace(go.Scatter(
        x=[f"Cluster {cluster}", f"Cluster {cluster}"],
        y=[min_value, max_value],
        mode='lines+markers',
        line=dict(width=2, color='rgba(0, 123, 255, 0.6)'),
        marker=dict(size=1, color='rgba(0, 123, 255, 0.6)'),
        name="Min/Max",
        visible=True  # Показываем по умолчанию
    ))
    
    # Точка на медиане
    fig.add_trace(go.Scatter(
        x=[f"Cluster {cluster}"],
        y=[median_value],
        mode='markers',
        marker=dict(size=10, color='rgba(255, 0, 0, 0.8)'),
        name="Médiane",
        visible=True  # Показываем по умолчанию
    ))

# Настройки кнопок для отображения
fig.update_layout(
    updatemenus=[
        dict(
            type="dropdown",
            showactive=True,
            buttons=[
                dict(
                    label="Tout",
                    method="update",
                    args=[{"visible": [True, True] * len(data['cluster'].unique())},  # Показываем всё
                          {"title": "Toutes les données"}]
                ),
                dict(
                    label="Min/Max",
                    method="update",
                    args=[{"visible": [True, False] * len(data['cluster'].unique())},  # Только минимум и максимум
                          {"title": "Seulement minimum et maximum"}]
                ),
                dict(
                    label="Médiane",
                    method="update",
                    args=[{"visible": [False, True] * len(data['cluster'].unique())},  # Только медиана
                          {"title": "Seulement médiane"}]
                )
            ]
        )
    ]
)

# Настройки графика
fig.update_layout(
    title="Temps de réponse par cluster",
    xaxis_title="Clusters",
    yaxis_title="Temps de réponse (heures)",
    template="plotly_white",
    font=dict(size=14)
)

# Показать график
fig.show()
