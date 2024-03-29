"""
Django settings for tango_with_django_project2 project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')  # 模板的路径变量
STATIC_DIR = os.path.join(BASE_DIR, 'static')  # 静态文件的路径变量
MEDIA_DIR = os.path.join(BASE_DIR, 'media')  # 媒体文件的路径变量


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x*0h0g$aa&ot*-vij=gfthg6h5==5$1z#i%#pvwo(ik3e7*-yx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',  # 管理页面
    'django.contrib.auth',  # 访问Django提供的身份验证系统
    'django.contrib.contenttypes',  # 供auth应用跟踪数据库中的模型
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rango2',  # 添加的新应用申明
    'registration',  # 增加registration包，用于用户注册登录管理等
    'bootstrap_toolkit',  # bootstrap工具包
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tango_with_django_project2.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],  # 配置添加模板的路径变量
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',  # 媒体文件的上下文
            ],
        },
    },
]

WSGI_APPLICATION = 'tango_with_django_project2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tango2',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '116226'
    }
}

# 密码哈希算法设置
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
# LOGIN_URL = '/rango2/login/'  # 如果未登录的用户访问了带login_required()装饰器的视图，会重定向到这里


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 6, }  # 密码最短6
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'  # 设置语言

TIME_ZONE = 'Asia/Chongqing'  # 设置时区

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = [STATIC_DIR, ]  # 配置添加静态文件的路径
STATIC_URL = '/static/'  # 配置静态文件的URL访问地址

MEDIA_ROOT = MEDIA_DIR  # 配置添加媒体文件
MEDIA_URL = '/media/'  # 配置媒体文件的URL访问地址

# registration变量配置
REGISTRATION_OPEN = True  # 允许用户注册
ACCOUNT_ACTIVATION_DAYS = 7  # 留一周的激活时间
REGISTRATION_AUTO_LOGIN = True  # 注册后自动登录
LOGIN_REDIRECT_URL = '/rango2/'  # 登录后呈现给用户的页面
LOGIN_URL = '/accunts/login/'  # 未登录以及访问需要验证身份的页面时重定向的页面
