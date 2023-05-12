<!-- markdownlint-disable MD031 MD033 MD036 MD041 -->

<div align="center">

# NoneBot-Plugin-FuckYou-Reset

_😅 你有几个 🐴，这么狂？ 😅_

</div>

## 📖 介绍

NoneBot2 骂人插件

将[lgc](https://github.com/lgc-NB2Dev)的插件做了一小部分修改

兼容了图片菜单插件：[PicMenu](https://github.com/hamo-reid/nonebot_plugin_PicMenu)
原github链接：[nonebot-plugin-fuckyou](https://github.com/lgc-NB2Dev/nonebot-plugin-fuckyou)
插件词库来源：[xiaoye12123/js](https://gitee.com/xiaoye12123/js)

## ⚙️ 配置

在 nonebot2 项目的 `.env` 文件中添加如下配置（非必须

`#fuckyou
fuckyou_group = [] # 全局回的群
fuckyou_tome_group = [] # 艾特机器人才回的群
fuckyou_violent_group = [] # 开启暴力词库的群(其他默认温柔词库
fuckyou_crazy_count = 5 # 往死了骂的条数
fuckyou_extend_words = [] # 额外触发词
fuckyou_extend_gentle = [] # 额外温柔词库
fuckyou_extend_violent = [] # 额外暴力词库
fuckyou_blacklist = [] # 黑名单(忽略这些用户
fuckyou_bl_to_wl = false # 黑名单反转白名单(仅对这些用户生效
fuckyou_block = false # 是否阻断 Matcher`

## 🎉 使用

1.自动回骂为关键词检测，触发关键词可以看看 [const.py](./nonebot_plugin_fuckyou_reset/const.py)
2.输入 "骂@xxxxxx"，机器人会艾特xxxxxx并调用群相应的词库骂他，可以艾特多个以及全体成员（全体成员需要管理员
3.输入 "温柔的骂@xxxxxx"，机器人会艾特xxxxxx并调用温柔词库骂他
4.输入 "狠狠的骂@xxxxxx"，机器人会艾特xxxxxx并调用暴力词库骂他
5.输入 "往死了骂@xxxxxx"，机器人会艾特xxxxxx并调用暴力词库根据fuckyou_crazy_count骂他n次

在 fuckyou_group 里的群全局检测关键词
在 fuckyou_tome_group 里的群需要艾特机器人才会检测关键词
在 fuckyou_violent_group 里的群默认回复会使用暴力词库, 反之使用温柔词库

adapter 只保留了onebotV11