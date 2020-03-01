import os
import json
import math
import pandas as pd
from pandas import json_normalize

TOTAL_DF_FILENAME = 'total_df.csv'
BASE_PATH = 'data/ga_sessions/'
BASE_FILENAME_WITH_SESSION_DATA = 'ga_sessions'


def get_total_df():
    total_df = pd.DataFrame()
    if TOTAL_DF_FILENAME not in os.listdir():
        for filename in os.listdir(BASE_PATH):
            if filename.startswith(BASE_FILENAME_WITH_SESSION_DATA):
                with open(BASE_PATH + filename) as handler:
                    sessions = []
                    for line in handler.readlines():
                        session = json.loads(line)
                        sessions.append(session)

                    df = json_normalize(sessions).drop(['customDimensions', 'hits'], axis='columns')
                    total_df = total_df.append(df)
        total_df.to_csv(TOTAL_DF_FILENAME)
    else:
        total_df = pd.read_csv(TOTAL_DF_FILENAME, index_col=0)

    return total_df


if __name__ == '__main__':
    total_df = get_total_df()

    print("###")
    print("Размер таблицы:")
    print(total_df.shape)

    print("\n###")
    print(total_df.info())

    count_unique_users = len(total_df['fullVisitorId'].unique())
    print("\n###")
    print("Количество уникальных пользователей:")
    print(count_unique_users)

    average_revenue = math.ceil(total_df['totals.totalTransactionRevenue'].sum() / count_unique_users)
    print("\n###")
    print("Средняя выручка:")
    print(average_revenue)
