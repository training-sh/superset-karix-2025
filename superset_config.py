# minimal superset_config.py
# SQLAlchemy connection for Superset metadata (Postgres)
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://superset:superset_pass@postgres:5432/superset"

# Optional - recommend later to set CACHE_CONFIG, CELERY configs, etc.
# SECRET_KEY can be set via env; SUPERSET_SECRET_KEY env is used above.

# superset_config.py
import os
from cachelib.redis import RedisCache

import logging
import sys

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
logging.basicConfig(
    handlers=[handler],
    level=logging.INFO,
    format="%(asctime)s [SUP_CONFIG] %(message)s",
)

logger = logging.getLogger(__name__)


REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))

# ---------------------------
# Query Results backend (SQL Lab / async results storage)
# ---------------------------
# Use Redis for results; cachelib RedisCache instance is fine.
RESULTS_BACKEND = RedisCache(
    host=REDIS_HOST,
    port=REDIS_PORT,
    key_prefix="superset_results",
)

# # ---------------------------
# # Flask / App cache (UI caches)
# # ---------------------------
# CACHE_CONFIG = {
#     "CACHE_TYPE": "redis",
#     "CACHE_DEFAULT_TIMEOUT": 300,
#     "CACHE_KEY_PREFIX": "superset_cache:",
#     "CACHE_REDIS_HOST": REDIS_HOST,
#     "CACHE_REDIS_PORT": REDIS_PORT,
#     "CACHE_REDIS_DB": 1,
# }

# # Superset data cache (some versions use DATA_CACHE_CONFIG)
# DATA_CACHE_CONFIG = {
#     "CACHE_TYPE": "redis",
#     "CACHE_DEFAULT_TIMEOUT": 300,
#     "CACHE_KEY_PREFIX": "superset_data_cache:",
#     "CACHE_REDIS_HOST": REDIS_HOST,
#     "CACHE_REDIS_PORT": REDIS_PORT,
#     "CACHE_REDIS_DB": 1,
# }

# ---------------------------
# Celery broker/result backend (defined but workers optional)
# ---------------------------
# You can leave these here; without workers tasks won't be processed.
from celery.schedules import crontab

CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/2"

class CeleryConfig:
    broker_url = CELERY_BROKER_URL
    result_backend = CELERY_RESULT_BACKEND
    timezone = "UTC"

CELERY_CONFIG = CeleryConfig

# ---------------------------
# Keep secret key consistent
# ---------------------------
SECRET_KEY = os.environ.get("SUPERSET_SECRET_KEY", "please-change-me")


# FEATURE_FLAGS = {"DASHBOARD_FILTERS_EXPERIMENTAL": True, 
#                  "DASHBOARD_NATIVE_FILTERS_SET": True, 
#                  "DASHBOARD_NATIVE_FILTERS": True, 
#                  "DASHBOARD_CROSS_FILTERS": True, 
#                  "ENABLE_TEMPLATE_PROCESSING": True}

# Task soft/hard time limits (in seconds)
CELERY_TASK_SOFT_TIME_LIMIT = 600    # soft limit (task can cleanup)
CELERY_TASK_TIME_LIMIT = 700         # hard limit (force kill)

# Optional: reduce concurrency to avoid resource exhaustion
CELERY_WORKER_CONCURRENCY = 8





# SELECT '{{ current_username() }}' as my_name;

# SELECT '{{ current_username() }}'  as my_name, '{{ default_region }}' as region, {{current_fiscal_year}} as year ;

# {{ current_user_region() }} - invoke the function, that calls python function
"""
SELECT '{{ current_username() }}'  as my_name, 
        '{{ default_region }}' as region, 
       {{current_fiscal_year}} as year, 
       '{{ current_username(add_to_cache_keys=False) }}', 
       {{ current_user_id(add_to_cache_keys=False) }} as id, 
      '{{ current_user_email(add_to_cache_keys=False) }}' as email
       ;
"""

from flask import g

def current_user_region():
    print ("***current_user_region called***", g.user)
    return getattr(g.user, "region", None)

def get_usd_to_inr_price():
    return 86 # you can get this from some db

JINJA_CONTEXT_ADDONS = {
    "default_region": "ASIA",
    "default_nation": "Vietnam",
    "tenant_account": "tvs12345",
    "current_fiscal_year": 2025,
    "current_user_region": current_user_region, # function is registered
    "get_usd_to_inr_price": get_usd_to_inr_price,
    "a": 1000,
    "b": 2000
}


# Superset Embedding


# FEATURE_FLAGS = {
#     "EMBEDDED_SUPERSET": True,
#     "GUEST_TOKEN": True,
# }

# Which role the anonymous/guest user will have (Gamma or a custom role you create)
GUEST_ROLE_NAME = "Gamma"  # Admin > Alpha > "Gamma"   # or "Public" or your custom role

# Guest token signing config — set a strong secret in production (use env var)
import os
GUEST_TOKEN_JWT_SECRET = os.environ.get("GUEST_TOKEN_JWT_SECRET", "token4324324324jwt")
GUEST_TOKEN_JWT_ALGO = "HS256"
GUEST_TOKEN_HEADER_NAME = "X-GuestToken"
GUEST_TOKEN_JWT_EXP_SECONDS = 300  # token lifetime in seconds (short, e.g. 300s)


# superset_config.py
from datetime import timedelta

# access token lifetime (example: 1 hour)
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

# refresh token lifetime (example: 7 days)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)

# guest token lifetime (used for embedding guest tokens)
GUEST_TOKEN_JWT_EXP_SECONDS = 6000   # default 300s (5 minutes)

# CSP / framing: Content Security Policy, Security

# Superset uses Flask-Talisman; by default framing may be blocked. 
# Allow your host in frame-ancestors or disable Talisman for the embed endpoint.
#  Example (simplest dev approach — production should use CSP that explicitly allows your host):
    

    # superset_config.py (dev)
# disable HTTPS enforcement from Talisman
TALISMAN_ENABLED = True
# TALISMAN_CONFIG = {
#     # do not force redirect to https
#     "force_https": False,
#     # optional: allow your embedding/testing origin(s)
#     "content_security_policy": {
#         "frame-ancestors": ["'self'"]
#     }
# }

# prefer plain http scheme for URL building
PREFERRED_URL_SCHEME = "http"

# proxy fix disabled for simple local setups
ENABLE_PROXY_FIX = False

TALISMAN_ENABLED = True
TALISMAN_CONFIG = {
     # do not force redirect to https
    "force_https": False,
    "content_security_policy": {
        "frame-ancestors": ["'self'", "http://localhost:3000", "http://127.0.0.1:3000"]
    }
}


# or totally disable tailsman

# TALISMAN_ENABLED = False
# PREFERRED_URL_SCHEME = "http"
# ENABLE_PROXY_FIX = False

# superset_config.py (dev only)
WTF_CSRF_ENABLED = False


FEATURE_FLAGS = {
  "DASHBOARD_FILTERS_EXPERIMENTAL": True,
  "DASHBOARD_NATIVE_FILTERS_SET": True,
  "DASHBOARD_NATIVE_FILTERS": True,
  "DASHBOARD_CROSS_FILTERS": True,
  "ENABLE_TEMPLATE_PROCESSING": True,
  "EMBEDDED_SUPERSET": True,
  "GUEST_TOKEN": True,
}


"""
a guest token is a short-lived JWT that Superset issues (signed with GUEST_TOKEN_JWT_SECRET) to allow 
unauthenticated / embedded sessions to view specific Superset resources (dashboards/charts) with a
 restricted role and optional row-level security (RLS). 
 It’s generated server-side (by an Admin or an endpoint you run) and 
 given to the client/iframe/SDK to access Superset without a full login.
"""

logger.warning(">>> superset_config.py loaded successfully")
