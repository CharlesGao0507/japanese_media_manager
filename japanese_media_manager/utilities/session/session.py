import time
import http
import urllib3
import requests

def get_retry_class(interval):
    class Retry(urllib3.util.Retry):
        def sleep(self, response=None):
            time.sleep(interval)
    return Retry

class Session(requests.Session):
    def __init__(self, *args, interval=0, timeout=None, proxies=None, retries=3, **kwargs):
        self.interval = interval
        self.timeout = timeout

        super().__init__(*args, **kwargs)
        self.proxies.update(proxies or {'http': None, 'https': None})
        self.last_access_time = 0

        retry = get_retry_class(interval)(
            total=retries,
            allowed_methods=["HEAD", "GET", "POST", "PUT", "DELETE", "OPTIONS", "TRACE"],
            status_forcelist=[
                http.HTTPStatus.BAD_GATEWAY,
                http.HTTPStatus.BAD_REQUEST,
                http.HTTPStatus.INTERNAL_SERVER_ERROR,
                http.HTTPStatus.FORBIDDEN,
            ],
        )

        adapter = requests.adapters.HTTPAdapter(max_retries=retry)

        self.mount('https://', adapter)
        self.mount('http://', adapter)

    def request(self, *args, **kwargs):
        time.sleep(max(0, self.interval - time.time() + self.last_access_time))
        self.last_access_time = time.time()
        kwargs['timeout'] = kwargs.get('timeout') or self.timeout
        return super().request(*args, **kwargs)
