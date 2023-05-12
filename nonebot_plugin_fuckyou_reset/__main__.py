import random
from typing import Set, List

from nonebot import on_message, on_command
from nonebot.params import EventMessage
from nonebot.internal.adapter import Event
from nonebot.matcher import Matcher

from nonebot.adapters.onebot.v11 import Message, MessageSegment, MessageEvent, GroupMessageEvent


from .config import config
from .const import DEFAULT_TRIGGER_WORDS, DEFAULT_GENTLE, DEFAULT_VIOLENT

# 触发词
TRIGGER_WORDS: Set[str] = DEFAULT_TRIGGER_WORDS | config.fuckyou_extend_words
# 温柔词库
GENTLE: List[str] = list(DEFAULT_GENTLE | config.fuckyou_extend_gentle)
# 暴力词库
VIOLENT: List[str] = list(DEFAULT_VIOLENT | config.fuckyou_extend_gentle)

# 获取温柔词库
def get_gentle_phase() -> str:
    return random.choice(GENTLE)

# 获取暴力词库
def get_violent_phase() -> str:
    return random.choice(VIOLENT)

# 获取被艾特的人
def find_user_id(msg: Message) -> Set[str]:
    users: Set[str] = set()
    for segment in msg:
        if segment.type == "at" and "qq" in segment.data:
            print(segment)
            users.add(str(segment.data["qq"]))
    return users

# 骂指定的人
async def fuck_this_people(matcher: Matcher, users: Set[str], is_violent: bool = False, is_finish: bool = True):
    if(not users):
        if(is_finish):
            matcher.finish()
    else:
        seg = MessageSegment.text(get_violent_phase() if is_violent else get_gentle_phase())
        for user in users:
            seg = MessageSegment.at(user) + seg
        if(is_finish):
            await matcher.finish(Message(seg))
        else:
            await matcher.send(Message(seg))

# 骂别人（基于群词库类型
fuck_other = on_command('骂', block=config.fuckyou_block)
@fuck_other.handle()
async def _(event: GroupMessageEvent, msg: Message = EventMessage()):
    if (str(event.group_id) not in config.fuckyou_violent_group):
        await fuck_this_people(fuck_other, find_user_id(msg))
    else:
        await fuck_this_people(fuck_other, find_user_id(msg), True)

# 温柔的骂别人（基于温柔词库
fuck_gentle_other = on_command('温柔的骂', block=config.fuckyou_block)
@fuck_gentle_other.handle()
async def _(event: GroupMessageEvent, msg: Message = EventMessage()):
    await fuck_this_people(fuck_gentle_other, find_user_id(msg))

# 狠狠的骂骂别人（基于暴力词库
fuck_violent_other = on_command('狠狠的骂', block=config.fuckyou_block)
@fuck_violent_other.handle()
async def _(event: GroupMessageEvent, msg: Message = EventMessage()):
    await fuck_this_people(fuck_violent_other, find_user_id(msg), True)

# 往死了骂别人（基于暴力词库, 按配置骂N条
fuck_crazy_other = on_command('往死了骂', block=config.fuckyou_block)
@fuck_crazy_other.handle()
async def _(event: GroupMessageEvent, msg: Message = EventMessage()):
    users = find_user_id(msg)
    if(users):
        for count in range(config.fuckyou_crazy_count):
            await fuck_this_people(fuck_violent_other, users, True, False)
    await fuck_crazy_other.finish()

# 自动回骂触发规则
def trigger_rule(event: Event):
    # 判断群消息
    if (isinstance(event, GroupMessageEvent)):
        gid = str(event.group_id)
        if (gid not in config.fuckyou_group) and (
            gid not in config.fuckyou_tome_group
        ):
            return False

        if (gid in config.fuckyou_tome_group) and (
            not event.is_tome()
        ):
            return False
    # 判断黑名单, user_id是str
    in_blacklist = event.get_user_id() in config.fuckyou_blacklist
    if config.fuckyou_bl_to_wl:
        in_blacklist = not in_blacklist
    if in_blacklist:
        return False
    # 判断消息
    try:
        msg = event.get_plaintext().lower()
    except:
        return False

    return any(w in msg for w in TRIGGER_WORDS)

# 自动回骂
trigger_matcher = on_message(rule=trigger_rule, block=config.fuckyou_block)
@trigger_matcher.handle()
async def _(matcher: Matcher, event: Event):
    kwargs = {}

    if (isinstance(event, MessageEvent)):
        kwargs["reply_message"] = True
    
    if (isinstance(event, GroupMessageEvent)):
        if (str(event.group_id) not in config.fuckyou_violent_group):
            await matcher.finish(get_gentle_phase(), **kwargs)

    await matcher.finish(get_violent_phase(), **kwargs)