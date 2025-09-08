import pandas as pd
import numpy as np
from io import StringIO


def load_and_prepare(path):

    cols = ['index', 'year', 'month', 'day', 'min_t', 'average_t', 'max_t', 'rainfall']

    df = pd.read_csv(
        path, sep=';', header=None, names=cols,
        dtype=str, skipinitialspace=True
    )

    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
    df = df.replace('', np.nan)

    for col in ['index', 'year', 'month', 'day']:
        df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')
    for col in ['min_t', 'average_t', 'max_t', 'rainfall']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df


def main(path='wr88125.txt'):
    # ================= Задание 1 =================
    print("Задание 1:\nЗагрузка данных и просмотр первых строк.\n")
    df = load_and_prepare(path)
    print(df.head(), "\n")

    # ================= Задание 2 =================
    print("Задание 2:\nУдаление столбца index.\n")
    if "index" in df.columns:
        df = df.drop(columns=['index'])
        print("Столбец 'index' удалён.\n")
    else:
        print("Столбец 'index' отсутствует.\n")

    # ================= Задание 3 =================
    print("Задание 3:\nИнформация о DataFrame и количество пропусков.\n")
    buf = StringIO()
    df.info(buf=buf)
    print(buf.getvalue())
    missing_per_col = df.isna().sum()
    print("Пропуски по столбцам:\n", missing_per_col, "\n")

    # ================= Задание 4 =================
    print("Задание 4:\nПоиск столбца и года с наибольшим количеством пропусков.\n")
    col_most_missing = missing_per_col.idxmax()
    print(f"Столбец с наибольшим количеством пропусков: {col_most_missing} ({missing_per_col.max()})")
    measure_cols = ['min_t','average_t','max_t','rainfall']
    missing_by_year = df.groupby('year')[measure_cols].apply(lambda g: g.isna().sum().sum())
    year_most_missing = int(missing_by_year.idxmax())
    print(f"Год с наибольшим количеством пропусков: {year_most_missing} ({missing_by_year.max()})\n")

    # ================= Задание 5 =================
    print("Задание 5:\nСоздание столбца Date.\n")
    df['Date'] = pd.to_datetime(df[['year','month','day']], errors='coerce')
    print(df[['year','month','day','Date']].head(), "\n")

    # ================= Задание 6 =================
    print("Задание 6:\nРасчёт суточного размаха температур и числа предшествующих сухих дней.\n")
    df = df.sort_values('Date').reset_index(drop=True)
    df['temp_range'] = df['max_t'] - df['min_t']
    df['dry'] = df['rainfall'] == 0
    preceding_dry = []
    dry_bool = df['dry'].fillna(False).astype(bool).to_list()
    for i in range(len(dry_bool)):
        cnt = 0
        j = i - 1
        while j >= 0 and dry_bool[j]:
            cnt += 1
            j -= 1
        preceding_dry.append(cnt)
    df['preceding_dry_days'] = preceding_dry
    print(df[['Date','min_t','max_t','temp_range','rainfall','preceding_dry_days']].head(), "\n")

    # ================= Задание 7 =================
    print("Задание 7:\nПоиск самой длинной засухи.\n")
    max_run = 0
    runs = []
    start_idx = None
    current_run = 0
    for i, val in enumerate(dry_bool):
        if val:
            if current_run == 0:
                start_idx = i
            current_run += 1
        else:
            if current_run > 0:
                runs.append((start_idx, i-1, current_run))
                max_run = max(max_run, current_run)
            current_run = 0
    if current_run > 0:
        runs.append((start_idx, len(dry_bool)-1, current_run))
        max_run = max(max_run, current_run)
    if max_run > 0:
        for s,e,l in runs:
            if l == max_run:
                drought_start = df.loc[s,'Date']
                drought_end = df.loc[e,'Date']
                break
        print(f"Самая длинная засуха: {max_run} дней, с {drought_start.date()} по {drought_end.date()}\n")
    else:
        print("Засух не найдено.\n")

    # ================= Задание 8 =================
    print("Задание 8:\nСреднегодовая температура и суммарные осадки.\n")
    yearly = df.groupby('year').agg(
        mean_avg_t=('average_t','mean'),
        total_rainfall=('rainfall','sum')
    )
    print(yearly.head(), "\n")
    warmest_year = yearly['mean_avg_t'].idxmax()
    coldest_year = yearly['mean_avg_t'].idxmin()
    wettest_year = yearly['total_rainfall'].idxmax()
    driest_year = yearly['total_rainfall'].idxmin()
    print(f"Тёплый год: {warmest_year}, холодный год: {coldest_year}")
    print(f"Влажный год: {wettest_year}, сухой год: {driest_year}\n")

    # ================= Задание 9.1 =================
    print("Задание 9.1:\nДни со средней температурой ниже -30°C.\n")
    res_9_1 = df[df['average_t'] < -30]
    print(f"Количество таких дней: {len(res_9_1)}")
    print(res_9_1[['Date','average_t','rainfall']].head(), "\n")

    # ================= Задание 9.2 =================
    print("Задание 9.2:\nДни с температурой > 27°C и более чем 3 сухими днями подряд.\n")
    res_9_2 = df[(df['average_t'] > 27) & (df['preceding_dry_days'] > 3)]
    print(f"Количество таких дней: {len(res_9_2)}")
    print(res_9_2[['Date','average_t','preceding_dry_days','rainfall']].head(), "\n")

    print("Анализ завершён.\n")
    return df, yearly

if __name__ == '__main__':
    main('wr88125.txt')
