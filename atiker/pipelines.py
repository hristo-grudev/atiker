import sqlite3


class AtikerPipeline:
    conn = sqlite3.connect('atiker.db')
    cursor = conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `atiker` (
                                                                                title varchar(100),
                                                                                description text,
                                                                                lang varchar(5)
                                                                                )''')
        self.conn.commit()

    def process_item(self, item, spider):
        title = item['title'][0]
        description = item['description'][0]
        lang = item['lang'][0]

        self.cursor.execute(f"""select * from atiker where title = '{title}' and lang = '{lang}'""")
        is_exist = self.cursor.fetchall()

        if len(is_exist) == 0:
            self.cursor.execute(f"""insert into `atiker`
                                        (`title`, `description`, `lang`)
                                        values (?, ?, ?)""", (title, description, lang))
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
