# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# pipelines.py

import pymysql
from scrapy.exceptions import DropItem

class MySQLPipeline:
    def open_spider(self, spider):
        self.connection = pymysql.connect(
            host=spider.settings.get('MYSQL_HOST'),
            user=spider.settings.get('MYSQL_USER'),
            password=spider.settings.get('MYSQL_PASSWORD'),
            database=spider.settings.get('MYSQL_DATABASE'),
            port=spider.settings.get('MYSQL_PORT'),
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """INSERT INTO books (Book_name, Price, Rating) VALUES (%s, %s, %s)""",
                (item['Book_name'], item['Price'], item['Rating'])
            )
            self.connection.commit()
        except pymysql.MySQLError as e:
            spider.logger.error(f"Error: {e}")
            raise DropItem(f"Error inserting item into MySQL: {e}")
        return item
