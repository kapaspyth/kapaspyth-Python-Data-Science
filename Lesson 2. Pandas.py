import pandas as pd
import numpy as np
authors = pd.DataFrame({
    'author_id': [1, 2, 3],
    'author_name': ['Тургенев', 'Чехов', 'Островский'],
})
book = pd.DataFrame({
    'author_id': [1, 1, 1, 2, 2, 3, 3],
    'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
    'price': [450, 300, 350, 500, 450, 370, 290],
})
authors_price = pd.merge(authors, book, on='author_id', how='outer')
# print(authors_price)
top5 = authors_price.nlargest(5, 'price')
# print(top5)

authors_stat_max = authors_price.groupby(by='author_name', ).agg({"price": "max"})
authors_stat_min = authors_price.groupby(by='author_name', ).agg({"price": "min"})
authors_stat_mean = authors_price.groupby(by='author_name', ).agg({"price": "mean"})
authors_stat = authors_stat_max.merge(authors_stat_min, on='author_name', how='outer').merge(authors_stat_mean, on='author_name', how='outer')
authors_stat.rename(columns={"price_x": "max_price ", "price_y": "min_price", "price": "mean_price"}) #почему не переименовывется?
# print(authors_stat)
# authors_stat.info()
authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
# print(authors_price)
book_info = pd.pivot_table(authors_price, values='price', index=['author_name'], columns=['cover'], aggfunc=np.sum, fill_value=0)
# print(book_info)
book_info.to_pickle("./book_info.pkl")
book_info2 = pd.read_pickle("./book_info.pkl")
print(book_info == book_info2)
