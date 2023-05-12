from typing import Set

from nonebot import get_driver
from pydantic import BaseModel


class ConfigModel(BaseModel):

    # 全局回的群
    fuckyou_group: Set[str] = set()
    # 艾特机器人才回的群
    fuckyou_tome_group: Set[str] = set()
    # 开启暴力词库的群
    fuckyou_violent_group: Set[str] = set()
    # 往死了骂的条数
    fuckyou_crazy_count: int = 5
    # 额外触发词
    fuckyou_extend_words: Set[str] = set()
    # 额外温柔词库
    fuckyou_extend_gentle: Set[str] = set()
    # 额外暴力词库
    fuckyou_extend_violent: Set[str] = set()
    # 黑名单
    fuckyou_blacklist: Set[str] = set()
    # 黑名单反转
    fuckyou_bl_to_wl: bool = False
    # 是否阻断 Matcher
    fuckyou_block: bool = False


config: ConfigModel = ConfigModel.parse_obj(get_driver().config.dict())