from task_2 import get_total_df
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

if __name__ == '__main__':
    show_columns = ['visitId', 'visitStartTime', 'date', 'fullVisitorId', 'totals.visits']
    total_df = get_total_df()
    # Просмотрели информацию о датафрейме
    print(total_df.info())

    # Установили формат даты
    total_df['date'] = pd.to_datetime(total_df['date'], format='%Y%m%d')
    df = total_df.loc[:, show_columns]
    print("\n###")
    print(df.head())

    # Посмотрели информацию об отдельных столбцах
    print(len(df['visitId'].unique()))
    print(len(df['fullVisitorId'].unique()))
    print(df['totals.visits'].unique())
    print(df['date'].unique())

    # Нашли дату начала активности каждого уникального пользователя
    df.set_index('fullVisitorId', inplace=True)
    df['first_date'] = df.groupby(level=0)['date'].min()

    # Нашли дельту времени активности пользователя
    df['timedelta'] = df['date'] - df['first_date']
    df['timedelta'] = df['timedelta'].apply(lambda l: l.days)

    df.reset_index(inplace=True)
    print("\n###")
    print(df.head())

    # Сделали сводную таблицу по дате начала и дельте активности
    pivot = pd.pivot_table(df, values='fullVisitorId',
                           index='first_date',
                           columns='timedelta',
                           aggfunc=np.size, fill_value=0)
    print("\n###")
    print(pivot)

    # Нормировали таблицу по каждой отдлеьной дате
    pivot = pivot.div(pivot[0], axis=0).round(2)
    print("\n###")
    print(pivot)
