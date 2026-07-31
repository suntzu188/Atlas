"""Atlas environment configuration."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    supabase_url: str = os.getenv("SUPABASE_URL", "")
    supabase_key: str = os.getenv("SUPABASE_KEY", "")
    ai_provider: str = os.getenv("AI_PROVIDER", "qwen")
    ai_api_key: str = os.getenv("AI_API_KEY", "")
    ai_model: str = os.getenv("AI_MODEL", "qwen-plus")
    ai_base_url: str = os.getenv(
        "AI_BASE_URL",
        "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
    )

    def validate(self):
        missing = []
        for key, value in {
            "SUPABASE_URL": self.supabase_url,
            "SUPABASE_KEY": self.supabase_key,
            "AI_API_KEY": self.ai_api_key,
        }.items():
            if not value:
                missing.append(key)

        if missing:
            raise RuntimeError(f"Missing configuration: {', '.join(missing)}")
