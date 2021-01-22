BOT_NAME = 'atiker'

SPIDER_MODULES = ['atiker.spiders']
NEWSPIDER_MODULE = 'atiker.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'atiker.pipelines.AtikerPipeline': 100,

}