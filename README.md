<div align="center">

简体中文 · [English](lang/README.en.md) · [Español](lang/README.es.md) · [Français](lang/README.fr.md) · [Deutsch](lang/README.de.md) · [Русский](lang/README.ru.md) · [日本語](lang/README.ja.md) · [한국어](lang/README.ko.md) · [العربية](lang/README.ar.md) · [Português](lang/README.pt.md) · [Italiano](lang/README.it.md) · [हिन्दी](lang/README.hi.md) · [ไทย](lang/README.th.md) · [Tiếng Việt](lang/README.vi.md) · [Bahasa Indonesia](lang/README.id.md) · [Türkçe](lang/README.tr.md) · [Nederlands](lang/README.nl.md)

</div>

# SilentCodeTeams 反馈

SilentCodeTeams 的集中反馈入口，用于提交缺陷报告、功能建议、使用问题与项目咨询。

**[反馈入口](https://silentcodeteams.github.io/feedback/)** — 请点击这里提交反馈。

## 反馈范围与提交路径

### 1. 不属于 SilentCodeTeams 的项目

部分 SilentStudio 项目可能尚未完成登记。此类项目请在 SilentStudio-CN 组织的反馈渠道提交；若该渠道尚未建立独立仓库，请通过 SilentStudio@Home.email.cn 联系。由于资源有限，无法保证逐一回复。

### 2. 属于 SilentCodeTeams、但尚未建立独立文件夹的项目

请直接在本仓库提交 issue，并在标题或正文开头注明项目名称、版本或提交号。

### 3. 已登记项目

反馈页的项目列表由 `scripts/generate_projects.py` 扫描仓库根目录自动生成。新增项目只需要在根目录添加一个项目文件夹，不需要修改 HTML 或脚本。以下四个类别子文件夹是标准配置：

- language：语言翻译、术语与本地化需求
- bug：程序或服务缺陷
- feature：功能建议与改进
- question：使用问题与咨询

具体项目可能没有全部标准文件夹，也可能增加自己的文件夹；请以项目文件夹的实际内容为准。提交 issue 时请注明项目名称与类别，例如 [project][bug]。

项目文件夹可以放置一个可选的 `project.json`，用于指定展示名、slug、排序和描述。没有该文件时，文件夹名就是项目名。生成结果写入 `docs/projects.json`，由 GitHub Actions 在推送后自动同步。

## 提交 issue 前

- 搜索是否已有相同问题
- 注明项目、版本或 commit、操作系统与架构
- 提供复现步骤、期望结果与实际结果
- 附上必要的日志或截图；不要包含密钥、令牌、个人数据
- 安全漏洞请勿公开提交，请发送至 SilentStudio@feedback.email.cn
- 请勿发布未经授权的测试细节或攻击性内容

## 响应

- 反馈按优先级处理，不承诺固定 SLA
- 安全漏洞按 SilentCodeTeams 维护与安全政策处理
- 善意报告者不会因测试行为被追责

## 链接

- SilentStudio: https://github.com/Silent-Studio-CN
- SilentCodeTeams: https://github.com/SilentCodeTeams
- 维护与安全政策: https://github.com/SilentCodeTeams
- 安全报告: SilentStudio@feedback.email.cn
- 一般联系: SilentStudio@Home.email.cn
