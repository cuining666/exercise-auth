#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
from src.utils import commons
from src.repository.user_info import UserInfoRepository


def add_user():
    user_repository = UserInfoRepository()
    password = '123456'
    user_repository.add(username='cnstar', password=commons.md5(password), email='aaa@aaa.com', user_type_id='1')
    print('创建用户成功')


def del_user():
    print('删除用户')
