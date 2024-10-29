from pathlib import Path
from urllib import parse

from pydantic import field_validator
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings
from typing import Union, Dict, Optional

# 获取当前文件所在目录的上一级目录
BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    # 应用配置
    APP_NAME: str = "My App"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "My App Description"
    APP_DEBUG: bool = True

    # 服务器配置
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    SERVER_URL: str = f"http://{SERVER_HOST}:{SERVER_PORT}"

    # 静态资源配置
    # 路由访问
    STATIC_URL: str = "/static"
    # 静态文件目录名
    STATIC_DIR: str = "static"
    # 静态文件目录绝对路径
    STATIC_ROOT: Path = BASE_DIR.joinpath(STATIC_DIR)

    # 文档标题
    TITLE: str = "能源管理平台API文档"
    # 版本号
    VERSION: str = "0.0.1"
    # 文档描述, 支持 Markdown 语法
    DESCRIPTION: Optional[str] = None
    # Swagger UI API文档路径
    DOCS_URL: Optional[str] = "/docs"
    # OpenAPI架构地址
    OPENAPI_URL: str = "/openapi.json"
    # ReDoc API文档路径
    REDOC_URL: Optional[str] = "/redoc"
    # OpenAPI路由前缀
    OPENAPI_PREFIX: str = ""

    # 获取 `FastAPI` 自定义属性
    @property
    def get_backend_app_attributes(self) -> Dict[str, Union[str, bool, None]]:
        """
        设置 `FastAPI` 自定义属性
        """
        if self.APP_DEBUG:
            return {
                "title": self.APP_NAME,
                "version": self.APP_VERSION,
                "description": self.APP_DESCRIPTION,
                "docs_url": self.DOCS_URL,
                "openapi_url": self.OPENAPI_URL,
                "redoc_url": self.REDOC_URL,
                "openapi_prefix": self.OPENAPI_PREFIX
            }
        else:
            return {
                "title": self.APP_NAME,
                "version": self.APP_VERSION,
                "description": self.APP_DESCRIPTION,
                "docs_url": None,
                "openapi_url": None,
                "redoc_url": None,
                "openapi_prefix": None
            }

settings = Settings()