from fastapi import FastAPI, applications
from contextlib import asynccontextmanager
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html

from backend.app.api import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting application")
    yield
    print("Stopping application")

def register_routers(app: FastAPI, prefix: str = "/api") -> None:
    """
    注册路由
    :param app: FastAPI实例
    :param prefix: 路由前缀
    """
    app.include_router(api_router, prefix=prefix)

def reset_api_docs() -> None:
    """
    修复Redoc API文档CDN无法访问的问题
    """

    def swagger_monkey_patch(*args, **kwargs):
        """
        修复Swagger API文档CDN无法访问的问题
        """
        return get_swagger_ui_html(
            *args, **kwargs,
            swagger_css_url="/static/swagger/swagger-ui/swagger-ui.css",
            swagger_js_url="/static/swagger/swagger-ui/swagger-ui-bundle.js",
            swagger_favicon_url="/static/swagger/favicon.png"
        )

    def redoc_monkey_patch(*args, **kwargs):
        return get_redoc_html(
            *args, **kwargs,
            redoc_js_url="/static/swagger/redoc/bundles/redoc.standalone.js",
            redoc_favicon_url="/static/swagger/favicon.png"
        )

    applications.get_swagger_ui_html = swagger_monkey_patch
    applications.get_redoc_html = redoc_monkey_patch