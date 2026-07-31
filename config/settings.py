import os

APP_ENV = os.getenv("APP_ENV", "development")

AI_PROVIDER = os.getenv("AI_PROVIDER", "qwen")
AI_API_KEY = os.getenv("AI_API_KEY", "")
AI_MODEL = os.getenv("AI_MODEL", "qwen-plus")
AI_BASE_URL = os.getenv(
    "AI_BASE_URL",
    "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
)

SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
