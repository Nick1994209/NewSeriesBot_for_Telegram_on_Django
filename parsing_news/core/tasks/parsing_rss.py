import logging

from core import models

logger = logging.getLogger('tasks')


def parsing_rss(*args, **kwargs):
    for rss in models.Rss.objects.filter(bots__users__isnull=False).distinct():
        try:
            new_rss_news = rss.get_news()
            message = """На rss канале "{channel}"
            {title}
            {url}
            {description}
            """
            for rss_news in new_rss_news:
                rss_news_message = message.format(
                    channel=rss_news.rss.name,
                    title=rss_news.title,
                    url=rss_news.url,
                    description=rss_news.description,
                )
                rss.users_send_message(rss_news_message)
        except Exception as e:
            logger.exception(e)