from nonebot.plugin import PluginMetadata

from .__main__ import get_gentle_phase
from .config import ConfigModel

__version__ = "0.2.0"

__plugin_meta__ = PluginMetadata(
    name = "FuckYou",
    description = get_gentle_phase(),
    usage = "与机器人对骂即可（关键词触发）",
    config = ConfigModel,
    extra = {
        'License': 'MIT',
        'Author': ['student_2333','Dogend'],
        'menu_data': [
            {
                'func': '自动回骂',
                'trigger_method': '关键词',
                'trigger_condition': '检测到关键词触发',
                'brief_des': '检测到关键词触发',
                'detail_des': '根据配置在收到消息或被艾特时\n'
                              '检测到关键词进行回骂'
            },{
                'func': '骂别人',
                'trigger_method': '指令',
                'trigger_condition': '骂@XXX',
                'brief_des': '让机器人骂XXX',
                'detail_des': '输入骂, 后面艾特想骂的人\n'
                              '机器人根据当前群设置的词库骂他'
            },{
                'func': '温柔的骂别人',
                'trigger_method': '指令',
                'trigger_condition': '温柔的骂@XXX',
                'brief_des': '让机器人温柔的骂XXX',
                'detail_des': '输入温柔的骂, 后面艾特想骂的人\n'
                              '机器人根据温柔词库骂他'
            },{
                'func': '狠狠的骂别人',
                'trigger_method': '指令',
                'trigger_condition': '狠狠的骂@XXX',
                'brief_des': '让机器人狠狠的骂XXX',
                'detail_des': '输入狠狠的骂, 后面艾特想骂的人\n'
                              '机器人根据暴力词库骂他'
            },{
                'func': '往死了骂别人',
                'trigger_method': '指令',
                'trigger_condition': '往死了骂@XXX',
                'brief_des': '让机器人往死了骂XXX',
                'detail_des': '输入往死了骂, 后面艾特想骂的人\n'
                              '机器人根据暴力词库, 按配置的条数骂他N次'
            }
        ],
        'menu_template': 'default'
    }
)