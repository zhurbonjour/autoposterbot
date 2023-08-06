from yadisk_api_service import YaCloudDispatcher
from bot import TelegramChannelDispatcher
from config import YA_TOKEN, TG_TOKEN


def main():
    YaCloudDispatcher(YA_TOKEN).dispatch_cloud()
    TelegramChannelDispatcher(TG_TOKEN).dispatch_channel()


if __name__ == "__main__":
    main()