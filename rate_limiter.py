import time
import threading
from collections import defaultdict

class SlidingWindowRateLimiter:
    """Thread-safe sliding window log rate limiter for API keys and IPs."""
    def __init__(self, max_requests: int = 100, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._logs = defaultdict(list)
        self._lock = threading.Lock()

    def allow_request(self, client_id: str) -> tuple[bool, dict]:
        now = time.time()
        cutoff = now - self.window_seconds
        with self._lock:
            timestamps = [t for t in self._logs[client_id] if t > cutoff]
            self._logs[client_id] = timestamps
            remaining = max(0, self.max_requests - len(timestamps))
            if len(timestamps) < self.max_requests:
                timestamps.append(now)
                return True, {"remaining": remaining - 1, "reset_in": self.window_seconds}
            reset_in = round(timestamps[0] + self.window_seconds - now, 2)
            return False, {"remaining": 0, "reset_in": max(0.0, reset_in)}

if __name__ == "__main__":
    limiter = SlidingWindowRateLimiter(max_requests=5, window_seconds=10)
    for i in range(7):
        allowed, meta = limiter.allow_request("client_google_eval")
        print(f"Req {i+1}: allowed={allowed} | meta={meta}")
