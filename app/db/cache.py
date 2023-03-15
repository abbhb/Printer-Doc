from setting import Setting
import redis

cache_ = redis.Redis.from_url(Setting().get_cache_source_url())

if __name__ == '__main__':
    cache_.set("hello", "world", ex=12)
    value = cache_.get("hello")
    print(value)
    print(cache_.get('test'))
